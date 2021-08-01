import { User } from './models/user';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';
import { IUser } from './models/iuser';
import { UserProfile } from './models/user-profile';
import { LoginRequest } from './models/login-request';

@Injectable({
  providedIn: 'root'
})
export class UserServiceService {

  private _url: string = 'http://localhost:8000/';

  constructor(private http: HttpClient) { }

  public getStudentList(): Observable<IUser[]> {
    return this.http.get<IUser[]>(this._url + 'list/');
  }

  public registerNewUser(userModel: User): Observable<IUser> {
    return this.http.post<IUser>(this._url + 'add-new/', userModel);
  }

  public updateUser(userModel: UserProfile,userId): Observable<any> {
    return this.http.post<any>(this._url + 'user-profile/'+userId, userModel);
  }

  public signIn(loginRequest: LoginRequest): Observable<IUser> {
    return this.http.post<IUser>(this._url + 'sign-in/', loginRequest);
  }
  
  public uploadImage(profileImage): Observable<any> {
    return this.http.post<any>(this._url + 'upload-file/', profileImage);
  }

  public getUserProfile(userId) {
    return this.http.get<any>(this._url + 'user-profile/'+userId);
  }
}
