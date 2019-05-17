from django.shortcuts import render
import json
import os
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from converter.models import MyClass, MyField, MyMethod, MyInput, MyProject
from django.views.decorators.csrf import csrf_exempt
from converter.serializers import MyClassSerializer, MyFieldSerializer, MyMethodSerializer, MyInputSerializer, \
     MyProjectSerializer


@api_view(['POST'])
def create_class(request):
    serializer = MyClassSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def test(request):
    serializer = MyProjectSerializer(data=request.data)
    print(serializer.data)
    # return Response(serializer.data, status=status.HTTP_201_CREATED)

@csrf_exempt
def makeParent(request, pk):
    try:
        my_class = MyClass.objects.get(id=pk)
    except MyClass.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == "GET":
        serializer = MyClassSerializer(my_class)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = json.loads(request.body)
        serializer = MyClassSerializer(instance=my_class, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    elif request.method == "DELETE":
        my_class.delete()
        return JsonResponse({})




@csrf_exempt
def extends(request, id1, id2):
    if request.method == "GET":

        #Parent Class
        parent_class = MyClass.objects.get(id=id1)
        child_class = MyClass.objects.get(id=id2)
        p_class = MyClassSerializer(parent_class)
        p_class2 = json.dumps(p_class.data)
        p_class3 = json.loads(p_class2)


        #Child Class
        c_class = MyClassSerializer(child_class)
        c_class2 = json.dumps(c_class.data)
        c_class3 = json.loads(c_class2)


        pathh = r'C:\Users\Алмас\Desktop\generatedCode' + '\\' + c_class3['name'] + '.java'
        with open(pathh, 'w+') as f:
            f.write(c_class3['name'] + ' extends '  + p_class3['name'])
    return JsonResponse({})




@csrf_exempt
def generate_code(request):
    if request.method == "GET":
        my_project_list = MyProject.objects.get(id=1)
        my_classes = MyClass.objects.all()
        my_fields = MyField.objects.all()
        my_methods = MyMethod.objects.all()

        my_c = MyClassSerializer(my_classes, many=True)
        my_c2 = json.dumps(my_c.data)
        my_c3 = json.loads(my_c2)

        my_f = MyFieldSerializer(my_fields, many=True)
        my_f2 = json.dumps(my_f.data)
        my_f3 = json.loads(my_f2)

        my_m = MyMethodSerializer(my_methods, many=True)
        my_m2 = json.dumps(my_m.data)
        my_m3 = json.loads(my_m2)
        for x in my_c3:
            pathh = r'C:\Users\Алмас\Desktop\generatedCode' + '\\' + x['name'] + '.java'
            if x['parent_class'] != -1:
                with open(pathh, 'w+') as f:
                    for g in my_c3:
                        if x['parent_class'] == g['id']:
                            f.write('public class ' + x['name'] + ' extends ' + g['name'] + '{\n')
                for y in my_f3:
                    if x['id'] == y['my_class']:
                        if y['fieldType'] == "String":
                            with open(pathh, 'a+') as f:
                                f.write(
                                    '\t' + y['myIdentifier'] + ' ' + y['fieldType'] + ' ' + y['name'] + " = " + "'" + y[
                                        'defaultValue'] + "'" + ';\n')

                        else:
                            with open(pathh, 'a+') as f:
                                f.write('\t' + y['myIdentifier'] + ' ' + y['fieldType'] + ' ' + y['name'] + " = " + y[
                                    'defaultValue'] + ';\n')

                with open(pathh, 'a+') as f:
                    f.write('\tpublic ' + x['name'] + '(')
                for h in my_c3:
                    if h['id'] == x['parent_class']:
                        for i in my_f3:
                            if i['my_class'] == h['id']:
                                with open(pathh, 'a+') as f:
                                    f.write(i['fieldType'] + ' ' + i['name'] + ',')


                for y in my_f3:
                    if x['id'] == y['my_class']:
                        with open(pathh, 'a+') as f:
                            f.write(y['fieldType'] + ' ' + y['name'] + ',')
                with open(pathh, 'rb+') as f:
                    f.seek(-1, os.SEEK_END)
                    f.truncate()
                with open(pathh, 'a+') as f:
                    f.write('){\n')

                #####SUPER EXTENDS
                for t in my_c3:
                    if x['parent_class'] == t['id']:
                        with open(pathh, 'a+') as f:
                            f.write('\t\tsuper(')
                            for j in my_f3:
                                if j['my_class'] == t['id']:
                                    f.write(j['name'] + ',')
                        with open(pathh, 'rb+') as f:
                            f.seek(-1, os.SEEK_END)
                            f.truncate()
                        with open(pathh, 'a+') as f:
                            f.write(');\n')





                for y in my_f3:
                    if x['id'] == y['my_class']:
                        with open(pathh, 'a+') as f:
                            f.write('\t\tthis.' + y['name'] + ' = ' + y['name'] + ';\n')


                with open(pathh, 'a+') as f:
                    f.write('\t}\n\n\n')
                with open(pathh, 'a+') as f:
                    f.write('\tpublic ' + x['name'] + '(){\n\t}\n\n')

                for y in my_f3:
                    if x['id'] == y['my_class']:
                        with open(pathh, 'a+') as f:
                            f.write(
                                '\tpublic ' + y['fieldType'] + ' get' + y['name'][0].upper() + y['name'][1:] + '(){\n')
                            f.write('\t\treturn this.' + y['name'] + ';\n\t}\n\n')

                for y in my_f3:
                    if x['id'] == y['my_class']:
                        with open(pathh, 'a+') as f:
                            f.write('\tpublic ' + y['fieldType'] + ' set' + y['name'][0].upper() + y['name'][1:] + '(')
                            f.write(y['fieldType'] + ' ' + y['name'] + '){\n')
                            f.write('\t\tthis.' + y['name'] + ' = ' + y['name'] + ';\n\t}\n\n')

                for y in my_m3:
                    if x['id'] == y['my_class']:
                        with open(pathh, 'a+') as f:
                            f.write(
                                '\t' + y['methodIdentifier'] + ' ' + y['methodType'] + ' ' + y['name'] + '(){\n\t}\n\n')

                with open(pathh, 'a+') as f:
                    f.write('\t//toString method for every class\n\tpublic ' + 'String toString(){\n\t\treturn "";\n\t}\n\n')
                for o in my_c3:
                    if x['parent_class'] == o['id']:
                        for p in my_m3:
                            if p['my_class'] == o['id']:
                                with open(pathh, 'a+') as f:
                                    f.write('\t@Override\n')
                                    f.write(
                                        '\t' + p['methodIdentifier'] + ' ' + p['methodType'] + ' ' + p[
                                            'name'] + '(){\n\t}\n\n')
                with open(pathh, 'a+') as f:
                    f.write('}\n')



            else:
                with open(pathh, 'w+') as f:
                    f.write('public class ' + x['name'] + '{\n')
                for y in my_f3:
                    if x['id'] == y['my_class']:
                        if y['fieldType'] == "String":
                            with open(pathh, 'a+') as f:
                                f.write(
                                    '\t' + y['myIdentifier'] + ' ' + y['fieldType'] + ' ' + y['name'] + " = " + "'" + y[
                                        'defaultValue'] + "'" + ';\n')

                        else:
                            with open(pathh, 'a+') as f:
                                f.write('\t' + y['myIdentifier'] + ' ' + y['fieldType'] + ' ' + y['name'] + " = " + y[
                                    'defaultValue'] + ';\n')

                with open(pathh, 'a+') as f:
                    f.write('\tpublic ' + x['name'] + '(')
                for y in my_f3:
                    if x['id'] == y['my_class']:
                        with open(pathh, 'a+') as f:
                            f.write(y['fieldType'] + ' ' + y['name'] + ',')
                with open(pathh, 'rb+') as f:
                    f.seek(-1, os.SEEK_END)
                    f.truncate()
                with open(pathh, 'a+') as f:
                    f.write('){\n')
                for y in my_f3:
                    if x['id'] == y['my_class']:
                        with open(pathh, 'a+') as f:
                            f.write('\t\tthis.' + y['name'] + ' = ' + y['name'] + ';\n')
                with open(pathh, 'a+') as f:
                    f.write('\t}\n\n\n')
                with open(pathh, 'a+') as f:
                    f.write('\tpublic ' + x['name'] + '(){\n\t}\n\n')

                for y in my_f3:
                    if x['id'] == y['my_class']:
                        with open(pathh, 'a+') as f:
                            f.write(
                                '\tpublic ' + y['fieldType'] + ' get' + y['name'][0].upper() + y['name'][1:] + '(){\n')
                            f.write('\t\treturn this.' + y['name'] + ';\n\t}\n\n')

                for y in my_f3:
                    if x['id'] == y['my_class']:
                        with open(pathh, 'a+') as f:
                            f.write('\tpublic ' + y['fieldType'] + ' set' + y['name'][0].upper() + y['name'][1:] + '(')
                            f.write(y['fieldType'] + ' ' + y['name'] + '){\n')
                            f.write('\t\tthis.' + y['name'] + ' = ' + y['name'] + ';\n\t}\n\n')

                for y in my_m3:
                    if x['id'] == y['my_class']:
                        with open(pathh, 'a+') as f:
                            f.write(
                                '\t' + y['methodIdentifier'] + ' ' + y['methodType'] + ' ' + y['name'] + '(){\n\t}\n\n')
                with open(pathh, 'a+') as f:
                    f.write('}\n')




        return HttpResponse({})





@csrf_exempt
def project_list(request):
    if request.method == "GET":
        my_project_list = MyProject.objects.all()
        serializer = MyProjectSerializer(my_project_list, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = MyProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # create function in serializer class
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)


@csrf_exempt
def project_list_detail(request, pk):
    try:
        my_project_list = MyProject.objects.get(id=pk)
    except MyProject.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == "GET":
        serializer = MyProjectSerializer(my_project_list)
        d = json.loads(serializer.data)
        print(d)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == "PUT":
        data = json.loads(request.body)
        serializer = MyProjectSerializer(instance=my_project_list, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    elif request.method == "DELETE":
        my_project_list.delete()
        return JsonResponse({})


@csrf_exempt
def class_list(request, pk):
    try:
        my_project_list = MyProject.objects.get(id=pk)
    except MyClass.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)

    if request.method == "GET":
        my_fields = my_project_list.myclass_set.all()
        serializer = MyClassSerializer(my_fields, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = MyClassSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # create function in serializer class
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)


@csrf_exempt
def class_list_detail(request, pk, pk1):
    try:
        my_class_list = MyClass.objects.get(id=pk1)
    except MyClass.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == "GET":
        serializer = MyClassSerializer(my_class_list)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = json.loads(request.body)
        serializer = MyClassSerializer(instance=my_class_list, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    elif request.method == "DELETE":
        my_class_list.delete()
        return JsonResponse({})


@csrf_exempt
def class_fields(request,pk):
    try:
        my_class_list = MyClass.objects.get(id=pk)
    except MyClass.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)
    if request.method == "GET":
        my_fields = my_class_list.myfield_set.all()
        serializer = MyFieldSerializer(my_fields, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = MyFieldSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # create function in serializer class
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

@csrf_exempt
def getFields(request,pk):
    try:
        my_class_list = MyClass.objects.get(id=pk)
    except MyClass.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)
    if request.method == "GET":
        my_fields = my_class_list.myfield_set.all()
        serializer = MyFieldSerializer(my_fields, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = MyFieldSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # create function in serializer class
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)


@csrf_exempt
def class_fields_detail(request, pk, pk1, pk2):
    try:
        my_field = MyField.objects.get(id=pk2)
    except MyClass.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)
    if request.method == "GET":
        serializer = MyFieldSerializer(my_field)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = json.loads(request.body)
        serializer = MyFieldSerializer(instance=my_field, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    elif request.method == "DELETE":
        my_field.delete()
        return JsonResponse({})

@csrf_exempt
def class_methods(request, pk):
    try:
        my_class_list = MyClass.objects.get(id=pk)
    except MyClass.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)
    if request.method == "GET":
        my_methods = my_class_list.mymethod_set.all()
        serializer = MyMethodSerializer(my_methods, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = MyMethodSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # create function in serializer class
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

@csrf_exempt
def getMethods(request, pk):
    try:
        my_class_list = MyClass.objects.get(id=pk)
    except MyClass.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)
    if request.method == "GET":
        my_methods = my_class_list.mymethod_set.all()
        serializer = MyMethodSerializer(my_methods, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = MyMethodSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # create function in serializer class
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)


@csrf_exempt
def class_methods_detail(request, pk, pk1, pk2):
    try:
        my_method = MyMethod.objects.get(id=pk2)
    except MyClass.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)
    if request.method == "GET":
        serializer = MyMethodSerializer(my_method)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = json.loads(request.body)
        serializer = MyMethodSerializer(instance=my_method, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    elif request.method == "DELETE":
        my_method.delete()
        return JsonResponse({})


@csrf_exempt
def method_inputs(request, pk, pk1, pk2):
    try:
        my_methods = MyMethod.objects.get(id=pk2)
    except MyClass.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)
    except MyMethod.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)
    if request.method == "GET":
        my_inputs = my_methods.myinput_set.all()
        serializer = MyInputSerializer(my_inputs, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = MyInputSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # create function in serializer class
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)


@csrf_exempt
def method_inputs_detail(request, pk, pk1, pk2, pk3):
    try:
        my_input = MyInput.objects.get(id=pk3)
    except MyClass.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)
    except MyMethod.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)
    if request.method == "GET":
        serializer = MyInputSerializer(my_input)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = json.loads(request.body)
        serializer = MyInputSerializer(instance=my_input, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    elif request.method == "DELETE":
        my_input.delete()
        return JsonResponse({})
