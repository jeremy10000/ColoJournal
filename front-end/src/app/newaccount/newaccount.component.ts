import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { UserService } from '../services/user.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Router } from '@angular/router';

@Component({
  selector: 'app-newaccount',
  templateUrl: './newaccount.component.html',
  // styleUrls: ['./newaccount.component.css']
})
export class NewaccountComponent implements OnInit {
  myformError = false;

  constructor(private userService: UserService,
              private router: Router,
              private snackBar: MatSnackBar) { }

  ngOnInit(): void { }
  onSubmit(form: NgForm) {
    const credentials = {
      email: form.value.username,
      password: form.value.password
    };
    this.register(credentials);
  }
  register(credentials) {
    this.userService.registerNewUser(credentials).subscribe(
      response => {
        this.snackBar.open('Le compte a été créé !', 'Retour', {
          duration: 2000
        }).afterDismissed().subscribe(() => {
          this.router.navigate(['/']);
        });
      },
      error => {
        this.myformError = true;
      }
    );
  }
}
