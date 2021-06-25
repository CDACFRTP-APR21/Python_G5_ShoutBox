import { Component, OnInit } from '@angular/core';
import { Comments } from 'src/app/models/comments';

@Component({
  selector: 'app-comments',
  templateUrl: './comments.component.html',
  styleUrls: ['./comments.component.scss'],
})
export class CommentsComponent implements OnInit {
  comments: Comments = new Comments();
  constructor() {}

  ngOnInit(): void {}
}
