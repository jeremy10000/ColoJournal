import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MyfriendpagesComponent } from './myfriendpages.component';

describe('MyfriendpagesComponent', () => {
  let component: MyfriendpagesComponent;
  let fixture: ComponentFixture<MyfriendpagesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MyfriendpagesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MyfriendpagesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
