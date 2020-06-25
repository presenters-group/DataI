import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { IVisualizer } from './visualizers.models';
import { BASE_URL } from 'src/utils/url.util';

@Injectable({
  providedIn: "root",
})
export class VisualizersService {

  URL : string = BASE_URL + "visualizers"

  constructor(private httpClient: HttpClient) {}

  create(data : IVisualizer) {
    return this.httpClient.post(`${this.URL}/`, { ...data });
  }

  update(data : IVisualizer) {
    return this.httpClient.put(this.URL, { ...data });
  }

  fetch() {
    return this.httpClient.get(this.URL);
  }

  delete(id : number) {
    return this.httpClient.delete(`${this.URL}/${id}`);
  }
}
