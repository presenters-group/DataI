import {
  Component,
  OnInit,
  AfterViewInit,
  ViewChild,
  ElementRef,
  Renderer2,
} from "@angular/core";
import { Store } from "@ngrx/store";
import {
  selectCurrentTree,
} from "src/store/core/selectors/core.selector";
import { AppState } from "src/store";
import { TreeService } from "./tree.service";
import { addToTapes } from "src/store/core/actions/core.actions";
import { ConditionalExpr } from '@angular/compiler';
import { first } from 'rxjs/operators';
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';
import { AddVisualizerComponent } from 'src/app/pages/visualizer/dialogs/add-visualizer/add-visualizer.component';
import { createVisualizer } from 'src/store/visualizers';
import { AddDataSourceComponent } from 'src/app/pages/data-source/dialogs/add-data-source/add-data-source.component';
@Component({
  selector: "app-tree-view",
  templateUrl: "./tree-view.component.html",
  styleUrls: ["./tree-view.component.scss"],
})
export class TreeViewComponent implements OnInit, AfterViewInit {
  @ViewChild("tree") tree: ElementRef;

  items
  constructor(
    private renderer: Renderer2,
    private store: Store<AppState>,
    private treeService: TreeService,
    public dialog: MatDialog
  ) {}

  ngOnInit(): void {}

  ngAfterViewInit(): void {
    this.store.select(selectCurrentTree).subscribe((value: any) => {
      this.treeService.fillOut(value).subscribe((tree) => {
        this.items = tree;
      });
      this.initialTree();
    });
  }
  initialTree() {
    this.tree.nativeElement.innerHTML = "";
    this.createTree(this.tree.nativeElement, this.items, 0);
  }

  createTree(element: ElementRef, items: any, level: number) {
    let itemElement = this.renderer.createElement("div");
    this.renderer.appendChild(element, itemElement);
    let content = this.renderer.createElement("div");
    content.content = items.content;
    if (content.content) {
      content.addEventListener("dblclick", ($event) => {
        this.onNameDoubleClick($event, this.renderer);
      });
      // content.addEventListener('click',this.onNameDoubleClick($event,this.renderer)) ;
    }
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

  onNameDoubleClick($event, renderer) {
    console.log("anything");
    let element = $event.srcElement;
    let parent = renderer.parentNode(element);
    console.log(parent.content);
    if (
      parent.content &&
      (parent.content.type == "filter" ||
        parent.content.type == "visualizer" ||
        parent.content.type == "dashboard" ||
        parent.content.type == "data-source")
    )
      this.store.dispatch(
        addToTapes({
          tap: {
            name: parent.content.name,
            type: parent.content.type,
            id: parent.content.id,
          },
        })
      );
  }

  onArrowClick($event, renderer) {
    let element = $event.srcElement;
    [...element.classList].includes("opened")
      ? renderer.removeClass(element, "opened")
      : renderer.addClass(element, "opened");
    let parent = renderer.parentNode(element);
    console.log(parent.content);
    let uncle = renderer.nextSibling(parent);
    [...uncle.classList].includes("closed")
      ? renderer.removeClass(uncle, "closed")
      : renderer.addClass(uncle, "closed");
  }

  onAddClick(){
    this.store.select(selectCurrentTree).pipe(first()).subscribe((value: any) => {
      console.log(value)
      switch(value){
        case 'data-sources':
          let dialogRefDataSource = this.dialog.open(AddDataSourceComponent);
           break;
        case 'visualizers':
          let dialogRefVisualizer = this.dialog.open(AddVisualizerComponent);
          dialogRefVisualizer.afterClosed().subscribe(result => {
            this.store.dispatch(createVisualizer({data:{...result.value, id: 0, isDeleted: false}}));
          });
      }
    });
  }

  onDeleteClick(){

  }

  onRefreshClick(){
    this.store.select(selectCurrentTree).subscribe((value: any) => {
      this.treeService.fillOut(value).subscribe((tree) => {
        this.items = tree;
      });
      this.initialTree();
    });
  }

}
