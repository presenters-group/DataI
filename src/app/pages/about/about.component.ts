import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.scss']
})
export class AboutComponent implements OnInit {
  members= [
    {
      img: '/assets/members/hamza.jpg',
      name: 'Hamza Alhindi',
      content:  ['Django Developer'],
      color: '#CDCDCD',
      email: 'bilal.azizieh.atg@gmail.com'
    },
    {
      img: '/assets/members/basel.jpg',
      name: 'Basel Hijazi',
      content:  ['Flutter - Mobile Developer'],
      color: '#ED1978',
      email: 'basel.hjz1999@gmail.com'
    },
    {
      img: '/assets/members/kareem.jpg',
      name: 'Kareem Yamani',
      content:  ['Pyhton - Chart Drawer'],
      color: '#5D4EA0',
      email: 'kareemmhdyamani@gmail.com'
    },
    {
      img: '/assets/members/fareek.jpg',
      name: 'Fareck Allony',
      content:  ['Python - Django Developer',
        'C# WPF Developer',
        'Java SE Developer',],
      color: '#227BC0',
      email: 'mr.allony5556@gmail.com'

    },
    {
      img: '/assets/members/bilal.jpg',
      name : 'Bilal Azizieh',
      content:  ['Angular - Web Developer','UX/UI Designer'],
      color: '#41C1C3',
      email: 'bilal.azizieh.atg@gmail.com'

    },
  ]
  constructor() { }

  ngOnInit(): void {
  }

}
