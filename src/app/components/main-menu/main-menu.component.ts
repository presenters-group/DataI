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
import { MatDialogRef, MatDialog } from "@angular/material/dialog";
import { GetNameComponent } from "../get-name/get-name.component";
import { HttpClient } from "@angular/common/http";
import { BASE_URL } from "src/utils/url.util";

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
    private httpClient: HttpClient
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
          this.httpClient
            .put(`${BASE_URL}excel-export/`, {
              fileName: `${name}.xlsx`,
            })
            .subscribe((data) => {
              console.log(data);
            });
        } else {
          this.httpClient
            .put(`${BASE_URL}csv-export/`, {
              fileName: `${name}.csv`,
            })
            .subscribe((data) => {
              console.log(data);
            });
        }
      }
    });
  }

  ngOnInit(): void {}
}
