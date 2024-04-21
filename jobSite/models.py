from django.db import models


# Create your models here.
def user_directory_path(instance, filename):
    return '{0}/{1}'.format("job_photos",filename)

class job_data(models.Model):
    job_Id = models.AutoField(primary_key=True)
    job_name = models.CharField(max_length=100,blank=False, null=False )
    job_title = models.CharField(max_length=100,blank=False, null=False )
    job_desc = models.CharField(max_length=255, blank=False, null=False)
    job_photo = models.ImageField(upload_to=user_directory_path, null = True, blank = True, verbose_name="")

    class Meta:
        db_table = 'jobs'