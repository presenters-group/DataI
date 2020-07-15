import {
  Component,
  OnInit,
  AfterViewInit,
  ViewChild,
  ElementRef,
  Renderer2,
} from "@angular/core";
import { Store } from "@ngrx/store";
import { selectCurrentTree } from "src/store/core/selectors/core.selector";
import { AppState } from "src/store";
import { TreeService } from "./tree.service";
import { addToTapes } from "src/store/core/actions/core.actions";
import { first } from "rxjs/operators";
import { MatDialog } from "@angular/material/dialog";
import { AddVisualizerComponent } from "src/app/pages/visualizer/dialogs/add-visualizer/add-visualizer.component";
import { createVisualizer, deleteVisualizer } from "src/store/visualizers";
import { AddDataSourceComponent } from "src/app/pages/data-source/dialogs/add-data-source/add-data-source.component";
import { AddFilterComponent } from "src/app/pages/filter/dialogs/add-filter/add-filter.component";
import { createFilter, deleteFilter } from "src/store/filters";
import { deleteDataSource } from "src/store/data-sources";
import { deleteDashboard, createDashboard } from "src/store/dashboards";
import { NotificationService } from "src/store/notifications/notifications.service";
import { AddDashboardComponent } from "src/app/pages/dashboard/dialogs/add-dashboard/add-dashboard.component";
@Component({
  selector: "app-tree-view",
  templateUrl: "./tree-view.component.html",
  styleUrls: ["./tree-view.component.scss"],
})
export class TreeViewComponent implements OnInit, AfterViewInit {
  @ViewChild("tree") tree: ElementRef;

  items;
  constructor(
    private renderer: Renderer2,
    private store: Store<AppState>,
    private treeService: TreeService,
    public dialog: MatDialog,
    private notification: NotificationService
  ) {}

  ngOnInit(): void {}

  ngAfterViewInit(): void {
    this.onRefreshClick();
  }
  initialTree() {
    this.tree.nativeElement.innerHTML = "";
    for (let i = 0; i < this.items.children.length; i++)
      this.createTree(this.tree.nativeElement, this.items.children[i], 0);
  }

  createTree(element: ElementRef, items: any, level: number) {
    let itemElement = this.renderer.createElement("div");
    this.renderer.appendChild(element, itemElement);
    let content = this.renderer.createElement("div");
    content.content = items.content;

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
    if (content.content) {
      this.renderer.addClass(content, "clickable");
      name.addEventListener("click", ($event) => {
        this.onNameClick($event, this.renderer);
      });
      let minus = this.renderer.createElement("img");
      this.renderer.setAttribute(minus, "src", "/assets/icons/minus.svg");
      this.renderer.appendChild(content, minus);
      this.renderer.addClass(minus, "minus");
      if (
        content.content.type == "filter" ||
        content.content.type == "visualizer" ||
        content.content.type == "dashboard"
      ) {
        let edit = this.renderer.createElement("img");
        this.renderer.setAttribute(edit, "src", "/assets/icons/edit.svg");
        this.renderer.addClass(edit, "edit");
        this.renderer.appendChild(content, edit);
        edit.addEventListener("click", ($event) => {
          this.onEditClick($event);
        });
      }
      minus.addEventListener("click", ($event) => {
        this.onDeleteClick($event);
      });
    }
  }

  onNameClick($event, renderer) {
    let element = $event.srcElement;
    let parent = renderer.parentNode(element);
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
    let uncle = renderer.nextSibling(parent);
    [...uncle.classList].includes("closed")
      ? renderer.removeClass(uncle, "closed")
      : renderer.addClass(uncle, "closed");
  }

  onAddClick() {
    this.store
      .select(selectCurrentTree)
      .pipe(first())
      .subscribe((value: any) => {
        switch (value) {
          case "data-sources":
            let dialogRefDataSource = this.dialog.open(AddDataSourceComponent);
            break;
          case "visualizers":
            let dialogRefVisualizer = this.dialog.open(AddVisualizerComponent);
            dialogRefVisualizer.afterClosed().subscribe((result) => {
              this.store.dispatch(
                createVisualizer({
                  data: { ...result.value, id: 0, isDeleted: false },
                })
              );
            });
            break;
          case "filters":
            let dialogRefFilter = this.dialog.open(AddFilterComponent);
            dialogRefFilter.afterClosed().subscribe((result) => {
              this.store.dispatch(
                createFilter({
                  data: {
                    ...result.value,
                    initValue: Number.parseInt(result.value.initValue),
                    id: 0,
                    isDeleted: false,
                  },
                })
              );
            });
            break;
          case "dashboards":
            let dialogRefDashboard = this.dialog.open(AddDashboardComponent);
            dialogRefDashboard.afterClosed().subscribe((result) => {
              this.store.dispatch(
                createDashboard({
                  data: { ...result.value, id: 0, isDeleted: false },
                })
              );
            });
            break;
        }
      });
  }

  onDeleteClick($event) {
    let element = $event.srcElement;
    let content = this.renderer.parentNode(element).content;

    this.notification
      .deleteConfirmAlert({
        title: `Are you sure you want to delete ${content.name}?`,
      })
      .subscribe((value) => {
        if (value == true) {
          switch (content.type) {
            case "visualizer":
              this.store.dispatch(deleteVisualizer({ id: content.id }));
              break;
            case "filter":
              this.store.dispatch(deleteFilter({ id: content.id }));
              break;
            case "data-source":
              this.store.dispatch(deleteDataSource({ id: content.id }));
              break;
            case "dashboard":
              this.store.dispatch(deleteDashboard({ id: content.id }));
              break;
          }
          this.onRefreshClick();
        }
      });
  }

  onRefreshClick() {
    this.store.select(selectCurrentTree).subscribe((value: any) => {
      this.treeService.fillOut(value).subscribe((tree) => {
        this.items = tree;
        this.initialTree();
      });
    });
  }

  onEditClick($event){
    let element = $event.srcElement;
    let content = this.renderer.parentNode(element).content;

          switch (content.type) {
            case "visualizer":
              this.store.dispatch(deleteVisualizer({ id: content.id }));
              break;
            case "filter":
              this.store.dispatch(
                addToTapes({
                  tap: {
                    name: content.name,
                    type: content.type,
                    id: content.id,
                  },
                }));
              break;
            // case "data-source":
            //   this.store.dispatch(deleteDataSource({ id: content.id }));
            //   break;
            case "dashboard":
              this.store.dispatch(deleteDashboard({ id: content.id }));
              break;
          }
          this.onRefreshClick();
  }
}
