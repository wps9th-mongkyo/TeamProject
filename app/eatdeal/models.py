from django.db import models

# Create your models here.
from restaurants.models import Restaurant


class Eatdeal(models.Model):

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        verbose_name='음식점',
    )
    deal_name = models.CharField('딜이름',max_length=50)
    sub_name = models.CharField('딜메뉴',max_length=100)
    start_date = models.DateField('시작일자', auto_now_add=True)
    end_date = models.DateField('종료일자', auto_now_add=True)
    base_price = models.PositiveIntegerField('기본가격', default=0)
    discount_rate = models.PositiveIntegerField('할인율', default=0)
    discount_price = models.PositiveIntegerField('할인가격', default=0)
    introduce_res = models.TextField('식당소개', max_length=255)
    introduce_menu = models.TextField('메뉴소개', max_length=255)
    _caution = models.TextField('유의사항', max_length=255, blank=True)
    _how_to_use = models.TextField('사용 방법', max_length=255, blank=True)
    _refund = models.TextField('환불규정', max_length=255, blank=True)

    _inquiry = models.EmailField('문의메일', max_length=100, blank=True)

    created_at = models.DateTimeField('회원가입날짜', auto_now_add=True)
    modified_at = models.DateTimeField('수정날짜', auto_now=True)


    '''
    기본값이 필요한 필드 
    '''

    @property
    def caution(self):
        if not self._caution:
            return (f'사용 기간: 구매 시점으로부터 93일\n'
                   f'테이블 당 1매만 사용 가능합니다.\n'
                   f'구매 전 전용 지점을 꼭 확인해주세요.\n'
                   '양도 및 재판매 불가합니다.방문 전 영업시간 및 휴무일 확인을 부탁드립니다.')
        return self._caution

    @caution.setter
    def caution(self, value):
        self._caution = value


    @property
    def how_to_use(self):
        if not self._how_to_use:
            return (f'구매하신 EAT딜은 최신 버전 앱에서만 사용 가능합니다.\n'
                    f'결제 시 망고플레이트 앱 > 내정보 > 구매한 EAT딜을 선택하여 매장에 비치된 QR코드를 스캔합니다.\n'
                    f'QR코드 스캔이 불가능할 시 매장 직원에게 화면 하단 12자리 숫자 코드를 보여주세요.\n'
                    '사용 처리가 완료된 EAT딜은 재사용 및 환불 불가합니다.')
        return self._how_to_use

    @how_to_use.setter
    def how_to_use(self, value):
        self._how_to_use = value

    @property
    def refund(self):
        if not self._refund:
            return (f'상품 사용 기간 내 환불 요청에 한해 구매 금액 전액 환불, 상품 사용 기간 이후 환불 요청 건은 수수료 10%를 제외한 금액 환불을 원칙으로 합니다.\n'
                    f'환불 기간 연장은 불가합니다.\n'
                    f'구매 후 93일 이내 환불 요청: 100% 환불\n'
                    f'구매 후 93일 이후 환불 요청: 90% 환불\n'
                     '환불은 구매 시 사용하였던 결제수단으로 환불됩니다.')
        return self._refund

    @refund.setter
    def refund(self, value):
        self._refund = value

    @property
    def inquiry(self):
        if not self._inquiry:
            return 'cs@mangoplate.com'
        return self._inquiry

    @inquiry.setter
    def inquiry(self, value):
        self._inquiry = value

    def save(self, *args, **kwargs):
        self.discount_price = self.base_price * (1 - (self.discount_rate / 100))
        super().save(*args, **kwargs)



class EatdealImage(models.Model):
    eatdeal = models.ForeignKey(
        Eatdeal,
        related_name='eatdealimages',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to='eatdeal', verbose_name='Eatdeal 이미지')
