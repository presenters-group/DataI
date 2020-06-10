import { Component, HostListener, OnInit, AfterViewInit } from "@angular/core";
import { Observable } from 'rxjs';
import { Store } from '@ngrx/store';
import { AppState } from 'src/store';
import { isTreeOpened } from 'src/store/core/selectors/core.selector';

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.scss"],
})
export class AppComponent implements OnInit, AfterViewInit {

  title = "DataI";
  width = 250;
  x = 100;
  oldX = 0;
  grabber = false;
  isTreeOpened : Observable<boolean>
  eventHandlers : any[] = [];
  constructor(private store : Store<AppState>){
    this.isTreeOpened = this.store.select(isTreeOpened);
  }
  ngOnInit(): void {}
  ngAfterViewInit(){
    let element = document.getElementById("grabber");
    this.isTreeOpened.subscribe((value)=>{
      if(value == true)
        this.setGrabberEvents(element);
      })
  }
  setGrabberEvents(element) {
    document.addEventListener("mousemove", (event) => {
      if (!this.grabber) {
        return;
      }
      this.resizer((event.clientX - this.oldX)*2);
      this.oldX = event.clientX;
    });
    document.addEventListener("mouseup", () => {
      this.grabber = false;
    });

    element.addEventListener("mousedown", (event) => {
      this.grabber = true;
      this.oldX = event.clientX;
      event.preventDefault();
    });
  }
  resizer(offsetX: number) {
    if (this.width + offsetX < 250 || this.width + offsetX > 1500) return;
    this.width += offsetX;
  }
}
