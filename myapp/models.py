from django.contrib.auth.models import User
from django.db import models

class Insert_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    english = models.CharField(max_length=50)
    kanji = models.CharField(max_length=50)
    hiragana = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.english}, {self.kanji}'
