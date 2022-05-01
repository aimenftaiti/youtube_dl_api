import { Component, OnInit } from '@angular/core';
import {DownloadService} from "../download.service";
import * as fileSaver from "file-saver";

@Component({
  selector: 'app-download',
  templateUrl: './download.component.html',
  styleUrls: ['./download.component.scss']
})
export class DownloadComponent implements OnInit {
  url: string = '';

  constructor(private downloadService:DownloadService) { }

  sendURL():void{
    this.downloadService.downloadFile(this.url).subscribe((response: any) => { //when you use stricter type checking
      let blob:any = new Blob([response], { type: 'video/mp4' });
      const url = window.URL.createObjectURL(blob);
      fileSaver.saveAs(blob, 'video.mp4');
    }), (error: any) => console.log('Error downloading the ' + error), //when you use stricter type checking
      () => console.info('File downloaded successfully');
  }

  ngOnInit(): void {
  }
}
