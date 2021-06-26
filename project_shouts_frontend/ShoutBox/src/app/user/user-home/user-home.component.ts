import { Comments } from 'src/app/models/comments';
import { CommentsService } from './../../comments.service';
import { DatePipe } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { Shouts } from 'src/app/models/shouts';
import { ShoutsService } from 'src/app/shouts.service';
import { UserService } from 'src/app/user.service';
import { UserTimeline } from 'src/app/models/user_timeline';
import { User } from 'src/app/models/user';
import { Router } from '@angular/router';

@Component({
  selector: 'app-user-home',
  templateUrl: './user-home.component.html',
  styleUrls: ['./user-home.component.scss'],
})
export class UserHomeComponent implements OnInit {
  user: User = new User();
  DateCreated!: any;

  user_shouts: UserTimeline[] = [];
  user_comments: Comments[] = [];
  text: any;
  fileData: any;
  CommentContent: any;
  ShoutsId: any;
  shoutIdList: number[] = [];
  numberList: number[] = [1];
  UserId = sessionStorage.getItem('UserId');
  
  constructor(
    private userService: UserService,
    private commentsService: CommentsService,
    private router:Router

  ) {}
  ngOnInit() {
    this.getUser();
    this.userService.getShouts().subscribe(
      (res: any) => {
        this.user_shouts = res;
        for (let i of res) {
          this.shoutIdList.push(i.ShoutsId);
        }
        console.log(this.shoutIdList);
        console.log('in onit');
        console.log(this.user_shouts);
        // let shoutList = JSON.stringify(this.shoutIdList);
        // const formData = new FormData();
        // formData.append('ShoutsId', shoutList);
        if (this.UserId != null)
          this.commentsService
            .getComments(this.shoutIdList, this.UserId)
            .subscribe(
              (res: any) => {
                this.user_comments = res;
                console.log('in onit');
                console.log(this.user_comments);
              },
              (err: any) => {
                console.log('hello');
                console.log(err);
              }
            );
      },
      (err: any) => {
        console.log('hello');
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
  logoutUser()
  {
    this.userService.logoutUser(this.user).subscribe((data: any) => {
      console.log(data);
      this.router.navigate(['/login']);
      
    });
    
    
    


  }

  // this.commentsService.getComments().subscribe(
  //   (res: any) => {
  //     this.user_shouts = res;
  //     console.log('in onit');
  //     console.log(this.user_shouts);
  //   },
  //   (err: any) => {
  //     console.log('hello');
  //     console.log(err);
  //   }
  // );

  onChange(event: any) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.fileData = file;
    }
  }
  shoutId(id: any) {
    this.ShoutsId = id;
    const formData = new FormData();
    formData.append('ShoutsId', this.ShoutsId);
    formData.append('CommentContent', this.CommentContent);
    this.CommentContent = '';
    if (this.UserId != null) formData.append('UserId', this.UserId);
    this.commentsService.AddComment(formData).subscribe(
      (res: any) => {
        console.log('after comment post');
        console.log(res);
        this.shoutIdList.length = 0;
        for (let i of this.user_shouts) {
          this.shoutIdList.push(i.ShoutsId);
        }
        console.log(this.shoutIdList);
        console.log('in onit');
        console.log(this.user_shouts);
        // let shoutList = JSON.stringify(this.shoutIdList);
        // const formData = new FormData();
        // formData.append('ShoutsId', shoutList);
        if (this.UserId != null)
          this.commentsService
            .getComments(this.shoutIdList, this.UserId)
            .subscribe(
              (res: any) => {
                this.user_comments = res;
                console.log('in onit');
                console.log(this.user_comments);
              },
              (err: any) => {
                console.log('hello');
                console.log(err);
              }
            );
      },
      // this.user_shouts = res;
      // console.log(this.user_shouts)
      (err: any) => {
        console.log('hello');
        console.log(err);
      }
    );
  }

  onSubmit() {
    const formData = new FormData();
    console.log(this.fileData);
    console.log(this.text);
    console.log(this.fileData.type);
    let element = new String(this.fileData.type);
    let FileType = '';
    console.log(element);
    for (let index = 0; index < element.length; index++) {
      if (element[index] == '/') {
        break;
      } else FileType = FileType + element[index];
    }
    console.log(FileType);

    let userid = sessionStorage.getItem('UserId');
    if (userid != null) {
      formData.append('TextContent', this.text);
      formData.append('File', this.fileData);
      formData.append('FileType', FileType);
      formData.append('UserId', userid);
    }
    this.userService.shoutUpload(formData).subscribe(
      (res: any) => {
        this.userService.getShouts().subscribe(
          (res: any) => {
            console.log('after upload post');
            this.user_shouts.length = 0;
            this.user_shouts = res;
            console.log(this.user_shouts);
          },
          (err: any) => {
            console.log('hello');
            console.log(err);
          }
        );
      },
      (err: any) => {
        console.log('hello');
        console.log(err);
      }
    );
  }
}
