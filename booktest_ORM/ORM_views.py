from django.shortcuts import render

# Create your views here.

# from datetime import date
#
# from booktest_ORM.models import BookInfo,HeroInfo
#
#
# #增加
# book = BookInfo(
#     btitle= '西游记',
#     bpud_date=date(1933, 1, 1),
#     bread=10,
#     bcomment=10,
# )
# book.save()
#
# hero = HeroInfo(
#
#     hname = '毒液',
#     hgender=0,
#     hcomment='变异',
#     hbook=book
# )
# hero.save()
# HeroInfo.objects.create(
#     hname='钢铁侠',
#     hgender=1,
#     hbook_id=2
#
# )


#  查找

#  get 查询单一结果
# all  查询多个结果
# count  查询结果数量
# BookInfo.objects.all() # 所有书籍

# book = BookInfo.objects.count() #查询数量


# book= BookInfo.objects.get(btitle='西游记').id #  根据书名查ID



#
#
# b =BookInfo.objects.get(id=1)
# b.heroinfo_set.all()
#
# c = BookInfo.objects.get(id=3)
# c.heroinfo_set.all()
#
#
# h=HeroInfo.objects.get(id=2)
# h.hbook
#
#
# l = HeroInfo.objects.get(id=3)
# l.hbook_id
#
#
#
# #
# BookInfo.objects.filter(heroinfo__hname__='毒液')

