import { createReducer, Action, on } from "@ngrx/store";
import { IVisualizer } from "./visualizers.models";
import * as fromActions from "./visualizers.actions";
import { MapInterface } from "src/store/core/models/mapinterface";
import { TEST_SVG_CHART } from "src/utils/static.chart";
export interface VisualizersState {
  entities: IVisualizer[];
}

export const initialState: VisualizersState = {
  entities: [
    {
      name: "visualization1",
      data: 0,
      usedColumns: [0, 2],
      xColumn: 1,
      chart: "BoundaryLineChart",
      filters: [0, 1],
      isDeleted: false,
    },
  ],
};
const visualizersReducer = createReducer(
  initialState,
  /**fetching */
  on(fromActions.fetchVisualizersSuccess, (state, { data }) => {
    const entities = data.reduce(
      (entities: MapInterface<IVisualizer>, visualizer) => ({
        ...entities,
        [visualizer.id]: visualizer,
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
    fromActions.updateVisualizerSuccess,
    fromActions.createVisualizerSuccess,
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
  on(fromActions.deleteVisualizerSuccess, (state, { data }) => {
    return {
      ...state,
      entities: {
        ...state.entities,
        [data.id]: { ...data },
      },
    };
  }),

  on(fromActions.fetchChartAsSVGSuccess, (state, { data }) => {
    let newState = {
      ...state,
      entities: {
        ...state.entities,
        [data.visualizerId]: {
          ...state.entities[data.visualizerId],
          chartSvg: data.svg,
          chartData: data.metaData,
        },
      },
    };
    return { ...newState };
  }),

  on(fromActions.addFilterToVisualizerSuccess, (state, { data }) => {
    console.log(data);
    let newState = {
      ...state,
      entities: {
        ...state.entities,
        [data.visioId]: {
          ...state.entities[data.visioId],
          filters: [
            ...state.entities[data.visioId].filters,
            { id: data.id, value: data.value, isActive: data.isActive },
          ],
        },
      },
    };
    return newState;
  }),

  on(fromActions.updateFilterInVisualizerSuccess, (state, { data }) => {
    let filters = state.entities[data.visioId].filters;
    let newFilters = [];
    for (let filter of filters) {
      if (filter.id == data.id)
        filter = { id: data.id, value: data.value, isActive: data.isActive };

      newFilters.push(filter);
    }

    let newState = {
      ...state,
      entities: {
        ...state.entities,
        [data.visioId]: {
          ...state.entities[data.visioId],
          filters: newFilters,
        },
      },
    };
    return newState;
  }),

  on(fromActions.removeFilterFromVisualizerSuccess, (state, { data }) => {
    let filters = state.entities[data.visioId].filters;
    let newFilters = [];
    for (let filter of filters) {
      if (filter.id != data.id) {
        newFilters.push(filter);
      }
    }

    let newState = {
      ...state,
      entities: {
        ...state.entities,
        [data.visioId]: {
          ...state.entities[data.visioId],
          filters: newFilters,
        },
      },
    };
    return newState;
  })
);

export function reducer(state: VisualizersState | undefined, action: Action) {
  return visualizersReducer(state, action);
}
