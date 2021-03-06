import { UserServiceService } from './../user-service.service';
import { Component, OnInit } from '@angular/core';
import { User } from '../models/user';

@Component({
  selector: 'app-user-registration',
  templateUrl: './user-registration.component.html',
  styleUrls: ['./user-registration.component.css']
})
export class UserRegistrationComponent implements OnInit {

  public userModel = new User('', '', '')
  public errorMessage = ''
  constructor(private _studentService: UserServiceService) { }

  ngOnInit(): void {
  }

  onSumit() {
    this._studentService.registerNewUser(this.userModel).subscribe((res) => {
      console.log(res)
      this.userModel.userName = ""
      this.userModel.password = ""
      this.userModel.role = ""
    }, (error) => {
      this.errorMessage = "Failed to load";
      this.userModel.userName = ""
      this.userModel.password = ""
      this.userModel.role = ""
    })
    console.log(JSON.stringify(this.userModel))
  }

  viewPassword(event: any) {
    event.currentTarget.type = 'text'
  }

  onBlurEvent(event: any) {
    event.currentTarget.type = 'text';
  }

}

