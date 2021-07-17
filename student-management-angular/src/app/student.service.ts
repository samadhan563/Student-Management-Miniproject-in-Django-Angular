import { LoginRequest } from './models/login-request';
import { User } from './models/user';
import { IUser } from './models/IUser';
import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
// @Injectable()
export class StudentService {

  private _url: string = 'http://localhost:8000/';

  constructor(private http: HttpClient) { }

  public getStudentList(): Observable<IUser[]> {
    return this.http.get<IUser[]>(this._url + 'list/');
  }

  public registerNewUser(userModel:User):Observable<IUser>{
    return this.http.post<IUser>(this._url + 'add-new/',userModel);
  }

  public signIn(loginRequest:LoginRequest):Observable<IUser>{
    return this.http.post<IUser>(this._url + 'sign-in/',loginRequest);
  }

}
