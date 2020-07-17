import { Component, OnInit } from "@angular/core";
import { AppState } from "src/store";
import { selectCurrentTree } from "src/store/core/selectors/core.selector";
import { Store } from "@ngrx/store";
import { updateCurrentTree } from "src/store/core/actions/core.actions";
import { trigger, state, style, transition, animate } from '@angular/animations';

@Component({
  selector: "app-left-nav",
  templateUrl: "./left-nav.component.html",
  styleUrls: ["./left-nav.component.scss"],
  animations: [
    trigger('menu',[
      state('void',style({
        left: '-200px'
      })),
      transition('* <=> void',[
        animate('0.5s')
      ])
    ])
  ],
})
export class LeftNavComponent implements OnInit {
  showFiller = false;
  showMenu;
  icons = [
    {
      name: "data-sources",
      color: "var(--blue)",
      current: true,
      hover: false,
      src: "/assets/icons/data-sources.svg",
      imageURL: "/assets/icons/data-sources.svg",
      imageURLClicked: "/assets/icons/data-sources-white.svg",
    },
    {
      name: "visualizers",
      color: "var(--pink)",
      current: false,
      hover: false,
      src: "/assets/icons/visualizers.svg",
      imageURL: "/assets/icons/visualizers.svg",
      imageURLClicked: "/assets/icons/visualizers-white.svg",
    },
    {
      name: "dashboards",
      color: "var(--purple)",
      current: false,
      hover: false,
      src: "/assets/icons/dashboards.svg",
      imageURL: "/assets/icons/dashboards.svg",
      imageURLClicked: "/assets/icons/dashboards-white.svg",
    },
    {
      name: "filters",
      color: "var(--sky-blue)",
      current: false,
      hover: false,
      src: "/assets/icons/filters.svg",
      imageURL: "/assets/icons/filters.svg",
      imageURLClicked: "/assets/icons/filters-white.svg",
    },
  ];

  constructor(private store: Store<AppState>) {
    this.store.select(selectCurrentTree).subscribe((value) => {
      for (let icon of this.icons) {
        if (icon.name == value) {
          icon.current = true;
          icon.hover = false;
          icon.src = icon.imageURLClicked;
        } else {
          icon.hover = false;
          icon.current = false;
          icon.src = icon.imageURL;
        }
      }
    });
  }

  ngOnInit(): void {}
  onIconEnter(index: number) {
    if (!this.icons[index].current) {
      this.icons[index].src = this.icons[index].imageURLClicked;
      this.icons[index].hover = true;
    }
  }
  onIconLeave(index: number) {
    if (!this.icons[index].current) {
      this.icons[index].src = this.icons[index].imageURL;
      this.icons[index].hover = false;
    }
  }

  onIconClick(index: number) {
    this.store.dispatch(updateCurrentTree({ name: this.icons[index].name }));
  }
}
