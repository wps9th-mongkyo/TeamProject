from django.contrib.auth.models import AbstractUser
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db import models


class User(AbstractUser):
    img_profile = models.ImageField('프로필 이미지', upload_to='user', blank=True)
    phone = models.PositiveIntegerField('전화번호', blank=True, null=True)
    email = models.EmailField('이메일', max_length=50, blank=True)
    introduce = models.TextField('소개', blank=True)

    following = models.ManyToManyField(
        'self',
        through='Follow',
        symmetrical=False,
        related_name='followers'
    )

    review_num = models.PositiveIntegerField('리뷰수', default=0)
    checkin_num = models.PositiveIntegerField('체크인수', default=0)
    followers_num = models.PositiveIntegerField('팔로워수', default=0)

    created_at = models.DateTimeField('회원가입날짜', auto_now_add=True)
    modified_at = models.DateTimeField('수정날짜', auto_now=True)

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = f'{verbose_name} 목록'

    @property
    def img_profile_url(self):
        """
        :return: 프로필 사진이 없으면 static/blank_user을 출력
        """
        if self.img_profile.url:
            return self.img_profile.url
        return static('images/dummy-user.jpg')

    @property
    def full_name(self):
        return self.first_name + self.last_name



class Follow(models.Model):
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='from_user_relations',
        related_query_name='from_user_relation',
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='to_user_relations',
        related_query_name='to_user_relation',
    )
    follow_date = models.DateTimeField(auto_now_add=True)

