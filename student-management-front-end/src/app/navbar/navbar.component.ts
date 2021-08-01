import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  public status = false;
  constructor() { }

  ngOnInit(): void {
    if (localStorage.getItem('status') == 'true')
      this.status = true
    else
      this.status = false
  }

}
