import { createFeatureSelector, createSelector } from "@ngrx/store";
import { AppState } from "..";
import { DashboardsState } from "./dashboards.reducers";
import { selectVisualizersEntities } from "../visualizers/visualizers.selectors";
import { selectDataSourcesEntities } from "../data-sources/data-sources.selectors";
import { selectFiltersEntities } from "../filters/filters.selectors";

export const selectDashboardsState = createFeatureSelector<
  AppState,
  DashboardsState
>("dashboards");

export const selectDashboardsEntities = createSelector(
  selectDashboardsState,
  (state) => state.entities
);

export const selectDashboardsTree = createSelector(
  selectDashboardsEntities,
  selectVisualizersEntities,
  selectFiltersEntities,
  (entities, visualizersEntities, filtersEntities) => {
    let tree: any = { name: "Dashboards", children: [] };
    for(let key in entities)
    // entities.forEach((entity, key) =>
    {
      let entity = entities[key]
      let dashboards = {
        name: entity.name,
        content: { type: "dashboard", id: key ,name: entity.name},
        children: [],
      };
      let visualizers = [];
      entity.visualizers.forEach((value, key) => {
        let visualizerEntity  = visualizersEntities[value.visualizationIndex]
        let visualizer = {
          name: visualizerEntity.name,
          content: { type: "visualizer", id: value.visualizationIndex ,name: visualizerEntity.name},
          children: [],
        };
        let filters = [];
        value.displayedFilters.forEach((value, key) => {
          let filterEntity = filtersEntities[value.filterIndex]
          filters.push({
            name: filterEntity.name,
            content: { type: "filters", id: key ,name: filterEntity.name},
          });
        });
        visualizer.children.push(...filters);
        visualizers.push(visualizer);
      });
      dashboards.children.push(...visualizers);
      console.log(dashboards);
      tree.children.push(dashboards);
    };
    return tree;
  }
);
