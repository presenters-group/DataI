import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AddVisualizerComponent } from './add-visualizer.component';

describe('AddVisualizerComponent', () => {
  let component: AddVisualizerComponent;
  let fixture: ComponentFixture<AddVisualizerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AddVisualizerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AddVisualizerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
