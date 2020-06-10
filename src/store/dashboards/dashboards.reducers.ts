import { createReducer, Action, on } from "@ngrx/store";
import { IDashboard } from "./dashboards.models";
import * as fromActions from "./dashboards.actions";
import { MapInterface } from "src/store/core/models/mapinterface";
export interface DashboardsState {
  entities: IDashboard[];
}

export const initialState: DashboardsState = {
  entities: [
    {
      name: "dashboard1",
      visualizers: [
        {
          visualizationIndex: 0,
          measurements: {
            width: 1.0,
            height: 1.0,
            x: 1.0,
            y: 1.0,
          },
          displayedFilters: [
            {
              filterIndex: 0,
              measurements: {
                width: 0.0,
                height: 0.0,
                x: 0.0,
                y: 0.0,
              },
            },
            {
              filterIndex: 1,
              measurements: {
                width: 1.0,
                height: 1.0,
                x: 1.0,
                y: 1.0,
              },
            },
          ],
        },
      ],
    },
  ],
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
  on(fromActions.deleteDashboardSuccess, (state, { id }) => {
    const { [id]: deletedDashboard, ...entities } = state.entities;

    return {
      ...state,
      entities: {
        [id]: { ...deletedDashboard, isDeleted: true },
        ...entities,
      },
    };
  })
);

export function reducer(state: DashboardsState | undefined, action: Action) {
  return dashboardsReducer(state, action);
}
