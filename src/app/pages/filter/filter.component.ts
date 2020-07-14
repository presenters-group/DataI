import { Component, OnInit } from "@angular/core";
import { Store } from "@ngrx/store";
import { AppState } from "src/store";
import { updateFilter } from "src/store/filters";
import { selectCurrentFilter } from "src/store/filters/filters.selectors";
import { selectDataSourcesEntities } from "src/store/data-sources/data-sources.selectors";
import { FormBuilder } from "@angular/forms";
import { first } from "rxjs/operators";
import { Validators } from "@angular/forms";
import { NotificationService } from "src/store/notifications/notifications.service";
import { fetchDataSources } from 'src/store/data-sources';

@Component({
  selector: "app-filter",
  templateUrl: "./filter.component.html",
  styleUrls: ["./filter.component.scss"],
})
export class FilterComponent implements OnInit {
  form;
  objectKeys = Object.keys;
  dataSources = this.store.select(selectDataSourcesEntities);
  filter = this.store.select(selectCurrentFilter);
  constructor(
    private swal: NotificationService,
    private store: Store<AppState>,
    private formBuilder: FormBuilder
  ) {}

  formBuild() {
    this.filter.subscribe((value) => {
      console.log(value);
      this.form = this.formBuilder.group({
        name: [value.name, Validators.required],
        dataSource: [value.dataSource.toString(), Validators.required],
        filteredColumn: [value.filteredColumn.toString(), Validators.required],
        type: [value.type, Validators.required],
        initValue: [value.initValue],
      });
      // this.form.get('dataSource').setValue(value.dataSource);
    });
  }

  ngOnInit(): void {
    this.formBuild();
  }

  onSaveClick() {
    if (this.form.valid) {
      this.filter.pipe(first()).subscribe((value) => {
        this.store.dispatch(
          updateFilter({ data: { ...this.form.value, id: value.id } })
        );
        this.formBuild();
      });
      this.store.dispatch(fetchDataSources());
    } else {
      this.swal.fail("Please Complete The Form With Valid Information Before Saving");
    }
  }

  onNoClick() {
    this.formBuild();
  }

  onChangeDataSource() {
    this.form.controls["filteredColumn"].setValue("");
    this.form.controls["type"].setValue("");
  }
}
