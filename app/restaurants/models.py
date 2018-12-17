from django.conf import settings
from django.db import models


class Restaurant(models.Model):
    name = models.CharField('가게이름',max_length=50)
    address = models.CharField('주소',max_length=250)
    phone_num = models.CharField('전화번호', max_length=20, blank=True)
    food_type = models.CharField('음식 종류', max_length=20, blank=True)
    price_level = models.CharField('가격대', max_length=50, blank=True)
    parking = models.CharField('주차', max_length=20, blank=True)
    Business_hour = models.TextField('영업시간', blank=True)
    break_time = models.CharField('쉬는시간', max_length=20, blank=True)
    last_order = models.CharField('마지막주문', max_length=20, blank=True)
    holiday = models.CharField('휴일', max_length=20, blank=True)
    website = models.URLField('사이트', max_length=150, blank=True)
    youtube = models.CharField('유튜브', max_length=255, blank=True)
    menu_text = models.TextField('메뉴텍스트', blank=True)
    want_togo = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='Wannago',
        symmetrical=False,
        verbose_name='가고싶다',
    )

    view_num = models.PositiveIntegerField('뷰수', default=0)
    review_num = models.PositiveIntegerField('리뷰수', default=0)
    want_num = models.PositiveIntegerField('가고싶다수', default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    latitude = models.FloatField('위도', blank=True)
    longitude = models.FloatField('경도', blank=True)

    rate_average = models.DecimalField('평점', default=0, max_digits=10, decimal_places=2)
    rate_good = models.IntegerField('맛있다', default=0)
    rate_normal = models.IntegerField('괜찮다', default=0)
    rate_bad = models.IntegerField('별로', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '음식점'
        verbose_name_plural = f'{verbose_name} 목록'
        ordering = ['pk']


class MenuImage(models.Model):
    post = models.ForeignKey(Restaurant, blank=True, on_delete=models.CASCADE, verbose_name='메뉴이미지', related_name='menuimage_res')
    image = models.ImageField(upload_to='menu', verbose_name='메뉴이미지', blank=True)


class Wannago(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateField(auto_now_add=True)
    class Meta:
        # 특정 User가 특정 restaurant를 가고싶은 정보는 Unique해야함.
        unique_together = (
            ('restaurant', 'user'),
        )
