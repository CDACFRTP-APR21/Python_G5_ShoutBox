import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ShoutsService {
  constructor(private http: HttpClient) {}

  UploadShout(val: any): Observable<any> {
    return this.http.post('http://127.0.0.1:8000/shouts/', val);
  }

  GetShouts(UserId: any) {
    return this.http.get('http://127.0.0.1:8000/shouts/' + UserId);
  }
}
