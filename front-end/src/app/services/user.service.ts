import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  authSubject = new Subject<boolean>();

  constructor(private http: HttpClient) { }

  // Verify TOKEN in localstorage. This runs once on application startup.
  checkUser() {
    if (this.getToken()) {
      this.emitAuthSubject(true);
    }
  }
  emitAuthSubject(value: boolean) {
    this.authSubject.next(value);
  }

  // Token

  getToken() {
    const token = JSON.parse(localStorage.getItem('Token'));
    if (token) { return token.token; }
    return false;
  }
  getUser() {
    const token = JSON.parse(localStorage.getItem('Token'));
    if (token) { return token.user; }
    return false;
  }
  saveToken(token) {
    localStorage.setItem('Token', JSON.stringify(token));
  }
  destroyToken() {
    localStorage.removeItem('Token');
  }

  // API

  loginUser(data): Observable<any> {
    return this.http.post(`${environment.api_url}/login/`, data);
  }
  registerNewUser(data): Observable<any> {
    return this.http.post(`${environment.api_url}/register/`, data);
  }

  getPages(id): Observable<any> {
    const token = this.getToken();
    const httpOptions = {
      headers: new HttpHeaders({ Authorization: 'Token ' + token}),
      params: new HttpParams().append('journal', id)
    };
    return this.http.get(`${environment.api_url}/pages/`, httpOptions);
  }

  getFriendships(): Observable<any> {
    const token = this.getToken();
    const httpOptions = {
      headers: new HttpHeaders({ Authorization: 'Token ' + token}),
    };
    return this.http.get(`${environment.api_url}/friendship/`, httpOptions);
  }

  getAllJournals(): Observable<any> {
    const token = this.getToken();
    const httpOptions = {
      headers: new HttpHeaders({ Authorization: 'Token ' + token}),
    };
    return this.http.get(`${environment.api_url}/journals/`, httpOptions);
  }
  getAllFriendJournals(id): Observable<any> {
    const token = this.getToken();
    const httpOptions = {
      headers: new HttpHeaders({ Authorization: 'Token ' + token}),
      params: new HttpParams().append('id', id)
    };
    return this.http.get(`${environment.api_url}/friend/`, httpOptions);
  }
  getFriendJournalPages(id): Observable<any> {
    const token = this.getToken();
    const httpOptions = {
      headers: new HttpHeaders({ Authorization: 'Token ' + token}),
      params: new HttpParams().append('id', id)
    };
    return this.http.get(`${environment.api_url}/friend/pages/`, httpOptions);
  }
  addJournal(data) {
    const token = this.getToken();
    const httpOptions = {
      headers: new HttpHeaders({ Authorization: 'Token ' + token}),
    };
    return this.http.post(`${environment.api_url}/journals/`, data, httpOptions);
  }
  getJournalId(id) {
    const token = this.getToken();
    const httpOptions = {
      headers: new HttpHeaders({ Authorization: 'Token ' + token}),
    };
    return this.http.get(`${environment.api_url}/journals/${id}/`, httpOptions);
  }
  patchJournal(id, data): Observable<any> {
    const token = this.getToken();
    const httpOptions = {
      headers: new HttpHeaders({ Authorization: 'Token ' + token}),
    };
    return this.http.patch(`${environment.api_url}/journals/${id}/`, data, httpOptions);
  }
  deleteJournal(id): Observable<any> {
    const token = this.getToken();
    const httpOptions = {
      headers: new HttpHeaders({ Authorization: 'Token ' + token}),
    };
    return this.http.delete(`${environment.api_url}/journals/${id}/`, httpOptions);
  }
  getOnePage(id): Observable<any> {
    const token = this.getToken();
    const httpOptions = {
      headers: new HttpHeaders({ Authorization: 'Token ' + token}),
    };
    return this.http.get(`${environment.api_url}/pages/${id}/`, httpOptions);
  }
  patchPage(id, data): Observable<any> {
    const token = this.getToken();
    const httpOptions = {
      headers: new HttpHeaders({ Authorization: 'Token ' + token}),
    };
    return this.http.patch(`${environment.api_url}/pages/${id}/`, data, httpOptions);
  }
  deletePage(id): Observable<any> {
    const token = this.getToken();
    const httpOptions = {
      headers: new HttpHeaders({ Authorization: 'Token ' + token}),
    };
    return this.http.delete(`${environment.api_url}/pages/${id}/`, httpOptions);
  }
  createPage(data) {
    const token = this.getToken();
    const httpOptions = {
      headers: new HttpHeaders({ Authorization: 'Token ' + token}),
    };
    return this.http.post(`${environment.api_url}/pages/`, data, httpOptions);
  }
  responseRelation(id, data): Observable<any> {
    const token = this.getToken();
    const httpOptions = {
      headers: new HttpHeaders({ Authorization: 'Token ' + token}),
    };
    return this.http.patch(`${environment.api_url}/friendship/${id}/`, data, httpOptions);
  }
  proposition(data): Observable<any> {
    const token = this.getToken();
    const httpOptions = {
      headers: new HttpHeaders({ Authorization: 'Token ' + token}),
    };
    return this.http.post(`${environment.api_url}/friendship/`, data, httpOptions);
  }

}
