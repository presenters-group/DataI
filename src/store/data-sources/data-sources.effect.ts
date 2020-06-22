import { Injectable } from "@angular/core";

import { of } from "rxjs";
import { catchError, debounceTime, map, switchMap } from "rxjs/operators";

import { Actions, createEffect, ofType } from "@ngrx/effects";
import { DataSourcesService } from "./data-sources.service";

import * as fromActions from "./data-sources.actions";
@Injectable()
export class DataSourcesEffects {
  constructor(
    private actions$: Actions,
    private dataSourcesService: DataSourcesService
  ) {}

  createVisualizer$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.createDataSource),

      debounceTime(100),

      switchMap(({ data }) =>
        this.dataSourcesService.create(data).pipe(
          map((data) => fromActions.createDataSourceSuccess({ data })),

          catchError((error) =>
            of(fromActions.createDataSourceFailed({ error }))
          )
        )
      )
    )
  );

  readeVisualizer$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.fetchDataSources),

      debounceTime(100),

      switchMap(() =>
        this.dataSourcesService.fetch().pipe(
          map((data) => fromActions.fetchDataSourcesSuccess({ data })),

          catchError((error) =>
            of(fromActions.fetchDataSourcesFailed({ error }))
          )
        )
      )
    )
  );

  updateVisualizer$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.updateDataSource),

      debounceTime(100),

      switchMap(({ data }) =>
        this.dataSourcesService.update(data).pipe(
          map((data) => fromActions.updateDataSourceSuccess({ data })),

          catchError((error) =>
            of(fromActions.updateDataSourceFailed({ error }))
          )
        )
      )
    )
  );

  deleteVisualizer$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.deleteDataSource),

      debounceTime(100),

      switchMap(({ id }) =>
        this.dataSourcesService.delete(id).pipe(
          map((id) => fromActions.deleteDataSourceSuccess({ id })),

          catchError((error) =>
            of(fromActions.deleteDataSourceFailed({ error }))
          )
        )
      )
    )
  );
}
