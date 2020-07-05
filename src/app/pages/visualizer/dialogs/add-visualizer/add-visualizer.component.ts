import { Component, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { FormBuilder } from '@angular/forms';
import { AppState } from 'src/store';
import { selectDataSourcesEntities } from 'src/store/data-sources/data-sources.selectors';
import { Store } from '@ngrx/store';
import { first } from 'rxjs/operators';
import { selectFiltersForDataSource } from 'src/store/filters/filters.selectors';
import { selectCharts } from 'src/store/core/selectors/core.selector';
import { Observable } from 'rxjs';


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
    private formBuilder : FormBuilder) {
      this.formBuild();
      this.filters = this.store.select(selectFiltersForDataSource,{dataSource : this.form.value.data})
    }

  formBuild(){
    this.form = this.formBuilder.group({
      data: [''],
      usedColumns: [[]],
      xColumn: [''],
      chart: [''],
      name: [''],
      filters:([[]]),
    })
  }
  onNoClick(): void {
    this.dialogRef.close();
  }

  onSelectDataSource(){
    this.filters = this.store.select(selectFiltersForDataSource,{dataSource : this.form.value.data})
  }

}

