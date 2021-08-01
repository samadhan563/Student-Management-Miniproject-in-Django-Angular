import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomePageComponent } from './home-page/home-page.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { SignInComponent } from './sign-in/sign-in.component';
import { SignOutComponent } from './sign-out/sign-out.component';
import { StudentListComponent } from './student-list/student-list.component';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { UserRegistrationComponent } from './user-registration/user-registration.component';

const routes: Routes = [
  //   { path: '', redirectTo: '', pathMatch: 'full' },
  { path: '', component: HomePageComponent },
  { path: 'register-new', component: UserRegistrationComponent },
  // { path: 'add-student', component: AddStudentComponent },
  { path: 'users-list', component: StudentListComponent },
  { path: 'sign-in', component: SignInComponent },
  { path: 'sign-out', component: SignOutComponent },
  { path: 'update-profile', component: UserProfileComponent },
  { path: '**', component: PageNotFoundComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

export const routingComponent = [
  // PageNotFoundComponent,
  // UserRegistrationComponent,
  // AddStudentComponent,
  // StudentListComponent
  UserProfileComponent
];