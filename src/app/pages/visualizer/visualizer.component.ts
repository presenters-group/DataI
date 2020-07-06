import {
  Component,
  OnInit,
  AfterViewInit,
  Sanitizer,
  OnDestroy,
  ViewChild,
  HostListener,
} from "@angular/core";
import { Observable } from "rxjs";
import { Store } from "@ngrx/store";
import { AppState } from "src/store";
import {
  selectCurrentVisualizer,
  selectCurrentVisualizerFilters,
  selectVisualizersState,
  selectVisualizersChart,
} from "src/store/visualizers/visualizers.selectors";
import { fetchChartAsSVGSuccess, fetchChartAsSVG } from "src/store/visualizers";
import { TEST_SVG_CHART } from "src/utils/static.chart";
import { HttpClient } from "@angular/common/http";
import { first, debounceTime, filter } from "rxjs/operators";
import { SafeHtml, DomSanitizer } from "@angular/platform-browser";

@Component({
  selector: "app-visualizer",
  templateUrl: "./visualizer.component.html",
  styleUrls: ["./visualizer.component.scss"],
})
export class VisualizerComponent implements AfterViewInit, OnDestroy {
  svg: Observable<SafeHtml> = this.store.select(selectVisualizersChart);
  visualizer: Observable<any> = this.store.select(selectCurrentVisualizer);
  filters: Observable<any> = this.store.select(selectCurrentVisualizerFilters);
  oldValue: number;
  @ViewChild("chart") chart;

  @HostListener('window:resize', ['$event'])
  onResize() {
    this.visualizer
    .pipe(first())
      .subscribe((value) => {
        this.oldValue = value.id;
        console.log(this.chart.nativeElement.offsetWidth,this.chart.nativeElement.offsetHeight)
        this.store.dispatch(
          fetchChartAsSVG({
            data: {
              visualizerId: value.id,
              width: this.chart.nativeElement.offsetWidth,
              height: this.chart.nativeElement.offsetHeight,
            },
          })
        );
      });

  }

  constructor(
    private store: Store<AppState>,
    private sanitizer: DomSanitizer
  ) {}

  ngAfterViewInit(): void {
    this.onResize()
  }

  ngOnDestroy() {
    this.oldValue = -1;
  }

  safe(data) {
    return this.sanitizer.bypassSecurityTrustHtml(data);
  }
}
