import { Component, OnInit, HostListener, ViewChild, Output, EventEmitter } from '@angular/core';
import * as FileSaver from 'file-saver';
import * as XLSX from 'xlsx';
import { selectCurrentDataSource } from "src/store/data-sources/data-sources.selectors";
import { AppState } from "src/store";
import { Store } from '@ngrx/store';
import { Observable } from 'rxjs';


@Component({
  selector: 'app-main-menu',
  templateUrl: './main-menu.component.html',
  styleUrls: ['./main-menu.component.scss']
})
export class MainMenuComponent implements OnInit {
  @ViewChild('container') container;
  opened : number = 0
  dataSource: Observable<any>;
  data : any[];
  @Output() onClose : EventEmitter<any> = new EventEmitter();
  constructor(private store: Store<AppState>) { 
    this.dataSource = this.store.select(selectCurrentDataSource);
  }

  @HostListener('document:click',['$event'])
  onClick($event){
    this.opened++;
    if(!$event.path.includes(this.container.nativeElement) && this.opened > 1)
      this.onClose.emit();
  }



  ngOnInit(): void {
  }

}
