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
    private filtersService: FiltersService
  ) {}

  createFilters$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.createFilter),

      debounceTime(100),

      switchMap(({ data }) =>
        this.filtersService.create(data).pipe(
          map((data) => fromActions.createFilterSuccess({ data })),

          catchError((error) => of(fromActions.createFilterFailed({ error })))
        )
      )
    )
  );

  readeFilters$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.fetchFilters),

      debounceTime(100),

      switchMap(() =>
        this.filtersService.fetch().pipe(
          map((data) => fromActions.fetchFiltersSuccess({ data })),

          catchError((error) => of(fromActions.fetchFiltersFailed({ error })))
        )
      )
    )
  );

  updateFilter$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.updateFilter),

      debounceTime(100),

      switchMap(({ data }) =>
        this.filtersService.update(data).pipe(
          map((data) => fromActions.updateFilterSuccess({ data })),

          catchError((error) => of(fromActions.updateFilterFailed({ error })))
        )
      )
    )
  );

  deleteFilter$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.deleteFilter),

      debounceTime(100),

      switchMap(({ id }) =>
        this.filtersService.delete(id).pipe(
          map((data) => fromActions.deleteFilterSuccess({ data })),

          catchError((error) => of(fromActions.deleteFilterFailed({ error })))
        )
      )
    )
  );
}
