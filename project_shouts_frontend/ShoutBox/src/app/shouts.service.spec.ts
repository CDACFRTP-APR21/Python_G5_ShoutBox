import { TestBed } from '@angular/core/testing';

import { ShoutsService } from './shouts.service';

describe('ShoutsService', () => {
  let service: ShoutsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ShoutsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
