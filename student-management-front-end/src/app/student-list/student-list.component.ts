import { UserServiceService } from './../user-service.service';
import { Component, OnInit } from '@angular/core';
import { IUser } from '../models/iuser';

@Component({
  selector: 'app-student-list',
  templateUrl: './student-list.component.html',
  styleUrls: ['./student-list.component.css']
})
export class StudentListComponent implements OnInit {

  public students: IUser[] = [];
  public errorMessage = "";

  constructor(private _studentService: UserServiceService) { }

  ngOnInit(): void {
    this._studentService.getStudentList().subscribe((res) => {
      this.students = res;
    },
      (error) => {
        this.errorMessage = "Failed to load"
      }
    );
  }

}