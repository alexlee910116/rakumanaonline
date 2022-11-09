from django.db import models

from users.models import BaseModel

from organizations.models import Teacher
from organizations.models import CourseOrg


class Course(BaseModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="講師")
    course_org = models.ForeignKey(CourseOrg, null=True, blank=True, on_delete=models.CASCADE, verbose_name="教育機関")
    name = models.CharField(verbose_name="コース名", max_length=50)
    desc = models.CharField(verbose_name="コース特徴", max_length=300)
    learn_times = models.IntegerField(default=0, verbose_name="総時間(分)")
    degree = models.CharField(verbose_name="難易度", choices=(("cj", "初級"), ("zj", "中級"), ("gj", "高級")), max_length=2)
    students = models.IntegerField(default=0, verbose_name='受講人数')
    fav_nums = models.IntegerField(default=0, verbose_name='お気に入り人数')
    click_nums = models.IntegerField(default=0, verbose_name="クリック数")
    notice = models.CharField(verbose_name="コースの知らせ", max_length=300, default="")
    category = models.CharField(default="バックエンド", max_length=20, verbose_name="コースのカテゴリ")
    tag = models.CharField(default="", verbose_name="コースのタグ", max_length=10)
    youneed_know = models.CharField(default="", max_length=300, verbose_name="知っておきたいこと")
    teacher_tell = models.CharField(default="", max_length=300, verbose_name="コースの概要")
    is_classics = models.BooleanField(default=False, verbose_name="クラシクかどうか")
    detail = models.TextField(verbose_name="コースの詳細")
    is_banner = models.BooleanField(default=False, verbose_name="バナーかどうか")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="コースの画像", max_length=100)

    class Meta:
        verbose_name = "コースの情報"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
    #
    # def lesson_nums(self):
    #     return self.lesson_set.all().count()
    #
    # def show_image(self):
    #     from django.utils.safestring import mark_safe
    #     return mark_safe("<img src='{}'>".format(self.image.url))
    # show_image.short_description = "图片"
    #
    # def go_to(self):
    #     from django.utils.safestring import mark_safe
    #     return mark_safe("<a href='/course/{}'>跳转</a>".format(self.id))
    # go_to.short_description = "跳转"


class CourseTag(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="コース")
    tag = models.CharField(max_length=100, verbose_name="タグ")

    class Meta:
        verbose_name = "コースのタグ"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="コース")  # on_delete表示对应的外键数据被删除后，当前的数据应该怎么办
    name = models.CharField(max_length=100, verbose_name="レクチャー名")
    learn_times = models.IntegerField(default=0, verbose_name="総時間(分)")

    class Meta:
        verbose_name = "コースのレクチャー"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def lesson_nums(self):
        return self.lesson_set.all().count()


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, verbose_name="レクチャー", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="ビデオ名")
    learn_times = models.IntegerField(default=0, verbose_name="総時間(分)")
    url = models.CharField(max_length=1000, verbose_name="ビデオURL")

    class Meta:
        verbose_name = "ビデオ"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="コース")
    name = models.CharField(max_length=100, verbose_name="コース名")
    file = models.FileField(upload_to="course/resource/%Y/%m", verbose_name="ダウンロードURL", max_length=200)

    class Meta:
        verbose_name = "コースのリソース"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
