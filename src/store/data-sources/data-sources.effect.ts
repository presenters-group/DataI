import { Injectable } from "@angular/core";

import { of } from "rxjs";
import { catchError, debounceTime, map, switchMap } from "rxjs/operators";

import { Actions, createEffect, ofType } from "@ngrx/effects";
import { DataSourcesService } from "./data-sources.service";

import * as fromActions from "./data-sources.actions";
import { closeTapFromTree } from "../core/actions/core.actions";
import { showError, showSuccess } from "../notifications";
import {
  CREATE_FAILED,
  CREATE_SUCCESSFUL,
  UPDATE_SUCCESSFUL,
  UPDATE_FAILED,
  DELETE_SUCCESSFUL,
  DELETE_FAILED,
  FETCH_FAILED,
} from "src/utils/messages.constants";
@Injectable()
export class DataSourcesEffects {
  constructor(
    private actions$: Actions,
    private dataSourcesService: DataSourcesService
  ) {}

  createDataSource$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.createDataSource),

      debounceTime(100),

      switchMap(({ data }) =>
        this.dataSourcesService.create(data).pipe(
          switchMap((data) => [
            fromActions.fetchDataSources(),
            showSuccess({ message: CREATE_SUCCESSFUL }),
          ]),

          catchError((error) => [
            fromActions.createDataSourceFailed({ error }),
            showError({ message: CREATE_FAILED }),
          ])
        )
      )
    )
  );

  readeDataSource$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.fetchDataSources),

      debounceTime(100),

      switchMap(() =>
        this.dataSourcesService.fetch().pipe(
          map((data) => fromActions.fetchDataSourcesSuccess({ data })),

          catchError((error) =>
            [
              fromActions.fetchDataSourcesFailed({ error }),
              showError({message : FETCH_FAILED})
            ]
            )
          )
        )
      )
    );

  updateDataSource$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.updateDataSource),

      debounceTime(100),

      switchMap(({ data }) =>
        this.dataSourcesService.update(data).pipe(
          switchMap((data) => [
            fromActions.updateDataSourceSuccess({ data }),
            showSuccess({ message: UPDATE_SUCCESSFUL }),
          ]),

          catchError((error) => [
            fromActions.updateDataSourceFailed({ error }),
            showError({ message: UPDATE_FAILED }),
          ])
        )
      )
    )
  );

  deleteDataSource$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.deleteDataSource),

      debounceTime(100),

      switchMap(({ id }) =>
        this.dataSourcesService.delete(id).pipe(
          switchMap((data) => [
            fromActions.deleteDataSourceSuccess({ data }),
            closeTapFromTree({
              tap: { type: "data-source", id: (data as any).id },
            }),
            showSuccess({ message: DELETE_SUCCESSFUL }),
          ]),

          catchError((error) => [
            fromActions.deleteDataSourceFailed({ error }),
            showError({ message: DELETE_FAILED }),
          ])
        )
      )
    )
  );

  updateCell$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.updateCell),

      debounceTime(100),

      switchMap(({ data }) =>
        this.dataSourcesService.updateCell(data).pipe(
          switchMap((data) => [
            fromActions.updateCellSuccess({ data }),
            showSuccess({ message: UPDATE_SUCCESSFUL }),
          ]),

          catchError((error) => [
            fromActions.updateDataSourceFailed({ error }),
            showError({ message: UPDATE_FAILED }),
          ])
        )
      )
    )
  );
}
