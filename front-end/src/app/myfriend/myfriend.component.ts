import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { JournalModel } from '../models/journal';

import { UserService } from '../services/user.service';

@Component({
  selector: 'app-myfriend',
  templateUrl: './myfriend.component.html',
  // styleUrls: ['./myfriend.component.css']
})
export class MyfriendComponent implements OnInit {

  userId: number;
  journals: JournalModel[];
  displayedColumns: string[] = ['name', 'date'];
  showTable = false;

  constructor(private router: Router,
              private userService: UserService,
              private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.userId = this.route.snapshot.params.id;
    this.getAllFriendJournals();
  }

  getAllFriendJournals() {
    this.userService.getAllFriendJournals(this.userId).subscribe(
      response => {
        this.journals = response;
        if (this.journals.length > 0) {
          this.showTable = true;
        }
      },
      error => {
        console.log('Error', error);
      }
    );
  }
  goJournal(id) {
    this.router.navigate(['/friend/journal', id]);
  }
}
