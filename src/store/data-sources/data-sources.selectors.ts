import { createFeatureSelector, createSelector } from "@ngrx/store";
import { AppState } from "..";
import { DataSourcesState } from "./data-sources.reducers";
import { selectCurrentTapObject } from "../core/selectors/core.selector";

export const selectDataSourcesState = createFeatureSelector<
  AppState,
  DataSourcesState
>("dataSources");

export const selectDataSourcesEntities = createSelector(
  selectDataSourcesState,
  (state) => {
    return state.entities
  }
);

export const selectUndeletedDataSourcesEntities = createSelector(
  selectDataSourcesState,
  (state) => {
    let newState = {}
    for(let key in state.entities){
      if(!state.entities[key].isDeleted)
        newState[key] = {...state.entities[key]}
    }
    return newState
  }
)

export const selectCurrentDataSource = createSelector(
  selectUndeletedDataSourcesEntities,
  selectCurrentTapObject,
  (entities, currentTap) => {
    return entities[currentTap.id];
  }
);


export const selectDataSourcesTree = createSelector(
  selectUndeletedDataSourcesEntities,
  (entities) => {
    let tree: any = { name: "Data Sources", children: [] };
    for (let key in entities) {
      let entity = entities[key];
      let dataSources = {
        name: entity.name,
        content: { type: "data-source", id: key, name: entity.name },
        children: [],
      };
      dataSources.children.push({ name: "Measures", children: [] });
      dataSources.children.push({ name: "Dimensions", children: [] });
      let measuresColumns = [];
      let dimensionsColumns = [];
      for (let columnKey in entity.columns) {
        let columnEntity = entity.columns[columnKey];
        if (columnEntity.columnType == "Measures")
          measuresColumns.push({
            name: columnEntity.name,
            // content: {
            //   type: "column-measures",
            //   tableId: key,
            //   id: columnKey,
            //   name: columnEntity.name,
            // },
          });
        if (columnEntity.columnType == "Dimensions")
          dimensionsColumns.push({
            name: columnEntity.name,
            // content: {
            //   type: "column-dimensions",
            //   tableId: key,
            //   id: columnKey,
            //   name: columnEntity.name,
            // },
          });
      }
      dataSources.children[0].children = measuresColumns;
      dataSources.children[1].children = dimensionsColumns;
      tree.children.push(dataSources);
    }
    return tree;
  }
);






