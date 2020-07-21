import { Injectable } from '@angular/core';
import { BASE_URL } from 'src/utils/url.util';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CoreService {

  URL : string = BASE_URL + "chartsNames/"

  constructor(private httpClient: HttpClient) {}

  fetch() {
      return this.httpClient.get(this.URL);
  }

  openProject(data){
    let testData: FormData = new FormData();
    testData.append("file_upload", data.file, data.file.name);
    return this.httpClient.post(BASE_URL + "dataI-upload/", testData);
  }

}
