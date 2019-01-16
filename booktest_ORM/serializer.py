from rest_framework import serializers
from .models import BookInfo

# DRF的魅力
# class BookInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         #  model
#         model = BookInfo
#         fields = '__all__'


class BookInfoSerializer(serializers.Serializer):
    """ 图书馆序列化器 """
    # 字段选项与模型选项相似
    id = serializers.IntegerField(label='ID', read_only=True)
    bcomment = serializers.CharField(label='评论量', required=True)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bpud_date = serializers.DateField(label='上传时间', required=True)
    btitle = serializers.CharField(label='名称', max_length=30)
    image = serializers.ImageField(label='图片', required=False)


    # def validate(self, attrs):
    #     """ validate 参数校验   """
    #     bread = attrs['bread']
    #     bcomment = attrs['bcomment']
    #     if bread< bcomment :
    #         raise serializers.ValidationError('阅读量小于评论量')
    #
    #     return attrs

    def create(self, validated_data):
        """新建"""

        return  BookInfo.objects.create(**validated_data)



    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例 """
        instance.btitle = validated_data.get('btitle',instance.btitle)
        instance.bpud_date = validated_data.get('bpud_date',instance.bpud_date)
        instance.bread = validated_data.get('bread',instance.bread)
        instance.comment = validated_data.get('comment',instance.comment)
        instance.save()
        return instance


class HeroInfoSerializer(serializers.Serializer):
    # 性别选框
    GENDER_CHOICES = (
        (0,'female'),
        (1,'male')
    )
    hid= serializers.IntegerField(label='ID',read_only=True)
    hname = serializers.CharField(label='名字',max_length=20,required=False)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES,label='性别',required=False)
    hcomment = serializers.CharField(max_length=200,allow_null=True,label='描述信息',required=False)
    hbook = serializers.PrimaryKeyRelatedField(label='图书',read_only=True)#外键

