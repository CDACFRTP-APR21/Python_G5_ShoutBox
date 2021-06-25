import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShoutsComponent } from './shouts.component';

describe('ShoutsComponent', () => {
  let component: ShoutsComponent;
  let fixture: ComponentFixture<ShoutsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShoutsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ShoutsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
