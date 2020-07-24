import { createFeatureSelector, createSelector } from "@ngrx/store";
import { AppState } from "src/store";
import { CoreState } from "../reducers";
export const selectCoreState = createFeatureSelector<AppState, CoreState>(
  "core"
);

export const selectCurrentTap = createSelector(
  selectCoreState,
  (state) => state.currentTap
);

export const selectCurrentTree = createSelector(
  selectCoreState,
  (state) => {
    return state.currentTree
  }
);

export const isTreeOpened = createSelector(
  selectCoreState,
  (state) => state.currentTree != null
);

export const selectIsThereACurrentTap = createSelector(
  selectCoreState,
  (state) => state.currentTap != null
);

export const selectTaps = createSelector(
  selectCoreState,
  (state) => state.taps
);

export const selectCurrentTapObject = createSelector(
  selectTaps,
  selectCurrentTap,
  (taps, id) => {
    return id != null ? taps[id] : null;
  }
);

export const selectCurrentTapLink = createSelector(
  selectTaps,
  selectCurrentTap,
  (taps, id) => {
    return id != null ? taps[id].type : "";
  }
);


export const selectCharts = createSelector(
  selectCoreState,
  (state) => {
    return state.charts;
  }
);
