import {
  Component,
  Input,
  AfterViewInit,
  OnDestroy,
  ViewChild,
  AfterViewChecked,
  Renderer2,
  ElementRef,
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
  @ViewChild("chartElement") chartElement;
  chart;
  change: boolean = false;
  @Input() set svg(value) {
    let forDelete = document.getElementsByClassName('tipTool-container');
    for(let element of (forDelete as any))
      this.renderer.removeChild(document.body,element);
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
    private renderer: Renderer2,
  ) {}

  ngAfterViewChecked() {
    // let el = document.getElementById("chartElement" + (this.visualizerId ? this.visualizerId : ''))
    if (this.change && this.chartElement) {
      this.chartElement.nativeElement.innerHTML = this.chart;
      setTimeout(() => {
        let parent = this.renderer.createElement("div");
        this.renderer.addClass(parent, "tipTool-container");
        let content;
        for (let i = 0; i < this.chartData.length; i++) {
          let elements = this.chartElement.nativeElement.getElementsByClassName(`${i}`);
          for(let element of elements){
          if (element) {
            // console.log(element)
            element.addEventListener("mouseover", ($event) => {
              // console.log($event)
              content = this.chartData[i];
              // content = this.renderer.createText(this.chartData[i]);
              this.renderer.appendChild(document.body, parent);

              this.renderer.setStyle(
                parent,
                "left",
                `${$event.pageX}px`
              );
              this.renderer.setStyle(element, "stroke-width", "5px");

              this.renderer.setStyle(
                parent,
                "top",
                `${$event.pageY}px`
              );
                parent.innerHTML = content;
              // this.renderer.appendChild(parent, content);
            });
            element.addEventListener("mouseleave", () => {
              this.renderer.removeChild(document.body, parent);
              this.renderer.removeChild(parent, content);

              this.renderer.setStyle(element, "stroke-width", "");
            });
          }
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
