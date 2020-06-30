import { Injectable } from "@angular/core";
import { IFilter } from "./filters.models";
import { HttpClient } from "@angular/common/http";
import { BASE_URL } from 'src/utils/url.util';
@Injectable({
  providedIn: "root",
})
export class FiltersService {
  URL: string = BASE_URL + "filters";

  constructor(private httpClient: HttpClient) {}

  create(data) {
    console.log(data)
    return this.httpClient.post(`${this.URL}/`, {
      ...data,
       dataSource: Number.parseInt(data.dataSource),
       filteredColumn: Number.parseInt(data.filteredColumn)
     });
  }

  update(data: IFilter) {
    return this.httpClient.put(this.URL, { ...data });
  }

  fetch() {
    return this.httpClient.get(this.URL);
  }

  delete(id: number) {
    return this.httpClient.delete(`${this.URL}/${id}`);
  }
}
