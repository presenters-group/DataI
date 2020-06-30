import { Component, OnInit } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';
import { Store } from '@ngrx/store';
import { AppState } from 'src/store';
import { FormBuilder } from '@angular/forms';
import { selectDataSourcesEntities } from 'src/store/data-sources/data-sources.selectors';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-add-filter',
  templateUrl: './add-filter.component.html',
  styleUrls: ['./add-filter.component.scss']
})
export class AddFilterComponent implements OnInit {
  form;
  objectKeys = Object.keys;
  dataSources = this.store.select(selectDataSourcesEntities);
  constructor(
    public dialogRef: MatDialogRef<AddFilterComponent>,
    private store: Store<AppState>,
    private formBuilder: FormBuilder
  ) {
    this.formBuild();
   }

   formBuild(){
    this.form = this.formBuilder.group({
      name: [''],
      dataSource: [''],
      filteredColumn: [''],
      type: [''],
      initValue: [''],
    })
  }

  ngOnInit(): void {
  }


  onNoClick(): void {
    this.dataSources.pipe(first()).subscribe((value)=>{
    })
    this.dialogRef.close();
  }

}
