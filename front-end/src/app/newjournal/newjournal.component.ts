import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-newjournal',
  templateUrl: './newjournal.component.html',
  // styleUrls: ['./newjournal.component.css']
})
export class NewjournalComponent implements OnInit {

  startDate: Date;
  myformError = false;
  journalDay: string;

  constructor(private userService: UserService,
              private router: Router,
              private snackBar: MatSnackBar) { }

  ngOnInit(): void { }
  showDate() {
    const day = this.startDate.getDate();
    const month = this.startDate.getMonth();
    const monthModified = month + 1;
    let monthString: string;
    if (monthModified < 10) { monthString = '0' + monthModified; } else { monthString = '' + monthModified; }
    const year = this.startDate.getFullYear();
    this.journalDay = year + '-' + monthString + '-' + day;
  }
  onSubmit(form: NgForm) {
    const data = {
      date: this.journalDay,
      name: form.value.title
    };
    this.addJournal(data);
  }
  addJournal(data) {
    this.userService.addJournal(data).subscribe(
      response => {
        this.snackBar.open('Le journal a été créé !', 'Retour', {
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
}
