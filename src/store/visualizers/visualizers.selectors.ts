import { createFeatureSelector, createSelector } from "@ngrx/store";
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


export const selectUndeletedVisualizersEntities = createSelector(
  selectVisualizersState,
  (state) => {
    let newState = {}
    for(let key in state.entities){
      if(!state.entities[key].isDeleted)
        newState[key] = {...state.entities[key]}
    }
    return newState
  }
)




export const selectVisualizersTree = createSelector(
  selectUndeletedVisualizersEntities,
  selectDataSourcesEntities,
  selectFiltersEntities,
  (entities, dataSourcesEntities, filtersEntities) => {
    let tree: any = { name: "Visualizers", children: [] };
      for(let key in entities)
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
      row.children.push({
        name: dataSourcesEntities[entity.data].columns[entity.xColumn].name,
      });

      let filters = { name: "Filters", children: [] };
      entity.filters.forEach((value, key) => {

        let filter = filtersEntities[value.id];
        console.log(value.id,filtersEntities,filter)
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
    return current && current.id != undefined ? state.entities[current.id] : null
  }
);


export const selectVisualizersChart = createSelector(
  selectVisualizersEntities,
  (entities,{visualizerId}) => {
    return entities[visualizerId] ? entities[visualizerId].chartSvg || '' : null;
  }
);




export const selectAllCurrentVisualizerFilters = createSelector(
  selectCurrentVisualizer,
  selectFiltersEntities,
  (visualizer,allFilters)=>{
    let filters = [];

    for(let filter of Object.keys(allFilters))
      {
        if(allFilters[filter].dataSource == visualizer.data )
        filters.push(allFilters[filter]);
      }
      return filters;
  }

)


export const selectCurrentVisualizerFilters = createSelector(
  selectCurrentVisualizer,
  selectFiltersEntities,
  (visualizer,AllFilters) => {
    let filters = [];

    for (let filter of visualizer.filters)
      filters.push({...AllFilters[filter.id],isActive: filter.isActive, value:filter.value})
    return filters;
  }
);
