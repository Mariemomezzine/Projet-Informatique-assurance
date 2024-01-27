import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MarkovitzComponent } from './markovitz.component';

describe('MarkovitzComponent', () => {
  let component: MarkovitzComponent;
  let fixture: ComponentFixture<MarkovitzComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MarkovitzComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MarkovitzComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
