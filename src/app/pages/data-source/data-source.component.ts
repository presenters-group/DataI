import { Component, AfterViewInit } from "@angular/core";
import { Observable } from "rxjs";
import { selectCurrentDataSource } from "src/store/data-sources/data-sources.selectors";
import { Store } from "@ngrx/store";
import { AppState } from "src/store";
import { updateCell, updateFilterInDataSource,addFilterToDataSource, removeFilterFromDataSource, updateDataSourceColumnColor, updateDataSourceRowColor } from "src/store/data-sources";
import { first } from 'rxjs/operators';
import { selectCurrentDataSourceFilters,  selectAllCurrentDataSourceFilters } from 'src/store/filters/filters.selectors';
import { NotificationService } from 'src/store/notifications/notifications.service';

@Component({
  selector: "app-data-source",
  templateUrl: "./data-source.component.html",
  styleUrls: ["./data-source.component.scss"],
})
export class DataSourceComponent implements AfterViewInit {
  dataSource: Observable<any>;
  objectKeys = Object.keys;
  filters: Observable<any> = this.store.select(selectCurrentDataSourceFilters);
  addableFilters : Observable<any> = this.store.select(selectAllCurrentDataSourceFilters);
  insertedFilter;
  insertFilter : boolean = false;
  constructor(private store: Store<AppState>,private notification : NotificationService) {
    this.dataSource = this.store.select(selectCurrentDataSource);
  }

  ngAfterViewInit(

  ): void {}



  onCellUpdate(columnId, cellIndex, cellValue,$event) {

    // return;
    let tableId;
    let acceptedValue;
    this.dataSource.pipe(first()).subscribe((value) => {
      let old = value.columns[columnId].cells[cellIndex];
      console.log("cell value in subscribe",cellValue, !(!cellValue))
      if(value.columns[columnId].columnType == 'Measures' && cellIndex != 0){
        cellValue = Number.parseInt(cellValue)
        if(isNaN(cellValue)){
          $event.target.innerHTML = old.value;
          this.notification.fail('Please add a valid value')
          return;
        }
      }
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


  onFilterChangeValue($event){
    console.log($event)
    this.dataSource.pipe(first()).subscribe((value)=>{
      this.store.dispatch(updateFilterInDataSource({data : {...$event,tableId : value.id}}))
    })
  }


  disableAddedFilter(filter,filters){
    return filters.map(x => x.id).includes(filter.id)
  }


  onAddFilter(){
    if(!this.insertedFilter){
      this.notification.fail("Please select filter before adding")
      return
    }
    this.dataSource.pipe(first()).subscribe((value)=>{
      this.store.dispatch(addFilterToDataSource({ data : {
      tableId: value.id,
      id: this.insertedFilter.id,
      value: this.insertedFilter.initValue ? this.insertedFilter.initValue : [],
      isActive: true
    }}))
    })
    this.insertedFilter = null;
    this.insertFilter = false;
  }

  onDeleteFilter($event){
    this.dataSource.pipe(first()).subscribe((value)=>{
      this.store.dispatch(removeFilterFromDataSource({ data : {
      tableId: value.id,
      id: $event.id,
    }}))
    })
  }


  onColumnColorChange(columnId,$event){
    this.dataSource.pipe(first()).subscribe((value)=>{
      this.store.dispatch(updateDataSourceColumnColor({ data : {color : $event.target.value, columnId,tableId: value.id}}))
    })
  }

  onRowColorChange(rowId,$event){
    this.dataSource.pipe(first()).subscribe((value)=>{
    this.store.dispatch(updateDataSourceRowColor({ data : {color : $event.target.value,rowId , tableId : value.id}}))
  })
  }
}


