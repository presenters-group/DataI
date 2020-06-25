import { Component, OnInit, AfterViewInit } from "@angular/core";
import { Observable } from "rxjs";
import { Store } from "@ngrx/store";
import { AppState } from "src/store";
import {
  selectCurrentVisualizer,
  selectCurrentVisualizerFilters,
} from "src/store/visualizers/visualizers.selectors";
import { fetchChartAsSVGSuccess, fetchChartAsSVG } from "src/store/visualizers";
import { TEST_SVG_CHART } from "src/utils/static.chart";
import { HttpClient } from '@angular/common/http';

@Component({
  selector: "app-visualizer",
  templateUrl: "./visualizer.component.html",
  styleUrls: ["./visualizer.component.scss"],
})
export class VisualizerComponent implements AfterViewInit {
  visualizer: Observable<any> = this.store.select(selectCurrentVisualizer);
  filters: Observable<any> = this.store.select(selectCurrentVisualizerFilters);
  constructor(private store: Store<AppState>,private httpClient: HttpClient) {}

  ngAfterViewInit(): void {
    this.visualizer.subscribe((value) => {
      let chart = (document.getElementById("chart"));
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

    this.visualizer.subscribe((value) => {
      let chart = document.getElementById("chart");
          this.httpClient.put(`http://127.0.0.1:8000/data/chart/`, {
            visualizerId: value.id,
            width: chart.offsetWidth,
            height: chart.offsetHeight,
          }).subscribe((value)=>{
      console.log(value)
      chart.innerHTML = (value as any).svg;
    })
    });
  }

  consol(data) {
    console.log(data);
    return data;
  }
}
