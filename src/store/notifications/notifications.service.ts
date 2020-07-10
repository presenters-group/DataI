import { Injectable } from '@angular/core';
import Swal, { SweetAlertOptions, SweetAlertResult } from "sweetalert2";
import { from, Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class NotificationService {

 private loadMixinOptions: SweetAlertOptions = {
  toast: true,
  position: "top-end",
  customClass: {
    container: "no-clicks"
  },
  onOpen: () => {
    this.sweetAlert.showLoading();
  }
}


private messagesMixinOptions: SweetAlertOptions = {
  toast: true,
  position: "top-end",
  timer: 5000,
  showConfirmButton: false,
  customClass: {
    container: 'rtl'
  }
}


sweetAlert: typeof Swal = Swal.mixin({ ...this.loadMixinOptions });



startLoading(loadingMessage: string = "Loading") {
  this.sweetAlert = Swal.mixin({
    ...this.loadMixinOptions,
    title: loadingMessage || "Loading",
  });

  this.sweetAlert.fire(loadingMessage)
}



stopLoading() { this.sweetAlert.close() }



isLoading() {
  return this.sweetAlert.isLoading()
}



success(successMessage?: string) {
  this.sweetAlert = Swal.mixin({
    ...this.messagesMixinOptions,
    icon: 'success',
    title: successMessage || "Success",
  })
  this.sweetAlert.fire();
}



fail(failMessage?: string) {
  this.sweetAlert = Swal.mixin({
    ...this.messagesMixinOptions,
    title: failMessage || "Error",
    icon: 'error',
  })
  this.sweetAlert.fire();
}


warning(warningMessage?: string) {
  this.sweetAlert = Swal.mixin({
    ...this.messagesMixinOptions,
    title: warningMessage || "Warning",
    icon: 'warning',
  })
  this.sweetAlert.fire();
}



info(infoMessage?: string, options?: SweetAlertOptions) {
  this.sweetAlert = Swal.mixin({
    ...this.messagesMixinOptions,
    title: infoMessage || "Do You Know!",
    icon: 'info',
    ...options,
  })

  this.sweetAlert.fire()
}




confirmAlert({
  title,
  confirmButtonText,
  cancelButtonText,
  text
}: SweetAlertOptions = {}): Observable<boolean> {
  return from(
    Swal.fire({
      text: text || '',
      title: title || 'Are You Sure',
      confirmButtonText: confirmButtonText || 'Yes',
      cancelButtonText: cancelButtonText || 'No',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#d33',
      cancelButtonColor: '#3085d6',
    })
  ).pipe(map(res => !!res.value));
}



deleteConfirmAlert(options) {
  return this.confirmAlert( {...options, confirmButtonText: 'Delete', cancelButtonText: 'Cancel' })

}


fireAlert(options: SweetAlertOptions): Promise<SweetAlertResult> {
  return Swal.fire(options);
}
}
