from django.db import models

class Bank(models.Model):
    name=models.CharField(max_length=149)
    bank_id=models.IntegerField(primary_key=True,default='0')
    def __str__(self):
        return self.name

class Branch(models.Model):
    ifsc=models.CharField(max_length=50,primary_key=True)
    bank_id=models.IntegerField(default='0')
    branch=models.CharField(max_length=74)
    address=models.CharField(max_length=195)
    city=models.CharField(max_length=150)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=26)
    bank_name=models.CharField(max_length=149,default='')

    def __str__(self):
        return self.ifsc