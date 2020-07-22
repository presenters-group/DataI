import { Injectable } from "@angular/core";

import { of } from "rxjs";
import { catchError, debounceTime, map, switchMap } from "rxjs/operators";

import { Actions, createEffect, ofType } from "@ngrx/effects";
import { CoreService } from "../services/core.service";

import * as fromActions from "../actions/core.actions";
import { fetchDataSources } from 'src/store/data-sources';
import { fetchDashboards } from 'src/store/dashboards';
import { fetchFilters } from 'src/store/filters';
import { fetchVisualizers } from 'src/store/visualizers';
@Injectable()
export class CoreEffects {
  constructor(
    private actions$: Actions,
    private coreService: CoreService,
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

  openProject$ = createEffect(() =>
  this.actions$.pipe(
    ofType(fromActions.openProject),

    debounceTime(100),

    switchMap(({data}) =>
      this.coreService.openProject(data).pipe(
        switchMap((data) => [
          fetchDataSources(),
          fetchDashboards(),
          fetchFilters(),
          fetchVisualizers(),
        ]),
      )
    )
  )
);


}
