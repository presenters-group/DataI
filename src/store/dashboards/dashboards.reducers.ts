import { createReducer, Action, on } from "@ngrx/store";
import { IDashboard } from "./dashboards.models";
import * as fromActions from "./dashboards.actions";
import { MapInterface } from "src/store/core/models/mapinterface";
export interface DashboardsState {
  entities: IDashboard[];
}

export const initialState: DashboardsState = {
  entities: [],
};
const dashboardsReducer = createReducer(
  initialState,
  /**fetching */
  on(fromActions.fetchDashboardsSuccess, (state, { data }) => {
    const entities = data.reduce(
      (entities: MapInterface<IDashboard>, dashboard) => ({
        ...entities,
        [dashboard.id]: dashboard,
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
    fromActions.updateDashboardSuccess,
    fromActions.createDashboardSuccess,
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
  on(fromActions.deleteDashboardSuccess, (state, { data }) => {
    return {
      ...state,
      entities: {
        ...state.entities,
        [data.id]: {...data},
      },
    };
  })
);

export function reducer(state: DashboardsState | undefined, action: Action) {
  return dashboardsReducer(state, action);
}
