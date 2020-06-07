import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";

import { AppRoutingModule } from "./app-routing.module";
import { AppComponent } from "./app.component";
import { StoreDevtoolsModule } from "@ngrx/store-devtools";
import { environment } from "src/environments/environment";
import { StoreModule } from '@ngrx/store';
import * as fromStore from "../store";
import { LeftNavComponent } from './components/left-nav/left-nav.component';
import { TreeViewComponent } from './components/tree-view/tree-view.component';
import { TapsComponent } from './components/taps/taps.component'
@NgModule({
  declarations: [AppComponent, LeftNavComponent, TreeViewComponent, TapsComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    StoreModule.forRoot({...fromStore.reducers}),
    StoreDevtoolsModule.instrument({
      maxAge: 25,
      logOnly: environment.production,
    }),
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
