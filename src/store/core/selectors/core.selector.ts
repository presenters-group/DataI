import { createFeatureSelector, createSelector } from "@ngrx/store";
import { AppState } from "src/store";
import { CoreState } from "../reducers";
export const selectCoreState = createFeatureSelector<AppState, CoreState>(
  "core"
);

export const selectCurrentTap = createSelector(
  selectCoreState,
  (state) => state.currentTap
)

export const selectCurrentTree = createSelector(
  selectCoreState,
  (state) => state.currentTree
)

export const isTreeOpened = createSelector(
  selectCoreState,
  (state) => state.currentTree != null
)
