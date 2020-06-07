import { Component, HostListener, OnInit } from "@angular/core";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.scss"],
})
export class AppComponent implements OnInit {
  title = "DataI";
  width = 250;
  x = 100;
  oldX = 0;
  grabber = false;

  ngOnInit(): void {
    let element = document.getElementById("grabber");
    this.setGrabberEvents(element);
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
