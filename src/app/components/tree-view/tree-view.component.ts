import {
  Component,
  OnInit,
  AfterViewInit,
  ViewChild,
  ElementRef,
  Renderer2,
} from "@angular/core";
import { element } from "protractor";
import { isLoweredSymbol } from "@angular/compiler";

@Component({
  selector: "app-tree-view",
  templateUrl: "./tree-view.component.html",
  styleUrls: ["./tree-view.component.scss"],
})
export class TreeViewComponent implements OnInit, AfterViewInit {
  @ViewChild("tree") tree: ElementRef;
  //TODO : get from store
  items = {
    name: "data-sources",
    closed: false,
    children: [
      {
        closed: false,
        name: "table1",
        children: [
          {
            closed: true,
            name: "dimensions",
            children: [
              {
                name: "column1",
              },
              {
                name: "column2",
              },
              {
                name: "column3",
              },
            ],
          },
          {
            name: "dimensions",
            closed: false,
            children: [
              {
                name: "column1",
              },
              {
                name: "column2",
              },
              {
                name: "column3",
              },
            ],
          },
          {
            name: "measurers",
            closed: true,
            children: [
              {
                name: "column3",
                closed: false,
                children: [{ name: "plus" }],
              },
              {
                name: "column4",
              },
              {
                name: "column5",
              },
            ],
          },
        ],
      },
      {},
      {},
    ],
  };
  constructor(private renderer: Renderer2) {}

  ngOnInit(): void {}

  ngAfterViewInit(): void {
    this.tree.nativeElement.innerHTML = "";
    this.createTree(this.tree.nativeElement, this.items, 0);
  }

  createTree(element: ElementRef, items: any, level: number) {
    let itemElement = this.renderer.createElement("div");
    this.renderer.appendChild(element, itemElement);
    let content = this.renderer.createElement("div");
    this.renderer.addClass(content, "content");
    this.renderer.appendChild(itemElement, content);
    if (items.children) {
      let arrow = this.renderer.createElement("img");
      this.renderer.setAttribute(arrow, "src", "/assets/icons/arrow.svg");
      this.renderer.appendChild(content, arrow);
      this.renderer.addClass(arrow, "arrow");
      arrow.addEventListener("click", ($event) => {
        this.onArrowClick($event, this.renderer);
      });
      let childrenContainerElement = this.renderer.createElement("div");
      this.renderer.addClass(
        childrenContainerElement,
        "childrenContainerElement"
      );
      this.renderer.setStyle(
        childrenContainerElement,
        "padding-bottom",
        `${level + 5}px`
      );
      this.renderer.setStyle(
        childrenContainerElement,
        "margin-bottom",
        `${level + 3}px`
      );
      this.renderer.appendChild(itemElement, childrenContainerElement);
      this.renderer.addClass(childrenContainerElement, "item");
      this.renderer.setStyle(
        childrenContainerElement,
        "padding-left",
        `${level + 20}px`
      );
      for (let item of items.children) {
        this.createTree(childrenContainerElement, item, level + 1);
      }
      if (!items.closed) {
        this.renderer.addClass(arrow, "opened");
      } else this.renderer.addClass(childrenContainerElement, "closed");
    }

    let name = this.renderer.createElement("div");
    name.data = items.data;
    let text = this.renderer.createText(items.name);
    this.renderer.appendChild(name, text);
    this.renderer.addClass(name, "name");
    this.renderer.appendChild(content, name);
    this.renderer.addClass(itemElement, "item");
  }

  onArrowClick($event, renderer) {
    let element = $event.srcElement;
    [...element.classList].includes("opened")
      ? renderer.removeClass(element, "opened")
      : renderer.addClass(element, "opened");
      console.log(renderer.nextSibling(element).data);
    let parent = renderer.parentNode(element);
    let uncle = renderer.nextSibling(parent);
    [...uncle.classList].includes("closed")
      ? renderer.removeClass(uncle, "closed")
      : renderer.addClass(uncle, "closed");
  }
}
