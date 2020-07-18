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
    let visualizers = data.visualizers.map(x => ({visualizationId: Number.parseInt(x.visualizationId),measurements: x.measurements}))
    return this.httpClient.post(`${this.URL}/`, { ...data, visualizers});
  }

  update(data : IDashboard) {
    let visualizers = data.visualizers.map(x => ({visualizationId: x.visualizationId, measurements: x.measurements}))
    return this.httpClient.put(`${this.URL}/${data.id}/`,
    {...data, visualizers}
    )
  }

  fetch() {
    return this.httpClient.get(this.URL);
  }

  delete(id : number) {
    return this.httpClient.delete(`${this.URL}/${id}/`);
  }

  fetchDashboardSVGs(data){
    this.httpClient.get(`${this.URL}/charts/${data.dashboardId}/`).subscribe((data)=>{
      console.log(data)
    })
    return this.httpClient.get(`${this.URL}/charts/${data.dashboardId}/`);
  }
}
