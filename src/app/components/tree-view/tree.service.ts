import { Injectable } from '@angular/core';
import { Store, State } from '@ngrx/store';
import { AppState } from 'src/store';
import { selectFiltersTree } from 'src/store/filters/filters.selectors';
import { Observable } from 'rxjs';
import { selectDataSourcesTree } from 'src/store/data-sources/data-sources.selectors';
import { selectDashboardsTree } from 'src/store/dashboards/dashboards.selectors';
import { selectVisualizersTree } from 'src/store/visualizers/visualizers.selectors';

@Injectable({
  providedIn: 'root'
})
export class TreeService {

  constructor(private store: Store<AppState>) { }

  fillOut(type : 'filters' | 'dashboards' | 'data-sources' | 'visualizers') : Observable<any>{
    switch(type)
    {
      case 'filters':
      return this.fillOutFilters();
      case 'dashboards':
      return this.fillOutDashboards();
      case 'data-sources':
      return this.fillOutDataSources();
      case 'visualizers':
      return this.fillOutVisualizers();
      default:
        return new Observable();

    }
  }
  fillOutDashboards(){
    return this.store.select(selectDashboardsTree);
  }
  fillOutDataSources(){
    return this.store.select(selectDataSourcesTree)
  }
  fillOutVisualizers(){
    return this.store.select(selectVisualizersTree)
  }
  fillOutFilters(){
    return this.store.select(selectFiltersTree)
  }
}
