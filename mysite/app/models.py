from django.db import models

# Create your models here.

class TbAdmin(models.Model):
    user_id = models.CharField(primary_key=True, max_length=45)
    user_pw = models.CharField(max_length=45, blank=True, null=True)
    branch = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_admin'