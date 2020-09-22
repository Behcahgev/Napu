from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):

    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=500,null=True, blank=True)
    sport = models.ForeignKey('Sport',null=True, on_delete=models.SET_NULL)
    players = models.ManyToManyField('Player', through='Team_player',
                                  related_name='+')
    class Meta:
        verbose_name = "team"
        ordering = ['name']


    def __str__(self):
        return self.name

class Sport(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "sport"
        ordering = ['name']

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=200)
    teams = models.ManyToManyField(Team, through='Team_player',
                                      related_name='+')

    class Meta:
        verbose_name = 'player'
        ordering = ['name']

    def __str__(self):
        return self.name



class Team_player(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # La liaison OneToOne vers le modèle User
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    signature = models.TextField(blank=True)



    def __str__(self):
        return "Profil de {0}".format(self.user.username)
