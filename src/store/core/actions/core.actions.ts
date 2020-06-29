import { createAction, props } from '@ngrx/store';

export const updateCurrentTree = createAction(
  "[LeftNavComponent] Update Current Tree",
  props<{ name }>()
);


export const addToTapes = createAction(
  "[TreeView] addToTapes",
  props<{ tap }>()
);


export const setCurrentTap = createAction(
  "[TreeView] Add To Tapes",
  props<{ tapIndex }>()
);

export const closeTap = createAction(
  "[TapsComponent] Close To Tapes",
  props<{ tapIndex }>()
);

export const fetchCharts = createAction(
  "[TapsComponent] fetch charts"
);


export const fetchChartsSuccess = createAction(
  "[TapsComponent] Fetch chart success",
  props<{ data }>()
);

export const fetchChartsFailed = createAction(
  "[TapsComponent] Fetch chart failed",
  props<{ error }>()
);
