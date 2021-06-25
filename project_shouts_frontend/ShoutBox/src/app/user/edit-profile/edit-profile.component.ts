import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { User } from 'src/app/models/user';
import { UserService } from 'src/app/user.service';

@Component({
  selector: 'app-edit-profile',
  templateUrl: './edit-profile.component.html',
  styleUrls: ['./edit-profile.component.scss'],
})
export class EditProfileComponent implements OnInit {
  user: User = new User();
  DateOfBirth!: any;
  public entries: any;
  private pranita!: string;
  emailpattern = '^[a-z0-9._%+-]+@[a-z0-9.-]+.[a-z]{2,4}$';
  firstnamepattern = '^[a-zA-Zd._ ]{2,50}$';
  lastnamepattern = '^[a-zA-Zd._ ]{2,50}$';
  phone = '^((\\+91-?))?[0-9]{10}$';

  constructor(
    private userService: UserService,
    private http: HttpClient,
    private router: Router,
    private route: ActivatedRoute
  ) {
    this.entries = [];
  }

  public ngOnInit() {
    this.getUser();
  }

  getUser() {
    this.userService.getUser().subscribe((data: any) => {
      console.log(data);
      this.user = data;
    });
  }

  updateUser() {
    console.log(this.user.UserName);
    this.userService
      .updateUser(this.user.UserId, this.user)
      .subscribe((data: any) => {
        console.log(data);
        alert('User Data Updated !!!');
      });
  }

  uploadImage() {}
}
