import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-taps',
  templateUrl: './taps.component.html',
  styleUrls: ['./taps.component.scss']
})
export class TapsComponent implements OnInit {
  currentTapIndex = 0;
  taps= [
    {
      name: "table 1",
      type: "data-source"
    },{
      name: "filter 1",
      type: "filter"
    },{
      name: "dashboard 1",
      type: "dashboard"
    }
  ]
  constructor() { }

  ngOnInit(): void {
  }

  onClose(i : number){
    this.taps = this.taps.filter((tap,index) => index != i)
  }
}
