import { Component, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { FormBuilder, Validators } from '@angular/forms';
import { AppState } from 'src/store';
import { selectDataSourcesEntities } from 'src/store/data-sources/data-sources.selectors';
import { Store } from '@ngrx/store';
import { first } from 'rxjs/operators';
import { selectFiltersForDataSource } from 'src/store/filters/filters.selectors';
import { selectCharts } from 'src/store/core/selectors/core.selector';
import { Observable } from 'rxjs';
import { NotificationService } from 'src/store/notifications/notifications.service';


@Component({
  selector: 'app-add-visualizer',
  templateUrl: './add-visualizer.component.html',
  styleUrls: ['./add-visualizer.component.scss']
})
export class AddVisualizerComponent {
  form;
  objectKeys = Object.keys;
  dataSources = this.store.select(selectDataSourcesEntities);
  filters = new Observable<any>();
  column;
  charts = this.store.select(selectCharts);
  constructor(
    public dialogRef: MatDialogRef<AddVisualizerComponent>,
    private store:Store<AppState>,
    private formBuilder : FormBuilder,
    private swal: NotificationService,
    @Inject(MAT_DIALOG_DATA) public data: any
    ) {
      this.formBuild();
      this.filters = this.store.select(selectFiltersForDataSource,{dataSource : this.form.value.data})
    }

  formBuild(){
    this.form = this.formBuilder.group({
      data: [this.data ? this.data.data.toString() : '',Validators.required],
      usedColumns: [this.data ? this.data.usedColumns.map(x=>x.toString()) : [],Validators.minLength(1)],
      xColumn: [this.data ? this.data.xColumn.toString() : '',Validators.required],
      chart: [this. data ?this.data.chart.toString() : '',Validators.required],
      name: [this.data ? this.data.name.toString() : '',Validators.required],
      animation: [this.data ? this.data.animation : false]
    })
  }
  onNoClick(): void {
    this.dialogRef.close();
  }
  onSave(): void {
    if (this.form.valid) this.dialogRef.close(this.form);
    else
      this.swal.fail(
        "Please Complete The Form With Valid Information Before Saving"
      );
  }
  onSelectDataSource(){
    this.filters = this.store.select(selectFiltersForDataSource,{dataSource : this.form.value.data})
  }

}

