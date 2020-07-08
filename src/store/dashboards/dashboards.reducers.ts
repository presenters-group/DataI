import { createReducer, Action, on } from "@ngrx/store";
import { IDashboard } from "./dashboards.models";
import * as fromActions from "./dashboards.actions";
import { MapInterface } from "src/store/core/models/mapinterface";
export interface DashboardsState {
  entities: IDashboard[]
}

export const initialState: DashboardsState = {
  entities: [{
    name: 'dashboard1',
    id: 0,
    isDeleted : false,
    visualizers: [
      {
        visualizationIndex: 0,
        measurements: {
          width: 500.0,
          height: 300.0,
          x: 100.0,
          y: 100.0,
        },
        displayedFilters: [
          {
            filterIndex: 0,
            measurements: {
              width: 100.0,
              height: 100.0,
              x: 100.0,
              y: 200.0,
            },
          },
          {
            filterIndex: 1,
            measurements: {
              width: 100.0,
              height: 100.0,
              x: 300.0,
              y: 150.0,
            }
          }
        ]
      }
    ]
  }],
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
        [data.id]: { ...data },
      },
    };
  })
);

export function reducer(state: DashboardsState | undefined, action: Action) {
  return dashboardsReducer(state, action);
}
