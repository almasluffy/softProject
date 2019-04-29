import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MyProject,MyClass,MyField,MyMethod,MyInput } from '../models/models';
import { UmlserviceService } from './umlservice.service';
import { namespaceMathML } from '@angular/core/src/render3';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends UmlserviceService{

  constructor(http:HttpClient){
    super(http);  
  }


  getMyProject():Promise<MyProject[]>{
    return this.get(`http://127.0.0.1:8000/converter/my_projects/`,{});
  }

  getMyClass(project:MyProject):Promise<MyClass[]>{
    return this.get(`http://127.0.0.1:8000/converter/my_projects/${project.id}/my_classes/`,{});
  }

  // getMyField(project:MyProject,myclass:MyClass):Promise<MyField[]>{
  //   return this.get(`http://127.0.0.1:8000/converter/my_projects/${project.id}/my_classes/${myclass.id}/fields/`,{});
  // }

  // getMyMethod(project:MyProject,myclass:MyClass):Promise<MyMethod[]>{
  //   return this.get(`http://127.0.0.1:8000/converter/my_projects/${project.id}/my_classes/${myclass.id}/methods`,{});
  // }

  // getMyInput(project:MyProject,myclass:MyClass,methods:MyMethod):Promise<MyInput[]>{
  //   return this.get(`http://127.0.0.1:8000/converter/my_projects/${project.id}/my_classes/${myclass.id}/methods/${methods.id}/inputs/`,{});
  // }

  createMyProject(name:any):Promise<MyProject>{
    return this.post(`http://127.0.0.1:8000/converter/my_projects/`,{
      name:name
    });
  }

  createMyClass(data:any):Promise<MyClass>{
    return this.post(`http://127.0.0.1:8000/converter/my_projects/create_class/`,data);
  }

  generateCode(){
    return this.get(`http://127.0.0.1:8000/converter/generate_code/`,{})
  }
  // createMyClass(project:MyProject,name:any):Promise<MyClass>{
  //   return this.post(`http://127.0.0.1:8000/converter/my_projects/${project.id}/my_classes/`,{
  //     name:name
  //   });
  // }
  
  // createMyField(project:MyProject,myclass:MyClass,name:any):Promise<MyField>{
  //   return this.post(`http://127.0.0.1:8000/converter/my_projects/${project.id}/my_classes/${myclass.id}/fields/`,{
  //     name:name,
  //     myIdentifier:name,
  //     fieldType:name
  //   });
  // }

  // createMyMethod(project:MyProject,myclass:MyClass,name:any):Promise<MyMethod>{
  //   return this.post(`http://127.0.0.1:8000/converter/my_projects/${project.id}/my_classes/${myclass.id}/methods`,{
  //     name:name,
  //     methodIdentifier:name,
  //     methodType:name
  //   });
  // }

  // createMyInput(project:MyProject,myclass:MyClass,methods:MyMethod,name:any):Promise<MyInput>{
  //   return this.post(`http://127.0.0.1:8000/converter/my_projects/${project.id}/my_classes/${myclass.id}/methods/${methods.id}/inputs/`,{
  //     inputType:name
  //   })
  // }

  updateProject(project: MyProject): Promise<MyProject> {
    return this.put(`http://127.0.0.1:8000/converter/my_projects/`, {
      name: project.name
    });
  }

  updateClass(project:MyProject,myclass: MyClass): Promise<MyClass> {
    return this.put(`http://127.0.0.1:8000/converter/my_projects/${project.id}/my_classes/`, {
      name: myclass.name
    });
  }

  // updateMethod(project:MyProject,myclass:MyClass,method:MyMethod): Promise<MyMethod> {
  //   return this.put(`http://127.0.0.1:8000/converter/my_projects/${project.id}/my_classes/${myclass.id}/methods/`, {
  //     name: method.name,
  //     methodIdentifier:method.methodIdentifier,
  //     methodType:method.methodType
  //   });
  // }

  // updateField(project:MyProject,myclass:MyClass,field: MyField): Promise<MyField> {
  //   return this.put(`http://127.0.0.1:8000/converter/my_projects/${project.id}/my_classes/${myclass.id}/fields/`, {
  //     name: field.name,
  //     myIdentifier: field.myIdentifier,
  //     fieldType: field.fieldType
  //   });
  // }

  // updateInput(project:MyProject,myclass:MyClass,methods:MyMethod,input: MyInput): Promise<MyInput> {
  //   return this.put(`http://127.0.0.1:8000/converter/my_projects/${project.id}/my_classes/${myclass.id}/methods/${methods.id}/inputs/`, {
  //     inputType: input.inputType
  //   });
  // }

  deleteProject(id: number): Promise<any> {
    return this.delet(`http://localhost:8000/converter/my_projects/${id}/`, {});
  }

  deleteClass(project:MyProject,id: number): Promise<any> {
    return this.delet(`http://127.0.0.1:8000/converter/my_projects/${project.id}/my_classes//${id}/`, {});
  }

  // deleteField(project:MyProject,myclass:MyClass,id: number): Promise<any> {
  //   return this.delet(`http://127.0.0.1:8000/converter/my_projects/${project.id}/my_classes/${myclass.id}/fields/${id}/`, {});
  // }

  // deleteMethod(project:MyProject,myclass:MyClass,id: number): Promise<any> {
  //   return this.delet(`http://127.0.0.1:8000/converter/my_projects/${project.id}/my_classes/${myclass.id}/methods/${id}/`, {});
  // }

  // deleteInput(project:MyProject,myclass:MyClass,methods:MyMethod,id: number): Promise<any> {
  //   return this.delet(`http://127.0.0.1:8000/converter/my_projects/${project.id}/my_classes/${myclass.id}/methods/${methods.id}/inputs/${id}/`, {});
  // }
}
