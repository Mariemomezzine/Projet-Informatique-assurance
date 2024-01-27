import { TestBed } from '@angular/core/testing';

import { ForexDataService } from './forex-data.service';

describe('ForexDataService', () => {
  let service: ForexDataService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ForexDataService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
