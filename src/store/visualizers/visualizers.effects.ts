import { Injectable } from "@angular/core";

import { of } from "rxjs";
import { catchError, debounceTime, map, switchMap } from "rxjs/operators";

import { Actions, createEffect, ofType } from "@ngrx/effects";
import { VisualizersService } from "./visualizers.service";

import * as fromActions from "./visualizers.actions";
import { closeTapFromTree, fetchCharts } from "../core/actions/core.actions";
import { showSuccess, showError } from "../notifications";
import {
  CREATE_SUCCESSFUL,
  CREATE_FAILED,
  UPDATE_SUCCESSFUL,
  UPDATE_FAILED,
  DELETE_SUCCESSFUL,
  DELETE_FAILED,
  FETCH_FAILED,
} from "src/utils/messages.constants";
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

      switchMap(({ data }) => {
        return this.visualizersService.create(data as any).pipe(
          switchMap((data) => [
            fromActions.createVisualizerSuccess({ data }),
            showSuccess({ message: CREATE_SUCCESSFUL }),
          ]),

          catchError((error) => [
            showError({ message: CREATE_FAILED }),
          ])
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

          catchError((error) => [
            fromActions.fetchVisualizersFailed({ error }),
            showError({ message: FETCH_FAILED }),
          ])
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
          switchMap((data) => [
            fromActions.updateVisualizerSuccess({ data }),
            showSuccess({ message: UPDATE_SUCCESSFUL }),
          ]),

          catchError((error) => [
            fromActions.updateVisualizerFailed({ error }),
            showError({ message: UPDATE_FAILED }),
          ])
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
          switchMap((data) => [
            fromActions.deleteVisualizerSuccess({ data }),
            showSuccess({ message: DELETE_SUCCESSFUL }),
            closeTapFromTree({
              tap: { type: "visualizer", id: (data as any).id },
            }),
          ]),

          catchError((error) => [
            fromActions.deleteVisualizerFailed({ error }),
            showError({ message: DELETE_FAILED }),
          ])
        )
      )
    )
  );

  fetchVisualizerChart$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.fetchChartAsSVG),

      debounceTime(100),

      switchMap(({ data }) =>
        this.visualizersService.fetchVisualizerChart(data).pipe(
          map((data) => {
            return fromActions.fetchChartAsSVGSuccess({ data });
          }),
          catchError((error) => of(fromActions.fetchChartAsSVGFiled({ error })))
        )
      )
    )
  );

  updateFilterInDataSource$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.updateFilterInVisualizer),
      debounceTime(100),

      switchMap(({ data }) =>
        this.visualizersService.updateFilterInVisualizer(data).pipe(
          switchMap((data) => [
            fromActions.updateFilterInVisualizerSuccess({ data }),
            showSuccess({ message: UPDATE_SUCCESSFUL }),
          ]),

          catchError((error) => [
            fromActions.updateFilterInVisualizerFailed({ error }),
            showError({ message: UPDATE_FAILED }),
          ])
        )
      )
    )
  );

  addFilterToDataSource$ = createEffect(() => this.actions$.pipe(
      ofType(fromActions.addFilterToVisualizer),
      debounceTime(100),

      switchMap(({ data }) =>
       this.visualizersService.addFilterToVisualizer(data).pipe(
          switchMap((data) => [
            fromActions.addFilterToVisualizerSuccess({ data }),
            showSuccess({ message: UPDATE_SUCCESSFUL }),
          ]),

          catchError((error) => [
            fromActions.addFilterToVisualizerFailed({ error }),
            showError({ message: UPDATE_FAILED }),
          ])
        )
      )
    )
  );

  removeFilterFromDataSource$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.removeFilterFromVisualizer),
      debounceTime(100),

      switchMap(({ data }) =>
        this.visualizersService.removeFilterFromVisualizer(data).pipe(
          switchMap((data) => [
            fromActions.removeFilterFromVisualizerSuccess({ data }),
            showSuccess({ message: UPDATE_SUCCESSFUL }),
          ]),

          catchError((error) => [
            fromActions.removeFilterFromVisualizerFailed({ error }),
            showError({ message: UPDATE_FAILED }),
          ])
        )
      )
    )
  );


  addSVGChart$ = createEffect(() =>
  this.actions$.pipe(
    ofType(fromActions.addSVGChart),
    debounceTime(100),

    switchMap(({ data }) =>
      this.visualizersService.addSVGChart(data).pipe(
        switchMap((data) => [
          fetchCharts(),
          showSuccess({ message: UPDATE_SUCCESSFUL }),
        ]),

        catchError((error) => [
          showError({ message: UPDATE_FAILED }),
        ])
      )
    )
  )
);
}
