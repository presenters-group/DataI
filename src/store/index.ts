// export * from "./actions";
import * as fromCore from './core';
import * as fromDataSources from './data-sources'
import * as fromVisualizers from './visualizers'
export const reducers = {
  core : fromCore.reducer,
  dataSources : fromDataSources.reducer,
  visualizers: fromVisualizers.reducer
}

export const effects = [

]
