import { Component, OnInit, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { FormControl, FormGroup, FormBuilder } from '@angular/forms';
import { AppState } from 'src/store';
import { selectDataSourcesEntities } from 'src/store/data-sources/data-sources.selectors';
import { Store } from '@ngrx/store';
import { DataSource } from '@angular/cdk/collections';
import { first } from 'rxjs/operators';

export interface DialogData {
  animal: string;
  name: string;
}


@Component({
  selector: 'app-add-visualizer',
  templateUrl: './add-visualizer.component.html',
  styleUrls: ['./add-visualizer.component.scss']
})
export class AddVisualizerComponent {
  form;
  objectKeys = Object.keys;
  dataSources = this.store.select(selectDataSourcesEntities);
  column;
  constructor(
    public dialogRef: MatDialogRef<AddVisualizerComponent>,
    @Inject(MAT_DIALOG_DATA) public data: DialogData,
    private store:Store<AppState>,
    private formBuilder : FormBuilder) {
      this.formBuild();
      this.getDataSource(this.dataSources)
      console.log(this.form.data)
    }

  formBuild(){
    this.form = this.formBuilder.group({
      data: [''],
      usedColumns: this.formBuilder.array([]),
      xColumn: [''],
      chart: [''],
      name: [''],
      filters: this.formBuilder.array([]),
    })
  }
  onNoClick(): void {
    console.log(this.form)
    this.dataSources.pipe(first()).subscribe((value)=>{
      console.log(value[this.form.value.data])
    })
    this.dialogRef.close();
  }

  getDataSource(dataSources){
    this.dataSources.pipe(first()).subscribe((value)=>{
      console.log(value)
    })
    console.log(dataSources);
    return dataSources
  }
  consol(data,t?){
    if(t)
      console.log('blablabla')
    // this.dataSources.pipe(first()).subscribe((value)=>{
    //   console.log(value[this.form.value.data])
    // })
    console.log(data);
    return data;
  }
}
