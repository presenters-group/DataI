import { AfterViewInit, Renderer2, ViewChild, ElementRef } from '@angular/core';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements AfterViewInit {
  dashboards = [
      {
          "visualizers": [
              {
                  "visualizationIndex": 0,
                  "measurements": {
                      "width": 100.0,
                      "height": 100.0,
                      "x": 100.0,
                      "y": 100.0
                  },
                  "displayedFilters": [
                      {
                          "filterIndex": 0,
                          "measurements": {
                              "width": 100.0,
                              "height": 100.0,
                              "x": 100.0,
                              "y": 200.0
                          }
                      },
                      {
                          "filterIndex": 1,
                          "measurements": {
                              "width": 100.0,
                              "height": 100.0,
                              "x": 300.0,
                              "y": 150.0
                          }
                      }
                  ]
              }
          ]
        }
    ]
  @ViewChild("visualizer") vis: ElementRef;
  child
  points : any = {}
  constructor(
    private renderer:Renderer2
  ) { }

  ngAfterViewInit(): void {
    this.points.topCircle = this.renderer.createElement('div');
    let leftCircle = this.renderer.createElement('div');
    let rightCircle = this.renderer.createElement('div');
    let bottomCircle = this.renderer.createElement('div');
    let topLeftCircle = this.renderer.createElement('div');
    let topRightCircle = this.renderer.createElement('div');
    let bottomLeftCircle = this.renderer.createElement('div');
    let bottomRightCircle = this.renderer.createElement('div');

    this.renderer.addClass(this.points.topCircle,'top');
    this.renderer.addClass(leftCircle,'left');
    this.renderer.addClass(rightCircle,'right');
    this.renderer.addClass(bottomCircle,'bottom');
    this.renderer.addClass(topLeftCircle,'left');
    this.renderer.addClass(topRightCircle,'right');
    this.renderer.addClass(bottomLeftCircle,'left');
    this.renderer.addClass(bottomRightCircle,'right');

    this.renderer.addClass(this.points.topCircle,'halfHorizontal');
    this.renderer.addClass(leftCircle,'halfVertical');
    this.renderer.addClass(rightCircle,'halfVertical');
    this.renderer.addClass(bottomCircle,'halfHorizontal');
    this.renderer.addClass(topLeftCircle,'top');
    this.renderer.addClass(topRightCircle,'top');
    this.renderer.addClass(bottomLeftCircle,'bottom');
    this.renderer.addClass(bottomRightCircle,'bottom');

    this.renderer.addClass(this.points.topCircle,'circle');
    this.renderer.addClass(leftCircle,'circle');
    this.renderer.addClass(rightCircle,'circle');
    this.renderer.addClass(bottomCircle,'circle');
    this.renderer.addClass(topLeftCircle,'circle');
    this.renderer.addClass(topRightCircle,'circle');
    this.renderer.addClass(bottomLeftCircle,'circle');
    this.renderer.addClass(bottomRightCircle,'circle');


    this.renderer.appendChild(this.vis.nativeElement,this.points.topCircle)
    this.renderer.appendChild(this.vis.nativeElement,leftCircle)
    this.renderer.appendChild(this.vis.nativeElement,rightCircle)
    this.renderer.appendChild(this.vis.nativeElement,bottomCircle)
    this.renderer.appendChild(this.vis.nativeElement,topLeftCircle)
    this.renderer.appendChild(this.vis.nativeElement,topRightCircle)
    this.renderer.appendChild(this.vis.nativeElement,bottomLeftCircle)
    this.renderer.appendChild(this.vis.nativeElement,bottomRightCircle)
  }


}
