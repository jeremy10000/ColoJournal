import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NewjournalComponent } from './newjournal.component';

describe('NewjournalComponent', () => {
  let component: NewjournalComponent;
  let fixture: ComponentFixture<NewjournalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NewjournalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NewjournalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
