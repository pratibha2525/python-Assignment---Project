from django.db import models
from django.utils import timezone
import math


# Create your models here.
class User(models.Model):
    email= models.EmailField(unique=True,max_length=50)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=10)
    otp = models.IntegerField(default=456)
    is_verify=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email

class Chairman(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)
    block_no = models.CharField(max_length=10,null=True)
    house_no = models.CharField(max_length=10,null=True)
    pic = models.FileField(upload_to='media/images/',default='media/default_chairman.png')
    about_me=models.TextField(null=True)

    def __str__(self) -> str:
        return self.firstname

class Member(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    email= models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=30,null=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    work = models.CharField(max_length=50,null=True)
    block_no = models.CharField(max_length=10,null=True)
    house_no = models.CharField(max_length=10,null=True)
    family_members = models.IntegerField(null=True)
    vehicle = models.IntegerField(null=True)
    contact = models.IntegerField(null=True)
    pic = models.FileField(upload_to='media/images/',default='media/default_chairman.png')
    about_member=models.TextField(null=True)

    def __str__(self):
        return self.email

class watchman(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    email=models.EmailField(max_length=50,null=True)
    password=models.CharField(max_length=30,null=True)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    contact = models.IntegerField(null=True)
    pic=models.FileField(upload_to='media/images/',default='media/default_chairman.png')
    address=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.firstname
class visitor(models.Model):
    email=models.EmailField(max_length=50,null=True)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    contact = models.IntegerField(null=True)
    Nametomeet=models.CharField(max_length=30,null=True)
    block_no = models.CharField(max_length=10,null=True)
    house_no = models.CharField(max_length=10,null=True)
    pic=models.FileField(upload_to='media/images/',default='media/default_chairman.png')
    address=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.firstname


class Notice(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    pic = models.FileField(upload_to='media/images/',null=True)
    video = models.FileField(upload_to='media/video/',null=True)
    content=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    def whenpublished(self):
        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >=0 and diff.seconds <60:
            seconds=diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"
            else:
                return str(seconds) + "seconds ago"

        if diff.days == 0 and diff.seconds >=60 and diff.seconds < 60:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + "minute ago"
            else:
                return str(minutes) + "minutes ago"
        if diff.days == 0 and diff.seconds >=3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + "hour ago"
            else:
                return str(hours) + "hours ago"

        # 1 DAY TO 30 DAYS
        if diff.days >=1 and diff.days<=30:
            days=diff.days
            if days == 1:
                return str(days) + "day ago"
            else:
                return str(days) + "days ago"
        if diff.days >=30 and diff.days<=365:
            months = math.floor(diff.days/30)
            if months == 1:
                return str(months) + "month ago"
            else:
                return str(months) + "months ago"
        if diff.days>=365:
            years=math.floor(diff.days/365)

            if years == 1:
                return str(years) + "year ago"
            else:
                return str(years) + "years ago"



class Notice_view(models.Model):
    notice_id=models.ForeignKey(Notice,on_delete=models.CASCADE)
    user_id = models.ForeignKey(Member,on_delete=models.CASCADE)
    view_at = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    pic = models.FileField(upload_to='media/images/',null=True)
    video = models.FileField(upload_to='media/video/',null=True)
    content=models.CharField(max_length=200)
    venue=models.CharField(max_length=30)
    Date=models.DateField(null=True)
    Time=models.TimeField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    def whenpublished(self):
        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >=0 and diff.seconds <60:
            seconds=diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"
            else:
                return str(seconds) + "seconds ago"

        if diff.days == 0 and diff.seconds >=60 and diff.seconds < 60:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + "minute ago"
            else:
                return str(minutes) + "minutes ago"
        if diff.days == 0 and diff.seconds >=3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + "hour ago"
            else:
                return str(hours) + "hours ago"

        # 1 DAY TO 30 DAYS
        if diff.days >=1 and diff.days<=30:
            days=diff.days
            if days == 1:
                return str(days) + "day ago"
            else:
                return str(days) + "days ago"
        if diff.days >=30 and diff.days<=365:
            months = math.floor(diff.days/30)
            if months == 1:
                return str(months) + "month ago"
            else:
                return str(months) + "months ago"
        if diff.days>=365:
            years=math.floor(diff.days/365)

            if years == 1:
                return str(years) + "year ago"
            else:
                return str(years) + "years ago"



