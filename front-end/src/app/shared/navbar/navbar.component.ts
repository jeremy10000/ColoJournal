import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { Router } from '@angular/router';
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  // styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit, OnDestroy {

  isAuth: boolean;
  userSubscription: Subscription;

  constructor(private router: Router, private userService: UserService) { }

  ngOnInit(): void {
    this.userSubscription = this.userService.authSubject.subscribe(
      (value: boolean) => {
        if (value) { this.isAuth = true; } else { this.isAuth = false; }
      },
      (error) => {
        this.isAuth = false;
      }
    );
  }

  goJournals() {
    this.router.navigate(['/journals']);
  }
  goFriends() {
    this.router.navigate(['/friends']);
  }
  goNewAccount() {
    this.router.navigate(['/new']);
  }
  logout() {
    this.userService.destroyToken();
    this.userService.emitAuthSubject(false);
    this.router.navigate(['/']);
  }

  ngOnDestroy(): void {
    this.userSubscription.unsubscribe();
  }

}
