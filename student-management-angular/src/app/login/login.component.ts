import { StudentService } from './../student.service';
import { LoginRequest } from './../models/login-request';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  public loginRequest: LoginRequest = new LoginRequest('', '')
  public errorMessage: string = ""
  constructor(private _studentService: StudentService) { }

  ngOnInit(): void {
  }

  onSignIn() {
    console.log(JSON.stringify(this.loginRequest))
    this._studentService.signIn(this.loginRequest).subscribe((res) => {
      console.log(JSON.stringify(res))
      this.loginRequest.userName = ""
      this.loginRequest.password = ""
    }, (error) => {
      this.errorMessage = "Failed to load";
      this.loginRequest.userName = ""
      this.loginRequest.password = ""
    })
   
  }


  viewPassword(event: any) {

  }

}
