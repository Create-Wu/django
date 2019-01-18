from django.db import models


# Create your models here.


class PatienceInfo(models.Model):
    id = models.IntegerField()
    pname = models.CharField(max_length=20, verbose_name='名字')
    pprice = models.IntegerField(default=10, verbose_name='价格')
    pcomment = models.IntegerField(default=0, verbose_name='评论量')
    psales = models.IntegerField(default=100, verbose_name='销量')
    pdescribe = models.CharField(max_length=200, verbose_name='描述信息')

    class Meta:
        app_label = 'meiduo'
        db_table = 'tb_patience'  # 指明数据库表名
        verbose_name = "美多"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pname
