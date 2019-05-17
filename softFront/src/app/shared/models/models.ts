export interface MyProject{
    id:number;
    name:string;
}

export interface MyClass{
    id:number;
    name:string;
    prop:MyField[];
    methods:MyMethod[];
    parent_class: number;
}

export interface MyField{
    id:number;
    name:string;
    myIdentifier:string;
    fieldType:string;
    defaultValue: string;
}

export interface MyMethod{
    id:number;
    name:string;
    methodIdentifier:string;
    methodType:string;
}

export interface MyInput{
    id:number;
    inputType:string;
}
