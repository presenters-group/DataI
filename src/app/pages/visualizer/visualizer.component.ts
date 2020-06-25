import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Store } from '@ngrx/store';
import { AppState } from 'src/store';
import { selectCurrentVisualizer, selectCurrentVisualizerFilters } from 'src/store/visualizers/visualizers.selectors';
import { fetchChartAsSVGSuccess } from 'src/store/visualizers';
import { TEST_SVG_CHART } from 'src/utils/static.chart';

@Component({
  selector: 'app-visualizer',
  templateUrl: './visualizer.component.html',
  styleUrls: ['./visualizer.component.scss']
})
export class VisualizerComponent implements OnInit {
  visualizer : Observable<any> = this.store.select(selectCurrentVisualizer);
  filters : Observable<any> = this.store.select(selectCurrentVisualizerFilters);
  constructor(private store :Store<AppState>) { }

  ngOnInit(): void {
    
    this.store.dispatch(fetchChartAsSVGSuccess({data : { svg : TEST_SVG_CHART, visualizerId: 0}}))
    this.visualizer.subscribe((value)=>{
      console.log(value.chartSvg)
      document.getElementById('chart').innerHTML = value.chartSvg
    })

  }

  consol(data){
    console.log(data);
    return data
  }

}
