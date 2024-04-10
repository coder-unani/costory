from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validate_symbols

# Create your models here.
class Post(models.Model):
    # 제목, 내용, 작성일, 수정일
    '''
    Validation
    blank= True | False
    null = True | False
    unique = True | False
    '''
    title = models.CharField(max_length=50, unique=True, error_messages={"unique": "제목이 중복되었습니다."})
    content = models.TextField(
        validators=[
            MinLengthValidator(10, "10자 이상 입력해주세요."),
            validate_symbols,
        ]
    )
    dt_created = models.DateTimeField(verbose_name="date created", auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name="date modified", auto_now=True)

    def __str__(self):
        return self.title