import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainComponent } from './main/main.component';
import { HttpClientModule } from '@angular/common/http';
import { ProviderService } from './shared/services/provider.service';
import {ReactiveFormsModule,FormsModule} from '@angular/forms';
import { NewclassFormComponent } from './newclass-form/newclass-form.component';
import { HeaderComponent } from './header/header.component';
import { AboutComponent } from './about/about.component';
import { ViewsComponent } from './views/views.component';

@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    NewclassFormComponent,
    HeaderComponent,
    AboutComponent,
    ViewsComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [
    ProviderService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
