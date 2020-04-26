import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { FlexLayoutModule } from '@angular/flex-layout';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { RichTextEditorModule } from '@syncfusion/ej2-angular-richtexteditor';

import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatTableModule } from '@angular/material/table';
import { MatDialogModule } from '@angular/material/dialog';
import {MatDatepickerModule} from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';
import {MatSnackBarModule} from '@angular/material/snack-bar';
import {MatMenuModule} from '@angular/material/menu';

import { NavbarComponent } from './shared/navbar/navbar.component';
import { HomeComponent } from './home/home.component';
import { JournalsComponent } from './journals/journals.component';
import { SinglejournalComponent } from './singlejournal/singlejournal.component';
import { DialogPageComponent } from './singlejournal/singlejournal.component';
import { FriendsComponent } from './friends/friends.component';
import { MyfriendComponent } from './myfriend/myfriend.component';
import { NewaccountComponent } from './newaccount/newaccount.component';
import { MyfriendpagesComponent } from './myfriendpages/myfriendpages.component';
import { DialogFriendPageComponent } from './myfriendpages/myfriendpages.component';
import { NewjournalComponent } from './newjournal/newjournal.component';
import { EditjournalComponent } from './editjournal/editjournal.component';
import { EditionpageComponent } from './editionpage/editionpage.component';
import { NewpageComponent } from './newpage/newpage.component';
import { PropositionComponent } from './proposition/proposition.component';

import { SafePipe } from './safe.pipe';

import { GuardService } from './guard.service';

import { registerLocaleData } from '@angular/common';
import localeFr from '@angular/common/locales/fr';
import { LOCALE_ID } from '@angular/core';

import { NotfoundComponent } from './notfound/notfound.component';

registerLocaleData(localeFr, 'fr');

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    HomeComponent,
    JournalsComponent,
    SinglejournalComponent,
    FriendsComponent,
    MyfriendComponent,
    DialogPageComponent,
    NewaccountComponent,
    MyfriendpagesComponent,
    DialogFriendPageComponent,
    NewjournalComponent,
    EditjournalComponent,
    EditionpageComponent,
    SafePipe,
    NewpageComponent,
    PropositionComponent,
    NotfoundComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    FormsModule,
    HttpClientModule,
    FlexLayoutModule,
    MatToolbarModule,
    MatIconModule,
    MatButtonModule,
    MatFormFieldModule,
    MatInputModule,
    MatTableModule,
    MatDialogModule,
    MatDatepickerModule,
    MatNativeDateModule,
    MatSnackBarModule,
    RichTextEditorModule,
    MatMenuModule,
  ],
  providers: [{ provide: LOCALE_ID, useValue: 'fr-FR' }, GuardService],
  bootstrap: [AppComponent],
  entryComponents: [DialogPageComponent, DialogFriendPageComponent]
})
export class AppModule { }
