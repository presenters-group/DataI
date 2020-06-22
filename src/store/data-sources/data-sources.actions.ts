import { createAction, props } from "@ngrx/store";

/**Fetching */
export const fetchDataSources = createAction("[TreeView] Fetch Data Sources");

export const fetchDataSourcesSuccess = createAction(
  "[DataSourceEffect] Fetch Data Sources Success",
  props<{ data }>()
);

export const fetchDataSourcesFailed = createAction(
  "[DataSourceEffect] Fetch Data Sources Failed",
  props<{ error }>()
);

/**Creating */
export const createDataSource = createAction(
  "[TreeView] Create Data Sources",
  props<{ data }>()
);

export const createDataSourceSuccess = createAction(
  "[DataSourceEffect] Create Data Sources Success",
  props<{ data }>()
);

export const createDataSourceFailed = createAction(
  "[DataSourceEffect] Create Data Sources Failed",
  props<{ error }>()
);

/**Deleting */
export const deleteDataSource = createAction(
  "[TreeView] Delete Data Sources",
  props<{ id }>()
);

export const deleteDataSourceSuccess = createAction(
  "[DataSourceEffect] Delete Data Sources Success",
  props<{ id }>()
);

export const deleteDataSourceFailed = createAction(
  "[DataSourceEffect] Delete Data Sources Failed",
  props<{ error }>()
);

/**Updating */
export const updateDataSource = createAction(
  "[TreeView] update Data Sources",
  props<{ data }>()
);

export const updateDataSourceSuccess = createAction(
  "[DataSourceEffect] update Data Sources Success",
  props<{ data }>()
);

export const updateDataSourceFailed = createAction(
  "[DataSourceEffect] update Data Sources Failed",
  props<{ error }>()
);
