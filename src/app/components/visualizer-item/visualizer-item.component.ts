import {
  Component,
  Input,
  AfterViewInit,
  OnDestroy,
  ViewChild,
  AfterViewChecked,
  Renderer2,
} from "@angular/core";
import { DomSanitizer, SafeHtml } from "@angular/platform-browser";
import { Store } from "@ngrx/store";
import { AppState } from "src/store";

import { Actions } from "@ngrx/effects";

@Component({
  selector: "app-visualizer-item",
  templateUrl: "./visualizer-item.component.html",
  styleUrls: ["./visualizer-item.component.scss"],
})

//TODO Complete the tooltips user renderer.
export class VisualizerItemComponent implements AfterViewChecked {
  chart;
  change: boolean = false;
  toolTip: { value: string; x: number; y: number };
  @Input() set svg(value) {
    console.log("changed;");
    this.chart = value;
    this.change = true;
  }
  chartData;
  @Input() set metaData(value) {
    if (Array.isArray(value)) this.chartData = value;
  }
  @Input() zoom: number = 1;
  constructor(
    private sanitizer: DomSanitizer,
    private store: Store<AppState>,
    private renderer: Renderer2
  ) {}

  ngAfterViewChecked() {
    if (this.change && document.getElementById("chartElement")) {
      document.getElementById("chartElement").innerHTML = this.chart;
      setTimeout(() => {
        let parent = this.renderer.createElement("div");
        this.renderer.addClass(parent, "tipTool-container");
        let content;
        for (let i = 0; i < this.chartData.length; i++) {
          let element = document.getElementById(`${i}`);
          if (element) {
            element.addEventListener("mouseover", () => {
              content = this.renderer.createText(this.chartData[i]);
              this.renderer.appendChild(document.body, parent);

              this.renderer.setStyle(
                parent,
                "left",
                `${element.getBoundingClientRect().x + 30}px`
              );
              this.renderer.setStyle(
                parent,
                "top",
                `${element.getBoundingClientRect().y + 30}px`
              );
              this.renderer.appendChild(parent, content);
              // this.toolTip = {
              //   value : this.chartData[i],
              //   x: element.getBoundingClientRect().x,
              //   y: element.getBoundingClientRect().y
              // }
              // console.log(this.toolTip)
            });
            element.addEventListener("mouseleave", () => {
              this.renderer.removeChild(document.body, parent);
              this.renderer.removeChild(parent, content);
            });
          }
        }
      }, 500);
      this.change = false;
    }
  }

  safe(data) {
    return this.sanitizer.bypassSecurityTrustHtml(data);
  }
}
