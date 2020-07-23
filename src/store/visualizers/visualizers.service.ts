import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { IVisualizer } from "./visualizers.models";
import { BASE_URL } from "src/utils/url.util";

@Injectable({
  providedIn: "root",
})
export class VisualizersService {
  URL: string = BASE_URL + "visualizers";

  constructor(private httpClient: HttpClient) {}

  create(data) {
    return this.httpClient.post(`${this.URL}/`, {
      ...data,
      usedColumns: data.usedColumns.map((x) => Number.parseInt(x)),
      xColumn: Number.parseInt(data.xColumn),
      data: Number.parseInt(data.data),
      filters : [],
      quality: Number.parseInt(data.quality)
    });
  }

  update(data) {
    return this.httpClient.put(`${this.URL}/${data.id}/`, {
      ...data,
      usedColumns: data.usedColumns.map((x) => Number.parseInt(x)),
      xColumn: Number.parseInt(data.xColumn),
      data: Number.parseInt(data.data),
      filters: [],
      quality: Number.parseInt(data.quality)
    });
  }

  fetch() {
    return this.httpClient.get(this.URL);
  }

  delete(id: number) {
    return this.httpClient.delete(`${this.URL}/${id}/`);
  }

  fetchVisualizerChart(data) {
    return this.httpClient.put(`http://127.0.0.1:8000/data/chart/`, {
      ...data,
    });
  }

  updateFilterInVisualizer(data) {
    return this.httpClient.put(
      `${this.URL}/update-filter/${data.visualizerId}/${data.id}/`,
      {
        id: data.id,
        value: data.value,
        isActive: data.active,
      }
    );
  }
  addFilterToVisualizer(data) {
    return this.httpClient.put(
      `${this.URL}/insert-filter/${data.visualizerId}/`,
      {
        id: data.id,
        value: data.value,
        isActive: data.isActive,
      }
    );
  }
  removeFilterFromVisualizer(data) {
    return this.httpClient.put(
      `${this.URL}/remove-filter/${data.visualizerId}/${data.id}/`,
      {}
    );
  }

  addSVGChart(data){
    let testData: FormData = new FormData();
    testData.append("file_upload", data.file, data.file.name);
    return this.httpClient.post(BASE_URL + "svg-upload/", testData);  }
}
