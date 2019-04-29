from rest_framework import serializers

from converter.models import MyClass, MyField, MyMethod, MyInput, MyProject


class MyProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProject
        fields = '__all__'


class MyFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyField
        fields = ('id', 'name', 'myIdentifier', 'fieldType', "my_class")
class MyMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyMethod
        fields = ('id', 'name', 'methodIdentifier', 'methodType', 'my_class')


class MyInputSerializer(serializers.ModelSerializer):
    my_method = MyMethodSerializer(required=False)

    class Meta:
        model = MyInput
        fields = ('id', 'inputType', 'my_method')

class MyClassSerializer(serializers.ModelSerializer):
    fields = MyFieldSerializer(many=True, write_only=True)
    methods = MyMethodSerializer(many=True, write_only=True)
    # inputs = MyInputSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = MyClass
        fields = ('id', 'name', 'my_project', 'fields', 'methods')

    def create(self, validated_data):
        fields = validated_data.pop('fields')
        methods = validated_data.pop('methods')
        # inputs = validated_data.pop('inputs')
        my_class = MyClass.objects.create(**validated_data)


        for field in fields:
            field['my_class'] = my_class
            MyField.objects.create(**field)

        for method in methods:
            method['my_class'] = my_class
            MyMethod.objects.create(**method)

        return my_class


