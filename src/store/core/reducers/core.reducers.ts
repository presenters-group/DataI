import { createReducer, Action, on } from "@ngrx/store";
import * as fromActions from "../actions/core.actions";

export interface Tap {
  type: "filter" | "dashboard" | "data-source" | "visualizer";
  id: number;
  name: string;
}
export interface CoreState {
  currentTree: "filters" | "dashboards" | "data-sources" | "visualizers";
  currentTap: number;
  taps: Tap[];
}

export const initialState: CoreState = {
  currentTap: null,
  currentTree: null,
  taps: [],
};
const appReducer = createReducer(
  initialState,
  on(fromActions.updateCurrentTree, (state, { name }) => ({
    ...state,
    currentTree: state.currentTree == name ? null : name,
  })),
  on(fromActions.setCurrentTap, (state, { tapIndex }) => ({
    ...state,
    currentTap: tapIndex,
  })),
  on(fromActions.closeTap, (state, { tapIndex }) => {
    let taps = [];
    for (let i = 0; i < state.taps.length; i++)
      if (i != tapIndex) taps.push(state.taps[i]);
    if (taps.length == 0) return { ...state, taps, currentTap: null };
    return {
      ...state,
      taps,
      currentTap: taps[tapIndex - 1] ? tapIndex - 1 : 0,
    };
  }),
  on(fromActions.addToTapes, (state, { tap }) => {
    let taps = [...state.taps];
    console.log("anything02");
    taps.push(tap);
    return { ...state, taps, currentTap: taps.length - 1 };
  })
);

export function reducer(state: CoreState | undefined, action: Action) {
  return appReducer(state, action);
}
