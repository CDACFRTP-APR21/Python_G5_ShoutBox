import { Component, OnInit } from '@angular/core';
import { ReportedShouts } from 'src/app/models/reported_shouts';

@Component({
  selector: 'app-reported-shouts',
  templateUrl: './reported-shouts.component.html',
  styleUrls: ['./reported-shouts.component.scss'],
})
export class ReportedShoutsComponent implements OnInit {
  reportedshouts: ReportedShouts = new ReportedShouts();
  constructor() {}

  ngOnInit(): void {}
}
