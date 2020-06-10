import { createFeatureSelector, createSelector } from "@ngrx/store";
import { AppState } from "..";
import { FiltersState } from "./filters.reducers";
import { selectDataSourcesEntities } from "../data-sources/data-sources.selectors";

export const selectFiltersState = createFeatureSelector<AppState, FiltersState>(
  "filters"
);

export const selectFiltersEntities = createSelector(
  selectFiltersState,
  (state) => state.entities
);

export const selectFiltersTree = createSelector(
  selectFiltersEntities,
  selectDataSourcesEntities,
  (entities, dataSourceEntities) => {
    let tree: any = { name: "filters", children: [] };
    entities.forEach((entity, key) => {
      let filter = {
        name: entity.name,
        content: { type: "filter", id: key },
        children: [],
      };
      let column = dataSourceEntities[entity.dataSource].columns[entity.filteredColumn];
      filter.children.push(
        {
        name : 'column',
        children : [{
        name: column.name,
        content: { type: "column", id: entity.filteredColumn },
      }]
      });
      filter.children.push(
        {
        name : 'data source',
        children : [{
        name: dataSourceEntities[entity.dataSource].name,
        content: { type: "data-source", id: entity.dataSource },
      }]
      });
      tree.children.push(filter);
    });
    return tree;
  }
);
