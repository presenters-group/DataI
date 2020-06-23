import { Injectable } from "@angular/core";

import { of } from "rxjs";
import { catchError, debounceTime, map, switchMap } from "rxjs/operators";

import { Actions, createEffect, ofType } from "@ngrx/effects";
import { DashboardsService } from "./dashboards.service";

import * as fromActions from "./dashboards.actions";
@Injectable()
export class DashboardsEffects {
  constructor(
    private actions$: Actions,
    private visualizersService: DashboardsService
  ) {}

  createVisualizer$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.createDashboard),

      debounceTime(100),

      switchMap(({ data }) =>
        this.visualizersService.create(data).pipe(
          map((data) => fromActions.createDashboardSuccess({ data })),

          catchError((error) =>
            of(fromActions.createDashboardFailed({ error }))
          )
        )
      )
    )
  );

  readeVisualizer$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.fetchDashboards),

      debounceTime(100),

      switchMap(() =>
        this.visualizersService.fetch().pipe(
          map((data) => fromActions.fetchDashboardsSuccess({ data })),

          catchError((error) =>
            of(fromActions.fetchDashboardsFailed({ error }))
          )
        )
      )
    )
  );

  updateVisualizer$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.updateDashboard),

      debounceTime(100),

      switchMap(({ data }) =>
        this.visualizersService.update(data).pipe(
          map((data) => fromActions.updateDashboardSuccess({ data })),

          catchError((error) =>
            of(fromActions.updateDashboardFailed({ error }))
          )
        )
      )
    )
  );

  deleteVisualizer$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.deleteDashboard),

      debounceTime(100),

      switchMap(({ id }) =>
        this.visualizersService.delete(id).pipe(
          map((id) => fromActions.deleteDashboardSuccess({ id })),

          catchError((error) =>
            of(fromActions.deleteDashboardFailed({ error }))
          )
        )
      )
    )
  );
}
