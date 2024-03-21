import { Component, OnInit } from '@angular/core';
import { MainPageServiceService } from '../services/main-page-service.service';
import { query } from '@angular/animations';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.css']
})
export class MainPageComponent implements OnInit {

  constructor(private mainPageService: MainPageServiceService) { }

  ngOnInit(): void {
  }

  llmReply = ''
  getPrompt(prompt:HTMLInputElement, query:HTMLInputElement){
    this.mainPageService.sendPrompt(prompt.value,query.value).subscribe((res:Response)=>{
      if(JSON.stringify(res)){
        console.log(JSON.stringify(res))
        let response = JSON.stringify(res) //Upadte this to become a response object and not a JSON string
        this.llmReply = response
      }
    })
  }
}
