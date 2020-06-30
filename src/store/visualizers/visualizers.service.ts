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
      usedColumns: data.usedColumns.map(x => Number.parseInt(x)),
      xColumn: Number.parseInt(data.xColumn),
      data: Number.parseInt(data.data)
    });
  }

  update(data: IVisualizer) {
    return this.httpClient.put(this.URL, { ...data });
  }

  fetch() {
    return this.httpClient.get(this.URL);
  }

  delete(id: number) {
    return this.httpClient.delete(`${this.URL}/${id}`);
  }

  fetchVisualizerChart(data) {
    return this.httpClient.put(`http://127.0.0.1:8000/data/chart/`, {
      ...data,
    });
  }
}
