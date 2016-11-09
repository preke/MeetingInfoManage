# -*- coding:utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class Meeting(models.Model):
    date =models.CharField('日期', max_length=100, default='2016/11/11')
    number = models.CharField('编号', max_length = 250, blank = True, default = "number")
    theme = models.CharField('活动主题', max_length = 250, blank = True, default = "theme")
    name_of_speecher = models.CharField('讲师名字', max_length = 250, blank = True, default = 'speecher')
    type_of_speecher = models.CharField('讲者类型', max_length = 250, blank = True, default = 'speecher')
    city_of_speecher = models.CharField('讲者城市', max_length = 250, blank = True, default = 'city')
    number_of_participant = models.IntegerField('参会人数', default = 0 )
    type_of_meeting = models.CharField('会议类型', max_length = 250, blank = True, default = 'meeting')
    weight_of_meeting = models.IntegerField('会议权重', default= 0)
    def __unicode__(self):
        return self.number
    def __str__(self):
        return self.number
    class Meta:
        verbose_name = '会议'
        verbose_name_plural = '会议'

