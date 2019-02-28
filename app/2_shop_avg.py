def shop_avg(shop_list):
    import numpy
    avg_week = numpy.average(shop_list[1:])
    return round(avg_week)


shop_1 = ['Магазин 1', 6000, 2000, 1000, 1000, 1000, 1000, 1000]
shop_2 = ['Магазин 2', 4000, 2000, 1000, 1000, 1000, 1000, 1000]
shop_3 = ['Магазин 3', 3000, 2000, 1000, 1000, 1000, 1000, 500]
shop_4 = ['Магазин 4', 6000, 2000, 1000, 1000, 1000, 1000, 500]
all_shops = [shop_1, shop_2, shop_3, shop_4]


all_shops.sort(key=shop_avg, reverse=True)
max_avg_shop = all_shops[0]
for shop in all_shops:
    if shop_avg(max_avg_shop) == shop_avg(shop):
        print(shop[0], '=', shop_avg(shop))
