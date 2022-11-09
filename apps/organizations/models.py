from django.db import models

from users.models import BaseModel
from django.contrib.auth import get_user_model

UserProfile = get_user_model()


class City(BaseModel):
    name = models.CharField(max_length=20, verbose_name="所在地")
    desc = models.CharField(max_length=200, verbose_name="説明")

    class Meta:
        verbose_name = "所在地"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(BaseModel):
    name = models.CharField(max_length=50, verbose_name="機関名")
    desc = models.TextField(verbose_name="説明")
    tag = models.CharField(default="全国", max_length=10, verbose_name="機関のタグ")
    category = models.CharField(default="pxjg", verbose_name="機関のカテゴリ", max_length=4,
                                choices=(("pxjg", "通信教育"), ("gr", "個人"), ("gx", "学校")))
    click_nums = models.IntegerField(default=0, verbose_name="クリック数")
    fav_nums = models.IntegerField(default=0, verbose_name="お気に入り数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="ロゴ", max_length=100)
    address = models.CharField(max_length=150, verbose_name="機関所在地")
    students = models.IntegerField(default=0, verbose_name="受講人数")
    course_nums = models.IntegerField(default=0, verbose_name="コース数")

    is_auth = models.BooleanField(default=False, verbose_name="認定かどうか")
    is_gold = models.BooleanField(default=False, verbose_name="特選かどうか")

    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="所在地")

    def courses(self):
        courses = self.course_set.filter(is_classics=True)[:3]
        return courses

    class Meta:
        verbose_name = "教育機関"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(BaseModel):
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="機関")
    name = models.CharField(max_length=50, verbose_name="講師名")
    work_years = models.IntegerField(default=0, verbose_name="勤務年数")
    work_company = models.CharField(max_length=50, verbose_name="就職会社")
    work_position = models.CharField(max_length=50, verbose_name="ポジション")
    points = models.CharField(max_length=50, verbose_name="特徴")
    click_nums = models.IntegerField(default=0, verbose_name="クリック数")
    fav_nums = models.IntegerField(default=0, verbose_name="お気に入り数")
    age = models.IntegerField(default=18, verbose_name="年齢")
    image = models.ImageField(upload_to="teacher/%Y/%m", verbose_name="画像", max_length=100)

    class Meta:
        verbose_name = "講師"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def course_nums(self):
        return self.course_set.all().count()