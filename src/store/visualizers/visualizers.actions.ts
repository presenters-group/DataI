import { createAction, props } from "@ngrx/store";

/**Fetching */
export const fetchVisualizers = createAction("[TreeView] Fetch Visualizers");

export const fetchVisualizersSuccess = createAction(
  "[VisualizersEffect] Fetch Visualizers Success",
  props<{ data }>()
);

export const fetchVisualizersFailed = createAction(
  "[VisualizersEffect] Fetch Visualizers Failed",
  props<{ error }>()
);

/**Creating */
export const createVisualizer = createAction(
  "[TreeView] Create Visualizer",
  props<{ data }>()
);

export const createVisualizerSuccess = createAction(
  "[VisualizersEffect] Create Visualizers Success",
  props<{ data }>()
);

export const createVisualizerFailed = createAction(
  "[VisualizersEffect] Create Visualizers Failed",
  props<{ error }>()
);

/**Deleting */
export const deleteVisualizer = createAction(
  "[TreeView] Delete Visualizer",
  props<{ id }>()
);

export const deleteVisualizerSuccess = createAction(
  "[VisualizersEffect] Delete Visualizer Success",
  props<{ id }>()
);

export const deleteVisualizerFailed = createAction(
  "[VisualizersEffect] Delete Visualizer Failed",
  props<{ error }>()
);

/**Updating */
export const updateVisualizer = createAction(
  "[TreeView] update Visualizer",
  props<{ data }>()
);

export const updateVisualizerSuccess = createAction(
  "[VisualizersEffect] update Visualizer Success",
  props<{ data }>()
);

export const updateVisualizerFailed = createAction(
  "[VisualizersEffect] update Visualizer Failed",
  props<{ error }>()
);
