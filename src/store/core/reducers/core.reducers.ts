import { createReducer, Action, on } from "@ngrx/store";
import * as fromActions from "../actions/core.actions";

export interface CoreState {
  currentTree: "filters" | "dashboards" | "data-sources" | "visualizers";
  currentTap: number;
  taps: any[];
}

export const initialState: CoreState = {
  currentTap: -1,
  currentTree: null,
  taps: [],
};
const appReducer = createReducer(
  initialState,
  on(fromActions.updateCurrentTree, (state, { name }) => ({
    ...state,
    currentTree: name,
  }))
);

export function reducer(state: CoreState | undefined, action: Action) {
  return appReducer(state, action);
}
