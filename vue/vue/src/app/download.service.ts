import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class DownloadService {

  constructor(private http: HttpClient) {}

  public downloadFile(url:string):any{
    return this.http.get('http://localhost:3000/download?videoUrl=' + url, {
      responseType: 'blob'
    });
  }
}
