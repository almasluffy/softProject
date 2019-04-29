from django.contrib import admin
from converter.models import MyClass, MyField, MyMethod, MyInput,MyProject

admin.site.register(MyClass)
admin.site.register(MyMethod)
admin.site.register(MyField)
admin.site.register(MyInput)
admin.site.register(MyProject)

