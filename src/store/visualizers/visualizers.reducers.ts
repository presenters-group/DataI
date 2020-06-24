import { createReducer, Action, on } from "@ngrx/store";
import { IVisualizer } from "./visualizers.models";
import * as fromActions from "./visualizers.actions";
import { MapInterface } from "src/store/core/models/mapinterface";
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
  on(fromActions.deleteVisualizerSuccess, (state, { id }) => {
    const { [id]: deletedVisualizer, ...entities } = state.entities;

    return {
      ...state,
      entities: {
        [id]: { ...deletedVisualizer, isDeleted: true },
        ...entities,
      },
    };
  })
);

export function reducer(state: VisualizersState | undefined, action: Action) {
  return visualizersReducer(state, action);
}
