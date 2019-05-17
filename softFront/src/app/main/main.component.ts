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
  public classList:MyClass[] = [];

  public name: any = '';
  projectId = '';
  public showed: boolean = false;

  public parent: number;
  public child: number;
  
  private form: FormGroup;

  public s_class: string;
  public s_parent: string;
  public s_fields: MyField[] = [];
  public s_methods: MyMethod[] = [];
  
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

    this.provider.getListOfClass().then(x=>{
      this.classList = x;
    })
     
    this.form = this.fb.group({
      name: [''],
      fields: this.fb.array([]),
      methods: this.fb.array([]),
    });

    this.addProps();
    this.addMethods();

  }

  show(myC: MyClass){
    this.s_class = myC.name;
    if(myC.parent_class == -1){
      this.s_parent = "have no Parent"
    }
    for(let cc of this.classList){
      if(myC.parent_class == cc.id){
        this.s_parent = cc.name;
      }
    }

    
    this.provider.getFields(myC.id).then(r2=>{
       this.s_fields = r2;
    });
    this.provider.getMethods(myC.id).then(r3=>{
      this.s_methods = r3;
    });
    this.showed = true;
  }

  doExtends(){
    this.provider.doExtends(this.parent, this.child).then(res=>{
      console.log("Extends is working");
    });
    this.updatePage();
  
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
      defaultValue: '',
    };
    
    this.fields.push(this.fb.group(tmp));
  }

  generate(){
    this.provider.generateCode().then(x=>{
      console.log("Your code generated to Java Code")
    })
  }

  makeParent(){
    this.provider.makeParent(this.parent, this.child).then(r=>{
      console.log("extends is working");
    });
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
        
        this.provider.getListOfClass().then(res=>{
          this.classList = res;
        });
      });

      
  }



  updatePage(): void {
    window.location.reload();
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
