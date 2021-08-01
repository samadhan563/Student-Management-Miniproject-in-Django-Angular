import { UserServiceService } from './../user-service.service';
import { Component, OnInit } from '@angular/core';
import { UserProfile } from '../models/user-profile';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})


export class UserProfileComponent implements OnInit {


  public userModel = new UserProfile('', '', '', '', '', '')
  public errorMessage = ''
  public file
  constructor(private _studentService: UserServiceService) { }


  ngOnInit(): void {
    this._studentService.getUserProfile(localStorage.getItem('user_id')).subscribe((res)=>{
      this.userModel=res;
    },(error)=>{
      console.log("Error to load.....")
    })

  }

  onSumit() {
    this._studentService.updateUser(this.userModel,localStorage.getItem('user_id')).subscribe((res) => {
      console.log(res)
    }, (error) => {
      this.errorMessage = "Failed to load";
      this.userModel.firstName = ""
      this.userModel.lastName = ""
      this.userModel.emaiId = "",
        this.userModel.mobileNumber = "",
        this.userModel.dateOfBirth = "",
        this.userModel.image = ""
    })
    console.log(JSON.stringify(this.userModel))
  }

  viewPassword(event) {
    event.currentTarget.type = 'text'
  }


  onBlurEvent(event) {
    event.currentTarget.type = 'text';
  }

  // fileName = '';
  onFileSelected(event) {
    const file: File = event.target.files[0];
    if (file) {
      var formData = new FormData();
      formData.append("files", event.target.files[0]);
      this._studentService.uploadImage(formData).subscribe((res) => {
        this.userModel.image = res;
        console.log(res)
      })
    }
  }
}
