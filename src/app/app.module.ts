import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";

import { AppRoutingModule } from "./app-routing.module";
import { AppComponent } from "./app.component";
import { StoreDevtoolsModule } from "@ngrx/store-devtools";
import { environment } from "src/environments/environment";
import { StoreModule } from "@ngrx/store";
import * as fromStore from "../store";
import { LeftNavComponent } from "./components/left-nav/left-nav.component";
import { TreeViewComponent } from "./components/tree-view/tree-view.component";
import { TapsComponent } from "./components/taps/taps.component";
import { HomeComponent } from "./pages/home/home.component";
import { DashboardComponent } from "./pages/dashboard/dashboard.component";
import { VisualizerComponent } from "./pages/visualizer/visualizer.component";
import { FilterComponent } from "./pages/filter/filter.component";
import { DataSourceComponent } from "./pages/data-source/data-source.component";
@NgModule({
  declarations: [
    AppComponent,
    LeftNavComponent,
    TreeViewComponent,
    TapsComponent,
    HomeComponent,
    DashboardComponent,
    VisualizerComponent,
    FilterComponent,
    DataSourceComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    StoreModule.forRoot({ ...fromStore.reducers }),
    StoreDevtoolsModule.instrument({
      maxAge: 25,
      logOnly: environment.production,
    }),
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
