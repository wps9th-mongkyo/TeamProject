from django.conf import settings
from django.db import models


class Restaurant(models.Model):
    name = models.CharField('가게이름',max_length=50)
    address = models.CharField('주소',max_length=100)
    address_detail = models.CharField('상세주소',max_length=100, unique=True)
    phone_num = models.CharField('전화번호', max_length=12)
    food_type = models.CharField('음식 종류', max_length=20, blank=True)
    price_level = models.CharField('가격대', max_length=50, blank=True)
    parking = models.CharField('주차', max_length=20, blank=True)
    Business_hour = models.TextField('영업시간', blank=True)
    break_time = models.CharField('쉬는시간', max_length=20, blank=True)
    last_order = models.CharField('마지막주문', max_length=20, blank=True)
    holiday = models.CharField('휴일', max_length=20, blank=True)
    website = models.URLField('사이트', max_length=150, blank=True)

    want_togo = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='Wannago',
        symmetrical=False,
        verbose_name = '가고싶다',
    )

    view_num = models.PositiveIntegerField('뷰수', default=0)
    review_num = models.PositiveIntegerField('리뷰수', default=0)
    want_num = models.PositiveIntegerField('가고싶다수', default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    gps_location = models.CharField('GPS', max_length=50, blank=True)


class Menu(models.Model):
    name = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='가게이름')
    menu_text = models.TextField('메뉴텍스트', blank=True)


class MenuImages(models.Model):
    post = models.ForeignKey(Menu, default=None, on_delete=models.CASCADE, verbose_name='메뉴이미지')
    image = models.ImageField(upload_to='menu', verbose_name='메뉴이미지', blank=True)


class Wannago(models.Model):
    Restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
    )
    User = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateField(auto_now_add=True)