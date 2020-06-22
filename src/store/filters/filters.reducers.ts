import { createReducer, Action, on } from "@ngrx/store";
import { IFilter } from "./filters.models";
import * as fromActions from "./filters.actions";
import { MapInterface } from "src/store/core/models/mapinterface";
export interface FiltersState {
  entities: IFilter[];
}

export const initialState: FiltersState = {
  entities: [
    {
      name: "filter1",
      dataSource: 0,
      filteredColumn: 1,
      initValue: 10,
      type: "Equality",
      isDeleted: false,
    },
    {
      name: "filter2",
      dataSource: 0,
      filteredColumn: 2,
      initValue: 15,
      type: "LessThan",
      isDeleted: false,
    },
    {
      name: "filter3",
      dataSource: 0,
      filteredColumn: 0,
      initValue: "Laptop",
      type: "Equality",
      isDeleted: false,
    },
  ],
};
const filtersReducer = createReducer(
  initialState,
  /**fetching */
  on(fromActions.fetchFiltersSuccess, (state, { data }) => {
    const entities = data.reduce(
      (entities: MapInterface<IFilter>, filter) => ({
        ...entities,
        [filter.id]: filter,
      }),
      {}
    );

    return {
      ...state,
      entities,
    };
  }),

  /**Updating and Creating */
  on(
    fromActions.updateFilterSuccess,
    fromActions.createFilterSuccess,
    (state, { data }) => {
      const entities = {
        ...state.entities,
        [data.id]: data,
      };

      return {
        ...state,
        entities,
      };
    }
  ),

  /**Deleting */
  on(fromActions.deleteFilterSuccess, (state, { id }) => {
    const { [id]: deletedFilter, ...entities } = state.entities;

    return {
      ...state,
      entities: {
        [id]: { ...deletedFilter, isDeleted: true },
        ...entities,
      },
    };
  })
);

export function reducer(state: FiltersState | undefined, action: Action) {
  return filtersReducer(state, action);
}
