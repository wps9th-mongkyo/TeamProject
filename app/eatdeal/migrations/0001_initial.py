# Generated by Django 2.1.4 on 2018-12-07 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eatdeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_name', models.CharField(max_length=50, verbose_name='가게이름')),
                ('deal_name', models.CharField(max_length=100, verbose_name='주소')),
                ('start_date', models.DateField(auto_now_add=True, verbose_name='시작일자')),
                ('end_date', models.DateField(auto_now_add=True, verbose_name='종료일자')),
                ('base_price', models.PositiveIntegerField(default=0, verbose_name='기본가격')),
                ('discount_rate', models.PositiveIntegerField(default=0, verbose_name='할인율')),
                ('discount_price', models.PositiveIntegerField(default=0, verbose_name='할인가격')),
                ('introduce_res', models.TextField(max_length=255, verbose_name='식당소개')),
                ('introduce_menu', models.TextField(max_length=255, verbose_name='메뉴소개')),
                ('_caution', models.TextField(blank=True, max_length=255, verbose_name='유의사항')),
                ('_how_to_use', models.TextField(blank=True, max_length=255, verbose_name='사용 방법')),
                ('_refund', models.TextField(blank=True, max_length=255, verbose_name='환불규정')),
                ('_inquiry', models.EmailField(blank=True, max_length=100, verbose_name='문의메일')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='회원가입날짜')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='수정날짜')),
            ],
        ),
        migrations.CreateModel(
            name='EatdealImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='eatdeal', verbose_name='Eatdeal 이미지')),
                ('eatdeal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eatdealimages', to='eatdeal.Eatdeal')),
            ],
        ),
    ]