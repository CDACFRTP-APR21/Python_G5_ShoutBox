import { Component, OnInit } from '@angular/core';
import { CommentsService } from 'src/app/comments.service';
import { FriendsService } from 'src/app/friends.service';
import { Comments } from 'src/app/models/comments';
import { Friends } from 'src/app/models/friends';
import { Shouts } from 'src/app/models/shouts';
import { User } from 'src/app/models/user';
import { ShoutsService } from 'src/app/shouts.service';
import { UserService } from 'src/app/user.service';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.scss'],
})
export class UserProfileComponent implements OnInit {
  user: User = new User();
  friends: Friends[] = [];
  shouts: Shouts[] = [];
  user_comments: Comments[] = [];
  shoutIdList: number[] = [];
  friendlist = false;
  shoutlist = false;
  constructor(
    private friendService: FriendsService,
    private userService: UserService,
    private shoutService: ShoutsService,
    private commentService: CommentsService
  ) {}

  ngOnInit(): void {
    this.getUser();
  }

  GetAllFriends() {
    this.shoutlist = false;
    this.friendlist = true;
    this.friendService
      .GetAllFriends(this.user.UserId)
      .subscribe((data: any) => {
        console.log(data);
        this.friends = data;
      });
  }

  GetAllShouts() {
    this.friendlist = false;
    this.shoutlist = true;
    this.shoutService.GetShouts(this.user.UserId).subscribe(
      (data: any) => {
        console.log(data);
        this.shouts = data;
        for (let i of data) {
          this.shoutIdList.push(i.ShoutsId);
        }
        console.log(this.shoutIdList);
        console.log(this.shouts);

        if (this.user.UserId != null)
          this.commentService
            .getComments(this.shoutIdList, this.user.UserId)
            .subscribe(
              (res: any) => {
                this.user_comments = res;
                console.log(this.user_comments);
              },
              (err: any) => {
                console.log(err);
              }
            );
      },
      (err: any) => {
        console.log(err);
      }
    );
  }

  getUser() {
    console.log('in user');
    this.userService.getUser().subscribe((data: any) => {
      console.log(data);
      this.user = data;
      console.log(this.user.ProfilePicURL);
    });
  }
}
