from django.db import models

from django.contrib.auth import get_user_model

from users.models import BaseModel
from courses.models import Course

UserProfile = get_user_model()


class Banner(BaseModel):
    title = models.CharField(max_length=100, verbose_name="タイトル")
    image = models.ImageField(upload_to="banner/%Y/%m", max_length=100, verbose_name="バナーの画像")
    url = models.URLField(max_length=100, verbose_name="URL")
    index = models.IntegerField(default=0, verbose_name="順番")

    class Meta:
        verbose_name = "バナー"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class UserAsk(BaseModel):
    name = models.CharField(max_length=20, verbose_name="ユーザー名")
    mobile = models.CharField(max_length=11, verbose_name="携帯番号")
    course_name = models.CharField(max_length=50, verbose_name="コース名")

    class Meta:
        verbose_name = "問い合わせ"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{name}_{course}({mobile})".format(name=self.name, course=self.course_name, mobile=self.mobile)


class CourseComments(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="ユーザー名")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="コース")
    comments = models.CharField(max_length=200, verbose_name="コメントの内容")

    class Meta:
        verbose_name = "コースのコメント"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comments


class UserFavorite(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="ユーザー名")
    fav_id = models.IntegerField(verbose_name="データID")
    fav_type = models.IntegerField(choices=((1, "コース"), (2, "教育機関"), (3, "講師")), default=1, verbose_name="お気に入りのカテゴリ")

    class Meta:
        verbose_name = "お気に入り"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{user}_{id}".format(user=self.user.username, id=self.fav_id)


class UserMessage(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="ユーザー名")
    message = models.CharField(max_length=200, verbose_name="メッセージ")
    has_read = models.BooleanField(default=False, verbose_name="既読")

    class Meta:
        verbose_name = "ユーザーのメッセージ"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message


class UserCourse(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="ユーザー名")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="コース")

    class Meta:
        verbose_name = "ユーザーのコース"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course.name
