# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Movies(models.Model):
    
    title = models.CharField(max_length=255, blank=True, null=True)
    genres = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'


class Ratings(models.Model):
    userid = models.IntegerField()
    movie_id = models.IntegerField()
    rating = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    rated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ratings'


class Tags(models.Model):
    userid = models.ForeignKey(Ratings, models.DO_NOTHING, db_column='userid')
    movie_id = models.IntegerField()
    tag = models.CharField(max_length=255, blank=True, null=True)
    rated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'
