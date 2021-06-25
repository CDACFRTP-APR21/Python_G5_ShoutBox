import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { CommentsComponent } from './user/comments/comments.component';
import { EditProfileComponent } from './user/edit-profile/edit-profile.component';
import { FriendsComponent } from './user/friends/friends.component';
import { LoginComponent } from './user/login/login.component';
import { RegisterComponent } from './user/register/register.component';
import { ShoutsComponent } from './user/shouts/shouts.component';
import { UserHomeComponent } from './user/user-home/user-home.component';
import { UserProfileComponent } from './user/user-profile/user-profile.component';

const routes: Routes = [
  { path: 'register', component: RegisterComponent },
  { path: 'login', component: LoginComponent },
  { path: 'userprofile', component: UserProfileComponent },
  {
    path: 'userhome',
    component: UserHomeComponent,
  },
  { path: 'editprofile', component: EditProfileComponent },
  { path: 'shouts', component: ShoutsComponent },
  { path: 'friends', component: FriendsComponent },
  { path: 'comments', component: CommentsComponent },
  { path: '**', component: HomeComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
