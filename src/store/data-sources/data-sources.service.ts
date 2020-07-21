import { Injectable } from "@angular/core";
import { IDataSource } from "./data-sources.models";
import { HttpClient } from "@angular/common/http";
import { BASE_URL } from "src/utils/url.util";
@Injectable({
  providedIn: "root",
})
export class DataSourcesService {
  URL: string = BASE_URL + "data-sources";

  constructor(private httpClient: HttpClient) {}

  create(data: { file; type }) {
    let testData: FormData = new FormData();
    testData.append("file_upload", data.file, data.file.name);
    if (data.type == "excel")
      return this.httpClient.post(BASE_URL + "excel-upload/", testData);
    else if (data.type == "csv")
      return this.httpClient.post(BASE_URL + "csv-upload/", testData);
  }

  update(data: IDataSource) {
    return this.httpClient.put(this.URL, { ...data });
  }

  fetch() {
    return this.httpClient.get(this.URL);
  }

  delete(id: number) {
    return this.httpClient.delete(`${this.URL}/${id}/`);
  }

  updateCell(data) {
    return this.httpClient.put(
      `${this.URL}/cell/${data.tableId}/${data.columnId}/${data.cellIndex}/`,
      {
        cellValue: data.cellValue,
      }
    );
  }

  updateFilterInDataSource(data) {
    console.log(data)
    return this.httpClient.put(
      `${this.URL}/update-filter/${data.tableId}/${data.id}/`,
      {
        id: data.id,
        value: data.value,
        isActive: data.active,
      }
    );
  }

  addFilterToDataSource(data) {
    console.log(data);
    return this.httpClient.put(`${this.URL}/insert-filter/${data.tableId}/`, {
      id: data.id,
      value: data.value,
      isActive: data.isActive,
    });
  }

  removeFilterFromDataSource(data) {
    return this.httpClient.put(
      `${this.URL}/remove-filter/${data.tableId}/${data.id}/`,
      {}
    );
  }


  updateDataSourceColumnColor(data){
    return this.httpClient.put(
      `${this.URL}/column-color/${data.tableId}/${data.columnId}/`,
      { color : data.color}
    )
  }

  updateDataSourceRowColor(data){
    return this.httpClient.put(
      `${this.URL}/row-color/${data.tableId}/${data.rowId}/`,
      { color : data.color}
    )
  }

  updateDataSourceAggregation(data){
    console.log(data)
    return this.httpClient.put(
      `${this.URL}/aggregation/${data.tableId}/${data.columnId}/`,
      {
        type: data.type,
        isActive: data.isActive
    }
    )
  }
}
