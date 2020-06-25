import { createReducer, Action, on } from "@ngrx/store";
import { IDataSource } from "./data-sources.models";
import * as fromActions from "./data-sources.actions";
import { MapInterface } from "src/store/core/models/mapinterface";

export interface DataSourcesState {
  entities: IDataSource[];
}

export const initialState: DataSourcesState = {
  entities: [
    // {
    //   name: "Table1",
    //   columns: [
    //     {
    //       name: "السعر",
    //       cells: [
    //         {
    //           value: "السعر",
    //           type: "string",
    //         },
    //         {
    //           value: 10,
    //           type: "numeric",
    //         },
    //         {
    //           value: 20,
    //           type: "numeric",
    //         },
    //         {
    //           value: 20,
    //           type: "numeric",
    //         },
    //         {
    //           value: 20,
    //           type: "numeric",
    //         },
    //         {
    //           value: 15,
    //           type: "numeric",
    //         },
    //         {
    //           value: 15,
    //           type: "numeric",
    //         },
    //         {
    //           value: 10,
    //           type: "numeric",
    //         },
    //         {
    //           value: 10,
    //           type: "numeric",
    //         },
    //       ],
    //       style: {
    //         color: "#26C485",
    //         lineWeight: 1.0,
    //         pointWeight: 1.0,
    //         font: "Calibri",
    //       },
    //       columnType: "Measures",
    //       valueCategories: [
    //         {
    //           value: "السعر",
    //           type: "string",
    //         },
    //         {
    //           value: 10,
    //           type: "numeric",
    //         },
    //         {
    //           value: 20,
    //           type: "numeric",
    //         },
    //         {
    //           value: 15,
    //           type: "numeric",
    //         },
    //       ],
    //       isDeleted: false,
    //     },
    //     {
    //       name: "الكمية",
    //       id: 40,
    //       cells: [
    //         {
    //           value: "الكمية",
    //           type: "string",
    //         },
    //         {
    //           value: 40,
    //           type: "numeric",
    //         },
    //         {
    //           value: 50,
    //           type: "numeric",
    //         },
    //         {
    //           value: 50,
    //           type: "numeric",
    //         },
    //         {
    //           value: 50,
    //           type: "numeric",
    //         },
    //         {
    //           value: 50,
    //           type: "numeric",
    //         },
    //         {
    //           value: 60,
    //           type: "numeric",
    //         },
    //         {
    //           value: 50,
    //           type: "numeric",
    //         },
    //         {
    //           value: 40,
    //           type: "numeric",
    //         },
    //       ],
    //       style: {
    //         color: "#3066BE",
    //         lineWeight: 1.0,
    //         pointWeight: 1.0,
    //         font: "Calibri",
    //       },
    //       columnType: "Measures",
    //       valueCategories: [
    //         {
    //           value: "الكمية",
    //           type: "string",
    //         },
    //         {
    //           value: 40,
    //           type: "numeric",
    //         },
    //         {
    //           value: 50,
    //           type: "numeric",
    //         },
    //         {
    //           value: 60,
    //           type: "numeric",
    //         },
    //       ],
    //       isDeleted: false,
    //     },
    //     {
    //       name: "النوع",
    //       id: 359,
    //       cells: [
    //         {
    //           value: "النوع",
    //           type: "string",
    //         },
    //         {
    //           value: "Laptop",
    //           type: "string",
    //         },
    //         {
    //           value: "Laptop",
    //           type: "string",
    //         },
    //         {
    //           value: "Laptop",
    //           type: "string",
    //         },
    //         {
    //           value: "Mouse",
    //           type: "string",
    //         },
    //         {
    //           value: "Mouse",
    //           type: "string",
    //         },
    //         {
    //           value: "Mouse",
    //           type: "string",
    //         },
    //         {
    //           value: "Keyboard",
    //           type: "string",
    //         },
    //         {
    //           value: "Keyboard",
    //           type: "string",
    //         },
    //       ],
    //       style: {
    //         color: "#DBD56E",
    //         lineWeight: 1.0,
    //         pointWeight: 1.0,
    //         font: "Calibri",
    //       },
    //       columnType: "Dimensions",
    //       valueCategories: [
    //         {
    //           value: "النوع",
    //           type: "string",
    //         },
    //         {
    //           value: "Laptop",
    //           type: "string",
    //         },
    //         {
    //           value: "Mouse",
    //           type: "string",
    //         },
    //         {
    //           value: "Keyboard",
    //           type: "string",
    //         },
    //       ],
    //       isDeleted: false,
    //     },
    //     {
    //       name: "الوزن",
    //       id: 501,
    //       cells: [
    //         {
    //           value: "الوزن",
    //           type: "string",
    //         },
    //         {
    //           value: 10,
    //           type: "string",
    //         },
    //         {
    //           value: 17,
    //           type: "string",
    //         },
    //         {
    //           value: 55,
    //           type: "string",
    //         },
    //         {
    //           value: 39,
    //           type: "string",
    //         },
    //         {
    //           value: 71,
    //           type: "string",
    //         },
    //         {
    //           value: 66,
    //           type: "string",
    //         },
    //         {
    //           value: 55,
    //           type: "string",
    //         },
    //         {
    //           value: 21,
    //           type: "string",
    //         },
    //       ],
    //       style: {
    //         color: "#EBD4AE",
    //         lineWeight: 1.5,
    //         pointWeight: 0.0,
    //         font: "Calibri",
    //       },
    //       columnType: "Measures",
    //       valueCategories: [
    //         {
    //           value: "الوزن",
    //           type: "string",
    //         },
    //         {
    //           value: 10,
    //           type: "string",
    //         },
    //         {
    //           value: 17,
    //           type: "string",
    //         },
    //         {
    //           value: 55,
    //           type: "string",
    //         },
    //         {
    //           value: 39,
    //           type: "string",
    //         },
    //         {
    //           value: 71,
    //           type: "string",
    //         },
    //         {
    //           value: 66,
    //           type: "string",
    //         },
    //         {
    //           value: 21,
    //           type: "string",
    //         },
    //       ],
    //       isDeleted: false,
    //     },
    //   ],
    //   columnsVisibility: [true, true, true],
    //   rowsVisibility: [true, true, true],
    //   properties: {
    //     sourceFileType: "DataI",
    //     zoomValue: 50,
    //     xColumn: 0,
    //   },
    //   rightToLeft: true,
    //   aggregator: null,
    //   isDeleted: false,
    // },
  ],
};
const dataSourcesReducer = createReducer(
  initialState,
  /**fetching */
  on(fromActions.fetchDataSourcesSuccess, (state, { data }) => {
    console.log(data);
    const entities = data.reduce(
      (entities: MapInterface<IDataSource>, dataSource) => {
        let columns = dataSource.columns.reduce(
          (columns, column) => ({
            ...columns,
            [column.id]: column,
          }),
          {}
        );
        return {
          ...entities,
          [dataSource.id]: { ...dataSource, columns: columns },
        };
      },
      {}
    );

    return {
      ...state,
      entities,
    };
  }),

  /**Updating and Creating */
  on(
    fromActions.updateDataSourceSuccess,
    fromActions.createDataSourceSuccess,
    (state, { data }) => {
      const entities = {
        ...state.entities,
        [data.id]: data,
      };

      return {
        ...state,
        entities,
      };
    }
  ),

  /**Deleting */
  on(fromActions.deleteDataSourceSuccess, (state, { id }) => {
    const { [id]: deletedDataSource, ...entities } = state.entities;

    return {
      ...state,
      entities: {
        [id]: { ...deletedDataSource, isDeleted: true },
        ...entities,
      },
    };
  }),
  //Updating Cell
  on(fromActions.updateCellSuccess, (state, { data }) => {
    // console.log(data);
    let cells = [...state.entities[data.tableId].columns[data.columnId].cells]
    cells[data.cellIndex] = {
      value : data.cellValue,
      type: state.entities[data.tableId].columns[data.columnId].cells[data.cellIndex].type
    }
    let newState = {
      entities : {...state.entities,
        [data.tableId] : {...state.entities[data.tableId],
          columns: {...state.entities[data.tableId].columns,
            [data.columnId]: {...state.entities[data.tableId].columns[data.columnId],
              cells: cells
            },
          }
        }
      }
    }
    return {...newState};
  })
);

export function reducer(state: DataSourcesState | undefined, action: Action) {
  return dataSourcesReducer(state, action);
}
