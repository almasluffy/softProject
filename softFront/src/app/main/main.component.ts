import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { MyProject, MyClass,MyField, MyMethod, MyInput } from '../shared/models/models';
import { FormBuilder, Form, FormGroup, FormArray } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public projects:MyProject[] = [];
  public myclasses:MyClass[] = [];

  public name: any = '';
  projectId = '';
  
  private form: FormGroup;
  
  constructor(
    private provider:ProviderService, 
    private fb: FormBuilder,
    private route: ActivatedRoute,
    ) { }

  get fields():FormArray {
    return this.form.get('fields') as FormArray;
  }

  get methods(): FormArray {
    return this.form.get('methods') as FormArray;
  }

  ngOnInit() {
    // this.route.data.pipe(
    //   map(data=> {
    //     this.projectId = data[]
    //   })
    // )
    this.form = this.fb.group({
      name: [''],
      fields: this.fb.array([]),
      methods: this.fb.array([]),
    });

    this.addProps();
    this.addMethods();

  }
  
  addMethods() {
    // throw new Error("Method not implemented.");
    const tmp = {
      methodType: '',
      name: '',
      methodIdentifier: '',
    };
    this.methods.push(this.fb.group(tmp));
  }
  
  addProps() {
    
    const tmp = {
      myIdentifier: '',
      name: '',
      fieldType: '',
    };
    
    this.fields.push(this.fb.group(tmp));
  }

  generate(){
    this.provider.generateCode().then(x=>{
      console.log("hey")
    })
  }

  save() {
    console.log(this.form.value);
    const tmp = this.form.value;
    tmp['my_project'] = 1;
  //   tmp['methods'] = [
  //     {
  //         "name": "show",
  //         "methodIdentifier": "public",
  //         "methodType": "void",
  //         "inputs": [
  //             {
  //                 "inputType": "int"
  //             }
  //         ]
  //     }
  // ];
    console.log(tmp)
      this.provider.createMyClass(tmp).then(x => {
        console.log(x);
        
      });
      
  }


  getMyClass(m:MyClass){
    this.provider.getMyClass(m).then(res => {
      console.log(res);

      this.myclasses = res;
    })  
  }

  
  createProject(){
    if(this.name != ''){
      this.provider.createMyProject(this.name).then(res =>{
        this.name = '';
        this.projects.push(res);
      });
    }
  } 
}
