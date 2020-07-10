import { Component, OnInit } from "@angular/core";
import { MatDialogRef } from "@angular/material/dialog";
import { Store } from "@ngrx/store";
import { AppState } from "src/store";
import { FormBuilder, Validators } from "@angular/forms";
import { selectDataSourcesEntities } from "src/store/data-sources/data-sources.selectors";
import { first } from "rxjs/operators";
import { NotificationService } from "src/store/notifications/notifications.service";

@Component({
  selector: "app-add-filter",
  templateUrl: "./add-filter.component.html",
  styleUrls: ["./add-filter.component.scss"],
})
export class AddFilterComponent implements OnInit {
  form;
  objectKeys = Object.keys;
  dataSources = this.store.select(selectDataSourcesEntities);
  constructor(
    public dialogRef: MatDialogRef<AddFilterComponent>,
    private store: Store<AppState>,
    private formBuilder: FormBuilder,
    private swal: NotificationService
  ) {
    this.formBuild();
  }

  formBuild() {
    this.form = this.formBuilder.group({
      name: ["", Validators.required],
      dataSource: ["", Validators.required],
      filteredColumn: ["", Validators.required],
      type: ["", Validators.required],
      initValue: [""],
    });
  }

  ngOnInit(): void {}

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
  onChangeDataSource() {
    this.form.controls["filteredColumn"].setValue("");
    this.form.controls["type"].setValue("");
  }
}
