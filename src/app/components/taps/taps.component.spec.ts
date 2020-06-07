import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TapsComponent } from './taps.component';

describe('TapsComponent', () => {
  let component: TapsComponent;
  let fixture: ComponentFixture<TapsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TapsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TapsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
