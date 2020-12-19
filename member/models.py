from django.db import models


class User(models.Model):
    # personal information
    nickname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # login information
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    # find password information


    # other informations
    joined_date = models.DateTimeField('date joined')

    def __str__(self):
        response = self.nickname + "의 회원가입 정보"
        return response


