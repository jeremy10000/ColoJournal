import { Component, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';
import { UserService } from '../services/user.service';
import { NgForm } from '@angular/forms';
import { ToolbarService, HtmlEditorService } from '@syncfusion/ej2-angular-richtexteditor';


@Component({
  selector: 'app-newpage',
  templateUrl: './newpage.component.html',
  // styleUrls: ['./newpage.component.css'],
  providers: [ToolbarService, HtmlEditorService]
})
export class NewpageComponent implements OnInit {

  journalId: number;
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
  myformError = false;

  @ViewChild('rte') public rteObj;

  constructor(private snackBar: MatSnackBar,
              private route: ActivatedRoute,
              private router: Router,
              private userService: UserService) { }

  ngOnInit(): void {
    this.textContent = '';
    this.journalId = this.route.snapshot.params.id;
  }
  onSubmit(form: NgForm) {
    const data = {
      name: form.value.title,
      text: this.rteObj.getHtml(),
      journal: this.journalId
    };
    this.createPage(data);
  }
  createPage(data) {
    this.userService.createPage(data).subscribe(
      response => {
        this.snackBar.open('La page a été créée !', 'Retour', {
          duration: 2000
        }).afterDismissed().subscribe(() => {
          this.router.navigate(['/journal', this.journalId]);
        });
      },
      error => {
        console.log('Error', error);
        this.myformError = true;
      }
    );
  }

}
