import { TestBed } from '@angular/core/testing';

import { UmlserviceService } from './umlservice.service';

describe('UmlserviceService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: UmlserviceService = TestBed.get(UmlserviceService);
    expect(service).toBeTruthy();
  });
});
