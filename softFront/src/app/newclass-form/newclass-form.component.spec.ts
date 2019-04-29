import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NewclassFormComponent } from './newclass-form.component';

describe('NewclassFormComponent', () => {
  let component: NewclassFormComponent;
  let fixture: ComponentFixture<NewclassFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NewclassFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NewclassFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
