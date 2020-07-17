import { Component, OnInit, HostListener, ViewChild, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-main-menu',
  templateUrl: './main-menu.component.html',
  styleUrls: ['./main-menu.component.scss']
})
export class MainMenuComponent implements OnInit {
  @ViewChild('container') container;
  opened : number = 0
  @Output() onClose : EventEmitter<any> = new EventEmitter();
  constructor() { }

  @HostListener('document:click',['$event'])
  onClick($event){
    this.opened++;
    if(!$event.path.includes(this.container.nativeElement) && this.opened > 1)
      this.onClose.emit();
  }

  ngOnInit(): void {
  }

}
