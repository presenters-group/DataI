import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { IDashboard } from './dashboards.models';
import { BASE_URL } from 'src/utils/url.util';

@Injectable({
  providedIn: "root",
})
export class DashboardsService {

  URL : string = BASE_URL + "dashboards"

  constructor(private httpClient: HttpClient) {}

  create(data : IDashboard) {
    return this.httpClient.post(`${this.URL}/`, { ...data });
  }

  update(data : IDashboard) {
    return this.httpClient.put(`${this.URL}/${data.id}/`,
    data
    )
  }

  fetch() {
    return this.httpClient.get(this.URL);
  }

  delete(id : number) {
    return this.httpClient.delete(`${this.URL}/${id}/`);
  }

  fetchDashboardSVGs(data){
    return this.httpClient.get(`${this.URL}/charts/${data.dashboardId}/`);
  }
}
