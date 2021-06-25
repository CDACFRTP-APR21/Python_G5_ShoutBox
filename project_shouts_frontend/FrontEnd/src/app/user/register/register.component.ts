import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/user.service';
import { User } from 'src/app/models/user';
import { DatePipe } from '@angular/common';
import {
  FormBuilder,
  FormControl,
  FormGroup,
  NgModel,
  Validators,
} from '@angular/forms';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss'],
})
export class RegisterComponent implements OnInit {
  myform!: FormGroup;
  this: any;
  submitted = false;
  user: User = new User();

  constructor(private userService: UserService, private datePipe: DatePipe) {}

  ngOnInit(): void {
    this.submitted = false;
    this.myform = new FormGroup({
      UserName: new FormControl('', [Validators.required, Validators.max(4)]),
      FirstName: new FormControl('', [
        Validators.required,
        Validators.pattern('^[a-zA-Zd._ ]{2,50}$'),
      ]),

      LastName: new FormControl('', [
        Validators.required,
        Validators.pattern('^[a-zA-Zd._ ]{2,50}$'),
      ]),
      Email: new FormControl('', [
        Validators.required,
        Validators.pattern('^^[a-z0-9._%+-]+@[a-z0-9.-]+.[a-z]{2,4}$'),
      ]),
      MobileNo: new FormControl('', [
        Validators.required,
        Validators.pattern('^((\\+91-?))?[0-9]{10}$'),
      ]),
      Password: new FormControl('', [Validators.required]),
      ConfirmPassword: new FormControl('', [Validators.required]),
      Gender: new FormControl('', [Validators.required]),
      DateOfBirth: new FormControl('', [Validators.required]),
    });
    {
      validators: this.checkPasswords(this.myform);
    }
  }
  checkPasswords(group: FormGroup) {
    if (
      this.myform.value.Password != null &&
      this.myform.value.ConfirmPassword != null
    ) {
      const password = this.myform.value.Password;
      const confirmPassword = this.myform.value.ConfirmPassword;
      return password === confirmPassword ? null : { notSame: true };
    }
    return;
  }

  registerNewUser() {
    this.submitted = true;
    if (this.myform.invalid) {
      return alert('Please Enter All Fields');
    }
    console.log(this.user.MobileNo);
    this.user = this.myform.value;
    this.userService
      .registerUser(this.myform.value)
      .subscribe((myform: any) => {
        alert('Register Successfully');
      });
    this.myform.reset();
  }

  get check() {
    return this.myform.controls;
  }
}
