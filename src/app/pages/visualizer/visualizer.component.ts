import { Component, OnInit, AfterViewInit, Sanitizer } from "@angular/core";
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
import { first } from "rxjs/operators";
import { SafeHtml, DomSanitizer } from "@angular/platform-browser";

@Component({
  selector: "app-visualizer",
  templateUrl: "./visualizer.component.html",
  styleUrls: ["./visualizer.component.scss"],
})
export class VisualizerComponent implements AfterViewInit {
  svg: Observable<SafeHtml> = this.store.select(selectVisualizersChart);
  visualizer: Observable<any> = this.store.select(selectCurrentVisualizer);
  filters: Observable<any> = this.store.select(selectCurrentVisualizerFilters);
  constructor(
    private store: Store<AppState>,
    private httpClient: HttpClient,
    private sanitizer: DomSanitizer
  ) {}

  ngAfterViewInit(): void {
    this.visualizer.pipe(first()).subscribe((value) => {
      let chart = document.getElementById("chart");

      this.store.dispatch(
        fetchChartAsSVG({
          data: {
            visualizerId: value.id,
            width: chart.offsetWidth,
            height: chart.offsetHeight,
          },
        })
      );
    });
  }

  safe(data) {
    return this.sanitizer.bypassSecurityTrustHtml(data);
  }
}
