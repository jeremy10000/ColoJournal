import { Component, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';
import { UserService } from '../services/user.service';
import { PageModel } from '../models/page';
import { NgForm } from '@angular/forms';
import { ToolbarService, HtmlEditorService } from '@syncfusion/ej2-angular-richtexteditor';

@Component({
  selector: 'app-editionpage',
  templateUrl: './editionpage.component.html',
  // styleUrls: ['./editionpage.component.css'],
  providers: [ToolbarService, HtmlEditorService]
})
export class EditionpageComponent implements OnInit {
  pageId: number;
  page: PageModel;
  pageName: string;
  myformError = false;
  public height = 300;
  public tools: object = {
    items: ['Undo', 'Redo', '|',
        'Bold', 'Italic', 'Underline', '|',
        'FontSize', 'FontColor', 'BackgroundColor', '|',
        'Formats', 'Alignments', '|', '|',
        'Indent', 'Outdent', '|',
        'SourceCode']
  };
  public textContent;

  @ViewChild('rte') public rteObj;

  constructor(private snackBar: MatSnackBar,
              private route: ActivatedRoute,
              private router: Router,
              private userService: UserService) { }

  ngOnInit(): void {
    this.pageId = this.route.snapshot.params.id;
    this.textContent = '';
    this.getOnePage();
  }
  getOnePage() {
    this.userService.getOnePage(this.pageId).subscribe(
      response => {
        this.page = response;
        this.textContent = this.page.text;
        this.pageName = this.page.name;
      },
      error => {
        console.log('Error', error);
      }
    );
  }
  onSubmit(form: NgForm) {
    const data = {
      name: form.value.title,
      text: this.rteObj.getHtml(),
      journal: this.page.journal
    };
    this.patchPage(data);
  }
  patchPage(data) {
    this.userService.patchPage(this.pageId, data).subscribe(
      response => {
        this.snackBar.open('La page a été modifiée !', 'Retour', {
          duration: 2000
        }).afterDismissed().subscribe(() => {
          this.router.navigate(['/journal', this.page.journal]);
        });
      },
      error => {
        console.log('Error', error);
        this.myformError = true;
      }
    );
  }
}
