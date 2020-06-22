import { createAction, props } from "@ngrx/store";

/**Fetching */
export const fetchFilters = createAction("[TreeView] Fetch Filters");

export const fetchFiltersSuccess = createAction(
  "[FiltersEffect] Fetch Filters Success",
  props<{ data }>()
);

export const fetchFiltersFailed = createAction(
  "[FiltersEffect] Fetch Filters Failed",
  props<{ error }>()
);

/**Creating */
export const createFilter = createAction(
  "[TreeView] Create Filter",
  props<{ data }>()
);

export const createFilterSuccess = createAction(
  "[FiltersEffect] Create Filter Success",
  props<{ data }>()
);

export const createFilterFailed = createAction(
  "[FiltersEffect] Create Filter Failed",
  props<{ error }>()
);

/**Deleting */
export const deleteFilter = createAction(
  "[TreeView] Delete Filter",
  props<{ id }>()
);

export const deleteFilterSuccess = createAction(
  "[FiltersEffect] Delete Filter Success",
  props<{ id }>()
);

export const deleteFilterFailed = createAction(
  "[FiltersEffect] Delete Filter Failed",
  props<{ error }>()
);

/**Updating */
export const updateFilter = createAction(
  "[TreeView] update Filter",
  props<{ data }>()
);

export const updateFilterSuccess = createAction(
  "[FiltersEffect] update Filter Success",
  props<{ data }>()
);

export const updateFilterFailed = createAction(
  "[FiltersEffect] update Filter Failed",
  props<{ error }>()
);
