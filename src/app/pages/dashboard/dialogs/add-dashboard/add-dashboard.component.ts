import { Component, OnInit } from "@angular/core";
import { MatDialogRef } from "@angular/material/dialog";
import { AppState } from "src/store";
import { FormBuilder, Form, FormGroup } from "@angular/forms";
import { Store } from "@ngrx/store";
import {
  selectVisualizersEntities,
  selectUndeletedVisualizersEntities,
  selectFiltersInVisualizer,
} from "src/store/visualizers/visualizers.selectors";
import { selectVisualizersFiltersTree } from 'src/store/dashboards/dashboards.selectors';

@Component({
  selector: "app-add-dashboard",
  templateUrl: "./add-dashboard.component.html",
  styleUrls: ["./add-dashboard.component.scss"],
})
export class AddDashboardComponent implements OnInit {
  objectKeys = Object.keys;
  visualizers = [];
  filters = [];
  allVisualizers = this.store.select(selectVisualizersFiltersTree)
  constructor(
    public dialogRef: MatDialogRef<AddDashboardComponent>,
    private store: Store<AppState>
  ) {}

  ngOnInit(): void {
   this.allVisualizers.subscribe((value)=>{
      console.log(value)
   })
  }


  drag($event,data) {
    $event.dataTransfer.setData("text", JSON.stringify(data));
  }

  onDrop($event){
    $event.preventDefault();
    var data = $event.dataTransfer.getData("text");
    data = JSON.parse(data);
    switch(data.type){
      case 'filter':
          this.filters.push(data)
        break;
      case 'visualizer':

        break;
    }
  }

  allowDrop(ev) {
    ev.preventDefault();
  }

}
