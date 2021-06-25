import { TestBed } from '@angular/core/testing';

import { ReportedShoutsService } from './reported-shouts.service';

describe('ReportedShoutsService', () => {
  let service: ReportedShoutsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ReportedShoutsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
