from django.db import models


# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    icons = models.CharField(max_length=80)
    desc = models.TextField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)


class Portfolio(models.Model):
    name = models.CharField(max_length=51, unique=True)
    slug = models.SlugField(max_length=51, unique=True, db_index=True)
    short_desc = models.CharField(max_length=100)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    project_name = models.CharField(max_length=60)
    desc = models.TextField()
    date = models.CharField(max_length=20)
    client = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='portfolios', blank=True)

    def __str__(self):
        return f'{self.name}'


class Team(models.Model):
    name = models.CharField(max_length=51, unique=True)
    slug = models.SlugField(max_length=51, unique=True, db_index=True)
    position = models.PositiveSmallIntegerField(unique=True)
    job_title = models.CharField(max_length=100, blank=True)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='teams', blank=True)
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    order = models.PositiveSmallIntegerField(unique=True)

    def get_social_link(self):
        social_link = {
            'twitter': self.twitter,
            'facebook': self.facebook,
            'linkedin': self.linkedin
        }
        return {platform: link for platform, link in social_link.items() if link}

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ('order',)
