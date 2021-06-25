import { DatePipe } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { Shouts } from 'src/app/models/shouts';
import { UserService } from 'src/app/user.service';

@Component({
  selector: 'app-shouts',
  templateUrl: './shouts.component.html',
  styleUrls: ['./shouts.component.scss'],
})
export class ShoutsComponent implements OnInit {
  shouts: Shouts = new Shouts();
  DateCreated!: any;

  constructor(private userService: UserService, private datePipe: DatePipe) {}

  ngOnInit(): void {}

  registerNewUser() {
    this.shouts.ShoutsId = 3;
    let strDate = this.datePipe.transform(this.DateCreated, 'yyyy-MM-dd');
    if (strDate != null) {
      this.shouts.DateCreated = strDate;
    }
    this.userService.registerUser(this.shouts).subscribe(
      (response) => {
        alert('new shout ' + this.shouts.ShoutsId + ' has been created !!!');
      },
      (error) => console.log('error', error)
    );
  }
}
