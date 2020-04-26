import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EditionpageComponent } from './editionpage.component';

describe('EditionpageComponent', () => {
  let component: EditionpageComponent;
  let fixture: ComponentFixture<EditionpageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EditionpageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EditionpageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
