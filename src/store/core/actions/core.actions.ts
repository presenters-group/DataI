import { createAction, props } from '@ngrx/store';

export const updateCurrentTree = createAction(
  "[LeftNavComponent] Update Current Tree",
  props<{ name }>()
);
