import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UserService } from '../services/user.service';
import { FriendshipModel } from '../models/friendship';


@Component({
  selector: 'app-friends',
  templateUrl: './friends.component.html',
  // styleUrls: ['./friends.component.css']
})
export class FriendsComponent implements OnInit {

  displayedColumns: string[] = ['mail'];
  displayedPropositionColumns: string[] = ['mail', 'status'];

  friendsYes: FriendshipModel[];
  friendsNo: FriendshipModel[];
  friendsReceived: FriendshipModel[];
  friendsWaiting: FriendshipModel[];

  // show tables if elements > 0
  showTableFriendsYes = false;
  showTableFriendsNo = false;
  showTableFriendsReceived = false;
  showTableFriendsWaiting = false;

  constructor(private router: Router, private userService: UserService) { }

  ngOnInit(): void {
    this.getFriendships();
  }
  goFriend(id) {
    this.router.navigate(['/friend', id]);
  }
  getFriendships() {
    this.userService.getFriendships().subscribe(
      response => {
        this.friendsYes = response.yes;
        this.friendsNo = response.no;
        this.friendsReceived = response.received;
        this.friendsWaiting = response.waiting;

        if (this.friendsYes.length > 0) { this.showTableFriendsYes = true; } else { this.showTableFriendsYes = false; }
        if (this.friendsNo.length > 0) { this.showTableFriendsNo = true; } else { this.showTableFriendsNo = false; }
        if (this.friendsReceived.length > 0) { this.showTableFriendsReceived = true; } else { this.showTableFriendsReceived = false; }
        if (this.friendsWaiting.length > 0) { this.showTableFriendsWaiting = true; } else { this.showTableFriendsWaiting = false; }
      },
      error => {
        console.log('Error', error);
      }
    );
  }
  yes(id, mail) {
    const data = {
      receiver: mail,
      sender : this.userService.getUser(),
      status: 'y'
    };
    this.responseRelation(id, data);
  }
  no(id, mail) {
    const data = {
      receiver: mail,
      sender : this.userService.getUser(),
      status: 'n'
    };
    this.responseRelation(id, data);
  }
  goProposition() {
    this.router.navigate(['/proposition']);
  }
  responseRelation(id, data) {
    this.userService.responseRelation(id, data).subscribe(
      response => {
        // this.router.navigate(['/friends']);
        this.getFriendships();
      },
      error => {
        console.log('Error', error);
      }
    );
  }
}
