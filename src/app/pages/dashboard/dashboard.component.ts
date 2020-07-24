import { AfterViewInit, Renderer2, ViewChild, ElementRef, OnDestroy } from "@angular/core";
import { Component, OnInit } from "@angular/core";
import { AppState } from "src/store";
import { Store } from "@ngrx/store";
import { selectVisualizersEntities } from "src/store/visualizers/visualizers.selectors";
import { selectFiltersEntities } from "src/store/filters/filters.selectors";
import { selectCurrentDashboard } from "src/store/dashboards/dashboards.selectors";
import {
  updateDashboard,
  fetchDashboardSVGs,
  changeVisualizerInDashboardZoom,
  updateDashboardSuccess,
  updateFilterInDashboard,
} from "src/store/dashboards";
import { first, takeUntil } from "rxjs/operators";
import { addToTapes } from 'src/store/core/actions/core.actions';
import { Actions, ofType } from '@ngrx/effects';
import { Subject } from 'rxjs';
@Component({
  selector: "app-dashboard",
  templateUrl: "./dashboard.component.html",
  styleUrls: ["./dashboard.component.scss"],
})
export class DashboardComponent implements AfterViewInit, OnDestroy {
  edit: boolean = false;
  visualizers = this.store.select(selectVisualizersEntities);
  filters = this.store.select(selectFiltersEntities);
  dashboard = this.store.select(selectCurrentDashboard);
  destroyed$ = new Subject<boolean>();
  zooms = [];


  onZoomChange($event, index) {
    this.zooms[index] = $event.value
  }

  constructor(private store: Store<AppState>,private update$:Actions) {
  }

  fetchSvgs(){
    this.dashboard.pipe(first()).subscribe((value) => {
      this.store.dispatch(
        fetchDashboardSVGs({ data: { dashboardId: value.id } })
      );
      this.zooms = []
      for(let visualizer of value.visualizers)
        this.zooms.push(100);
    });
  }

  ngAfterViewInit(): void {
    setTimeout(()=>{
      this.fetchSvgs();
    },0)

    this.update$
    .pipe(
      ofType(
        addToTapes,
        updateDashboardSuccess,
      ),
      takeUntil(this.destroyed$)
    )
    .subscribe(() => {
      setTimeout(()=>{
        this.fetchSvgs();
      },500)
    });
  }

  ngOnDestroy(){
    this.destroyed$.next(false);
    this.destroyed$.complete();
  }
  onSave() {
    this.dashboard.subscribe((value) => {
      let newDashboard = { ...JSON.parse(JSON.stringify(value)) };
      for (let visualizer of newDashboard.visualizers) {
        let visElement = document.getElementById(
          `visualizer${visualizer.visualizationId}`
        );
        visualizer.measurements = {
          width: visElement.offsetWidth,
          height: visElement.offsetHeight,
          x: visElement.offsetLeft,
          y: visElement.offsetTop,
        };
      }
      for (let filter of newDashboard.filters) {
        let filterElement = document.getElementById(`filter${filter.id}`);
        filter.measurements = {
          width: filterElement.offsetWidth,
          height: filterElement.offsetHeight,
          x: filterElement.offsetLeft,
          y: filterElement.offsetTop,
        };
      }

      this.store.dispatch(updateDashboard({ data: newDashboard }));

      this.edit = !this.edit;
    });
  }

  goToVisualizer(visualizerId){
    this.visualizers.pipe(first()).subscribe((entities)=>{

      this.store.dispatch(
        addToTapes({
          tap: {
            name: entities[visualizerId].name,
            type: 'visualizer',
            id: visualizerId,
          },
        })
      );

    })
  }


  onFilterChangeValue($event,filter){
    this.dashboard.pipe(first()).subscribe((dashboard)=>{
      this.store.dispatch(updateFilterInDashboard({ data : {
        ...filter,
        dashboardId: dashboard.id,
        visioId: filter.visioId,
        id: filter.id,
        value: $event.value,
        isActive: $event.active,
      }}))

    })

    this.fetchSvgs();
  }


  print(): void {
    let printContents, popupWin;
    printContents = document.getElementById('print-section').innerHTML;
    popupWin = window.open('', '_blank', 'top=0,left=0,height=100%,width=auto');
    popupWin.document.open();
    popupWin.document.write(`
      <html>
        <head>
          <title>Print tab</title>
        </head>
    <body onload="window.print();window.close()">${printContents}</body>
      </html>`
    );
    popupWin.document.close();
}

}
