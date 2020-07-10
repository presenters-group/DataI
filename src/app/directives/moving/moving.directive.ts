import {
  Directive,
  ElementRef,
  HostListener,
  Renderer2,
  AfterViewInit,
  Input,
} from "@angular/core";

@Directive({
  selector: "[moving]",
})
export class MovingDirective implements AfterViewInit {
  points: any = {};
  state: MoveState;
  oldEvent;
  isScalable: boolean = false;
  @Input() scalable : boolean = true;

  constructor(private el: ElementRef, private renderer: Renderer2) {}

  ngAfterViewInit() {
    this.el.nativeElement;
  }

  addScalePoints() {
    this.renderer.addClass(this.el.nativeElement, "move-element");

    this.points.top = this.renderer.createElement("div");
    this.points.left = this.renderer.createElement("div");
    this.points.right = this.renderer.createElement("div");
    this.points.bottom = this.renderer.createElement("div");
    this.points.topLeft = this.renderer.createElement("div");
    this.points.topRight = this.renderer.createElement("div");
    this.points.bottomLeft = this.renderer.createElement("div");
    this.points.bottomRight = this.renderer.createElement("div");

    this.renderer.addClass(this.points.top, "move-top");
    this.renderer.addClass(this.points.left, "move-left");
    this.renderer.addClass(this.points.right, "move-right");
    this.renderer.addClass(this.points.bottom, "move-bottom");
    this.renderer.addClass(this.points.topLeft, "move-left");
    this.renderer.addClass(this.points.topRight, "move-right");
    this.renderer.addClass(this.points.bottomLeft, "move-left");
    this.renderer.addClass(this.points.bottomRight, "move-right");

    this.renderer.addClass(this.points.topLeft, "move-top");
    this.renderer.addClass(this.points.topRight, "move-top");
    this.renderer.addClass(this.points.bottomLeft, "move-bottom");
    this.renderer.addClass(this.points.left, "move-halfVertical");
    this.renderer.addClass(this.points.top, "move-halfHorizontal");
    this.renderer.addClass(this.points.right, "move-halfVertical");
    this.renderer.addClass(this.points.bottomRight, "move-bottom");
    this.renderer.addClass(this.points.bottom, "move-halfHorizontal");

    this.renderer.addClass(this.points.top, "move-circle");
    this.renderer.addClass(this.points.left, "move-circle");
    this.renderer.addClass(this.points.right, "move-circle");
    this.renderer.addClass(this.points.bottom, "move-circle");
    this.renderer.addClass(this.points.topLeft, "move-circle");
    this.renderer.addClass(this.points.topRight, "move-circle");
    this.renderer.addClass(this.points.bottomLeft, "move-circle");
    this.renderer.addClass(this.points.bottomRight, "move-circle");

    this.renderer.appendChild(this.el.nativeElement, this.points.top);
    this.renderer.appendChild(this.el.nativeElement, this.points.left);
    this.renderer.appendChild(this.el.nativeElement, this.points.right);
    this.renderer.appendChild(this.el.nativeElement, this.points.bottom);
    this.renderer.appendChild(this.el.nativeElement, this.points.topLeft);
    this.renderer.appendChild(this.el.nativeElement, this.points.topRight);
    this.renderer.appendChild(this.el.nativeElement, this.points.bottomLeft);
    this.renderer.appendChild(this.el.nativeElement, this.points.bottomRight);

    this.isScalable = true;
  }

  removeScalePoints() {
    this.renderer.removeClass(this.el.nativeElement, "move-element");

    this.renderer.removeChild(this.el.nativeElement, this.points.top);
    this.renderer.removeChild(this.el.nativeElement, this.points.left);
    this.renderer.removeChild(this.el.nativeElement, this.points.right);
    this.renderer.removeChild(this.el.nativeElement, this.points.bottom);
    this.renderer.removeChild(this.el.nativeElement, this.points.topLeft);
    this.renderer.removeChild(this.el.nativeElement, this.points.topRight);
    this.renderer.removeChild(this.el.nativeElement, this.points.bottomLeft);
    this.renderer.removeChild(this.el.nativeElement, this.points.bottomRight);

    this.points = {};

    this.isScalable = false;
  }
  @HostListener("document:mousedown", ["$event"]) onClick($event) {
    if(this.scalable){
      console.log($event);
      if (
        $event.target == this.el.nativeElement ||
        Object.values(this.points).includes($event.target)
      ) {
        if (!this.isScalable) this.addScalePoints();
      } else if (this.isScalable) this.removeScalePoints();
    }
  }

