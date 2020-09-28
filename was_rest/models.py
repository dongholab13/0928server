from django.db import models
from datetime import datetime
# Create your models here.
class MediaFile(models.Model):
    name = models.CharField(max_length = 1000, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        super(MediaFile, self).save(*args, **kwargs)
        print('[TIME : %s] MediaFile save' % str(datetime.now()))

    def delete(self, *args, **kwargs):
        super(MediaFile, self).delete(*args, **kwargs)
        print('[TIME : %s] MediaFile delete' % str(datetime.now()))  

class Stream_1(models.Model):
    name = models.CharField(max_length = 10000, blank=True, null=True)
    file_list = models.CharField(max_length = 10000, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        super(Stream_1, self).save(*args, **kwargs)
        print('[TIME : %s] Stream_1 save' % str(datetime.now()))

    def delete(self, *args, **kwargs):
        super(Stream_1, self).delete(*args, **kwargs)
        print('[TIME : %s] Stream_1 delete' % str(datetime.now())) 

class Stream_trajectory(models.Model):
    name = models.CharField(max_length = 10000, blank=True, null=True)
    file_list = models.CharField(max_length = 10000, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        super(Stream_trajectory, self).save(*args, **kwargs)
        print('[TIME : %s] Stream_trajectory save' % str(datetime.now()))

    def delete(self, *args, **kwargs):
        super(Stream_trajectory, self).delete(*args, **kwargs)
        print('[TIME : %s] Stream_trajectory delete' % str(datetime.now()))  
