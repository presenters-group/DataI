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
      let measuresColumns = [];
      let dimensionsColumns = [];
      let dateTimeColumns = [];
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
            if (columnEntity.columnType == "DateTime")
            dateTimeColumns.push({
              name: columnEntity.name,
              // content: {
                //   type: "column-dimensions",
                //   tableId: key,
                //   id: columnKey,
                //   name: columnEntity.name,
                // },
              });
            }
            let index = 0
            if(measuresColumns.length)
            {
                dataSources.children.push({ name: "Measures", children: [] });
                dataSources.children[index].children = measuresColumns;
                index++;
            }
            if(dimensionsColumns.length){
              dataSources.children.push({ name: "Dimensions", children: [] });
              dataSources.children[index].children = dimensionsColumns;
              index++;
            }
            if(dateTimeColumns.length){
              dataSources.children.push({ name: "DateTime", children: [] });
              dataSources.children[index].children = dateTimeColumns;
              index++;
            }
            tree.children.push(dataSources);
          }
          return tree;
        }
        );