  @HostListener("mousedown", ["$event"]) onMouseDown($event) {
    this.oldEvent = $event;
    this.oldEvent.oldLeft = parseInt(this.el.nativeElement.style.left, 10);
    this.oldEvent.oldTop = parseInt(this.el.nativeElement.style.top, 10);
    this.oldEvent.oldWidth = parseInt(this.el.nativeElement.style.width);
    this.oldEvent.oldHeight = parseInt(this.el.nativeElement.style.height);
    for (let pointPosition of Object.keys(this.points))
      if ($event.target == this.points[pointPosition])
        this.state = MoveState[pointPosition];
    if ($event.target == this.el.nativeElement) this.state = MoveState.move;
  }

  @HostListener("document:mousemove", ["$event"]) onMouseMove($event) {
    const newEvent = $event;
    const oldEvent = this.oldEvent;
    switch (this.state) {
      case MoveState.move:
        this.moveLeft(oldEvent, newEvent);
        this.moveTop(oldEvent, newEvent);
        break;

      case MoveState.top:
        this.scaleTop(oldEvent, newEvent);
        break;

      case MoveState.bottom:
        this.scaleBottom(oldEvent, newEvent);
        break;
      case MoveState.left:
        this.scaleLeft(oldEvent, newEvent);
        break;
      case MoveState.right:
        this.scaleRight(oldEvent, newEvent);
        break;
      case MoveState.topLeft:
        this.scaleTopLeft(oldEvent, newEvent);
        break;
      case MoveState.topRight:
        this.scaleTopRight(oldEvent, newEvent);
        break;
      case MoveState.bottomLeft:
        this.scaleBottomLeft(oldEvent, newEvent);
        break;
      case MoveState.bottomRight:
        this.scaleBottomRight(oldEvent, newEvent);
        break;
      default:
        return;
    }

    // if (this.el.nativeElement.id === 'dashboard'){
    //   if(this.element != undefined){
    //     this.element.style.top = 762-this.el.nativeElement.clientYpx;
    //     this.element.style.left = 1429-this.el.nativeElement.clientXpx;
    //   }
    // }
  }

  moveTop(oldEvent, newEvent) {
    this.el.nativeElement.style.top = `${
      oldEvent.oldTop + (newEvent.pageY - oldEvent.pageY)
    }px`;
  }
  moveLeft(oldEvent, newEvent) {
    this.el.nativeElement.style.left = `${
      oldEvent.oldLeft + (newEvent.pageX - oldEvent.pageX)
    }px`;
  }
  scaleTop(oldEvent, newEvent) {
    this.el.nativeElement.style.height = `${
      oldEvent.oldHeight + (oldEvent.pageY - newEvent.pageY)
    }px`;
    this.moveTop(oldEvent, newEvent);
  }
  scaleBottom(oldEvent, newEvent) {
    this.el.nativeElement.style.height = `${
      oldEvent.oldHeight + (newEvent.pageY - oldEvent.pageY)
    }px`;
  }
  scaleLeft(oldEvent, newEvent) {
    this.el.nativeElement.style.width = `${
      oldEvent.oldWidth + (oldEvent.pageX - newEvent.pageX)
    }px`;
    this.moveLeft(oldEvent, newEvent);
  }

  scaleRight(oldEvent, newEvent) {
    this.el.nativeElement.style.width = `${
      oldEvent.oldWidth + (newEvent.pageX - oldEvent.pageX)
    }px`;
  }

  scaleTopLeft(oldEvent, newEvent) {
    this.scaleTop(oldEvent, newEvent);
    this.scaleLeft(oldEvent, newEvent);
  }

  scaleTopRight(oldEvent, newEvent) {
    this.scaleTop(oldEvent, newEvent);
    this.scaleRight(oldEvent, newEvent);
  }
  scaleBottomLeft(oldEvent, newEvent) {
    this.scaleBottom(oldEvent, newEvent);
    this.scaleLeft(oldEvent, newEvent);
  }
  scaleBottomRight(oldEvent, newEvent) {
    this.scaleBottom(oldEvent, newEvent);
    this.scaleRight(oldEvent, newEvent);
  }

  @HostListener("document:mouseup", ["$event"]) onMouseUp($event) {
    this.state = MoveState.none;
  }
}

enum MoveState {
  top = "top",
  bottom = "bottom",
  left = "left",
  right = "right",
  topLeft = "topLeft",
  topRight = "topRight",
  bottomLeft = "bottomLeft",
  bottomRight = "bottomRight",
  move = "move",
  none = "none",
}
