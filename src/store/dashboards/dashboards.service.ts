import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { IDashboard } from './dashboards.models';

@Injectable({
  providedIn: "root",
})
export class DashboardsService {

  URL : string = "/dashboards"

  constructor(private httpClient: HttpClient) {}

  create(data : IDashboard) {
    return this.httpClient.post(this.URL, { ...data });
  }

  update(data : IDashboard) {
    return this.httpClient.put(this.URL, { ...data });
  }

  fetch() {
    return this.httpClient.get(this.URL);
  }

  delete(id : number) {
    return this.httpClient.delete(`${this.URL}/${id}`);
  }
}
