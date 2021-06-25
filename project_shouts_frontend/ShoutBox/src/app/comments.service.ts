import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class CommentsService {
  constructor(private http: HttpClient) {}

  AddComment(val: any): Observable<any> {
    return this.http.post('http://127.0.0.1:8000/commentsUpload/', val);
  }

  getComments(ShoutId: any, UserId: any): Observable<any> {
    console.log(ShoutId);
    return this.http.get(
      'http://127.0.0.1:8000/comments/' + ShoutId + '/' + UserId
    );
  }
}
