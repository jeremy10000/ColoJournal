import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SinglejournalComponent } from './singlejournal.component';

describe('SinglejournalComponent', () => {
  let component: SinglejournalComponent;
  let fixture: ComponentFixture<SinglejournalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SinglejournalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SinglejournalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
