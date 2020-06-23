import { Injectable } from "@angular/core";

import { of } from "rxjs";
import { catchError, debounceTime, map, switchMap } from "rxjs/operators";

import { Actions, createEffect, ofType } from "@ngrx/effects";
import { FiltersService } from "./filters.service";

import * as fromActions from "./filters.actions";
@Injectable()
export class FiltersEffects {
  constructor(
    private actions$: Actions,
    private visualizersService: FiltersService
  ) {}

  createVisualizer$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.createFilter),

      debounceTime(100),

      switchMap(({ data }) =>
        this.visualizersService.create(data).pipe(
          map((data) => fromActions.createFilterSuccess({ data })),

          catchError((error) => of(fromActions.createFilterFailed({ error })))
        )
      )
    )
  );

  readeVisualizer$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.fetchFilters),

      debounceTime(100),

      switchMap(() =>
        this.visualizersService.fetch().pipe(
          map((data) => fromActions.fetchFiltersSuccess({ data })),

          catchError((error) => of(fromActions.fetchFiltersFailed({ error })))
        )
      )
    )
  );

  updateVisualizer$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.updateFilter),

      debounceTime(100),

      switchMap(({ data }) =>
        this.visualizersService.update(data).pipe(
          map((data) => fromActions.updateFilterSuccess({ data })),

          catchError((error) => of(fromActions.updateFilterFailed({ error })))
        )
      )
    )
  );

  deleteVisualizer$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.deleteFilter),

      debounceTime(100),

      switchMap(({ id }) =>
        this.visualizersService.delete(id).pipe(
          map((id) => fromActions.deleteFilterSuccess({ id })),

          catchError((error) => of(fromActions.deleteFilterFailed({ error })))
        )
      )
    )
  );
}
