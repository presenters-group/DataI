import { createFeatureSelector, createSelector } from "@ngrx/store";
import { AppState } from "..";
import { DataSourcesState } from "./data-sources.reducers";

export const selectDataSourcesState = createFeatureSelector<
  AppState,
  DataSourcesState
>("dataSources");

export const selectDataSourcesEntities = createSelector(
  selectDataSourcesState,
  (state) => state.entities
);


export const selectDataSourcesTree = createSelector(
  selectDataSourcesEntities,
  (entities) => {
    let tree: any = { name: "Data Sources", children: [] };
    entities.forEach((entity, key) => {
      let dataSources = {
        name: entity.name,
        content: { type: "data-source", id: key },
        children: [],
      };
      console.log(entity);
      dataSources.children.push({name:'Measures' , children: []})
      dataSources.children.push({name:'Dimensions' , children: []})
      console.log(dataSources)
      let measuresColumns = [];
      let dimensionsColumns = [];
      entity.columns.forEach((entity,key)=>{
        if(entity.columnType == 'Measures')
          measuresColumns.push({name :entity.name,content: {type: 'column',id: key}});
        if(entity.columnType == 'Dimensions')
          dimensionsColumns.push({name :entity.name,content: {type: 'column',id: key}});

      })
      dataSources.children[0].children = measuresColumns;
      dataSources.children[1].children = dimensionsColumns;
      tree.children.push(dataSources);
    });
    return tree;
  }
);
