import { Component, OnInit, Inject, HostListener } from "@angular/core";
import { MatDialogRef, MAT_DIALOG_DATA } from "@angular/material/dialog";
import { AppState } from "src/store";
import { Store } from "@ngrx/store";
import { selectVisualizersEntities } from "src/store/visualizers/visualizers.selectors";
import { selectVisualizersFiltersTree } from "src/store/dashboards/dashboards.selectors";
import { first } from "rxjs/operators";
import { NotificationService } from "src/store/notifications/notifications.service";
import { selectFiltersEntities } from "src/store/filters/filters.selectors";

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
  selectedFromPreview;
  constructor(
    public dialogRef: MatDialogRef<AddDashboardComponent>,
    private store: Store<AppState>,
    private notification: NotificationService,
    @Inject(MAT_DIALOG_DATA) public data: any
  ) {}

  ngOnInit(): void {
    if (this.data) {
      this.store
        .select(selectVisualizersEntities)
        .pipe(first())
        .subscribe((value) => {
          this.visualizers = this.data.visualizers.map((x) => ({
            id: x.visualizationId,
            measurements: x.measurements,
            name: value[x.visualizationId].name,
          }));
        });
      this.store
        .select(selectFiltersEntities)
        .pipe(first())
        .subscribe((value) => {
          this.filters = this.data.filters.map((x) => ({
            id: x.id,
            measurements: x.measurements,
            name: value[x.id].name,
          }));
        });
      this.name = this.data.name;
    }

    document.addEventListener("keypress", (event) => {
      if(event.key == 'Delete')
        this.delete();
    });
  }

  drag($event, data) {
    $event.dataTransfer.setData("text", JSON.stringify(data));
  }

  onPreviewClick($event) {
    if (this.selectedEntity) {
      $event.preventDefault();
      let data = this.selectedEntity;
      this.addToEntities(data, $event);
      this.selectedEntity = null;
    }
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
        {
          this.notification.warning("Can't add an already added filter")
          return;
        }
        if(!this.visualizers.find(x => x.visualizationId == data.visioId)){
          this.notification.warning("Can't add filter without it's visualizer")
          return;
        }
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
        if (this.visualizers.map((x) => x.id).includes(data.id))
        {
          this.notification.warning("Can't add an already added visualizer")
          return;
        }
        this.visualizers.push({
          ...data,
          visualizationId: data.id,
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
    if (!this.checkValidation()) {
      this.notification.fail("Please set a valid information before save");
      return;
    }

    console.log("visualizers : ", this.visualizers);
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
    if (this.name) return true;
    else return false;
  }

  delete() {
    if (this.selectedFromPreview) {
      switch (this.selectedFromPreview.type) {
        case "visualizer":
          this.visualizers = this.visualizers.filter(
            (x) => x.visualizationId != this.selectedFromPreview.visualizationId
          );
          this.filters = this.filters.filter(
            x => x.visioId != this.selectedFromPreview.visualizationId
          )
          break;

        case "filter":
          this.filters = this.filters.filter(
            (x) =>
              x.id != this.selectedFromPreview.id ||
              x.visioId != this.selectedFromPreview.visioId
          );
          break;
      }
    }
  }

  selectFromAdded(select) {
    this.selectedFromPreview = select;
  }
}
