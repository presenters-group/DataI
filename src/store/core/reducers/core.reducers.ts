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
  charts: string[];
  taps: Tap[];
}

export const initialState: CoreState = {
  currentTap: null,
  currentTree: null,
  charts: [
    'bar-chart',
    'line-chart',
    'pie-chart'
  ],
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

  on(fromActions.closeTapFromTree, (state, { tap }) => {
    let taps = [];
    let tapIndex;
    for (let i = 0; i < state.taps.length; i++)
      if (state.taps[i].type != tap.type || state.taps[i].id != tap.id) {
        taps.push(state.taps[i]);
        tapIndex = i
      }
    if (taps.length == 0) return { ...state, taps, currentTap: null };
    return {
      ...state,
      taps,
      currentTap: taps[tapIndex - 1] ? tapIndex - 1 : 0,
    };
  }),


  on(fromActions.addToTapes, (state, { tap }) => {
    let taps = [...state.taps];
    let chosenTap = -1;
    let i;
    for(i = 0 ; i < taps.length; i ++)
      if(taps[i] .type == tap.type && taps[i].id == tap.id){
        chosenTap = i
        break;
      }
    if(chosenTap == -1)
      taps.push(tap);
    else
      return { ...state, taps, currentTap: i }
    return { ...state, taps, currentTap: taps.length - 1 };
  }),
  on(fromActions.fetchChartsSuccess, (state, {data})=> ({...state, charts: data.chartsNames}))
);

export function reducer(state: CoreState | undefined, action: Action) {
  return appReducer(state, action);
}
