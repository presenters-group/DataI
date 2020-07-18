import {
  Component,
  Input,
  AfterViewInit,
  OnDestroy,
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
export class VisualizerItemComponent{
  @Input() svg : SafeHtml;
  @Input() zoom: number = 1;
  constructor(
    private sanitizer: DomSanitizer,
    private store: Store<AppState>,
  ) {}

  safe(data) {
    return this.sanitizer.bypassSecurityTrustHtml(data);
  }
}
