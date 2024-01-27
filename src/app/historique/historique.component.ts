import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ForexDataService } from '../services/forex-data.service';
import { formatDate } from '@angular/common';

@Component({
  selector: 'app-historique',
  templateUrl: './historique.component.html',
  styleUrls: ['./historique.component.css']
})
export class HistoriqueComponent implements OnInit{
  historicalData: any[] = [];

  constructor(private forexService: ForexDataService, private route: ActivatedRoute) {}

  ngOnInit() {
    this.route.params.subscribe((params) => {
      const currency = params['currency'];
      this.forexService.getHistoricalData(currency).subscribe(
        (data) => {
          this.historicalData = data;
          console.log('Historical Data:', data);
        },
        (error) => {
          console.error('Error fetching historical data:', error);
        }
      );
    });
  }







  }

