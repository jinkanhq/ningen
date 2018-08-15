from django.db import models
from django.utils import timezone


class Tag(models.Model):
    slug = models.SlugField()

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.slug


class Person(models.Model):
    name = models.CharField(max_length=32, verbose_name='称谓')
    title = models.CharField(max_length=32, blank=True, verbose_name='头衔')
    avatar = models.ImageField(upload_to='avatars', verbose_name='头像')
    company = models.CharField(
        max_length=32, blank=True, verbose_name='服务处所')
    education = models.CharField(
        max_length=32, blank=True, verbose_name='毕业院校')

    class Meta:
        verbose_name = '人物'
        verbose_name_plural = '人物'

    def __str__(self):
        return self.name


class Item(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=32, verbose_name='名称')
    vendor = models.CharField(max_length=32, verbose_name='厂商')
    description = models.TextField(verbose_name='描述')
    link = models.URLField(verbose_name='链接')

    class Meta:
        verbose_name = '物品'
        verbose_name_plural = '物品'

    def __str__(self):
        return self.name

    def get_full_name(self):
        return "{0} {1}".format(self.vendor, self.name)


class Interview(models.Model):
    slug = models.SlugField()
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, verbose_name='人物')
    body = models.TextField(verbose_name='内容')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    create_on = models.DateTimeField(
        default=timezone.now, verbose_name='采访日期')

    class Meta:
        verbose_name = '采访稿'
        verbose_name_plural = '采访稿'

    def __str__(self):
        return self.slug
