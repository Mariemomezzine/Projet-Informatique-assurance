import { NgModule } from '@angular/core';

import { WelcomeRoutingModule } from './welcome-routing.module';
import { NzTableModule } from 'ng-zorro-antd/table';
import { WelcomeComponent } from './welcome.component';
import { CommonModule } from '@angular/common';


import { NzDividerModule } from 'ng-zorro-antd/divider';

import { NzModalModule } from 'ng-zorro-antd/modal';
import { NzDropDownModule } from 'ng-zorro-antd/dropdown';
import { FormsModule } from '@angular/forms';
import { NzIconModule } from 'ng-zorro-antd/icon';
@NgModule({
  imports: [WelcomeRoutingModule],
  declarations: [],
  exports: [
    CommonModule,
    NzTableModule ,
    NzDividerModule,
    NzModalModule,
    NzDropDownModule,
    FormsModule,
    NzIconModule
  ]
})
export class WelcomeModule { }
