import { Component, OnInit } from "@angular/core";
import { MatDialogRef } from "@angular/material/dialog";
import { AppState } from "src/store";
import { FormBuilder } from "@angular/forms";
import { Store } from "@ngrx/store";

@Component({
  selector: "app-add-dashboard",
  templateUrl: "./add-dashboard.component.html",
  styleUrls: ["./add-dashboard.component.scss"],
})
export class AddDashboardComponent implements OnInit {
  form;
  constructor(
    public dialogRef: MatDialogRef<AddDashboardComponent>,
    private store: Store<AppState>,
    private formBuilder: FormBuilder
  ) {
    this.formBuild();
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

  ngOnInit(): void {}
}
