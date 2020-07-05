import { Injectable } from "@angular/core";

import { of } from "rxjs";
import { catchError, debounceTime, map, switchMap } from "rxjs/operators";

import { Actions, createEffect, ofType } from "@ngrx/effects";
import { FiltersService } from "./filters.service";

import * as fromActions from "./filters.actions";
import { closeTapFromTree } from "../core/actions/core.actions";
import {
  UPDATE_SUCCESSFUL,
  UPDATE_FAILED,
  CREATE_SUCCESSFUL,
  DELETE_SUCCESSFUL,
  DELETE_FAILED,
  FETCH_FAILED,
} from "src/utils/messages.constants";
import { showSuccess, showError } from "../notifications";
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
          switchMap((data) => [
            fromActions.createFilterSuccess({ data }),
            showSuccess({ message: CREATE_SUCCESSFUL }),
          ]),

          catchError((error) => [
            fromActions.createFilterFailed({ error }),
            showError({ message: CREATE_SUCCESSFUL }),
          ])
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

          catchError((error) => [fromActions.fetchFiltersFailed({ error }),
            showError({message : FETCH_FAILED})
          ])
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
          switchMap((data) => [
            fromActions.updateFilterSuccess({ data }),
            showSuccess({ message: UPDATE_SUCCESSFUL }),
          ]),

          catchError((error) => [
            fromActions.updateFilterFailed({ error }),
            showError({ message: UPDATE_FAILED }),
          ])
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
          switchMap((data) => [
            fromActions.deleteFilterSuccess({ data }),
            showSuccess({ message: DELETE_SUCCESSFUL }),
            closeTapFromTree({ tap: { type: "filter", id: (data as any).id } }),
          ]),

          catchError((error) => [
            fromActions.deleteFilterFailed({ error }),
            showError({ message: DELETE_FAILED }),
          ])
        )
      )
    )
  );
}
