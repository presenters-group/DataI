import { Component, OnInit, Input, Output, EventEmitter } from "@angular/core";
import { IFilter } from "src/store/filters";
import { AppState } from "src/store";
import { Store } from "@ngrx/store";
import { selectDataSourcesEntities } from "src/store/data-sources/data-sources.selectors";
import { initialState } from "src/store/core";
import { setCurrentTap, addToTapes } from "src/store/core/actions/core.actions";
import { isArray, isNumber } from "util";
import { first } from 'rxjs/operators';

@Component({
  selector: "app-filter-item",
  templateUrl: "./filter-item.component.html",
  styleUrls: ["./filter-item.component.scss"],
})
export class FilterItemComponent implements OnInit {
  filter: IFilter;
  @Input('filter') set filterSetter(value){
    console.log('blablabla')

    this.checkValue();

    this.filter = value;
  };
  @Input() visualizerName: string;
  @Input() enabled: boolean = false;
  @Input() value: any;
  @Input() showOptions: boolean;
  dataSources = this.store.select(selectDataSourcesEntities);
  @Output() onMinus: EventEmitter<any> = new EventEmitter();
  @Output() onChange: EventEmitter<any> = new EventEmitter();

  constructor(private store: Store<AppState>) {}

  ngOnInit(): void {
    this.checkValue();
  }

  checkValue(){
    this.dataSources.pipe(first()).subscribe((dataSources)=>{
      let type = dataSources[this.filter.dataSource].columns[this.filter.filteredColumn].columnType;
      if(type == 'Dimensions' && !Array.isArray(this.value)) {console.log('arrainaize'); this.value = []}
      else if (type == 'Measures' && !(typeof this.value == 'number') ) this.value = this.filter.initValue;
      else if (type == 'DateTime' ) this.value = this.value ?  new Date(this.value).toISOString().slice(0,10) : '1-1-2009';
    });
  }

  onEnableClicked() {
    this.enabled = !this.enabled;
    this.onChangeValue();
  }

  onDimChangeValue(value) {
    if (!Array.isArray(this.value)) this.value = [];
    if (this.value.includes(value))
      this.value = this.value.filter((v) => v != value);
    else this.value = [...this.value, value];
    this.onChangeValue();
  }

  onChangeMeasure($event) {
    console.log($event.target.value)
    this.dataSources.pipe(first()).subscribe((dataSources)=>{
      let type = dataSources[this.filter.dataSource].columns[this.filter.filteredColumn].columnType;
      console.log(type)
      if(type == 'DateTime'){
        console.log('DateTime')
        this.onChangeData($event);
      }
      else{
        console.log("Mesueres")
        this.value = Number.parseInt($event.target.value);
        this.onChangeValue();
      }
    })
  }

  onChangeData($event){
    this.value = $event.target.value;
    this.onChangeValue();
  }

  onChangeValue() {
    this.onChange.emit({
      value: this.value,
      active: this.enabled,
      id: this.filter.id,
    });
  }

  onMinusClick() {
    this.onMinus.emit(this.filter);
  }

  onEditClick() {
    this.store.dispatch(
      addToTapes({
        tap: {
          name: this.filter.name,
          type: "filter",
          id: this.filter.id,
        },
      })
    );
  }

  consol(data){
    console.log(data);
    return data
  }
}
