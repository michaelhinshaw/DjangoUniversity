from django.db import models

# Create your models here.
class djangoClasses(models.Model):
    title = models.CharField(max_length=50)
    course_number = models.IntegerField(default="", blank=True, null=False)
    instructor_name = models.CharField(max_length=50, default="", blank=True, null=False)
    duration = models.FloatField(max_length=6, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.title