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
  (state) => state.entities
);

export const selectCurrentDataSource = createSelector(
  selectDataSourcesEntities,
  selectCurrentTapObject,
  (entities, currentTap) => {
    return entities[currentTap.id];
  }
);

export const selectDataSourcesTree = createSelector(
  selectDataSourcesEntities,
  (entities) => {
    let tree: any = { name: "Data Sources", children: [] };
    // entities.forEach((entity, key) =>
    for (let key in entities) {
      let entity = entities[key];
      let dataSources = {
        name: entity.name,
        content: { type: "data-source", id: key, name: entity.name },
        children: [],
      };
      console.log(entity);
      dataSources.children.push({ name: "Measures", children: [] });
      dataSources.children.push({ name: "Dimensions", children: [] });
      console.log(dataSources);
      let measuresColumns = [];
      let dimensionsColumns = [];
      // entity.columns.forEach((entity,columnKey)=>
      for (let columnKey in entity.columns) {
        let columnEntity = entity.columns[columnKey];
        if (columnEntity.columnType == "Measures")
          measuresColumns.push({
            name: columnEntity.name,
            content: {
              type: "column-measures",
              tableId: key,
              id: columnKey,
              name: columnEntity.name,
            },
          });
        if (columnEntity.columnType == "Dimensions")
          dimensionsColumns.push({
            name: columnEntity.name,
            content: {
              type: "column-dimensions",
              tableId: key,
              id: columnKey,
              name: columnEntity.name,
            },
          });
      }
      dataSources.children[0].children = measuresColumns;
      dataSources.children[1].children = dimensionsColumns;
      tree.children.push(dataSources);
    }
    return tree;
  }
);
