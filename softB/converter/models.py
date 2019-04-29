from django.db import models


class MyProject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class MyClass(models.Model):
    name = models.CharField(max_length=200)

    my_project = models.ForeignKey(MyProject, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class MyField(models.Model):
    name = models.CharField(max_length=200)
    myIdentifier = models.CharField(max_length=200)
    fieldType = models.CharField(max_length=200)

    # my_class = models.ForeignKey(MyClass, on_delete=models.CASCADE)

    my_class = models.ForeignKey(MyClass, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'myIdentifier': self.myIdentifier,
            'fieldType': self.fieldType
        }


class MyMethod(models.Model):
    name = models.CharField(max_length=200)
    methodIdentifier = models.CharField(max_length=200)
    methodType = models.CharField(max_length=200)

    # my_class = models.ForeignKey(MyClass, on_delete=models.CASCADE)

    my_class = models.ForeignKey(MyClass, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'methodIdentifier': self.methodIdentifier,
            'methodType': self.methodType
        }


class MyInput(models.Model):
    inputType = models.CharField(max_length=200)

    my_method = models.ForeignKey(MyMethod, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.inputType)

    def to_json(self):
        return {
            'id': self.id,
            'inputType': self.inputType
        }
