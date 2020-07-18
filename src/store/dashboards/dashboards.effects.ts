import { Injectable } from "@angular/core";

import { of } from "rxjs";
import { catchError, debounceTime, map, switchMap } from "rxjs/operators";

import { Actions, createEffect, ofType } from "@ngrx/effects";
import { DashboardsService } from "./dashboards.service";

import * as fromActions from "./dashboards.actions";
import { closeTapFromTree } from '../core/actions/core.actions';
import { CREATE_SUCCESSFUL, CREATE_FAILED, UPDATE_SUCCESSFUL, UPDATE_FAILED, DELETE_SUCCESSFUL, DELETE_FAILED, FETCH_FAILED } from 'src/utils/messages.constants';
import { showSuccess, showError } from '../notifications';
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



          switchMap((data) => [
            fromActions.createDashboardSuccess({ data }),
            showSuccess({ message: CREATE_SUCCESSFUL }),
          ]),

          catchError((error) => [
            fromActions.createDashboardFailed({ error }),
            showError({ message: CREATE_FAILED }),
          ])
        )
      )
    )
  );

  readDashboard$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.fetchDashboards),

      debounceTime(100),

      switchMap(() =>
        this.dashboardsService.fetch().pipe(
          map((data) => fromActions.fetchDashboardsSuccess({ data })),

          catchError((error) =>
            [
              fromActions.fetchDashboardsFailed({ error }),
              showError({message : FETCH_FAILED})
            ]
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
          switchMap((data) => [
            fromActions.updateDashboardSuccess({ data }),
            showSuccess({ message: UPDATE_SUCCESSFUL }),
          ]),

          catchError((error) => [
            fromActions.updateDashboardFailed({ error }),
            showError({ message: UPDATE_FAILED }),
          ])
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


          switchMap((data) => [
            fromActions.deleteDashboardSuccess({ data }),
            showSuccess({ message: DELETE_SUCCESSFUL }),
            closeTapFromTree({tap :{type : 'dashboard',id : (data as any).id}})
          ]),

          catchError((error) => [
            fromActions.deleteDashboardFailed({ error }),
            showError({ message: DELETE_FAILED }),
          ])
        )
      )
    )
  );



  fetchDashboardSVGs$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.fetchDashboardSVGs),

      debounceTime(100),

      switchMap(({ data }) =>
        this.dashboardsService.fetchDashboardSVGs(data).pipe(


          switchMap((data) => [
            fromActions.fetchDashboardSVGsSuccess({ data }),
          ]),

          catchError((error) => [
            fromActions.fetchDashboardSVGsFailed({ error }),
          ])
        )
      )
    )
  );
}
