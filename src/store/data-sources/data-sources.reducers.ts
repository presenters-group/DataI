import { createReducer, Action, on } from "@ngrx/store";
import { IDataSource } from "./data-sources.models";
import * as fromActions from "./data-sources.actions";
import { MapInterface } from "src/store/core/models/mapinterface";

export interface DataSourcesState {
  entities: IDataSource[];
}

export const initialState: DataSourcesState = {
  entities: [],
};
const dataSourcesReducer = createReducer(
  initialState,
  /**fetching */
  on(fromActions.fetchDataSourcesSuccess, (state, { data }) => {
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
  on(fromActions.deleteDataSourceSuccess, (state, { data }) => {
    return {
      ...state,
      entities: {
        ...state.entities,
        [data.id]: {...data},
      },
    };
  }),
  //Updating Cell
  on(fromActions.updateCellSuccess, (state, { data }) => {
    let cells = [...state.entities[data.tableID].columns[data.columnId].cells]
    cells[data.cellIndex] = {
      value : data.cellValue,
      type: state.entities[data.tableID].columns[data.columnId].cells[data.cellIndex].type
    }
    let newState = {
      entities : {...state.entities,
        [data.tableID] : {...state.entities[data.tableID],
          columns: {...state.entities[data.tableID].columns,
            [data.columnId]: {...state.entities[data.tableID].columns[data.columnId],
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
