import { Injectable } from "@angular/core";

import { of } from "rxjs";
import { debounceTime, switchMap } from "rxjs/operators";

import { Actions, createEffect, ofType } from "@ngrx/effects";

import { NotificationService } from "./notifications.service";
import * as fromActions from "./notifications.actions";
import { Action } from "rxjs/internal/scheduler/Action";
@Injectable()
export class NotificationsEffects {
  constructor(
    private actions$: Actions,
    private notificationService: NotificationService
  ) {}

  showError$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.showError),
      debounceTime(100),

      switchMap(({ message }) => {
        this.notificationService.fail(message); return of(null)
      })
    )
  ,{dispatch : false});

  showSuccess$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fromActions.showSuccess),

      debounceTime(100),

      switchMap(({ message }) => {
        this.notificationService.success(message);
        return of(null);
      })
    )
  ,{dispatch: false});
}
