import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { JournalModel } from '../models/journal';
import { UserService } from '../services/user.service';


@Component({
  selector: 'app-journals',
  templateUrl: './journals.component.html',
  styleUrls: ['./journals.component.css']
})
export class JournalsComponent implements OnInit {

  displayedColumns: string[] = ['name', 'shared', 'date'];
  showTable = false;
  journals: JournalModel[];

  constructor(private router: Router, private userService: UserService) { }

  ngOnInit(): void {
    this.getAllJournals();
  }

  getAllJournals() {
    this.userService.getAllJournals().subscribe(
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
    this.router.navigate(['/journal', id]);
  }
  newJournal() {
    this.router.navigate(['/newjournal']);
  }
}
