import { Injectable } from "@angular/core";

import { of } from "rxjs";
import { catchError, debounceTime, map, switchMap, filter, tap } from "rxjs/operators";

import { Actions, createEffect, ofType } from "@ngrx/effects";
import { CoreService } from "../services/core.service";

import * as fromActions from "../actions/core.actions";
import { NotificationService } from './notification.service';
import { Action } from 'rxjs/internal/scheduler/Action';
@Injectable()
export class NotificationsEffects {
  constructor(
    private actions$: Actions,
    private notificationService: NotificationService
  ) {}



  showError$ = createEffect(() =>
    this.actions$.pipe(
      ofType(),
      debounceTime(100),

      switchMap((action) =>
        {this.notificationService.fail((action as any).error); return of(null)}
      )
    )
  );


  showSuccess$ = createEffect(() =>
  this.actions$.pipe(
    ofType(),

    debounceTime(100),

    switchMap((_) =>
      {this.notificationService.success('Success'); return of(null)}
    )
  )
);


}
