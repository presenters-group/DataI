import { createFeatureSelector, createSelector } from "@ngrx/store";
import { AppState } from "..";
import { DashboardsState } from "./dashboards.reducers";
import { selectVisualizersEntities } from "../visualizers/visualizers.selectors";
import { selectDataSourcesEntities } from "../data-sources/data-sources.selectors";
import { selectFiltersEntities } from "../filters/filters.selectors";
import { selectCurrentTapObject } from '../core/selectors/core.selector';

export const selectDashboardsState = createFeatureSelector<
  AppState,
  DashboardsState
>("dashboards");



export const selectDashboardsEntities = createSelector(
  selectDashboardsState,
  (state) => state.entities
);


export const selectUndeletedDashboardsEntities = createSelector(
  selectDashboardsState,
  (state) => {
    let newState = {}
    for(let key in state.entities){
      if(!state.entities[key].isDeleted)
        newState[key] = {...state.entities[key]}
    }
    return newState
  }
)



export const selectDashboardsTree = createSelector(
  selectUndeletedDashboardsEntities,
  selectVisualizersEntities,
  selectFiltersEntities,
  (entities, visualizersEntities, filtersEntities) => {
    let tree: any = { name: "Dashboards", children: [] };
    for(let key in entities)
    {
      let entity = entities[key]
      let dashboards = {
        name: entity.name,
        content: { type: "dashboard", id: key ,name: entity.name},
        children: [],
      };
      let visualizers = [];
      entity.visualizers.forEach((value, key) => {
        let visualizerEntity  = visualizersEntities[value.visualizationId]
        console.log(visualizersEntities,visualizerEntity)
        let visualizer = {
          name: visualizerEntity.name,
          content: { type: "visualizer", id: value.visualizationId ,name: visualizerEntity.name},
          children: [],
        };
        let filters = [];
        entity.filters.filter((filter)=>filter.visioId == value.visualizationId).forEach((value, key) => {
          let filterEntity = filtersEntities[value.id]
          filters.push({
            name: filterEntity.name,
            content: { type: "filter", id: key ,name: filterEntity.name},
          });
        });
        visualizer.children.push(...filters);
        visualizers.push(visualizer);
      });
      dashboards.children.push(...visualizers);
      tree.children.push(dashboards);
    };
    console.log('plaplapla: ',tree)
    return tree;
  }
);


export const selectCurrentDashboard = createSelector(
  selectDashboardsState,
  selectCurrentTapObject,
  (state,current) => {return current && current.id != undefined ? state.entities[current.id] : null}
);
