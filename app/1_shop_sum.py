def sum_shop(shop_list):
    return sum(shop_list[1:])


shop_1 = ['Магазин 1', 5000, 2000, 1000, 1000, 1000, 1000, 1000]
shop_2 = ['Магазин 2', 4000, 2000, 1000, 1000, 1000, 1000, 1000]
shop_3 = ['Магазин 3', 5000, 2000, 1000, 1000, 1000, 1000, 500]
shop_4 = ['Магазин 4', 6000, 2000, 1000, 1000, 1000, 1000, 500]
all_shops = [shop_1, shop_2, shop_3, shop_4]

all_shops.sort(key=sum_shop, reverse=True)
max_shop = all_shops[0]
for shop in all_shops:
    if sum_shop(max_shop) == sum_shop(shop):
        print(shop[0], '=', sum_shop(shop))
