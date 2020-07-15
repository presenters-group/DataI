import { Component, OnInit, Input, Output, EventEmitter } from "@angular/core";
import { IFilter } from "src/store/filters";
import { AppState } from "src/store";
import { Store } from "@ngrx/store";
import { selectDataSourcesEntities } from "src/store/data-sources/data-sources.selectors";
import { initialState } from 'src/store/core';
import { setCurrentTap, addToTapes } from 'src/store/core/actions/core.actions';
import { isArray } from 'util';

@Component({
  selector: "app-filter-item",
  templateUrl: "./filter-item.component.html",
  styleUrls: ["./filter-item.component.scss"],
})
export class FilterItemComponent implements OnInit {
  @Input() filter: IFilter;
  @Input() visualizerName: string;
  @Input() enabled: boolean = false;
  @Input() value: any;
  @Input() showOptions: boolean;
  dataSources = this.store.select(selectDataSourcesEntities);
  @Output() onMinus : EventEmitter<any> = new EventEmitter();
  @Output() onChange : EventEmitter<any> = new EventEmitter();

  constructor(private store: Store<AppState>) {}

  ngOnInit(): void {
    console.log(this.value);
    if(this.value == undefined) this.value = this.filter.initValue
  }

  onEnableClicked() {
    this.enabled = !this.enabled;
    this.onChangeValue();
  }

  onDimChangeValue(value) {
    console.log()
    if (!Array.isArray(this.value)) this.value = [];
    if (this.value.includes(value))
      this.value = this.value.filter((v) => v != value);
    else this.value = [...this.value , value];
    this.onChangeValue();
  }

  onChangeMeasure($event){
    this.value = Number.parseInt($event.target.value);
    this.onChangeValue();
  }

  onChangeValue(){
    console.log({value: this.value,active : this.enabled});
    this.onChange.emit({value: this.value,active : this.enabled,id :this.filter.id})
  }

  onMinusClick(){
    this.onMinus.emit(this.filter)
  }

  onEditClick(){
    this.store.dispatch(
      addToTapes({
        tap: {
          name: this.filter.name,
          type: 'filter',
          id: this.filter.id,
        },
      })
    );  }
}
