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


  onZoomChange($event, visualizationId) {
    this.dashboard.pipe(first()).subscribe((value) => {
      this.store.dispatch(
        changeVisualizerInDashboardZoom({
          data: {
            zoom: $event.value,
            visualizerId: visualizationId,
            dashboardId: value.id,
          },
        })
      );
    });
  }

  constructor(private store: Store<AppState>,private update$:Actions) {
  }

  fetchSvgs(){
    this.dashboard.pipe(first()).subscribe((value) => {
      this.store.dispatch(
        fetchDashboardSVGs({ data: { dashboardId: value.id } })
      );
    });
  }

  consol(data) {
    console.log(data);
    return data;
  }
  ngAfterViewInit(): void {
    this.fetchSvgs();

    this.update$
    .pipe(
      // delay(500),
      ofType(
        // updateFilterInVisualizerSuccess,
        // addFilterToVisualizerSuccess,
        // removeFilterFromVisualizerSuccess,
        // updateVisualizerSuccess,
        addToTapes,
        updateDashboardSuccess,
        // updateCurrentTree
      ),
      takeUntil(this.destroyed$)
    )
    .subscribe(() => {
      console.log('update')
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
        console.log(visualizer.visualizationId,visElement)
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
}
