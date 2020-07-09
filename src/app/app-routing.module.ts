import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { VisualizerComponent } from './pages/visualizer/visualizer.component';
import { FilterComponent } from './pages/filter/filter.component';
import { DataSourceComponent } from './pages/data-source/data-source.component';


const routes: Routes = [
  {
    path:"",
    component:HomeComponent,
  },
  {
    path:"dashboard",
    component:DashboardComponent,
  },
  {
    path:"visualizer",
    component:VisualizerComponent,
  },
  {
    path:"filter",
    component:FilterComponent,
  },
  {
    path:"data-source",
    component:DataSourceComponent,
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
