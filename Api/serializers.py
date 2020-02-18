from rest_framework import serializers
from .models import Bank,Branch

class Bankserializers(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('name','bank_id')


class Branchesserializers(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('ifsc','bank_id','branch','address','city','district','state','bank_name')
