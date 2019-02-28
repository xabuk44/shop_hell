def shop_day_max(shop_list):
    return max(shop_list[1:])

shop_1 = ['Shop 1', 5000, 2000, 1000, 1000, 1000, 1000, 1000]
shop_2 = ['Shop 2', 4000, 2000, 1000, 1000, 1000, 1000, 1000]
shop_3 = ['Shop 3', 5000, 2000, 1000, 1000, 1000, 1000, 500]
shop_4 = ['Shop 4', 6000, 2000, 1000, 1000, 1000, 1000, 500]
all_shops = [shop_1, shop_2, shop_3, shop_4]

print('The best daily revenue of the shop(-s) per week:')
all_shops.sort(key=shop_day_max,  reverse=True)
max_day_shop = all_shops[0]
for shop in all_shops:
    if shop_day_max(max_day_shop) == shop_day_max(shop):
        print(shop[0], '=', shop_day_max(shop))
