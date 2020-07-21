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
  props<{ data }>()
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

export const fetchChartAsSVG = createAction(
  "[VisualizerComponent] fetch svg chart",
  props<{ data : {visualizerId : number, width: number ,height: number} }>()
);

export const fetchChartAsSVGSuccess = createAction(
  "[VisualizerEffects] fetch svg chart success",
  props<{ data }>()
);


export const fetchChartAsSVGFiled = createAction(
  "[VisualizerEffects] fetch svg chart Filed",
  props<{ error }>()
);



export const addFilterToVisualizer = createAction(
  "[VisualizerComponent] add filter to visualizer",
  props<{ data }>()
)


export const updateFilterInVisualizer = createAction(
  "[VisualizerComponent] update filter in visualizer",
  props<{ data }>()
)


export const removeFilterFromVisualizer = createAction(
  "[VisualizerComponent] remove filter from visualizer",
  props<{ data }>()
)


export const addFilterToVisualizerSuccess = createAction(
  "[VisualizerComponent] add filter to visualizer success",
  props<{ data }>()
)


export const updateFilterInVisualizerSuccess = createAction(
  "[VisualizerComponent] update filter in visualizer success",
  props<{ data }>()
)


export const removeFilterFromVisualizerSuccess = createAction(
  "[VisualizerComponent] remove filter from visualizer success",
  props<{ data }>()
)


export const addFilterToVisualizerFailed = createAction(
  "[VisualizerComponent] add filter to visualizer failed",
  props<{ error }>()
)


export const updateFilterInVisualizerFailed = createAction(
  "[VisualizerEffect] update filter in visualizer failed",
  props<{ error }>()
)


export const removeFilterFromVisualizerFailed = createAction(
  "[VisualizerEffect] remove filter from visualizer failed",
  props<{ error }>()
)

export const removeSvgForVisualizer = createAction(
  "[VisualizerComponent] remove svg from visualizer",
  props<{data : {visualizerId: number}}>()
)

export const addSVGChart = createAction(
  "[AddVisualizerComponent] add svg chart",
  props<{data}>()
)
