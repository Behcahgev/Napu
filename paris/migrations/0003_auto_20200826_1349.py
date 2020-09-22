# Generated by Django 3.1 on 2020-08-26 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paris', '0002_auto_20200826_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'player',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='team',
            name='icon',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='Team_player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paris.player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paris.team')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='teams',
            field=models.ManyToManyField(related_name='_player_teams_+', through='paris.Team_player', to='paris.Team'),
        ),
    ]
