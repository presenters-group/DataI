import { createFeatureSelector, createSelector, select } from "@ngrx/store";
import { AppState } from "..";
import { VisualizersState } from "./visualizers.reducers";
import { selectFiltersEntities } from "../filters/filters.selectors";
import { selectDataSourcesEntities } from "../data-sources/data-sources.selectors";
import { selectCurrentTapObject } from '../core/selectors/core.selector';

export const selectVisualizersState = createFeatureSelector<
  AppState,
  VisualizersState
>("visualizers");

export const selectVisualizersEntities = createSelector(
  selectVisualizersState,
  (state) => state.entities
);

export const selectVisualizersTree = createSelector(
  selectVisualizersEntities,
  selectDataSourcesEntities,
  selectFiltersEntities,
  (entities, dataSourcesEntities, filtersEntities) => {
    let tree: any = { name: "Visualizers", children: [] };
      for(let key in entities)
    // entities.forEach((entity, key) =>
    {
      let entity = entities[key]
      let visualizers = {
        name: entity.name,
        content: { type: "visualizer", id: key, name: entity.name },
        children: [],
      };
      let columns = { name: "Columns", children: [] };
      entity.usedColumns.forEach((value, key) => {

        columns.children.push({
          name: dataSourcesEntities[entity.data].columns[value].name,
        });
      });

      let row = { name: "Row", children: [] };
      console.log(dataSourcesEntities[entity.data].columns[entity.xColumn]);
      console.log(entity.data);
      console.log(entity.xColumn);
      row.children.push({
        name: dataSourcesEntities[entity.data].columns[entity.xColumn].name,
      });

      let filters = { name: "Filters", children: [] };
      entity.filters.forEach(({id: value}, key) => {
        let filter = filtersEntities[value];
        filters.children.push({
          name: filter.name,
          content: {id : value , type : 'filter' , name : filter.name}
        });
      });

      visualizers.children.push(columns);
      visualizers.children.push(row);
      visualizers.children.push(filters);

      tree.children.push(visualizers);
    };
    return tree;
  }
);

export const selectCurrentVisualizer = createSelector(
  selectVisualizersState,
  selectCurrentTapObject,
  (state,current) => {
    return state.entities[current.id]
  }
);


export const selectVisualizersChart = createSelector(
  selectCurrentVisualizer,
  (visualizer) => {
    return visualizer.chartSvg || '';
  }
);

export const selectCurrentVisualizerFilters = createSelector(
  selectCurrentVisualizer,
  selectFiltersEntities,
  (visualizer,AllFilters) => {
    let filters = [];

    for (let filter of visualizer.filters)
      filters.push(AllFilters[filter.id])
    return filters;
  }
);
