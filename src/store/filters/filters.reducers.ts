import { createReducer, Action, on } from "@ngrx/store";
import { IFilter } from "./filters.models";
import * as fromActions from "./filters.actions";
import { MapInterface } from "src/store/core/models/mapinterface";
export interface FiltersState {
  entities: IFilter[];
}

export const initialState: FiltersState = {
  entities: [],
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
  on(fromActions.deleteFilterSuccess, (state, { data }) => {
    return {
      ...state,
      entities: {
        ...state.entities,
        [data.id]: {...data},
      },
    };
  })
);

export function reducer(state: FiltersState | undefined, action: Action) {
  return filtersReducer(state, action);
}
