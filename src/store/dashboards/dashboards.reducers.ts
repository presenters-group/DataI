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
      console.log(data)
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
  }),

  on(fromActions.fetchDashboardSVGsSuccess, (state, { data }) => {
    let newDashboard = JSON.parse(
      JSON.stringify(state.entities[data.dashboardId])
    );
    for (let chart of data.charts) {
      newDashboard.visualizers.find(
        (x) => x.visualizationId == chart.visualizerId
      ).chart = chart.svg;
      newDashboard.visualizers.find(
        (x) => x.visualizationId == chart.visualizerId
      ).mettaData = chart.metaData;
      newDashboard.visualizers.find(
        (x) => x.visualizationId == chart.visualizerId
      ).zoom = 100;
    }

    return {
      ...state,
      entities: {
        ...state.entities,
        [data.dashboardId]: { ...newDashboard },
      },
    };
  }),

  on(fromActions.changeVisualizerInDashboardZoom, (state, { data }) => {
    let newDashboard = JSON.parse(
      JSON.stringify(state.entities[data.dashboardId])
    );
    newDashboard.visualizers.find(
      (x) => x.visualizationId == data.visualizerId
    ).zoom = data.zoom;

    return {
      ...state,
      entities: {
        ...state.entities,
        [data.dashboardId]: { ...newDashboard },
      },
    };
  }),

  on(fromActions.updateFilterInDashboardSuccess, (state, { data }) => {
    let newDashboard = JSON.parse(
      JSON.stringify(state.entities[data.dashboardId])
    );
    newDashboard.filters = newDashboard.filters.map((x) => {
      if (x.id == data.id) {
        return {
          id: data.id,
          visioId: data.visioId,
          value: data.value,
          isActive: data.isActive,
          measurements: data.measurements
        };
      } else return x;
    });
    return {
      ...state,
      entities: {
        ...state.entities,
        [data.dashboardId]: { ...newDashboard },
      },
    };
  })
);

export function reducer(state: DashboardsState | undefined, action: Action) {
  return dashboardsReducer(state, action);
}
