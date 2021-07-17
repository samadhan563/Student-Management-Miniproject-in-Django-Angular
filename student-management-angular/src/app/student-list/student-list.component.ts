import { IUser } from './../models/IUser';
import { StudentService } from './../student.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-student-list',
  templateUrl: './student-list.component.html',
  styleUrls: ['./student-list.component.css']
})
export class StudentListComponent implements OnInit {
  public students: IUser[] = [];
  public errorMessage = "";

  constructor(private _studentService: StudentService) { }

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
