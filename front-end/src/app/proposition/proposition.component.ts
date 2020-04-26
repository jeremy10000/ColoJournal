import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-proposition',
  templateUrl: './proposition.component.html',
  // styleUrls: ['./proposition.component.css']
})
export class PropositionComponent implements OnInit {
  myformError = false;

  constructor(
    private userService: UserService,
    private router: Router,
    private snackBar: MatSnackBar) { }

  ngOnInit(): void { }
  onSubmit(form: NgForm) {
    const data = {
      sender: this.userService.getUser(),
      receiver: form.value.mail,
      status: 'w'
    };
    this.proposition(data);
  }
  proposition(data) {
    this.userService.proposition(data).subscribe(
      response => {
        this.snackBar.open('La demande a été envoyée !', 'Retour', {
          duration: 2000
        }).afterDismissed().subscribe(() => {
          this.router.navigate(['/friends']);
        });
      },
      error => {
        console.log('Error', error);
        this.myformError = true;
      }
    );
  }

}
