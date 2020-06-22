import { Component, HostListener, OnInit, AfterViewInit } from "@angular/core";
import { Observable } from "rxjs";
import { Store } from "@ngrx/store";
import { AppState } from "src/store";
import {
  isTreeOpened,
  selectIsThereACurrentTap,
} from "src/store/core/selectors/core.selector";
import { fetchDataSourcesSuccess } from "src/store/data-sources";
import { fetchVisualizersSuccess } from "src/store/visualizers";
import { fetchDashboardsSuccess } from "src/store/dashboards";
import { fetchFiltersSuccess } from "src/store/filters";
import { Router } from "@angular/router";

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
  constructor(private store: Store<AppState>, private router: Router) {
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
    this.store.dispatch(
      fetchDataSourcesSuccess({
        data: [
          {
            name: "Table1",
            id: 0,
            columns: [
              {
                name: "السعر",
                id: 500,
                cells: [
                  {
                    value: "السعر",
                    type: "string",
                  },
                  {
                    value: 10,
                    type: "numeric",
                  },
                  {
                    value: 20,
                    type: "numeric",
                  },
                  {
                    value: 20,
                    type: "numeric",
                  },
                  {
                    value: 20,
                    type: "numeric",
                  },
                  {
                    value: 15,
                    type: "numeric",
                  },
                  {
                    value: 15,
                    type: "numeric",
                  },
                  {
                    value: 10,
                    type: "numeric",
                  },
                  {
                    value: 10,
                    type: "numeric",
                  },
                ],
                style: {
                  color: "#26C485",
                  lineWeight: 1.0,
                  pointWeight: 1.0,
                  font: "Calibri",
                },
                columnType: "Measures",
                valueCategories: [
                  {
                    value: "السعر",
                    type: "string",
                  },
                  {
                    value: 10,
                    type: "numeric",
                  },
                  {
                    value: 20,
                    type: "numeric",
                  },
                  {
                    value: 15,
                    type: "numeric",
                  },
                ],
                isDeleted: false,
              },
              {
                name: "الكمية",
                id: 40,
                cells: [
                  {
                    value: "الكمية",
                    type: "string",
                  },
                  {
                    value: 40,
                    type: "numeric",
                  },
                  {
                    value: 50,
                    type: "numeric",
                  },
                  {
                    value: 50,
                    type: "numeric",
                  },
                  {
                    value: 50,
                    type: "numeric",
                  },
                  {
                    value: 50,
                    type: "numeric",
                  },
                  {
                    value: 60,
                    type: "numeric",
                  },
                  {
                    value: 50,
                    type: "numeric",
                  },
                  {
                    value: 40,
                    type: "numeric",
                  },
                ],
                style: {
                  color: "#3066BE",
                  lineWeight: 1.0,
                  pointWeight: 1.0,
                  font: "Calibri",
                },
                columnType: "Measures",
                valueCategories: [
                  {
                    value: "الكمية",
                    type: "string",
                  },
                  {
                    value: 40,
                    type: "numeric",
                  },
                  {
                    value: 50,
                    type: "numeric",
                  },
                  {
                    value: 60,
                    type: "numeric",
                  },
                ],
                isDeleted: false,
              },
              {
                name: "النوع",
                id: 359,
                cells: [
                  {
                    value: "النوع",
                    type: "string",
                  },
                  {
                    value: "Laptop",
                    type: "string",
                  },
                  {
                    value: "Laptop",
                    type: "string",
                  },
                  {
                    value: "Laptop",
                    type: "string",
                  },
                  {
                    value: "Mouse",
                    type: "string",
                  },
                  {
                    value: "Mouse",
                    type: "string",
                  },
                  {
                    value: "Mouse",
                    type: "string",
                  },
                  {
                    value: "Keyboard",
                    type: "string",
                  },
                  {
                    value: "Keyboard",
                    type: "string",
                  },
                ],
                style: {
                  color: "#DBD56E",
                  lineWeight: 1.0,
                  pointWeight: 1.0,
                  font: "Calibri",
                },
                columnType: "Dimensions",
                valueCategories: [
                  {
                    value: "النوع",
                    type: "string",
                  },
                  {
                    value: "Laptop",
                    type: "string",
                  },
                  {
                    value: "Mouse",
                    type: "string",
                  },
                  {
                    value: "Keyboard",
                    type: "string",
                  },
                ],
                isDeleted: false,
              },
              {
                name: "الوزن",
                id: 501,
                cells: [
                  {
                    value: "الوزن",
                    type: "string",
                  },
                  {
                    value: 10,
                    type: "string",
                  },
                  {
                    value: 17,
                    type: "string",
                  },
                  {
                    value: 55,
                    type: "string",
                  },
                  {
                    value: 39,
                    type: "string",
                  },
                  {
                    value: 71,
                    type: "string",
                  },
                  {
                    value: 66,
                    type: "string",
                  },
                  {
                    value: 55,
                    type: "string",
                  },
                  {
                    value: 21,
                    type: "string",
                  },
                ],
                style: {
                  color: "#EBD4AE",
                  lineWeight: 1.5,
                  pointWeight: 0.0,
                  font: "Calibri",
                },
                columnType: "Measures",
                valueCategories: [
                  {
                    value: "الوزن",
                    type: "string",
                  },
                  {
                    value: 10,
                    type: "string",
                  },
                  {
                    value: 17,
                    type: "string",
                  },
                  {
                    value: 55,
                    type: "string",
                  },
                  {
                    value: 39,
                    type: "string",
                  },
                  {
                    value: 71,
                    type: "string",
                  },
                  {
                    value: 66,
                    type: "string",
                  },
                  {
                    value: 21,
                    type: "string",
                  },
                ],
                isDeleted: false,
              },
            ],
            columnsVisibility: [true, true, true],
            rowsVisibility: [true, true, true],
            properties: {
              sourceFileType: "DataI",
              zoomValue: 50,
              xColumn: 0,
            },
            rightToLeft: true,
            aggregator: null,
            isDeleted: false,
          },
        ],
      })
    );

    this.store.dispatch(
      fetchVisualizersSuccess({
        data: [
          {
            name: "visualization1",
            id: 0,
            data: 0,
            usedColumns: [500, 359],
            usedRow: 501,
            chart: "BoundaryLineChart",
            filters: [0, 1],
            isDeleted: false,
          },
        ],
      })
    );

    this.store.dispatch(
      fetchDashboardsSuccess({
        data: [
          {
            name: "dashboard1",
            id: 0,
            visualizers: [
              {
                visualizationIndex: 0,
                measurements: {
                  width: 1.0,
                  height: 1.0,
                  x: 1.0,
                  y: 1.0,
                },
                displayedFilters: [
                  {
                    filterIndex: 0,
                    measurements: {
                      width: 0.0,
                      height: 0.0,
                      x: 0.0,
                      y: 0.0,
                    },
                  },
                  {
                    filterIndex: 1,
                    measurements: {
                      width: 1.0,
                      height: 1.0,
                      x: 1.0,
                      y: 1.0,
                    },
                  },
                ],
              },
            ],
          },
        ],
      })
    );

    this.store.dispatch(
      fetchFiltersSuccess({
        data: [
          {
            name: "filter1",
            id: 0,
            dataSource: 0,
            filteredColumn: 40,
            initValue: 10,
            type: "Equality",
            isDeleted: false,
          },
          {
            name: "filter2",
            id: 1,
            dataSource: 0,
            filteredColumn: 359,
            initValue: 15,
            type: "LessThan",
            isDeleted: false,
          },
          {
            name: "filter3",
            id: 2,
            dataSource: 0,
            filteredColumn: 500,
            initValue: "Laptop",
            type: "Equality",
            isDeleted: false,
          },
        ],
      })
    );
  }
}
