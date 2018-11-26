from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='작성자',
    )
    context = models.TextField('리뷰텍스트')

    rate = models.PositiveIntegerField(
        '음식점평가',
        default=3,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class PostImages(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post', verbose_name='이미지')
