import { Component, OnInit } from '@angular/core';
import { ForexDataService } from 'src/app/services/forex-data.service';

@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.css']
})
export class WelcomeComponent implements OnInit {
  forexData: any;
  constructor(private forexService: ForexDataService) { }

  ngOnInit() {
    this.forexService.getForexData().subscribe(data => {
      this.forexData = data;
      console.log(this.forexData)
    });
  }

}
