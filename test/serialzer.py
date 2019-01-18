from rest_framework import serializers


class PatienceInfoSerialzer(serializers.Serializer):
    id = serializers.IntegerField(label='ID',read_only=True)
    pname = serializers.CharField(label='名称', read_only=True)
    pprice = serializers.IntegerField(label='价格', read_only=True)
    pcomment = serializers.CharField(label='评论', read_only=True)
    psales = serializers.IntegerField(label='销量', read_only=True)
    pdescribe = serializers.CharField(label='描述信息', read_only=True)


