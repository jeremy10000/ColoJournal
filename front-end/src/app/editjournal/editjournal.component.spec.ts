import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EditjournalComponent } from './editjournal.component';

describe('EditjournalComponent', () => {
  let component: EditjournalComponent;
  let fixture: ComponentFixture<EditjournalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EditjournalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EditjournalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
