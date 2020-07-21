import { Component, OnInit } from "@angular/core";
import { Store } from "@ngrx/store";
import { AppState } from "src/store";
import { updateFilter } from "src/store/filters";
import { selectCurrentFilter } from "src/store/filters/filters.selectors";
import { selectDataSourcesEntities } from "src/store/data-sources/data-sources.selectors";
import { FormBuilder } from "@angular/forms";
import { first } from "rxjs/operators";
import { Validators } from "@angular/forms";
import { NotificationService } from "src/store/notifications/notifications.service";
import { fetchDataSources } from 'src/store/data-sources';
import { IfStmt } from '@angular/compiler';

@Component({
  selector: "app-filter",
  templateUrl: "./filter.component.html",
  styleUrls: ["./filter.component.scss"],
})
export class FilterComponent implements OnInit {
  form;
  objectKeys = Object.keys;
  dataSources = this.store.select(selectDataSourcesEntities);
  filter = this.store.select(selectCurrentFilter);
  value = [];
  constructor(
    private swal: NotificationService,
    private store: Store<AppState>,
    private formBuilder: FormBuilder
  ) {}

  formBuild() {
    this.filter.subscribe((value) => {
      this.form = this.formBuilder.group({
        name: [value.name, Validators.required],
        dataSource: [value.dataSource.toString(), Validators.required],
        filteredColumn: [value.filteredColumn.toString(), Validators.required],
        type: [value.type, Validators.required],
        initValue: [value.initValue],
      });
    });
  }

  ngOnInit(): void {
    // this.initialize();
    this.filter.subscribe((value)=>{
      console.log('initialize')
      this.initialize();
    })
  }

  initialize(){
    setTimeout(()=>{
      this.formBuild();
      this.dataSources.pipe(first()).subscribe((dataSources)=>{
        let type = dataSources[this.form.value.dataSource].columns[this.form.value.filteredColumn].columnType;
        if(type == 'DateTime')
          this.form.controls['initValue'].setValue(new Date(this.form.value.initValue).toISOString().slice(0,10))
        if(type == "Dimension")
        this.form.controls['initValue'].setValue([]);
          console.log(type,this.form.value.initValue)
      })
    },100)
  }

  onSaveClick() {

    if (this.form.valid)
    this.dataSources.pipe(first()).subscribe((dataSources)=>{
      let type = dataSources[this.form.value.dataSource].columns[this.form.value.filteredColumn].columnType
      if(type == 'DateTime'){
        console.log("DateTime")
        this.form.controls['initValue'].setValue(new Date(this.form.value.initValue).toLocaleDateString())
      }
      else if (type == 'Measures'){
        let num = Number.parseInt(this.form.value.initValue);
        if(!num){
          this.swal.fail(
            "Init value cant have a character"
          );
          return;
        }
        this.form.controls['initValue'].setValue(Number.parseInt(this.form.value.initValue));
      }
      this.filter.pipe(first()).subscribe((value) => {
        this.store.dispatch(
          updateFilter({ data: { ...this.form.value, id: value.id } })
        );
        this.formBuild();
      });
      this.store.dispatch(fetchDataSources());

    }); else {
      this.swal.fail("Please Complete The Form With Valid Information Before Saving");
    }
  }

  onNoClick() {
    this.initialize();
  }

  onChangeDataSource() {
    this.form.controls["filteredColumn"].setValue("");
    this.form.controls["type"].setValue("");
  }
}
