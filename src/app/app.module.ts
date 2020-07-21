


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
import { HttpClientModule }    from '@angular/common/http';
import { EffectsModule } from '@ngrx/effects';
import { AddVisualizerComponent } from './pages/visualizer/dialogs/add-visualizer/add-visualizer.component';
import {MatDialogModule} from '@angular/material/dialog';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule } from '@angular/forms';
import {MatFormFieldModule} from '@angular/material/form-field';
import { ReactiveFormsModule } from '@angular/forms';
import {MatInputModule} from '@angular/material/input';
import {MatIconModule} from '@angular/material/icon';
import {MatMenuModule} from '@angular/material/menu';
import {MatButtonModule} from '@angular/material/button';
import {MatSelectModule} from '@angular/material/select';
import {MatSidenavModule} from '@angular/material/sidenav'
import { AddDataSourceComponent } from './pages/data-source/dialogs/add-data-source/add-data-source.component';
import {MatRippleModule, MatNativeDateModule} from '@angular/material/core';
import { MovingDirective } from './directives/moving/moving.directive';
import { AddDashboardComponent } from './pages/dashboard/dialogs/add-dashboard/add-dashboard.component';
import { AddFilterComponent } from './pages/filter/dialogs/add-filter/add-filter.component';
import { SweetAlert2Module } from '@sweetalert2/ngx-sweetalert2';
import { FilterItemComponent } from './pages/filter/components/filter-item/filter-item.component';
import {MatCheckboxModule} from '@angular/material/checkbox';
import { VisualizerItemComponent } from './components/visualizer-item/visualizer-item.component';
import { InsertFilterComponent } from './pages/filter/dialogs/insert-filter/insert-filter.component';
import { MainMenuComponent } from './components/main-menu/main-menu.component';
import {MatProgressSpinnerModule} from '@angular/material/progress-spinner';
import {MatSliderModule} from '@angular/material/slider';
import {MatDatepickerModule} from '@angular/material/datepicker';

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
    AddVisualizerComponent,
    AddDataSourceComponent,
    MovingDirective,
    AddDashboardComponent,
    AddFilterComponent,
    FilterItemComponent,
    VisualizerItemComponent,
    InsertFilterComponent,
    MainMenuComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    StoreModule.forRoot({ ...fromStore.reducers },{
      runtimeChecks: {
        strictStateImmutability: true,
        strictActionImmutability: true
    }}
    ),
    StoreDevtoolsModule.instrument({
      maxAge: 25,
      logOnly: environment.production,
    }),
    EffectsModule.forRoot([ ...fromStore.effects ]),
    HttpClientModule,
    MatDialogModule,
    BrowserAnimationsModule,
    FormsModule,
    MatFormFieldModule,
    ReactiveFormsModule,
    MatInputModule,
    MatButtonModule,
    MatSelectModule,
    MatRippleModule,
    MatMenuModule,
    MatIconModule,
    MatSidenavModule,
    SweetAlert2Module,
    MatCheckboxModule,
    MatProgressSpinnerModule,
    MatSliderModule,
    MatDatepickerModule,
    MatNativeDateModule
    ],
  providers: [],
  bootstrap: [AppComponent],
  entryComponents: [AddVisualizerComponent]
})
export class AppModule {}
