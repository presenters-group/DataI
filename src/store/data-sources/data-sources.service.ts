import { Injectable } from "@angular/core";
import { IDataSource } from "./data-sources.models";
import { HttpClient } from "@angular/common/http";
@Injectable({
  providedIn: "root",
})
export class DataSourcesService {
  URL: string = "/data-source";

  constructor(private httpClient: HttpClient) {}

  create(data: IDataSource) {
    return this.httpClient.post(this.URL, { ...data });
  }

  update(data: IDataSource) {
    return this.httpClient.put(this.URL, { ...data });
  }

  fetch() {
    return this.httpClient.get(this.URL);
  }

  delete(id: number) {
    return this.httpClient.delete(`${this.URL}/${id}`);
  }
}
