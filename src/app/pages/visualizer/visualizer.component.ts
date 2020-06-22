import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Store } from '@ngrx/store';
import { AppState } from 'src/store';
import { selectCurrentVisualizer, selectCurrentVisualizerFilters } from 'src/store/visualizers/visualizers.selectors';

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
  }

}
