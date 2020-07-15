import { Component, ViewChild } from "@angular/core";
import { Observable } from "rxjs";
import { Store } from "@ngrx/store";
import { AppState } from "src/store";
import {
  selectCurrentVisualizer,
  selectAllCurrentVisualizerFilters,
  selectCurrentVisualizerFilters,
} from "src/store/visualizers/visualizers.selectors";
import { VisualizerItemComponent } from "src/app/components/visualizer-item/visualizer-item.component";
import { first } from "rxjs/operators";
import { NotificationService } from "src/store/notifications/notifications.service";
import {
  addFilterToVisualizer,
  removeFilterFromVisualizer,
  updateFilterInVisualizer,
} from "src/store/visualizers";

@Component({
  selector: "app-visualizer",
  templateUrl: "./visualizer.component.html",
  styleUrls: ["./visualizer.component.scss"],
})
export class VisualizerComponent {
  @ViewChild(VisualizerItemComponent) visualizerItemComponent;
  visualizer: Observable<any> = this.store.select(selectCurrentVisualizer);
  filters: Observable<any> = this.store.select(selectCurrentVisualizerFilters);
  addableFilters: Observable<any>;
  insertFilter: boolean = false;
  insertedFilter;
  objectKeys = Object.keys;
  constructor(
    private store: Store<AppState>,
    private notification: NotificationService
  ) {
    this.addableFilters = this.store.select(selectAllCurrentVisualizerFilters);
    this.visualizer.subscribe(()=>{
      this.visualizerItemComponent.onResize();
    })
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

  consol(data) {
    return data;
  }

  onAddClicked() {
    this.insertFilter = true;
  }
}
