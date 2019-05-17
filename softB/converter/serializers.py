from rest_framework import serializers

from converter.models import MyClass, MyField, MyMethod, MyInput, MyProject


class MyProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProject
        fields = '__all__'


class MyFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyField
        fields = ('id', 'name', 'myIdentifier', 'fieldType', 'defaultValue', "my_class")
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
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False)
    fields = MyFieldSerializer(many=True, write_only=True, required=False)
    methods = MyMethodSerializer(many=True, write_only=True, required=False)
    # inputs = MyInputSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = MyClass
        fields = ('id', 'name', 'my_project', 'fields', 'methods', 'parent_class')

    def create(self, validated_data):
        fields = validated_data.pop('fields')
        methods = validated_data.pop('methods')
        #parent_class = validated_data.pop('parent_class')
        # inputs = validated_data.pop('inputs')
        my_class = MyClass.objects.create(**validated_data)


        for field in fields:
            field['my_class'] = my_class
            MyField.objects.create(**field)

        for method in methods:
            method['my_class'] = my_class
            MyMethod.objects.create(**method)

        return my_class


