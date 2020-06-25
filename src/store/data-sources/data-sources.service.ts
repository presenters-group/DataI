import { Injectable } from "@angular/core";
import { IDataSource } from "./data-sources.models";
import { HttpClient } from "@angular/common/http";
import { BASE_URL } from 'src/utils/url.util';
@Injectable({
  providedIn: "root",
})
export class DataSourcesService {
  URL: string = BASE_URL + "data-sources";

  constructor(private httpClient: HttpClient) {}

  create(data: IDataSource) {
    return this.httpClient.post(this.URL, { ...data });
  }

  update(data: IDataSource) {
    return this.httpClient.put(this.URL, { ...data });
  }

  fetch() {
    this.httpClient.get(this.URL).subscribe((value)=> console.log(value))
    return this.httpClient.get(this.URL);
  }

  delete(id: number) {
    return this.httpClient.delete(`${this.URL}/${id}`);
  }

  updateCell(data){
    console.log(data)
    return this.httpClient.put(`${this.URL}/cell/${data.tableId}/${data.columnId}/${data.cellIndex}`,{
      cellValue: data.cellValue
    })
  }
}
