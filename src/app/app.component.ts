import { Component, HostListener, OnInit, AfterViewInit } from "@angular/core";
import { Observable } from "rxjs";
import { Store } from "@ngrx/store";
import { AppState } from "src/store";
import {
  isTreeOpened,
  selectIsThereACurrentTap,
} from "src/store/core/selectors/core.selector";
import {
  fetchDataSourcesSuccess,
  fetchDataSources,
} from "src/store/data-sources";
import {
  fetchVisualizersSuccess,
  fetchVisualizers,
  fetchChartAsSVGSuccess,
} from "src/store/visualizers";
import { fetchDashboardsSuccess, fetchDashboards, updateDashboard } from "src/store/dashboards";
import { fetchFiltersSuccess, fetchFilters } from "src/store/filters";
import { Router } from "@angular/router";
import { HttpClient } from "@angular/common/http";
import { BASE_URL } from "src/utils/url.util";
import { TEST_SVG_CHART } from "src/utils/static.chart";
import { fetchCharts } from 'src/store/core/actions/core.actions';

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.scss"],
})
export class AppComponent implements OnInit, AfterViewInit {
  title = "DataI";
  width = 250;
  x = 100;
  oldX = 0;
  grabber = false;
  isTreeOpened: Observable<boolean>;
  isThereAnOpenedTap: Observable<boolean>;
  eventHandlers: any[] = [];
  constructor(
    private store: Store<AppState>,
    private router: Router,
    private http: HttpClient
  ) {
    this.isThereAnOpenedTap = this.store.select(selectIsThereACurrentTap);
    this.isTreeOpened = this.store.select(isTreeOpened);
  }
  ngOnInit(): void {
    this.fillTheStoreOut();
  }
  ngAfterViewInit() {
    this.isTreeOpened.subscribe((value) => {
      if (value == true) {
        setTimeout(() => {
          let element = document.getElementById("grabber");
          this.setGrabberEvents(element);
        }, 1000);
      }
    });
    this.store.select(selectIsThereACurrentTap).subscribe((value) => {
      if (value == false) this.router.navigate([""]);
    });
  }
  setGrabberEvents(element) {
    document.addEventListener("mousemove", (event) => {
      if (!this.grabber) {
        return;
      }
      this.resizer((event.clientX - this.oldX) * 2);
      this.oldX = event.clientX;
    });
    document.addEventListener("mouseup", () => {
      this.grabber = false;
    });

    element.addEventListener("mousedown", (event) => {
      this.grabber = true;
      this.oldX = event.clientX;
      event.preventDefault();
    });
  }
  resizer(offsetX: number) {
    if (this.width + offsetX < 250 || this.width + offsetX > 1500) return;
    this.width += offsetX;
  }

  fillTheStoreOut() {
    this.store.dispatch(fetchDataSources());

    this.store.dispatch(fetchVisualizers());

    this.store.dispatch(fetchDashboards());

    this.store.dispatch(updateDashboard({data : {
        name: 'dashboard1',
        id: 0,
        isDeleted : false,
        visualizers: [
          {
            visualizationIndex: 0,
            measurements: {
              width: 500.0,
              height: 300.0,
              x: 100.0,
              y: 100.0,
            },
            displayedFilters: [
              {
                filterIndex: 0,
                measurements: {
                  width: 100.0,
                  height: 100.0,
                  x: 100.0,
                  y: 200.0,
                },
              },
              {
                filterIndex: 1,
                measurements: {
                  width: 100.0,
                  height: 100.0,
                  x: 300.0,
                  y: 150.0,
                }
              }
            ]
          }
        ]
    }}))

    this.store.dispatch(fetchFilters());

    this.store.dispatch(fetchCharts());
  }
}
