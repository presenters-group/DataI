import { Component, OnInit } from "@angular/core";
import { Observable } from "rxjs";
import { selectCurrentDataSource } from "src/store/data-sources/data-sources.selectors";
import { Store } from "@ngrx/store";
import { AppState } from "src/store";
import { updateCell } from "src/store/data-sources";
import { first } from 'rxjs/operators';

@Component({
  selector: "app-data-source",
  templateUrl: "./data-source.component.html",
  styleUrls: ["./data-source.component.scss"],
})
export class DataSourceComponent implements OnInit {
  dataSource: Observable<any>;
  objectKeys = Object.keys;
  constructor(private store: Store<AppState>) {
    this.dataSource = this.store.select(selectCurrentDataSource);
  }

  ngOnInit(): void {}

  onCellUpdate(columnId, cellIndex, cellValue) {
      let tableId;
      this.dataSource.pipe(first()).subscribe((value) => {
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
      });
  }
}
