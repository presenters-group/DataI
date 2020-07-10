import { props, createAction } from '@ngrx/store';

export const showError = createAction(
  "[*Effects] Show Error",
  props<{ message }>()
);

export const showSuccess = createAction(
  "[*Effects] Show Success",
  props<{ message }>()
);
