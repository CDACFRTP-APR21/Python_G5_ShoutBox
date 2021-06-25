import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class FriendsService {
  constructor(private http: HttpClient) {}

  AddNewFriend(val: any): Observable<any> {
    return this.http.post('http://127.0.0.1:8000/friends/', val);
  }

  GetAllFriends(UserID: any) {
    console.log('in frined service' + UserID);
    return this.http.get('http://127.0.0.1:8000/friendsList/' + UserID);
  }
}
