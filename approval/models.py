from django.db import models


class Paper(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published') #create date
    drafter = models.CharField(max_length=20) #name
    status = models.CharField(max_length=8, default='기안')

    def __str__(self):
        return self.title


class Related_person(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE) #paper id
    first = models. CharField(max_length=10) #name
    second = models.CharField(max_length=10) #name
    third = models.CharField(max_length=10) #name
    four = models.CharField(max_length=10) #name

    def __str__(self):
        response = "(" + self.paper.title + ")의 건에 관한 결재자"
        return response
