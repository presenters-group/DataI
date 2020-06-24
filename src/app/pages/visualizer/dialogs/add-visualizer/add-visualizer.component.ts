import { Component, OnInit, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';

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

  constructor(
    public dialogRef: MatDialogRef<AddVisualizerComponent>,
    @Inject(MAT_DIALOG_DATA) public data: DialogData) {}

  onNoClick(): void {
    this.dialogRef.close();
  }

}
