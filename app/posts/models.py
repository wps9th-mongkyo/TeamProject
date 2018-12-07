from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Avg

from restaurants.models import Restaurant


class Post(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='작성자',
    )

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete = models.CASCADE,
        verbose_name='음식점',
    )
    content = models.TextField('리뷰텍스트')

    rate = models.IntegerField(
        '음식점평가',
        default=3,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        average = Post.objects.all().aggregate(Avg('rate'))
        a = Restaurant.objects.get(pk=self.restaurant.pk)
        a.rate_average = average['average__avg']
        a.save()




class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='postimage_posts',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to='post', verbose_name='이미지')
