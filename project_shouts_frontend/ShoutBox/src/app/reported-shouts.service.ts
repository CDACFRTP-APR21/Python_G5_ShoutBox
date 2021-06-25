import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ReportedShoutsService {
  constructor(private http: HttpClient) {}

  AddReportedShouts(val: any): Observable<any> {
    return this.http.post('http://127.0.0.1:8000/reportedShouts/', val);
  }
}
