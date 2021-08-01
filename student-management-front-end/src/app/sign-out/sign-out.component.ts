import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-sign-out',
  templateUrl: './sign-out.component.html',
  styleUrls: ['./sign-out.component.css']
})
export class SignOutComponent implements OnInit {

 
  constructor(private router: Router) { }

  ngOnInit(): void {
    localStorage.removeItem('status')
    localStorage.removeItem('user_name')
    localStorage.removeItem('password')
    localStorage.removeItem('user_role')
    alert("Sign out successfully take care.....")
    this.router.navigate([''])

  }

}
