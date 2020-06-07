import { createReducer, Action } from "@ngrx/store";
import { IVisualizer } from "../models/model";

export interface VisualizersState {
  entities: IVisualizer[];
}

export const initialState: VisualizersState = {
  entities: [
    {
      "data": {
          "columns": [
              {
                  "cells": [
                      {
                          "value": "السعر",
                          "type": "string"
                      },
                      {
                          "value": 10,
                          "type": "numeric"
                      },
                      {
                          "value": 20,
                          "type": "numeric"
                      },
                      {
                          "value": 20,
                          "type": "numeric"
                      },
                      {
                          "value": 20,
                          "type": "numeric"
                      },
                      {
                          "value": 15,
                          "type": "numeric"
                      },
                      {
                          "value": 15,
                          "type": "numeric"
                      },
                      {
                          "value": 10,
                          "type": "numeric"
                      },
                      {
                          "value": 10,
                          "type": "numeric"
                      }
                  ],
                  "name": "السعر",
                  "style": {
                      "color": "#26C485",
                      "lineWeight": 1.0,
                      "pointWeight": 1.0,
                      "font": "Calibri"
                  },
                  "columnType": "Measures",
                  "valueCategories": [
                      {
                          "value": "السعر",
                          "type": "string"
                      },
                      {
                          "value": 10,
                          "type": "numeric"
                      },
                      {
                          "value": 20,
                          "type": "numeric"
                      },
                      {
                          "value": 15,
                          "type": "numeric"
                      }
                  ]
              },
              {
                  "cells": [
                      {
                          "value": "السعر",
                          "type": "string"
                      },
                      {
                          "value": 10,
                          "type": "numeric"
                      },
                      {
                          "value": 20,
                          "type": "numeric"
                      },
                      {
                          "value": 20,
                          "type": "numeric"
                      },
                      {
                          "value": 20,
                          "type": "numeric"
                      },
                      {
                          "value": 15,
                          "type": "numeric"
                      },
                      {
                          "value": 15,
                          "type": "numeric"
                      },
                      {
                          "value": 10,
                          "type": "numeric"
                      },
                      {
                          "value": 10,
                          "type": "numeric"
                      }
                  ],
                  "name": "السعر",
                  "style": {
                      "color": "#26C485",
                      "lineWeight": 1.0,
                      "pointWeight": 1.0,
                      "font": "Calibri"
                  },
                  "columnType": "Measures",
                  "valueCategories": [
                      {
                          "value": "السعر",
                          "type": "string"
                      },
                      {
                          "value": 10,
                          "type": "numeric"
                      },
                      {
                          "value": 20,
                          "type": "numeric"
                      },
                      {
                          "value": 15,
                          "type": "numeric"
                      }
                  ]
              },
              {
                  "cells": [
                      {
                          "value": "النوع",
                          "type": "string"
                      },
                      {
                          "value": "Laptop",
                          "type": "string"
                      },
                      {
                          "value": "Laptop",
                          "type": "string"
                      },
                      {
                          "value": "Laptop",
                          "type": "string"
                      },
                      {
                          "value": "Mouse",
                          "type": "string"
                      },
                      {
                          "value": "Mouse",
                          "type": "string"
                      },
                      {
                          "value": "Mouse",
                          "type": "string"
                      },
                      {
                          "value": "Keyboard",
                          "type": "string"
                      },
                      {
                          "value": "Keyboard",
                          "type": "string"
                      }
                  ],
                  "name": "النوع",
                  "style": {
                      "color": "#DBD56E",
                      "lineWeight": 1.0,
                      "pointWeight": 1.0,
                      "font": "Calibri"
                  },
                  "columnType": "Measures",
                  "valueCategories": [
                      {
                          "value": "النوع",
                          "type": "string"
                      },
                      {
                          "value": "Laptop",
                          "type": "string"
                      },
                      {
                          "value": "Mouse",
                          "type": "string"
                      },
                      {
                          "value": "Keyboard",
                          "type": "string"
                      }
                  ]
              }
          ],
          "columnsVisibility": [
              true,
              true,
              true
          ],
          "rowsVisibility": [
              true,
              true,
              true
          ],
          "name": "Table1",
          "properties": {
              "sourceFileType": "DataI",
              "zoomValue": 50,
              "xColumn": 0
          },
          "rightToLeft": true,
          "aggregators": [
              null
          ]
      },
      "name": "visualizer1",

      "filters": [
          {
              "filteredColumnData": [
                  null
              ],
              "visualizationSource": 0,
              "filteredColumn": 1,
              "addedFilters": [
                  1,
                  2
              ],
              "isActive": [
                  true,
                  true
              ],
              "isVisible": [
                  true,
                  true
              ]
          },
          {
              "filteredColumnData": [
                  null
              ],
              "visualizationSource": 0,
              "filteredColumn": 0,
              "addedFilters": [
                  1,
                  3
              ],
              "isActive": [
                  true,
                  true
              ],
              "isVisible": [
                  true,
                  true
              ]
          },
          {
              "filteredColumnData": [
                  null
              ],
              "visualizationSource": 0,
              "filteredColumn": 2,
              "addedFilters": [
                  3
              ],
              "isActive": [
                  true
              ],
              "isVisible": [
                  true
              ]
          }
      ]
  }
  ],
};
const visualizersReducer = createReducer(initialState);

export function reducer(state: VisualizersState | undefined, action: Action) {
  return visualizersReducer(state, action);
}
