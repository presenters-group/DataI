import { createAction, props } from "@ngrx/store";

/**Fetching */
export const fetchDashboards = createAction("[TreeView] Fetch Dashboards");

export const fetchDashboardsSuccess = createAction(
  "[DashboardsEffect] Fetch Dashboards Success",
  props<{ data }>()
);

export const fetchDashboardsFailed = createAction(
  "[DashboardsEffect] Fetch Dashboards Failed",
  props<{ error }>()
);

/**Creating */
export const createDashboard = createAction(
  "[TreeView] Create Dashboard",
  props<{ data }>()
);

export const createDashboardSuccess = createAction(
  "[DashboardEffect] Create Dashboard Success",
  props<{ data }>()
);

export const createDashboardFailed = createAction(
  "[DashboardsEffect] Create Dashboards Failed",
  props<{ error }>()
);

/**Deleting */
export const deleteDashboard = createAction(
  "[TreeView] Delete Dashboard",
  props<{ id }>()
);

export const deleteDashboardSuccess = createAction(
  "[DashboardsEffect] Delete Dashboard Success",
  props<{ data }>()
);

export const deleteDashboardFailed = createAction(
  "[DashboardEffect] Delete Dashboard Failed",
  props<{ error }>()
);

/**Updating */
export const updateDashboard = createAction(
  "[TreeView] update Dashboard",
  props<{ data }>()
);

export const updateDashboardSuccess = createAction(
  "[DashboardsEffect] update Dashboard Success",
  props<{ data }>()
);

export const updateDashboardFailed = createAction(
  "[DashboardsEffect] update Dashboard Failed",
  props<{ error }>()
);


export const fetchDashboardSVGs = createAction(
  "[DashboardComponent] fetch dashboard svgs",
  props<{ data }>()
);


export const fetchDashboardSVGsSuccess = createAction(
  "[DashboardComponent] fetch dashboard svgs success",
  props<{ data }>()
);

export const fetchDashboardSVGsFailed = createAction(
  "[DashboardComponent] fetch dashboard svgs failed",
  props<{ error }>()
);


export const changeVisualizerInDashboardZoom = createAction(
  "[DashboardComponent] change visualizer in dashboard zoom",
  props<{ data: {visualizerId : number, zoom : number, dashboardId : number} }>()
);
