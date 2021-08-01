import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css']
})
export class HomePageComponent implements OnInit {

  public marqueClasss = [' h4 text-primary font-weight-bold',
    'h4 text-light font-italic',
    'h4 text-warning font-weight-bold font-italic',
    'h4 text-success font-weight-bold ',
    'h4 text-info font-weight-bold',
    'h4 text-danger font-italic',]
  public marqueClass = "h4 text-light font-weight-bold ";
  public i = 0;
  constructor() { }

  ngOnInit(): void {
    setInterval(() => {
      this.marqueClass = this.marqueClasss[this.i];
      this.i++;
      if (this.i == this.marqueClasss.length)
        this.i = 0;
    }, 5000);
  }
}
