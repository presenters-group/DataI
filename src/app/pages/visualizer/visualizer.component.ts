import { Component, ViewChild, ElementRef, AfterViewInit, OnDestroy, HostListener } from "@angular/core";
import { Observable, Subject } from "rxjs";
import { Store } from "@ngrx/store";
import { AppState } from "src/store";
import {
  selectCurrentVisualizer,
  selectAllCurrentVisualizerFilters,
  selectCurrentVisualizerFilters,
} from "src/store/visualizers/visualizers.selectors";
import { VisualizerItemComponent } from "src/app/components/visualizer-item/visualizer-item.component";
import { first, takeUntil, delay } from "rxjs/operators";
import { NotificationService } from "src/store/notifications/notifications.service";
import {
  addFilterToVisualizer,
  removeFilterFromVisualizer,
  updateFilterInVisualizer,
  fetchChartAsSVG,
  updateFilterInVisualizerSuccess,
  addFilterToVisualizerSuccess,
  removeFilterFromVisualizerSuccess,
  updateVisualizerSuccess,
  removeSvgForVisualizer,
} from "src/store/visualizers";
import { Actions, ofType } from '@ngrx/effects';
import { addToTapes, updateCurrentTree } from 'src/store/core/actions/core.actions';

@Component({
  selector: "app-visualizer",
  templateUrl: "./visualizer.component.html",
  styleUrls: ["./visualizer.component.scss"],
})
export class VisualizerComponent implements AfterViewInit, OnDestroy {
  @ViewChild(VisualizerItemComponent) visualizerItem : VisualizerItemComponent;
  filters: Observable<any> = this.store.select(selectCurrentVisualizerFilters);
  addableFilters: Observable<any>;
  insertFilter: boolean = false;
  insertedFilter;
  objectKeys = Object.keys;
  visualizer = this.store.select(selectCurrentVisualizer);
  destroyed$ = new Subject<boolean>();
  zoom : number = 100;


  @HostListener('window:resize')
  onResize(){
    this.fetchSvg();
  }

  constructor(
    private store: Store<AppState>,
    private notification: NotificationService,
    private update$: Actions,
  ) {
    this.addableFilters = this.store.select(selectAllCurrentVisualizerFilters);

  }
  ngAfterViewInit(): void {
    this.removeSvg();
    setTimeout(()=>{
      this.fetchSvg();
    },500)
    this.update$
    .pipe(
      // delay(500),
      ofType(
        updateFilterInVisualizerSuccess,
        addFilterToVisualizerSuccess,
        removeFilterFromVisualizerSuccess,
        updateVisualizerSuccess,
        addToTapes,
        // updateCurrentTree
      ),
      takeUntil(this.destroyed$)
    )
    .subscribe(() => {
      this.removeSvg();
      setTimeout(()=>{
        this.fetchSvg();
      },100)
    });
  }
  disableAddedFilter(filter, filters) {
    return filters.map((x) => x.id).includes(filter.id);
  }
  onAddFilter() {
    if (!this.insertedFilter) {
      this.notification.fail("Please select filter before adding");
      return;
    }
    this.visualizer.pipe(first()).subscribe((value) => {
      this.store.dispatch(
        addFilterToVisualizer({
          data: {
            visualizerId: value.id,
            id: this.insertedFilter.id,
            value: this.insertedFilter.initValue
              ? this.insertedFilter.initValue
              : [],
            isActive: true,
          },
        })
      );
    });
    this.insertedFilter = null;
    this.insertFilter = false;
  }

  onDeleteFilter($event) {
    this.visualizer.pipe(first()).subscribe((value) => {
      this.store.dispatch(
        removeFilterFromVisualizer({
          data: {
            visualizerId: value.id,
            id: $event.id,
          },
        })
      );
    });
  }

  onFilterChangeValue($event) {
    this.visualizer.pipe(first()).subscribe((value) => {
      this.store.dispatch(
        updateFilterInVisualizer({
          data: { ...$event, visualizerId: value.id },
        })
      );
    });
  }

  consol(data,...rest) {
    return data;
  }


  fetchSvg(){
    let svg = document.getElementById('svg')
    this.visualizer.pipe(first()).subscribe((value)=>{
      this.store.dispatch(fetchChartAsSVG({
        data : {
          visualizerId : value.id,
          width: svg.offsetWidth,
          height: svg.offsetHeight
        }
      }))

    })
  }

  onAddClicked() {
    this.insertFilter = true;
    this.fetchSvg()
  }

  ngOnDestroy(){
    this.destroyed$.next(false);
    this.destroyed$.complete();
  }

  removeSvg(){

    this.visualizer.pipe(first()).subscribe((value)=>{
      this.store.dispatch(removeSvgForVisualizer({ data: {visualizerId: value.id}}))
    })
  }

  download(as : string){
    switch(as){
      case 'svg':
        //TODO: download as svg;
      case 'png':
          //TODO: download as png;

    }
  }

}
