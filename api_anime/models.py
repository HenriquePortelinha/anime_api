from django.db import models


class Anime(models.Model):
    id_anime = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    image_url = models.URLField()
    score = models.FloatField()
    episodes = models.IntegerField()
    synopsis = models.TextField()
    type = models.CharField(max_length=100)
    release_date = models.DateField()
    rank = models.IntegerField()
    members = models.IntegerField()
    url = models.URLField()
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id_anime']
        verbose_name_plural = 'animes'
        verbose_name = 'anime'
        db_table = 'anime'
        indexes = [
            
            models.Index(fields=['id_anime']),
            models.Index(fields=['title']),
            models.Index(fields=['image_url']),
            models.Index(fields=['score']),
            models.Index(fields=['episodes']),
            models.Index(fields=['synopsis']),
            models.Index(fields=['type']),
            models.Index(fields=['release_date']),
            models.Index(fields=['rank']),
            models.Index(fields=['members']),
            models.Index(fields=['url']),
        ]
        
        
class Character(models.Model):
    id_character = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id_character']
        verbose_name_plural = 'characters'
        verbose_name = 'character'
        db_table = 'character'
        indexes = [
            models.Index(fields=['id_character']),
            models.Index(fields=['name']),
            models.Index(fields=['id_character', 'name'], name='character_indices'),
        ]
        
class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    favorite_anime = models.ManyToManyField(Anime)

    def __str__(self):
        return self.username