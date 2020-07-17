import { Component, OnInit, Inject } from "@angular/core";
import { MatDialogRef, MAT_DIALOG_DATA } from "@angular/material/dialog";
import { AppState } from "src/store";
import { FormBuilder, Form, FormGroup } from "@angular/forms";
import { Store } from "@ngrx/store";
import {
  selectVisualizersEntities,
  selectUndeletedVisualizersEntities,
  selectFiltersInVisualizer,
} from "src/store/visualizers/visualizers.selectors";
import { selectVisualizersFiltersTree } from "src/store/dashboards/dashboards.selectors";
import { filter, first } from "rxjs/operators";
import { NotificationService } from "src/store/notifications/notifications.service";
import { selectFiltersEntities } from 'src/store/filters/filters.selectors';

@Component({
  selector: "app-add-dashboard",
  templateUrl: "./add-dashboard.component.html",
  styleUrls: ["./add-dashboard.component.scss"],
})
export class AddDashboardComponent implements OnInit {
  objectKeys = Object.keys;
  visualizers = [];
  filters = [];
  allVisualizers = this.store.select(selectVisualizersFiltersTree);
  visualizersEntities = this.store.select(selectVisualizersEntities);
  selectedEntity;
  oldEvent;
  name;
  constructor(
    public dialogRef: MatDialogRef<AddDashboardComponent>,
    private store: Store<AppState>,
    private notification: NotificationService,
    @Inject(MAT_DIALOG_DATA) public data: any
  ) {}

  ngOnInit(): void {
    if(this.data){
      this.store.select(selectVisualizersEntities).pipe(first()).subscribe((value)=>{
        this.visualizers = this.data.visualizers.map((x)=>({
          id: x.visualizationId,
          measurements: x.measurements,
          name: value[x.visualizationId].name,
        }));
      });
      this.store.select(selectFiltersEntities).pipe(first()).subscribe((value)=>{
        this.filters = this.data.filters.map(x => ({
          id: x.id,
          measurements: x.measurements,
          name: value[x.id].name,
        }));

      });
      this.name = this.data.name;
    }
  }

  drag($event, data) {
    $event.dataTransfer.setData("text", JSON.stringify(data));
  }

  onPreviewClick($event) {
    $event.preventDefault();
    let data = this.selectedEntity;
    this.addToEntities(data, $event);
    this.selectedEntity = null;
  }
  onDrop($event) {
    $event.preventDefault();
    var data = $event.dataTransfer.getData("text");
    data = JSON.parse(data);
    this.addToEntities(data, $event);
  }

  addToEntities(data, $event) {
    switch (data.type) {
      case "filter":
        console.log(data.visioId, this.filters);
        if (
          this.filters
            .map((x) => ({ id: x.id, visioId: x.visioId }))
            .reduce(
              (prev, curr) =>
                (curr.id == data.id && curr.visioId == data.visioId) || prev,
              false
            )
        )
          return;
        this.filters.push({
          ...data,
          measurements: {
            width: 100,
            height: 100,
            x: $event.offsetX,
            y: $event.offsetY,
          },
        });
        break;
      case "visualizer":
        if (this.visualizers.map((x) => x.id).includes(data.id)) return;
        this.visualizers.push({
          ...data,
          measurements: {
            width: 500,
            height: 300,
            x: $event.offsetX,
            y: $event.offsetY,
          },
        });
        break;
    }
  }

  allowDrop(ev) {
    ev.preventDefault();
  }

  onEntityClick($event, data) {
    this.selectedEntity = data;
  }

  onNoClick() {
    this.dialogRef.close();
    }

  onSave() {
    if (this.checkValidation()) {
      this.notification.fail("Please set a valid information before save");
      return;
    }

    for (let visualizer of this.visualizers) {
      let visElement = document.getElementById(
        `visualizer${visualizer.visualizationId}`
      );
      visualizer.measurements = {
        width: visElement.offsetWidth,
        height: visElement.offsetHeight,
        x: visElement.offsetLeft,
        y: visElement.offsetTop,
      };
    }


    for (let filter of this.filters) {
      let filterElement = document.getElementById(`filter${filter.id}`);
      filter.measurements = {
        width: filterElement.offsetWidth,
        height: filterElement.offsetHeight,
        x: filterElement.offsetLeft,
        y: filterElement.offsetTop,
      };
    }


    this.dialogRef.close({
      name: this.name,
      visualizers: this.visualizers.map((x) => ({
        visualizationId: x.id,
        measurements: x.measurements,
      })),
      filters: this.filters,
    });
  }

  checkValidation(): boolean {
    if (name) return true;
    else return false;
  }
}
