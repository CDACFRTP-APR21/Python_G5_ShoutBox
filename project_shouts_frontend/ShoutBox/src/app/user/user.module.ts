import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RegisterComponent } from './register/register.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { UserHomeComponent } from './user-home/user-home.component';
import { EditProfileComponent } from './edit-profile/edit-profile.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ShoutsComponent } from './shouts/shouts.component';
import { FriendsComponent } from './friends/friends.component';
import { CommentsComponent } from './comments/comments.component';
import { ReportedShoutsComponent } from './reported-shouts/reported-shouts.component';
import { LoginComponent } from './login/login.component';

@NgModule({
  declarations: [
    RegisterComponent,
    LoginComponent,
    HeaderComponent,
    FooterComponent,
    UserHomeComponent,
    UserProfileComponent,
    EditProfileComponent,
    ShoutsComponent,
    FriendsComponent,
    CommentsComponent,
    ReportedShoutsComponent,
  ],
  imports: [CommonModule, FormsModule, ReactiveFormsModule],
})
export class UserModule {}
