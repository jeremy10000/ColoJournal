import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './home/home.component';
import { JournalsComponent } from './journals/journals.component';
import { SinglejournalComponent } from './singlejournal/singlejournal.component';
import { FriendsComponent } from './friends/friends.component';
import { MyfriendComponent } from './myfriend/myfriend.component';
import { MyfriendpagesComponent } from './myfriendpages/myfriendpages.component';
import { NewaccountComponent } from './newaccount/newaccount.component';
import { NewjournalComponent } from './newjournal/newjournal.component';
import { EditjournalComponent } from './editjournal/editjournal.component';
import { EditionpageComponent } from './editionpage/editionpage.component';
import { NewpageComponent } from './newpage/newpage.component';
import { PropositionComponent } from './proposition/proposition.component';
import { NotfoundComponent } from './notfound/notfound.component';

import { GuardService } from './guard.service';


const routes: Routes = [
  { path: '', component: HomeComponent },
  // My journal list.
  { path: 'journals', canActivate: [GuardService], component: JournalsComponent },
  // The pages of my journal.
  { path: 'journal/:id', canActivate: [GuardService], component: SinglejournalComponent },
  // My friend list.
  { path: 'friends', canActivate: [GuardService], component: FriendsComponent },
  // A friend's journals.
  { path: 'friend/:id', canActivate: [GuardService], component: MyfriendComponent },
  // A friend's pages.
  { path: 'friend/journal/:id', canActivate: [GuardService], component: MyfriendpagesComponent },
  // Register.
  { path: 'new', component: NewaccountComponent },
  // create a journal
  { path: 'newjournal', canActivate: [GuardService], component: NewjournalComponent },
  // Edit a journal.
  { path: 'editjournal/:id', canActivate: [GuardService], component: EditjournalComponent },
  // Edit a page.
  { path: 'editpage/:id', canActivate: [GuardService], component: EditionpageComponent },
  // add a page to a journal.
  { path: 'addpage/:id', canActivate: [GuardService], component: NewpageComponent },
  // Request for friendship.
  { path: 'proposition', canActivate: [GuardService], component: PropositionComponent },
  // 404 Not Found.
  {path: '404', component: NotfoundComponent},
  {path: '**', redirectTo: '/404'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
