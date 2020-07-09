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
export class VisualizerComponent {
  visualizer: Observable<any> = this.store.select(selectCurrentVisualizer);
  filters: Observable<any> = this.store.select(selectCurrentVisualizerFilters);

  constructor(
    private store: Store<AppState>,
  ) {}

}
