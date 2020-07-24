import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-contact-us',
  templateUrl: './contact-us.component.html',
  styleUrls: ['./contact-us.component.scss']
})
export class ContactUsComponent implements OnInit {
  members= [
    {
      img: '/assets/members/hamza.jpg',
      name: 'Hamza Alhindi',
      content:  ['Python - Django Developer','Angular - Front End'],
      color: '#C4C4C4',
      email: 'hamzaalhinde2000@gmail.com'
    },
    {
      img: '/assets/members/basel.jpg',
      name: 'Basel Hijazi',
      content:  ['Flutter - Android Developer','UX/UI Adobe XD','PHP - FireBase Developer'],
      color: '#ED1978',
      email: 'basel.hjz1999@gmail.com'
    },
    {
      img: '/assets/members/kareem.jpg',
      name: 'Kareem Yamani',
      content:  ['C# WPF developer','Graphic Designer','Pyhton Developer'],
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
      content:  ['Angular - Web Developer','UX/UI Designer','Nodejs - NestJs developer'],
      color: '#41C1C3',
      email: 'bilal.azizieh.atg@gmail.com'

    },
  ]
  constructor() { }

  ngOnInit(): void {
  }

}
