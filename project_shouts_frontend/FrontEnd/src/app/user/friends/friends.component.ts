import { Component, OnInit } from '@angular/core';
import { Friends } from 'src/app/models/friends';

@Component({
  selector: 'app-friends',
  templateUrl: './friends.component.html',
  styleUrls: ['./friends.component.scss'],
})
export class FriendsComponent implements OnInit {
  friends: Friends = new Friends();
  constructor() {}

  ngOnInit(): void {}
}
