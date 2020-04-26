import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgForm } from '@angular/forms';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  // styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  myformError = false;

  constructor(private userService: UserService, private router: Router) { }

  ngOnInit(): void {
    const isAuth = this.userService.getToken();
    if (isAuth) {
      this.router.navigate(['/journals']);
    }
  }
  onSubmit(form: NgForm) {
    const credentials = {
      username: form.value.username,
      password: form.value.password
    };
    this.login(credentials);
  }
  login(credentials) {
    this.userService.loginUser(credentials).subscribe(
      response => {
        this.userService.saveToken(response);
        this.router.navigate(['/journals']);
      },
      error => {
        console.log('Error', error);
        this.myformError = true;
      }
    );
  }
}
