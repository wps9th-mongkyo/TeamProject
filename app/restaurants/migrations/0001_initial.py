# Generated by Django 2.1.3 on 2018-11-27 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_text', models.TextField(blank=True, verbose_name='메뉴텍스트')),
            ],
        ),
        migrations.CreateModel(
            name='MenuImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='menu', verbose_name='메뉴이미지')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='restaurants.Menu', verbose_name='메뉴이미지')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='가게이름')),
                ('address', models.CharField(max_length=100, verbose_name='주소')),
                ('address_detail', models.CharField(max_length=100, unique=True, verbose_name='상세주소')),
                ('phone_num', models.CharField(max_length=20, verbose_name='전화번호')),
                ('food_type', models.CharField(blank=True, max_length=20, verbose_name='음식 종류')),
                ('price_level', models.CharField(blank=True, max_length=50, verbose_name='가격대')),
                ('parking', models.CharField(blank=True, max_length=20, verbose_name='주차')),
                ('Business_hour', models.TextField(blank=True, verbose_name='영업시간')),
                ('break_time', models.CharField(blank=True, max_length=20, verbose_name='쉬는시간')),
                ('last_order', models.CharField(blank=True, max_length=20, verbose_name='마지막주문')),
                ('holiday', models.CharField(blank=True, max_length=20, verbose_name='휴일')),
                ('website', models.URLField(blank=True, max_length=150, verbose_name='사이트')),
                ('view_num', models.PositiveIntegerField(default=0, verbose_name='뷰수')),
                ('review_num', models.PositiveIntegerField(default=0, verbose_name='리뷰수')),
                ('want_num', models.PositiveIntegerField(default=0, verbose_name='가고싶다수')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('latitude', models.FloatField(verbose_name='위도')),
                ('longitude', models.FloatField(verbose_name='경도')),
            ],
        ),
        migrations.CreateModel(
            name='Wannago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('Restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='want_togo',
            field=models.ManyToManyField(through='restaurants.Wannago', to=settings.AUTH_USER_MODEL, verbose_name='가고싶다'),
        ),
        migrations.AddField(
            model_name='menu',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant', verbose_name='가게이름'),
        ),
    ]
