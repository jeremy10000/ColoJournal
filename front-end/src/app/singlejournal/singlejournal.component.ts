import { Component, OnInit, Inject } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import {MatDialog, MAT_DIALOG_DATA} from '@angular/material/dialog';
import {MatSnackBar} from '@angular/material/snack-bar';
import { PageModel } from '../models/page';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-singlejournal',
  templateUrl: './singlejournal.component.html',
  // styleUrls: ['./singlejournal.component.css']
})
export class SinglejournalComponent implements OnInit {

  pages: PageModel[];
  journalId: number;
  journalName: string;

  displayedColumns: string[] = ['name'];
  showTable = false;

  constructor(private userService: UserService,
              private route: ActivatedRoute,
              private router: Router,
              private snackBar: MatSnackBar,
              public dialog: MatDialog) { }

  ngOnInit(): void {
    this.journalId = this.route.snapshot.params.id;
    this.getJournalPages();
  }
  getJournalPages() {
    this.userService.getPages(this.journalId).subscribe(
      response => {
        this.pages = response;
        if (this.pages.length > 0) {
          this.showTable = true;
          this.journalName = this.pages[0].journal_name;
        } else {
          this.journalName = 'Mon journal';
        }
      },
      error => {
        console.log('Error', error);
      }
    );
  }
  editJournal() {
    this.router.navigate(['/editjournal', this.journalId]);
  }
  deleteJournal() {
    this.userService.deleteJournal(this.journalId).subscribe(
      response => {
        this.snackBar.open('Le journal a été éffacé !', 'Retour', {
          duration: 2000
        }).afterDismissed().subscribe(() => {
          this.router.navigate(['/journals']);
        });
      },
      error => {
        console.log('Error', error);
      }
    );
  }
  openDialog(page) {
    this.dialog.open(DialogPageComponent, {
      data: {
        id: page.id,
        name: page.name,
        text: page.text
      },
      width: '90%'
    });
  }
  addPage() {
    this.router.navigate(['/addpage', this.journalId]);
  }

}

@Component({
  selector: 'app-dialog-page',
  templateUrl: 'app-dialog-page.html',
})
export class DialogPageComponent {
  id: number;
  constructor(@Inject(MAT_DIALOG_DATA) public data,
              private router: Router, private userService: UserService,
              private snackBar: MatSnackBar) {}
  goEdit() {
    this.id = this.data.id;
    this.router.navigate(['/editpage', this.id]);
  }
  deletePage() {
    this.userService.deletePage(this.data.id).subscribe(
      response => {
        this.snackBar.open('La page a été éffacée !', 'Retour', {
          duration: 2000
        }).afterDismissed().subscribe(() => {
          this.router.navigate(['/journals']);
        });
      },
      error => {
        console.log('Error', error);
      }
    );
  }
}
