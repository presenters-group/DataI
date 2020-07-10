import { Injectable } from "@angular/core";

import { of } from "rxjs";
import { catchError, debounceTime, map, switchMap } from "rxjs/operators";

import { Actions, createEffect, ofType } from "@ngrx/effects";
import { CoreService } from "../services/core.service";

import * as fromActions from "../actions/core.actions";
@Injectable()
export class CoreEffects {
  constructor(
    private actions$: Actions,
    private coreService: CoreService
  ) {}



  readeVisualizer$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.fetchCharts),

      debounceTime(100),

      switchMap(() =>
        this.coreService.fetch().pipe(
          map((data) => fromActions.fetchChartsSuccess({ data })),

          catchError((error) =>
            of(fromActions.fetchChartsFailed({ error }))
          )
        )
      )
    )
  );


}
