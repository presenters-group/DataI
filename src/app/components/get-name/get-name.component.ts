import { Component, OnInit } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';
import { NotificationService } from 'src/store/notifications/notifications.service';

@Component({
  selector: 'app-get-name',
  templateUrl: './get-name.component.html',
  styleUrls: ['./get-name.component.scss']
})
export class GetNameComponent implements OnInit {
  name;

  constructor(public dialogRef: MatDialogRef<GetNameComponent>,
    private swal : NotificationService) { }

  ngOnInit(): void {
  }

  onNoClick(){
    this.dialogRef.close();
  }

  onSave(){
    if(name)
      this.dialogRef.close(name);
    else
    this.swal.fail(
      "please set a name before saving"
    );
  }
}
