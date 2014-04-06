from django.db import models

class Major(models.Model):
    major_text = models.CharField(max_length=100)
    major_id = models.CharField(max_length=30)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.major_text

class Requirements(models.Model):
    major = models.ForeignKey(Major)
    num = models.CharField(max_length=30)
    distribution = models.CharField(max_length=100)


class Courses1(models.Model):
    major_connect = models.ForeignKey(Major)
    major = models.CharField(max_length=30)
    course_text = models.CharField(max_length=30)
    requirement = models.CharField(max_length=30)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.course_text

class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class UserClasses(models.Model):
    user = models.ForeignKey(Users)
    course = models.CharField(max_length=30)

class FallCourse(models.Model):
    area = models.CharField(max_length=30)
    num = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    descript = models.CharField(max_length=500)
    dist = models.CharField(max_length=30)
    days = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    max = models.CharField(max_length=30)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title
