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
  props<{ data:{file,type} }>()
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
  props<{ data }>()
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



export const updateCell = createAction(
  "[DataSourceEffect] update cell",
  props<{ data: {tableId: number, columnId : number, cellIndex: number, cellValue: any} }>()
);


export const updateCellSuccess = createAction(
  "[DataSourceEffect] update cell Success",
  props<{ data }>()
);


export const updateCellField = createAction(
  "[DataSourceEffect] update cell Field",
  props<{ error }>()
);

export const updateFilterInDataSource = createAction(
  "[DataSourceComponent] update filter value in data source",
  props<{ data }>()
)


export const addFilterToDataSource = createAction(
  "[DataSourceComponent] add filter to dataSource",
  props<{ data }>()
)


export const removeFilterFromDataSource = createAction(
  "[DataSourceComponent] remove filter from dataSource",
  props<{ data }>()
)


export const updateDataSourceRowColor = createAction(
  "[DataSourceComponent] update data source row color",
  props<{ data }>()
)

export const updateDataSourceColumnColor = createAction(
  "[DataSourceComponent] update data source column color",
  props<{ data }>()
)
