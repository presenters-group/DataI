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
    private dashboardsService: DashboardsService
  ) {}

  createDashboard$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.createDashboard),

      debounceTime(100),

      switchMap(({ data }) =>
        this.dashboardsService.create(data).pipe(
          map((data) => fromActions.createDashboardSuccess({ data })),

          catchError((error) =>
            of(fromActions.createDashboardFailed({ error }))
          )
        )
      )
    )
  );

  readeDashboard$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.fetchDashboards),

      debounceTime(100),

      switchMap(() =>
        this.dashboardsService.fetch().pipe(
          map((data) => fromActions.fetchDashboardsSuccess({ data })),

          catchError((error) =>
            of(fromActions.fetchDashboardsFailed({ error }))
          )
        )
      )
    )
  );

  updateDashboard$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.updateDashboard),

      debounceTime(100),

      switchMap(({ data }) =>
        this.dashboardsService.update(data).pipe(
          map((data) => fromActions.updateDashboardSuccess({ data })),

          catchError((error) =>
            of(fromActions.updateDashboardFailed({ error }))
          )
        )
      )
    )
  );

  deleteDashboard$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.deleteDashboard),

      debounceTime(100),

      switchMap(({ id }) =>
        this.dashboardsService.delete(id).pipe(
          map((data) => fromActions.deleteDashboardSuccess({ data })),

          catchError((error) =>
            of(fromActions.deleteDashboardFailed({ error }))
          )
        )
      )
    )
  );
}
