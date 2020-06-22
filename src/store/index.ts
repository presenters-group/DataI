// export * from "./actions";
import * as fromCore from './core';
import * as fromDataSources from './data-sources'
import * as fromVisualizers from './visualizers'
import * as fromDashboards from './dashboards'
import * as fromFilters from './filters'
import { ActionReducerMap } from '@ngrx/store';
import { CoreState } from './core';
import { DataSourcesState } from './data-sources';
import { VisualizersState } from './visualizers';
import { FiltersState } from './filters';
import { DashboardsState } from './dashboards';
export interface AppState{
  core : CoreState;
  dataSources : DataSourcesState;
  visualizers : VisualizersState;
  filters : FiltersState;
  dashboards : DashboardsState
}
export const reducers : ActionReducerMap<AppState> = {
  core : fromCore.reducer,
  dataSources : fromDataSources.reducer,
  visualizers: fromVisualizers.reducer,
  filters : fromFilters.reducer,
  dashboards : fromDashboards.reducer
}

export const effects = [

]
