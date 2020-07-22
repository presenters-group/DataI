import {
  Component,
  OnInit,
  HostListener,
  ViewChild,
  Output,
  EventEmitter,
} from "@angular/core";
import { selectCurrentDataSource } from "src/store/data-sources/data-sources.selectors";
import { AppState } from "src/store";
import { Store } from "@ngrx/store";
import { Observable } from "rxjs";
import { MatDialog } from "@angular/material/dialog";
import { GetNameComponent } from "../get-name/get-name.component";
import { HttpClient } from "@angular/common/http";
import { BASE_URL } from "src/utils/url.util";
import { saveAs } from "file-saver";
import { NotificationService } from 'src/store/notifications/notifications.service';
import {openProject} from '../../../store/core/actions/core.actions'
@Component({
  selector: "app-main-menu",
  templateUrl: "./main-menu.component.html",
  styleUrls: ["./main-menu.component.scss"],
})
export class MainMenuComponent implements OnInit {
  @ViewChild("container") container;
  opened: number = 0;
  dataSource: Observable<any>;
  data: any[];
  @Output() onClose: EventEmitter<any> = new EventEmitter();
  constructor(
    private store: Store<AppState>,
    public dialog: MatDialog,
    private httpClient: HttpClient,
    private notification:NotificationService
  ) {
    this.dataSource = this.store.select(selectCurrentDataSource);
  }

  @HostListener("document:click", ["$event"])
  onClick($event) {
    this.opened++;
    if (!$event.path.includes(this.container.nativeElement) && this.opened > 1)
      this.onClose.emit();
  }

  onExport(as: string) {
    let dialogRef = this.dialog.open(GetNameComponent);
    dialogRef.afterClosed().subscribe((name) => {
      console.log(name);
      if (name) {
        if (as == "excel") {
          console.log(`${BASE_URL}excel-export/`);
          this.httpClient
            .get(
              `${BASE_URL}excel-export/`,
              { responseType: "blob" }
            )
            .subscribe((res) =>
              this.saveFile(res, "application/ms-excel", `${name}.xlsx`)
            );
        } else if(as == 'csv') {
          console.log(`${BASE_URL}csv-export/`);
          this.httpClient
            .get(
              `${BASE_URL}csv-export/`,
              {
                responseType: "blob",
              }
            )
            .subscribe((response) => this.saveFile(response, "text/csv", `${name}.csv`));
        }
        else if(as == 'dataI'){
          console.log(`${BASE_URL}dataI-export//`);
          this.httpClient
            .get(
              `${BASE_URL}dataI-export/`,
              {
                responseType: "blob",
              }
            )
            .subscribe((response) => this.saveFile(response, "text/datai", `${name}.dataI`));
        }
      }
    });
  }

  // downloadFile(data: any, type: string) {
  //   const blob = new Blob([data], { type: type });

  //   const url = window.URL.createObjectURL(blob);
  //   window.open(url);
  // }

  saveFile = (blobContent: Blob, type: string, fileName: string) => {
    const blob = new Blob([blobContent], { type: "application/octet-stream" });
    saveAs(blob, fileName);
  };
  // downLoadFile(data: any, type: string) {
  //   let blob = new Blob([data], { type: type});
  //   let url = window.URL.createObjectURL(blob);
  //   let pwa = window.open(url);
  //   console.log(pwa,url,blob)
  //   if (!pwa || pwa.closed || typeof pwa.closed == 'undefined') {
  //       alert( 'Please disable your Pop-up blocker and try again.');
  //   }
  // }
  onOpenClick($event){
    let x = $event.target.files[0].name.split('.')
    console.log(x,$event.target.files[0].name);
    if(x[x.length-1].toLowerCase() == 'datai'){
      let file = $event.target.files[0]
      this.store.dispatch(openProject({data: {file : file}}))
    }
    else
      this.notification.fail('Please Add a Valid File');
  }

  ngOnInit(): void {}
}
