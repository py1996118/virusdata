# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Details(models.Model):
    province = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    confirm = models.IntegerField(blank=True, null=True)
    confirm_now = models.IntegerField(blank=True, null=True)
    confirm_add = models.IntegerField(blank=True, null=True)
    heal = models.IntegerField(blank=True, null=True)
    dead = models.IntegerField(blank=True, null=True)
    tme = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'details'


class Province(models.Model):
    province = models.CharField(max_length=50, blank=True, null=True)
    confirm = models.IntegerField(blank=True, null=True)
    confirm_now = models.IntegerField(blank=True, null=True)
    confirm_add = models.IntegerField(blank=True, null=True)
    heal = models.IntegerField(blank=True, null=True)
    dead = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province'


class TotalAdd(models.Model):
    id = models.IntegerField(primary_key=True)
    confirm = models.IntegerField(blank=True, null=True)
    heal = models.IntegerField(blank=True, null=True)
    dead = models.IntegerField(blank=True, null=True)
    nowconfirm = models.IntegerField(db_column='nowConfirm', blank=True, null=True)  # Field name made lowercase.
    importcase = models.IntegerField(db_column='importCase', blank=True, null=True)  # Field name made lowercase.
    noinfect = models.IntegerField(db_column='noInfect', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'total_add'
