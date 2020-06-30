import { Injectable } from '@angular/core';
import { BASE_URL } from 'src/utils/url.util';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CoreService {

  URL : string = BASE_URL + "chartsNames"

  constructor(private httpClient: HttpClient) {}

  fetch() {
      return this.httpClient.get(this.URL);
  }

}
