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
    let filters = data.filters.map(x => ({...x, id: Number.parseInt(x.id),visioId : Number.parseInt(x.visioId)}))
    return this.httpClient.post(`${this.URL}/`, { ...data, filters, visualizers});
  }

  update(data : IDashboard) {
    let visualizers = data.visualizers.map(x => ({visualizationId: Number.parseInt(x.visualizationId), measurements: x.measurements}))
    let filters = data.filters.map(x => ({...x, id: Number.parseInt(x.id),visioId : Number.parseInt(x.visioId)}))
    console.log(data.id)

    return this.httpClient.put(`${this.URL}/${data.id}/`,
    {...data, filters,visualizers}
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

  updateFilterInDashboard(data){
    return this.httpClient.put(`${this.URL}/update-filter/${data.dashboardId}/${data.visioId}/${data.id}/`,{
        id: data.id,
        visioId: data.visioId,
        value: data.value,
        isActive: data.isActive,
        measurements: data.measurements
    });
  }
}
