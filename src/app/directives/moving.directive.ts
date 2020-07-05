import { Directive, ElementRef, HostListener, Renderer2 } from '@angular/core';


@Directive({
  selector: '[appMoving]'
})
export class MovingDirective {

  originalColor;
  top;
  buttom;
  right;
  left;
  move = false;
  element = undefined;
  constructor(private el:ElementRef) {

  }

  @HostListener('mousedown') onMouseDown($event){
    this.element = this.el.nativeElement;
  }

  @HostListener('mousemove') onMouseMove($event){
    if (this.el.nativeElement.id === 'dashboard'){
      if(this.element != undefined){
        this.element.style.top = 762-this.el.nativeElement.clientYpx;
        this.element.style.left = 1429-this.el.nativeElement.clientXpx;
      }
    }

  }

}


enum place {
  top,
  left,
  right,
  buttom
}
