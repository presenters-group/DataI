import { createReducer, Action } from "@ngrx/store";
import { IDashboard } from "../models/model";

export interface DashboardsState {
  entities: IDashboard[];
}

export const initialState: DashboardsState = {
  entities: [
    {
      visualizers : [ {
        visualizerIndex :  0,
        height: 100,
        width: 100,
        x: 0,
        y: 0,
      }
       ],
      name : "dashboard 1",
    }
  ],
};
const visualizersReducer = createReducer(initialState);

export function reducer(state: DashboardsState | undefined, action: Action) {
  return visualizersReducer(state, action);
}
