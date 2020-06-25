import { Injectable } from "@angular/core";

import { of } from "rxjs";
import { catchError, debounceTime, map, switchMap } from "rxjs/operators";

import { Actions, createEffect, ofType } from "@ngrx/effects";
import { VisualizersService } from "./visualizers.service";

import * as fromActions from "./visualizers.actions";
@Injectable()
export class VisualizersEffects {
  constructor(
    private actions$: Actions,
    private visualizersService: VisualizersService
  ) {}

  createVisualizer$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.createVisualizer),

      debounceTime(100),

      switchMap(({data}) => {
        console.log(data)
        return this.visualizersService.create(data as any).pipe(
          map((data) => fromActions.createVisualizerSuccess({ data })),

          catchError((error) =>
            of(fromActions.createVisualizerFailed({ error }))
          )
        );
      })
    )
  );

  readeVisualizer$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.fetchVisualizers),

      debounceTime(100),

      switchMap(() =>
        this.visualizersService.fetch().pipe(
          map((data) => fromActions.fetchVisualizersSuccess({ data })),

          catchError((error) =>
            of(fromActions.fetchVisualizersFailed({ error }))
          )
        )
      )
    )
  );

  updateVisualizer$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.updateVisualizer),

      debounceTime(100),

      switchMap(({ data }) =>
        this.visualizersService.update(data).pipe(
          map((data) => fromActions.updateVisualizerSuccess({ data })),

          catchError((error) =>
            of(fromActions.updateVisualizerFailed({ error }))
          )
        )
      )
    )
  );

  deleteVisualizer$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.deleteVisualizer),

      debounceTime(100),

      switchMap(({ id }) =>
        this.visualizersService.delete(id).pipe(
          map((id) => fromActions.deleteVisualizerSuccess({ id })),

          catchError((error) =>
            of(fromActions.deleteVisualizerFailed({ error }))
          )
        )
      )
    )
  );
}
