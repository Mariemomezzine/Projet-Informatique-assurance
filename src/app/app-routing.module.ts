import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { WelcomeComponent } from './pages/welcome/welcome.component';
import { HistoriqueComponent } from './historique/historique.component';
import { MarkowitzPlotComponent } from './markovitz/markovitz.component';

const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: '/welcome' },
  { path: 'welcome', loadChildren: () => import('./pages/welcome/welcome.module').then(m => m.WelcomeModule) },
  { path: 'welcome', component: WelcomeComponent },
  { path: 'historical-data/:currency', component: HistoriqueComponent },
  { path: 'markowitz_plot', component: MarkowitzPlotComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
