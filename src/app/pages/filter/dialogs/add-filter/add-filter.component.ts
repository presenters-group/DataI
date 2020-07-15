import { Component, OnInit, Inject } from "@angular/core";
import { MatDialogRef, MAT_DIALOG_DATA } from "@angular/material/dialog";
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
    private swal: NotificationService,
    @Inject(MAT_DIALOG_DATA) public data: any
  ) {
    this.formBuild();
  }

  formBuild() {
    this.form = this.formBuilder.group({
      name: ["", Validators.required],
      dataSource: ["", Validators.required],
      filteredColumn: ["", Validators.required],
      type: ["", Validators.required],
      initValue: [0,[Validators.required,Validators.pattern("^[0-9]*$")]],
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
  onChangeColumn() {
    this.form.controls['initValue'].setValue(0)
    this.form.controls['type'].setValue("");
  }

}
