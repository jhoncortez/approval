from django.db import models
from datetime import datetime

class User(models.Model):
    # personal information
    nickname = models.CharField(max_length=30)
    first_name = models.CharField(max_length=5)
    last_name = models.CharField(max_length=5)

    # login information
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

    # find password information


    # other informations
    joined_date = models.DateTimeField('date joined', default=datetime.now)
    is_active = models.CharField(max_length=1, default='1')

    # output
    def __str__(self):
        response = self.nickname
        return response


class AuthInfo(models.Model):
    # basic information
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)

    #other informations
    created_date = models.DateTimeField('date created', default=datetime.now)
    is_valid = models.CharField(max_length=1, default='1')

    # output
    def __str__(self):
        response = self.name + "(" + self.is_valid + ")"
        return response


class UserAuth(models.Model):
    # basic information
    UserId = models.ForeignKey(User, on_delete=models.PROTECT, related_name='isGivenName')
    AuthId = models.ForeignKey(AuthInfo, on_delete=models.PROTECT)

    # authorization information
    authorization = models.ForeignKey(User, on_delete=models.PROTECT, related_name='givenName')

    # ohter informations
    given_date = models.DateTimeField('date given', default=datetime.now)
    modified_date = models.DateTimeField('date modified', default=datetime.now)
    is_valid = models.CharField(max_length=1, default='1')

    # output
    def __str__(self):
        response = self.UserId + "(" + self.AuthId + ")"
        return response