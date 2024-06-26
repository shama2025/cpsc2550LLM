import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
@Injectable({
  providedIn: 'root'
})
export class MainPageServiceService {

  constructor(private http: HttpClient) { }

  url:string = ""

  sendPrompt(prompt:string, query:string, llmSelect:number):Observable<any>{
    this.url = `${environment.apiBaseUrl}/api/prompt-response?prompt=${prompt}&query=${query}&llmSelect=${llmSelect}`
    return this.http.get(this.url)
  }
}
