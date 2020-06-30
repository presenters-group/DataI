import { Injectable } from "@angular/core";
import { IDataSource } from "./data-sources.models";
import { HttpClient } from "@angular/common/http";
import { BASE_URL } from 'src/utils/url.util';
import { first } from 'rxjs/operators';
@Injectable({
  providedIn: "root",
})
export class DataSourcesService {
  URL: string = BASE_URL + "data-sources";

  constructor(private httpClient: HttpClient) {}

  create(data: {file ,type}) {
    let testData:FormData = new FormData();
    testData.append('file_upload', data.file, data.file.name);
    if(data.type == 'excel')
      return this.httpClient.post(BASE_URL+'excel-upload/', testData)
    else if(data.type == 'csv')
      return this.httpClient.post(BASE_URL+'csv-upload/', testData)
  }

  update(data: IDataSource) {
    return this.httpClient.put(this.URL, { ...data });
  }

  fetch() {
    this.httpClient.get(this.URL).subscribe((value)=> console.log(value))
    return this.httpClient.get(this.URL);
  }

  delete(id: number) {
    return this.httpClient.delete(`${this.URL}/${id}/`);
  }

  updateCell(data){
    console.log(JSON.stringify({
      cellValue: data.cellValue
    }))
    return this.httpClient.put(`${this.URL}/cell/${data.tableId}/${data.columnId}/${data.cellIndex}/`,{
      cellValue: data.cellValue
    })
  }
}
