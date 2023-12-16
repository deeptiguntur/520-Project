import { Component, EventEmitter, Input, Output } from '@angular/core';
import { SellerService } from '../seller.service';
import { Observable } from 'rxjs';
import { HttpEventType, HttpResponse } from '@angular/common/http';

@Component({
  selector: 'app-upload-images',
  templateUrl: './upload-images.component.html',
  styleUrls: ['./upload-images.component.scss']
})
export class UploadImagesComponent {

  selectedFiles?: FileList;
  previews: string[] = [];
  imageInfos?: Observable<any>;

  // Input property to receive files from the parent component
  @Input() files: any;

  // Output property to emit image data back to the parent component
  @Output() imgData: EventEmitter<any> = new EventEmitter<any>();

  constructor(private sellerService: SellerService) { }

  ngOnInit(): void {}

  ngOnChanges() {
    if (this.files) {
      console.log(this.files)
      this.selectFiles(this.files);
    }
  }

  // Method to show selected files as image preview in UI
  selectFiles(event: any): void {
    this.selectedFiles = event.target.files;
    this.previews = [];
    if (this.selectedFiles && this.selectedFiles[0]) {
      const numberOfFiles = this.selectedFiles.length;
      for (let i = 0; i < numberOfFiles; i++) {
        const reader = new FileReader();
        reader.onload = (e: any) => {
          this.previews.push(e.target.result);
          if (this.previews.length === numberOfFiles) {
            this.imgData.emit(this.previews);
          }
        };
        reader.readAsDataURL(this.selectedFiles[i]);
      }
    }
  }

}
