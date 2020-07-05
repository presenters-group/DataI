import { Component, OnInit } from '@angular/core';
import { AppState } from 'src/store';
import { Store } from '@ngrx/store';
import { createDataSource } from 'src/store/data-sources';
import { MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-add-data-source',
  templateUrl: './add-data-source.component.html',
  styleUrls: ['./add-data-source.component.scss']
})
export class AddDataSourceComponent {
  file
  constructor(private store : Store<AppState>,
    public dialogRef: MatDialogRef<AddDataSourceComponent>,
    ) { }

  onExcelClick($event){
    if($event.target.files[0].type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'){
      this.file = $event.target.files[0]
      this.store.dispatch(createDataSource({data: {file : this.file, type: 'excel'}}))
      this.dialogRef.close();
    }
  }

  onCsvClick($event){
    if($event.target.files[0].type == 'text/csv'){
      this.file = $event.target.files[0]
      this.store.dispatch(createDataSource({data: {file : this.file, type: 'csv'}}))
      this.dialogRef.close();
    }
  }

}
