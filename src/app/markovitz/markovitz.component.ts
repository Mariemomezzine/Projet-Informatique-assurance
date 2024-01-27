import { Component, OnInit } from '@angular/core';
import { ForexDataService } from '../services/forex-data.service';

@Component({
  selector: 'app-markovitz',
  templateUrl: './markovitz.component.html',
  styleUrls: ['./markovitz.component.css']
})
export class MarkowitzPlotComponent implements OnInit {
  chartImage!: Blob;
  loading = true;
  error!: string;

  constructor(private financialChartService: ForexDataService) {}

  ngOnInit(): void {
    this.loadMarkowitzPlot();
  }

  loadMarkowitzPlot() {
    this.financialChartService.getMarkowitzPlot().subscribe(
      (image: Blob) => {
        this.chartImage = image;
        this.loading = false;
      },
      (error) => {
        this.error = 'Failed to load Markowitz plot.';
        this.loading = false;
      }
    );
  }

  getImageUrl(): string {
    return URL.createObjectURL(this.chartImage);
  }
}
