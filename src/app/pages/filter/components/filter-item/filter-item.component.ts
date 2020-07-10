import { Component, OnInit, Input } from '@angular/core';
import { IFilter } from 'src/store/filters';
import { AppState } from 'src/store';
import { Store } from '@ngrx/store';
import { selectDataSourcesEntities } from 'src/store/data-sources/data-sources.selectors';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-filter-item',
  templateUrl: './filter-item.component.html',
  styleUrls: ['./filter-item.component.scss']
})
export class FilterItemComponent implements OnInit {
  @Input() filter : IFilter
  dataSources = this.store.select(selectDataSourcesEntities);
  @Input() visualizerName: string;
  @Input()enabled: boolean = false;
  value : any[] = [];

  constructor(private store: Store<AppState>) {

  }

  ngOnInit(): void {
  }

  onEnableClicked(){
    this.enabled = !this.enabled
  }


  onDimChangeValue(value){
    if(this.value  == undefined)
      this.value = [];
    if(this.value.includes(value))
      this.value = this.value.filter((value)=> value != value);
    else
      this.value.push(value)
  }


}
