[出处](https://www.jianshu.com/p/fb93c64abe8a)

### 1、统计每个月的订单总数
```py
# extra: 在 QuerySet 生成的 SQL 从句中注入新子句

Order.objects.extra(
    select={'created_on': "strftime('%%Y-%%m',created_on)"}
).values("created_on").annotate(count=Count("id")).order_by()
```

```
# 结果：
<QuerySet [{'created_on': '2018-03', 'count': 3}, {'created_on': '2018-04', 'count': 39}]>
```

### 2、统计每年的订单总数
```py
# 将上面的 select 换成：
select={'created_on': "strftime('%%Y', created_on)"}
```
```
# 结果：
<QuerySet [{'created_on': '2018', 'count': 42}]>
```
### 3、统计每件商品卖出去的订单总额(分组显示)
```py
OrderItem.objects.values('price_tag').annotate(Sum('price'))
```

```
# 结果：
<QuerySet [{'price__sum': Decimal('770.00'), 'price_tag': 1}, {'price__sum': Decimal('450.00'), 'price_tag': 2}, {'price__sum': Decimal('100.00'), 'price_tag': 3}, {'price__sum': Decimal('80.00'), 'price_tag': 4}, {'price__sum': Decimal('0.17'), 'price_tag': 6}, {'price__sum': Decimal('0.12'), 'price_tag': 7}, {'price__sum': Decimal('5000.00'), 'price_tag': 8}]>
```
### 4、统计所有订单的订单总额
```py
order_item = OrderItem.objects.all().aggregate(sum_price=Sum('price'))