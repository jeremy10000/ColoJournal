import { Component, OnInit, Inject } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MatDialog, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { PageModel } from '../models/page';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-myfriendpages',
  templateUrl: './myfriendpages.component.html',
  // styleUrls: ['./myfriendpages.component.css']
})
export class MyfriendpagesComponent implements OnInit {

  pages: PageModel[];
  journalId: number;
  journalName: string;
  displayedColumns: string[] = ['name'];
  showTable = false;

  constructor(private userService: UserService,
              private route: ActivatedRoute,
              public dialog: MatDialog) { }

  ngOnInit(): void {
    this.journalId = this.route.snapshot.params.id;
    this.getFriendJournalPages();
  }
  getFriendJournalPages() {
    this.userService.getFriendJournalPages(this.journalId).subscribe(
      response => {
        this.pages = response;
        if (this.pages.length > 0) {
          this.showTable = true;
          this.journalName = this.pages[0].journal_name;
        } else {
          this.journalName = 'Mon journal';
        }
      },
      error => {
        console.log('Error', error);
      }
    );
  }
  openDialog(page) {
    this.dialog.open(DialogFriendPageComponent, {
      data: {
        name: page.name,
        text: page.text
      },
      width: '90%'
    });
  }
}

@Component({
  selector: 'app-dialog-page-friend',
  templateUrl: 'app-dialog-page-friend.html',
})
export class DialogFriendPageComponent {
  constructor(@Inject(MAT_DIALOG_DATA) public data) {}
}
