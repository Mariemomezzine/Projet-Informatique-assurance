import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ForexDataService {
  private apiUrl = 'http://127.0.0.1:5000/get_forex_data';
   private baseUrl = 'http://127.0.0.1:5000';
  constructor(private http: HttpClient) { }
  getForexData(): Observable<any> {
    return this.http.get(this.apiUrl);
  }


  getHistoricalData(currency: string): Observable<any> {
    const url = `${this.baseUrl}/get_historical_data?currency=${currency}`;
    return this.http.get<any>(url);
  }
  getMarkowitzPlot(): Observable<Blob> {

    return this.http.get(`${this.baseUrl}/markowitz_plot`, {
      responseType: 'blob', // Treat the response as a binary blob (image)
    });
  }


}
