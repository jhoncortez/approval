from django.db import models
from datetime import datetime
import sys
from os import path


# Fix Model Import Error
if __name__ == '__main__':
    if __package__ is None:
        sys.path.append(path.dirname(path.dirname( path.abspath(__file__))))
        from ..member.models import User
    else:
        from ..member.models import User


class Docs(models.Model):
    # Basic Information
    title = models.CharField(max_length=30)

    # Other Informations
    pub_date = models.DateTimeField('date published', default=datetime.now)
    score = models.CharField(max_length=1, default='0')

    # output
    def __str__(self):
        response = self.title + "(" + self.score + ")"
        return response


class Docs_advanced(models.Model):
    # Basic Information
    docs_id = models.ForeignKey(Docs, on_delete=models.PROTECT)
    drafter = models.ForeignKey(User, on_delete=models.PROTECT)

    # Signed Information
    stf1 = models.ForeignKey(User, on_delete=models.PROTECT)
    stf1_date = models.DateTimeField('date signed', related_name='first_date')

    stf2 = models.ForeignKey(User, on_delete=models.PROTECT)
    stf2_date = models.DateTimeField('date signed', related_name='second_date')

    stf3 = models.ForeignKey(User, on_delete=models.PROTECT)
    stf3_date = models.DateTimeField('date signed', related_name='third_date')

    # Other Informations
    reason = models.CharField(max_length=50)
    status = models.CharField(max_length=5, default='기안')

    # output
    def __str__(self):
        response = self.drafter + "(" + self.status + ")"
        return response
