import uuid
from django.db import models


class PartModels(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    photo = models.ImageField(verbose_name='Rasmi', upload_to='part_photos/')
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    caption = models.TextField(verbose_name="Izoh")
    movie = models.ForeignKey('MovieModels', on_delete=models.CASCADE, related_name='part', verbose_name="Kino")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.movie.title} {self.title}"

    class Meta:
        verbose_name = "Kino qismi"
        verbose_name_plural = "Kino qismlari"


class SeasonModels(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    photo = models.ImageField(upload_to='season_photos/', verbose_name="Rasmi")
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    caption = models.TextField(verbose_name="Izoh")
    season = models.ForeignKey(PartModels, on_delete=models.CASCADE, related_name='season', verbose_name="Fasl")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kino fasli"
        verbose_name_plural = "Kino fasllari"


class MovieModels(models.Model):
    Categories = (
        ('films', 'films'),
        ('series', 'series'),
        ('animes', 'animes'),
        ('primieras', 'primieras'),
    )
    file_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    caption = models.TextField(verbose_name="Izoh")
    photo = models.ImageField(max_length=255, null=True, blank=True, upload_to='kino_photos/', verbose_name="Rasmi")
    category = models.CharField(max_length=25, choices=Categories, default='primieras', verbose_name="Kategoriyasi")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    key = models.CharField(max_length=255, unique=True, null=True, blank=True, verbose_name="Kalit/Kod")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.key} {self.title}"

    class Meta:
        verbose_name = "Kino"
        verbose_name_plural = "Kinolar"
