import {
  Component,
  ViewChild,
  ElementRef,
  AfterViewInit,
  OnDestroy,
  HostListener,
} from "@angular/core";
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
import { Actions, ofType } from "@ngrx/effects";
import {
  addToTapes,
  updateCurrentTree,
} from "src/store/core/actions/core.actions";
import { HttpClient } from "@angular/common/http";
import { BASE_URL } from "src/utils/url.util";
import { saveAs } from "file-saver";
import { MatDialog } from "@angular/material/dialog";
import { GetNameComponent } from "src/app/components/get-name/get-name.component";

@Component({
  selector: "app-visualizer",
  templateUrl: "./visualizer.component.html",
  styleUrls: ["./visualizer.component.scss"],
})
export class VisualizerComponent implements AfterViewInit, OnDestroy {
  @ViewChild(VisualizerItemComponent) visualizerItem: VisualizerItemComponent;
  filters: Observable<any> = this.store.select(selectCurrentVisualizerFilters);
  addableFilters: Observable<any>;
  insertFilter: boolean = false;
  insertedFilter;
  objectKeys = Object.keys;
  visualizer = this.store.select(selectCurrentVisualizer);
  destroyed$ = new Subject<boolean>();
  zoom: number = 100;

  @HostListener("window:resize")
  onResize() {
    this.fetchSvg();
  }

  constructor(
    private store: Store<AppState>,
    private notification: NotificationService,
    private update$: Actions,
    private httpClient: HttpClient,
    private dialog: MatDialog
  ) {
    this.addableFilters = this.store.select(selectAllCurrentVisualizerFilters);
  }
  ngAfterViewInit(): void {
    setTimeout(() => {
      this.removeSvg();
      this.fetchSvg();
    }, 0);
    this.update$
      .pipe(
        ofType(
          updateFilterInVisualizerSuccess,
          addFilterToVisualizerSuccess,
          removeFilterFromVisualizerSuccess,
          updateVisualizerSuccess,
          addToTapes
          // updateCurrentTree
        ),
        takeUntil(this.destroyed$)
      )
      .subscribe(() => {
        this.removeSvg();
        setTimeout(() => {
          this.fetchSvg();
        }, 100);
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

  fetchSvg() {
    let svg = document.getElementById("svg");
    if (svg)
      this.visualizer.pipe(first()).subscribe((value) => {
        this.store.dispatch(
          fetchChartAsSVG({
            data: {
              visualizerId: value.id,
              width: svg.offsetWidth,
              height: svg.offsetHeight,
            },
          })
        );
      });
  }

  onAddClicked() {
    this.insertFilter = true;
    this.fetchSvg();
  }

  ngOnDestroy() {
    this.destroyed$.next(false);
    this.destroyed$.complete();
  }

  removeSvg() {
    this.visualizer.pipe(first()).subscribe((value) => {
      this.store.dispatch(
        removeSvgForVisualizer({ data: { visualizerId: value.id } })
      );
    });
  }

  download(as: string) {
    let svg = document.getElementById("svg");
    let dialogRef = this.dialog.open(GetNameComponent);
    dialogRef.afterClosed().subscribe((name) => {
      switch (as) {
        case "svg":
          this.visualizer.pipe(first()).subscribe((visualizer) => {
            this.httpClient
              .put(
                `${BASE_URL}svg-export/`,
                {
                  visualizerId: visualizer.id,
                  width: svg.offsetWidth,
                  height: svg.offsetWidth,
                  animation: visualizer.animation,
                },
                {
                  responseType: "blob",
                }
              )
              .subscribe((response) =>
                this.saveFile(response, "image/svg+xml", `${name}.svg`)
              );
          });
          break;
        case "png":
          this.visualizer.pipe(first()).subscribe((visualizer) => {
            this.httpClient
              .put(
                `${BASE_URL}png-export/`,
                {
                  visualizerId: visualizer.id,
                  width: svg.offsetWidth,
                  height: svg.offsetWidth,
                  animation: false,
                },
                {
                  responseType: "blob",
                }
              )
              .subscribe((response) =>
                this.saveFile(response, "image/png", `${name}.png`)
              );
          });
          break;
      }
    });
  }

  saveFile = (blobContent: Blob, type: string, fileName: string) => {
    const blob = new Blob([blobContent], { type: "application/octet-stream" });
    saveAs(blob, fileName);
  };

  print(): void {
    let printContents, popupWin;
    printContents = document.getElementById("print-section").innerHTML;
    popupWin = window.open("", "_blank", "top=0,left=0,height=100%,width=auto");
    popupWin.document.open();
    popupWin.document.write(`
      <html>
        <head>
          <title>Print tab</title>
        </head>
    <body onload="window.print();window.close()">${printContents}</body>
      </html>`);
    popupWin.document.close();
  }
}
