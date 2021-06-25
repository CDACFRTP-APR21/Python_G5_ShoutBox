import { stringify } from '@angular/compiler/src/util';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { User } from 'src/app/models/user';
import { UserService } from 'src/app/user.service';
import { throwError } from 'rxjs';
import { CookieService } from 'ngx-cookie-service';
import { JsonPipe } from '@angular/common';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent implements OnInit {
  user: User = new User();
  public user1: any;
  UserName!: 'Pranita';
  public errors: any = [];

  loginForm!: FormGroup;
  loading = false;
  submitted = false;
  returnUrl!: string;
  emailPattern = '^[a-z0-9._%+-]+@[a-z0-9.-]+.[a-z]{2,4}$';

  constructor(
    public userService: UserService,
    private formBuilder: FormBuilder,
    private router: Router,
    private cookie: CookieService
  ) {}

  ngOnInit() {
    this.user1 = { Email: '', Password: '' };
  }

  // get f() {
  //   return this.loginForm.controls;
  // }

  onLogin() {
    this.submitted = true;
    this.userService
      .loginUser({
        Email: this.user1.Email,
        Password: this.user1.Password,
      })
      .subscribe(
        (data: any) => {
          console.log(data);
          this.cookie.set('jwt', data.jwt);
          console.log(this.cookie.get('jwt'));
          alert('User ' + this.user1.Email + ' logged.');
          this.getUser();
          // this.router.navigate(['/userhome']);
        },
        (err) => {
          alert('Invalid Credential !!!');
          this.errors = err['error'];
        }
      );
  }

  getUser() {
    this.userService.getUser().subscribe((data: any) => {
      console.log('in userservice');
      console.log(data.UserId);
      console.log(data);
      sessionStorage.setItem('UserId', data.UserId);
      this.router.navigate(['/userhome'], { queryParams: data });
    });
  }
}
