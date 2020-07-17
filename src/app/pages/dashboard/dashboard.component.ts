import { AfterViewInit, Renderer2, ViewChild, ElementRef } from "@angular/core";
import { Component, OnInit } from "@angular/core";
import { AppState } from "src/store";
import { Store } from "@ngrx/store";
import { selectVisualizersEntities } from "src/store/visualizers/visualizers.selectors";
import { selectFiltersEntities } from "src/store/filters/filters.selectors";
import { selectCurrentDashboard } from "src/store/dashboards/dashboards.selectors";
import { updateDashboard, fetchDashboardSVGs } from "src/store/dashboards";
import { first } from 'rxjs/operators';
@Component({
  selector: "app-dashboard",
  templateUrl: "./dashboard.component.html",
  styleUrls: ["./dashboard.component.scss"],
})
export class DashboardComponent implements AfterViewInit {
  edit: boolean = false;
  visualizers = this.store.select(selectVisualizersEntities);
  filters = this.store.select(selectFiltersEntities);
  dashboard = this.store.select(selectCurrentDashboard);
  constructor(private store: Store<AppState>) {
    this.dashboard.pipe(first()).subscribe((value)=>{
      this.store.dispatch(fetchDashboardSVGs({data : {dashboardId : value.id}}))
    });

  }
  consol(data) {
    console.log(data);
    return data;
  }
  ngAfterViewInit(): void {}

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
          let filterElement = document.getElementById(
            `filter${filter.id}`
          );
          filter.measurements = {
            width: filterElement.offsetWidth,
            height: filterElement.offsetHeight,
            x: filterElement.offsetLeft,
            y: filterElement.offsetTop,
          };
        }

      this.store.dispatch(updateDashboard({ data: newDashboard }));

      this.edit = !this.edit
    });
  }
}
