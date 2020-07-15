import { createFeatureSelector, createSelector } from "@ngrx/store";
import { AppState } from "..";
import { FiltersState } from "./filters.reducers";
import { selectDataSourcesEntities, selectCurrentDataSource } from "../data-sources/data-sources.selectors";
import { selectCurrentTapObject } from '../core/selectors/core.selector';
export const selectFiltersState = createFeatureSelector<AppState, FiltersState>(
  "filters"
);

export const selectFiltersEntities = createSelector(
  selectFiltersState,
  (state) => state.entities
);


export const selectUndeletedFiltersEntities = createSelector(
  selectFiltersState,
  (state) => {
    let newState = {}
    for(let key in state.entities){
      if(!state.entities[key].isDeleted)
        newState[key] = {...state.entities[key]}
    }
    return newState
  }
)


export const selectFiltersTree = createSelector(
  selectUndeletedFiltersEntities,
  selectDataSourcesEntities,
  (entities, dataSourceEntities) => {
    let tree: any = { name: "Filters", children: [] };
    for (let key in entities) {
      let entity = entities[key];
      let filter = {
        name: entity.name,
        content: { type: "filter", id: key, name: entity.name },
        children: [],
      };
      let column =
        dataSourceEntities[entity.dataSource].columns[entity.filteredColumn];
      filter.children.push({
        name: "column",
        children: [
          {
            name: column.name,
            content: {
              type: "column",
              id: entity.filteredColumn,
              name: column.name,
            },
          },
        ],
      });
      filter.children.push({
        name: "data source",
        children: [
          {
            name: dataSourceEntities[entity.dataSource].name,
            content: {
              type: "data-source",
              id: entity.dataSource,
              name: dataSourceEntities[entity.dataSource].name,
            },
          },
        ],
      });
      tree.children.push(filter);
    }
    return tree;
  }
);


export const selectFiltersForDataSource = createSelector(
  selectUndeletedFiltersEntities,
  (state,props) => {
      console.log(props.dataSource,)
      return props.dataSource != '' ? objectFilter(state,(value)=>value.dataSource != props.dataSource) : {}
  });

export const selectCurrentFilter = createSelector(
  selectFiltersState,
  selectCurrentTapObject,
  (state,current) => {return current && current.id != undefined ? state.entities[current.id] : null}
);


export const selectCurrentFilterDataSource = createSelector(
  selectDataSourcesEntities,
  selectCurrentFilter,
  (state,{dataSource}) => state[dataSource]
);



function objectFilter (obj, predicate){
    let result = {}, key;
    console.log(obj,predicate)

    for (key in obj) {
        if (obj.hasOwnProperty(key) && !predicate(obj[key])) {
            result[key] = obj[key];
        }
    }

    return result;
};


export const selectCurrentDataSourceFilters = createSelector(
  selectCurrentDataSource,
  selectFiltersEntities,
  (dataSource,allFilters) => {
    let filters = [];
    for (let filter of dataSource.filters){
      console.log({...allFilters[filter.id] ,value: filter.value, active : filter.isActive})
        filters.push({...allFilters[filter.id] ,value: filter.value, active : filter.isActive})
    }
    return filters;
  }
);




export const selectAllCurrentDataSourceFilters = createSelector(

  selectCurrentDataSource,
  selectFiltersEntities,
  (dataSource,allFilters)=>{
    let filters = [];

    for(let filter of Object.keys(allFilters))
      {
        if(allFilters[filter].dataSource == dataSource.id )
        filters.push(allFilters[filter]);
      }
      return filters;
  }

)



