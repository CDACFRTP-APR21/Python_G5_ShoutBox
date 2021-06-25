import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReportedShoutsComponent } from './reported-shouts.component';

describe('ReportedShoutsComponent', () => {
  let component: ReportedShoutsComponent;
  let fixture: ComponentFixture<ReportedShoutsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ReportedShoutsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ReportedShoutsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
