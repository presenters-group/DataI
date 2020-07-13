import { Component, OnInit, AfterViewInit } from "@angular/core";
import { Observable } from "rxjs";
import { selectCurrentDataSource } from "src/store/data-sources/data-sources.selectors";
import { Store } from "@ngrx/store";
import { AppState } from "src/store";
import { updateCell } from "src/store/data-sources";
import { first, take } from 'rxjs/operators';
import { selectCurrentDataSourceFilters } from 'src/store/filters/filters.selectors';

@Component({
  selector: "app-data-source",
  templateUrl: "./data-source.component.html",
  styleUrls: ["./data-source.component.scss"],
})
export class DataSourceComponent implements AfterViewInit {
  dataSource: Observable<any>;
  objectKeys = Object.keys;
  filters: Observable<any> = this.store.select(selectCurrentDataSourceFilters);
  constructor(private store: Store<AppState>) {
    this.dataSource = this.store.select(selectCurrentDataSource);
  }

  ngAfterViewInit(

  ): void {}

 

  onCellUpdate(columnId, cellIndex, cellValue) {
    console.log("cellValue",cellValue)
    let tableId;
    this.dataSource.pipe(first()).subscribe((value) => {
      let old = value.columns[columnId].cells[cellIndex];
      if (old.value != cellValue){
          console.log('OldValue',old.value);
          tableId = value.id;
          this.store.dispatch(
            updateCell({
              data: {
                tableId,
                columnId,
                cellIndex, 
                cellValue,
              },
            })
          );
        }
      });
  }

  consol(data){
    console.log(data)
    return data
  }
}
