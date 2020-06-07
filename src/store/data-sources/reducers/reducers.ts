import { createReducer, Action } from "@ngrx/store";
import { IDataSourceModel } from "../models/model";

export interface DataSourcesState {
  entities: IDataSourceModel[];
}

export const initialState: DataSourcesState = {
  entities: [
    {
      columns: [
        {
          cells: [
            {
              value: "السعر",
              type: "string",
            },
            {
              value: 10,
              type: "numeric",
            },
            {
              value: 20,
              type: "numeric",
            },
            {
              value: 20,
              type: "numeric",
            },
            {
              value: 20,
              type: "numeric",
            },
            {
              value: 15,
              type: "numeric",
            },
            {
              value: 15,
              type: "numeric",
            },
            {
              value: 10,
              type: "numeric",
            },
            {
              value: 10,
              type: "numeric",
            },
          ],
          name: "السعر",
          style: {
            color: "#26C485",
            lineWeight: 1.0,
            pointWeight: 1.0,
            font: "Calibri",
          },
          columnType: "Measures",
          valueCategories: [
            {
              value: "السعر",
              type: "string",
            },
            {
              value: 10,
              type: "numeric",
            },
            {
              value: 20,
              type: "numeric",
            },
            {
              value: 15,
              type: "numeric",
            },
          ],
        },
        {
          cells: [
            {
              value: "السعر",
              type: "string",
            },
            {
              value: 10,
              type: "numeric",
            },
            {
              value: 20,
              type: "numeric",
            },
            {
              value: 20,
              type: "numeric",
            },
            {
              value: 20,
              type: "numeric",
            },
            {
              value: 15,
              type: "numeric",
            },
            {
              value: 15,
              type: "numeric",
            },
            {
              value: 10,
              type: "numeric",
            },
            {
              value: 10,
              type: "numeric",
            },
          ],
          name: "السعر",
          style: {
            color: "#26C485",
            lineWeight: 1.0,
            pointWeight: 1.0,
            font: "Calibri",
          },
          columnType: "Measures",
          valueCategories: [
            {
              value: "السعر",
              type: "string",
            },
            {
              value: 10,
              type: "numeric",
            },
            {
              value: 20,
              type: "numeric",
            },
            {
              value: 15,
              type: "numeric",
            },
          ],
        },
        {
          cells: [
            {
              value: "النوع",
              type: "string",
            },
            {
              value: "Laptop",
              type: "string",
            },
            {
              value: "Laptop",
              type: "string",
            },
            {
              value: "Laptop",
              type: "string",
            },
            {
              value: "Mouse",
              type: "string",
            },
            {
              value: "Mouse",
              type: "string",
            },
            {
              value: "Mouse",
              type: "string",
            },
            {
              value: "Keyboard",
              type: "string",
            },
            {
              value: "Keyboard",
              type: "string",
            },
          ],
          name: "النوع",
          style: {
            color: "#DBD56E",
            lineWeight: 1.0,
            pointWeight: 1.0,
            font: "Calibri",
          },
          columnType: "Measures",
          valueCategories: [
            {
              value: "النوع",
              type: "string",
            },
            {
              value: "Laptop",
              type: "string",
            },
            {
              value: "Mouse",
              type: "string",
            },
            {
              value: "Keyboard",
              type: "string",
            },
          ],
        },
      ],
      columnsVisibility: [true, true, true],
      rowsVisibility: [true, true, true],
      name: "Table1",
      properties: {
        sourceFileType: "DataI",
        zoomValue: 50,
        xColumn: 0,
      },
      rightToLeft: true,
      aggregators: [null],
    },
  ],
};
const dataSourcesReducer = createReducer(initialState);

export function reducer(state: DataSourcesState | undefined, action: Action) {
  return dataSourcesReducer(state, action);
}
