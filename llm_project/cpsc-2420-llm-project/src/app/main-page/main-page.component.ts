import { Component, OnInit } from '@angular/core';
import { MainPageServiceService } from '../services/main-page-service.service';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.css']
})
export class MainPageComponent implements OnInit {

  constructor(private mainPageService: MainPageServiceService) { }

  ngOnInit(): void {
  }

  promptText = document.getElementById("prompt-res")

  getPrompt(prompt:HTMLInputElement){
    this.mainPageService.sendPrompt(prompt.value).subscribe((res:Response)=>{
      if(JSON.stringify(res)){
        console.log(JSON.stringify(res))
        // this.promptText ? this.promptText.append(JSON.stringify(res)) : null;
      }
    })
  }
}
