import { Component, OnInit, Input, HostListener, ViewChild, AfterViewInit } from '@angular/core';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';
import { Observable } from 'rxjs';
import { Store } from '@ngrx/store';
import { AppState } from 'src/store';
import { selectVisualizersChart } from 'src/store/visualizers/visualizers.selectors';
import { fetchChartAsSVG } from 'src/store/visualizers';

@Component({
  selector: 'app-visualizer-item',
  templateUrl: './visualizer-item.component.html',
  styleUrls: ['./visualizer-item.component.scss']
})
export class VisualizerItemComponent implements AfterViewInit {
  @ViewChild('chart') chart;
  id: number;
  done: boolean = false
  @Input() set visualizerId(id : number){
    console.log(this.done)
    if(this.done){
      this.store.dispatch(
        fetchChartAsSVG({
          data: {
            visualizerId: id,
            width: this.chart.nativeElement.offsetWidth,
            height: this.chart.nativeElement.offsetHeight,
          },
        })
      );
    this.svg = this.store.select(selectVisualizersChart,{visualizerId : id});
    }
    this.id = id;
  };
  svg: Observable<SafeHtml>;

  constructor(private sanitizer : DomSanitizer,private store:Store<AppState>) { }


  ngAfterViewInit(){
    this.onResize();


    this.svg = this.store.select(selectVisualizersChart,{visualizerId : this.id});

    this.svg.subscribe(()=>{
      this.onResize()
    })


    this.done = true;
  }
  @HostListener('window:resize', ['$event'])
  onResize() {
        this.store.dispatch(
          fetchChartAsSVG({
            data: {
              visualizerId: this.id,
              width: this.chart.nativeElement.offsetWidth,
              height: this.chart.nativeElement.offsetHeight,
            },
          })
        );
  }


  safe(data) {
    return this.sanitizer.bypassSecurityTrustHtml(data);
  }
}
