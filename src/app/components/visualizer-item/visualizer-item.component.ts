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
export class VisualizerItemComponent implements AfterViewInit, OnDestroy {
  // @ViewChild("chart") chart;
  // id: number;
  // done: boolean = false;
  // destroyed$ = new Subject<boolean>();

  @Input() svg : SafeHtml;
  // @Input() set visualizerId(id: number) {
  //   console.log(this.done);
  //   if (this.done) {
  //     this.store.dispatch(
  //       fetchChartAsSVG({
  //         data: {
  //           visualizerId: id,
  //           width: this.chart.nativeElement.offsetWidth,
  //           height: this.chart.nativeElement.offsetHeight,
  //         },
  //       })
  //     );

  //     this.svg = this.store.select(selectVisualizersChart, {
  //       visualizerId: id,
  //     });
  //   }
  //   this.id = id;
  // }
  // svg: Observable<SafeHtml>;

  constructor(
    private sanitizer: DomSanitizer,
    private store: Store<AppState>,
  ) {}

  ngOnDestroy() {
    // this.destroyed$.complete();

    // this.destroyed$.next(false);
    // this.destroyed$.complete();
  }
  ngAfterViewInit() {
    // this.onResize();

    // this.svg = this.store.select(selectVisualizersChart, {
    //   visualizerId: this.id,
    // });

    // this.svg.subscribe(() => {
    //   this.onResize();
    // });

    // this.done = true;


    // this.update$
    // .pipe(
    //   ofType(
    //     updateFilterInVisualizerSuccess,
    //     addFilterToVisualizerSuccess,
    //     removeFilterFromVisualizerSuccess,
    //     updateVisualizerSuccess
    //   ),
    //   takeUntil(this.destroyed$)
    // )
    // .subscribe(() => {
    //   this.onResize();
    // });
  }
  // @HostListener("window:resize", ["$event"])
  // onResize() {
  //   this.store.dispatch(
  //     fetchChartAsSVG({
  //       data: {
  //         visualizerId: this.id,
  //         width: this.chart.nativeElement.offsetWidth,
  //         height: this.chart.nativeElement.offsetHeight,
  //       },
  //     })
  //   );
  // }

  safe(data) {
    return this.sanitizer.bypassSecurityTrustHtml(data);
  }
}
