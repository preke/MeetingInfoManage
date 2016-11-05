# -*- coding:utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import hashlib
# Create your models here.

def encry_password(password):
    p = hashlib.md5()
    p.update(password)
    return p.hexdigest()

@python_2_unicode_compatible
class Client(models.Model):
    name = models.CharField('姓名', max_length = 50, default = "名字")
    sex = models.CharField('性别', max_length = 10, default = "性别");
    birth = models.CharField('出生年月', max_length = 50, default = "birth")
    job = models.CharField('职务', max_length = 50, default = "job")
    office = models.CharField('科室', max_length = 50, default = "office")
    major = models.CharField('专业', max_length = 50, default = "major")
    title = models.CharField('职称', max_length = 50, default = "title")
    unit = models.CharField('单位', max_length = 50, default = "unit")
    phone = models.CharField('手机', max_length = 20, default = "phone")
    email = models.EmailField('邮箱', max_length = 50, default = "email")
    institute_job = models.CharField('学会任职', max_length = 50, default = "institute")
    strong_point = models.CharField('特长', max_length = 250, default = "string_point")
    # speaker_rate = models.IntegerField('讲者级别', default = 0)
    # purpose = models.TextField('参与活动目的')
    # demand = models.TextField('参会需求')
    region_manager = models.CharField('负责大区经理', max_length = 50, default = "manage")
    # district_manager = models.CHarField('负责地区经理', max_length = 50)
    # represent_type = models.CharField('负责代表类型', max_length = 50)
    potential_weight = models.IntegerField('客户潜力权重', default = 0)
    chairman_times = models.IntegerField('主席统计', default = 0)
    speecher_times = models.IntegerField('讲师统计', default = 0)
    # member_cover = models.IntegerField('参会覆盖', default = 0)

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    class Meta :
        verbose_name = '用户'
        verbose_name_plural = '用户'
        ordering = ['name']

# 大区经理
@python_2_unicode_compatible
class RSM(models.Model):
    user_name = models.CharField('用户名', max_length = 250, default = 'user_name')
    password = models.CharField('密码', max_length = 250, default = encry_password('123456'))
    district = models.CharField('地区', max_length = 250, default = "district")
    members = models.ManyToManyField(Client, verbose_name = '负责的客户群', default = "member")
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '大区经理'
        verbose_name_plural = '大区经理'

# 地区经理
@python_2_unicode_compatible
class RMM(models.Model):
    user_name = models.CharField('用户名', max_length = 250, default = 'user_name')
    password = models.CharField('密码', max_length = 250, default = encry_password('123456'))
    def __unicode__(self):
        return self.user_name
    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = '地区经理'
        verbose_name_plural = '地区经理'
