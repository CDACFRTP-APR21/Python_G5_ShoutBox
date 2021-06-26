import { Injectable } from '@angular/core';
import { catchError, map, tap } from 'rxjs/operators';
import {
  HttpClient,
  HttpErrorResponse,
  HttpHeaders,
} from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';
import { stringify } from '@angular/compiler/src/util';
import * as jwt_decode from 'jwt-decode';
import { CookieService } from 'ngx-cookie-service';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  private httpOptions: any;
  public token!: string;
  public token_expires!: Date;
  public Email!: string;
  public errors: any = [];
  public UserName!: string;

  constructor(private http: HttpClient, private router: Router) {
    this.httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        Accept: 'application/json',
      }),
    };
  }

  registerUser(val: any): Observable<any> {
    return this.http.post('http://127.0.0.1:8000/user/', val);
  }

  getUser() {
    console.log('hi');
    return this.http.get('http://127.0.0.1:8000/users');
  }

  public loginUser(user1: any) {
    return this.http.post(
      'http://127.0.0.1:8000/login',
      JSON.stringify(user1),
      this.httpOptions
    );
  }
  public logoutUser(user1: any) {
    return this.http.post(
      'http://127.0.0.1:8000/logout',
      JSON.stringify(user1),
      this.httpOptions
    );
  }

  updateUser(UserId: any, data: any): Observable<any> {
    console.log(UserId);
    console.log(data);
    return this.http.put('http://127.0.0.1:8000/user/' + UserId, data);
  }

  shoutUpload(val: any) {
    return this.http.post('http://127.0.0.1:8000/shouts/3', val);
  }

  getShouts() {
    let userId;
    userId = sessionStorage.getItem('UserId');
    console.log(userId);
    return this.http.get('http://127.0.0.1:8000/friendShouts/' + userId);
  }
}
