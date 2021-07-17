import { LoginComponent } from './login/login.component';
import { StudentListComponent } from './student-list/student-list.component';
import { AddStudentComponent } from './add-student/add-student.component';
import { UserRegistrationComponent } from './user-registration/user-registration.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
const routes: Routes = [
  { path: '', redirectTo: 'emplpyees', pathMatch: 'full' },
  { path: 'register-new', component: UserRegistrationComponent },
  { path: 'add-student', component: AddStudentComponent },
  { path: 'users-list', component: StudentListComponent },
  { path: 'sign-in', component: LoginComponent },
  // { path: 'departments-list/:id', component: DepartmentDetailsComponent },
  { path: '**', component: PageNotFoundComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponent = [
  PageNotFoundComponent,
  UserRegistrationComponent,
  AddStudentComponent,
  StudentListComponent
];