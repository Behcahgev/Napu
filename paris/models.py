from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils import timezone

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
    avatar = models.ImageField(null=True, blank=True, default='paris/static/paris/images/avatars/default.png', upload_to="paris/static/paris/images/avatars/")
    signature = models.TextField(blank=True)

    rooms = models.ManyToManyField('BetRoom', through='BetRoom_Profile',
                                          related_name='+')

    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return "Profil de {0}".format(self.user.username)


class BetRoom(models.Model):
    name = models.CharField(max_length=200, blank=True)
    creator = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)

    public = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)

    users = models.ManyToManyField('Profile', through='BetRoom_Profile',
                                          related_name='+')


    def __str__(self):
        return "Bet Room n°{0}".format(self.id)


class BetRoom_Profile(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    BetRoom = models.ForeignKey(BetRoom, on_delete = models.CASCADE)

    ADMINISTRATOR = 'AD'
    PARTICIPANT = 'P'

    ROLE_CHOICES = [
        (ADMINISTRATOR, 'Administrator'),
        (PARTICIPANT, 'Participant')
    ]

    role = models.CharField(
        max_length=2,
        choices=ROLE_CHOICES,
        default=PARTICIPANT,
    )
