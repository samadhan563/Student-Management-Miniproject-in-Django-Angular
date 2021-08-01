import { UserServiceService } from './../user-service.service';
import { Component, OnInit } from '@angular/core';
import { LoginRequest } from '../models/login-request';
import { Router } from '@angular/router';

@Component({
  selector: 'app-sign-in',
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.css']
})
export class SignInComponent implements OnInit {

  public loginRequest: LoginRequest = new LoginRequest('', '')
  public message: string = ""
  constructor(private _studentService: UserServiceService,private router: Router) { }

  ngOnInit(): void {
  }

  onSignIn() {
    console.log(JSON.stringify(this.loginRequest))
    this._studentService.signIn(this.loginRequest).subscribe((res) => {
      console.log(JSON.stringify(res))
      localStorage.setItem('status','true')
      localStorage.setItem('user_id',res.id)
      localStorage.setItem('user_name',res.userName)
      localStorage.setItem('password',res.password)
      localStorage.setItem('user_role',res.role)
      this.loginRequest.userName = ""
      this.loginRequest.password = ""

      this.router.navigate([''])

    }, (error) => {
      this.message = "Failed to load";
      this.loginRequest.userName = ""
      this.loginRequest.password = ""
    })
   
  }


  viewPassword(event: any) {

  }}