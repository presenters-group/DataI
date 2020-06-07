import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-left-nav',
  templateUrl: './left-nav.component.html',
  styleUrls: ['./left-nav.component.scss']
})
export class LeftNavComponent implements OnInit {

  icons = [
    {
      color: "var(--blue)",
      current: true,
      hover: false,
      src:"/assets/icons/data-sources.svg",
      imageURL: '/assets/icons/data-sources.svg',
      imageURLClicked: '/assets/icons/data-sources-white.svg'
    },
    {
      color: "var(--pink)",
      current: false,
      hover: false,
      src:"/assets/icons/visualizers.svg",
      imageURL: '/assets/icons/visualizers.svg',
      imageURLClicked: '/assets/icons/visualizers-white.svg'
    },
    {
      color: "var(--purple)",
      current: false,
      hover: false,
      src:"/assets/icons/dashboards.svg",
      imageURL: '/assets/icons/dashboards.svg',
      imageURLClicked: '/assets/icons/dashboards-white.svg'
    },
    {
      color: "var(--sky-blue)",
      current: false,
      hover: false,
      src:"/assets/icons/filters.svg",
      imageURL: '/assets/icons/filters.svg',
      imageURLClicked: '/assets/icons/filters-white.svg'
    }
  ]

  constructor() { }

  ngOnInit(): void {
    for(let icon of this.icons)
      if(icon.current == true)
        icon.src = icon.imageURLClicked
  }
  onIconEnter(index : number){
    if(!this.icons[index].current){
      this.icons[index].src = this.icons[index].imageURLClicked;
      this.icons[index].hover = true;
    }
  }
  onIconLeave(index : number){
    if(!this.icons[index].current){
      this.icons[index].src = this.icons[index].imageURL;
      this.icons[index].hover = false;
    }
  }
}
