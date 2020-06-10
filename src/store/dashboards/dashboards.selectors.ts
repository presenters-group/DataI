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
    entities.forEach((entity, key) => {
      let dashboards = {
        name: entity.name,
        content: { type: "dashboards", id: key },
        children: [],
      };
      let visualizers = [];
      entity.visualizers.forEach((value, key) => {
        let visualizer = {
          name: visualizersEntities[value.visualizationIndex].name,
          content: { type: "visualizer", id: key },
          children: [],
        };
        let filters = [];
        value.displayedFilters.forEach((value, key) => {
          filters.push({
            name: filtersEntities[value.filterIndex].name,
            content: { type: "filters", id: key },
          });
        });
        visualizer.children.push(...filters);
        visualizers.push(visualizer);
      });
      dashboards.children.push(...visualizers);
      console.log(dashboards);
      tree.children.push(dashboards);
    });
    return tree;
  }
);
