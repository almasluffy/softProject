import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MainComponent } from './main/main.component';
import { NewclassFormComponent } from './newclass-form/newclass-form.component';
import { AboutComponent } from './about/about.component';
import { ViewsComponent } from './views/views.component';

const routes: Routes = [
  // { path: '', redirectTo: '/main', pathMatch: 'full' },
  { path: 'main', component: MainComponent },
  { path: 'newclass-form',component:NewclassFormComponent},
  // { path: 'main', component: MainComponent },
  { path: 'about', component: AboutComponent },
  { path: 'views', component: ViewsComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
