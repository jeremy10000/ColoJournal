import { Component, OnInit } from '@angular/core';
import { UserService } from '../services/user.service';
import { ActivatedRoute, Router } from '@angular/router';
import { NgForm } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { JournalModel } from '../models/journal';


@Component({
  selector: 'app-editjournal',
  templateUrl: './editjournal.component.html',
  // styleUrls: ['./editjournal.component.css']
})
export class EditjournalComponent implements OnInit {

  journal: JournalModel;
  journalId: number;
  journalDay: string;
  journalTitle: string;

  shareButton = false;
  startDate: Date;
  myformError = false;

  constructor(private snackBar: MatSnackBar,
              private userService: UserService,
              private route: ActivatedRoute,
              private router: Router) { }

  ngOnInit(): void {
    this.journalId = this.route.snapshot.params.id;
    this.getJournalId();
  }
  getJournalId() {
    this.userService.getJournalId(this.journalId).subscribe(
      (response: JournalModel) => {
        this.journal = response;
        this.journalTitle = this.journal.name;
        this.shareButton = this.journal.shared;
      },
      error => {
        console.log('Error', error);
      }
    );
  }
  shareNo() {
    this.shareButton = false;
  }
  shareYes() {
    this.shareButton = true;
  }
  onSubmit(form: NgForm) {
    const data = {
      date: this.journalDay,
      name: form.value.title,
      shared: this.shareButton
    };
    this.patchJournal(data);
  }
  patchJournal(data) {
    this.userService.patchJournal(this.journalId, data).subscribe(
      response => {
        this.snackBar.open('Le journal a été modifié !', 'Retour', {
          duration: 2000
        }).afterDismissed().subscribe(() => {
          this.router.navigate(['/journals']);
        });
      },
      error => {
        console.log('Error', error);
        this.myformError = true;
      }
    );
  }
  showDate() {
    const day = this.startDate.getDate();
    const month = this.startDate.getMonth();
    const monthModified = month + 1;
    let monthString: string;
    if (monthModified < 10) { monthString = '0' + monthModified; } else { monthString = '' + monthModified; }
    const year = this.startDate.getFullYear();
    this.journalDay = year + '-' + monthString + '-' + day;
    console.log('newDay', this.journalDay);
    console.log('monthString', monthString);
  }
}
