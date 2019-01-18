from booktest_ORM.models import BookInfo, HeroInfo
from rest_framework.viewsets import ModelViewSet
from booktest_ORM.serializer import BookInfoSerializer, HeroInfoSerializer
from rest_framework import serializers

# DRF的魅力
# class BookInfoViewSet(ModelViewSet):
#
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer


# serializer序列化器的使用

# book = BookInfo.objects.get(id=2)
# serializers = BookInfoSerializer(book)
# serializers.data    #  data 属性可以获得序列化后的数据


# hero= HeroInfo.objects.get(id=2)
# serializers=HeroInfoSerializer(hero)
# serializers.data


# 反序列化,查看创建的序列化器中字段的read_only 的值是否为True，是则需要传入参数，False则不是必须的
# data ={'bpud_date':123}
# serializers = BookInfoSerializer(data=data)
# serializers.is_valid()   # 返回False
# serializers.errors  #  获取错误信息
# # {'bcomment': [ErrorDetail(string='This field is required.', code='required')], 'bpud_date': [ErrorDetail(string='Date has wrong format. Use one of these formats instead: YYYY-MM-DD.', code='invalid')], 'btitle': [ErrorDetail(string='This field is required.', code='required')]}
#
# serializers.validated_data

"""
测试反序列化
data = {'btitle':'烽火','bname':'雪中悍刀行','bpud_date':'1992-1-3','bcomment':'徐凤年'}
serializers = BookInfoSerializer(data=data)
serializers.is_valid()
serializers.errors
serializers.validated_data


测试保存新建功能


data = {'btitle':'剑来','bpud_date':'2018-3-1','bcomment':'来了','bread':'10'}
serializers = BookInfoSerializer(data=data)
serializers.is_valid()
serializers.errors
serializers.save()






"""
