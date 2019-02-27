def sum_shop(shop):
    return sum(shop[1:])


shop_1 = ['shop_1', 500, 200, 200, 100, 500, 200, 200]
shop_2 = ['shop_2', 400, 200, 200, 100, 500, 200, 200]
shop_3 = ['shop_3', 500, 200, 200, 100, 500, 200, 200]
shop_4 = ['shop_4', 500, 200, 200, 100, 500, 200, 200]
all_shops = [shop_1, shop_2, shop_3, shop_4]

max_shop = []
final_max_shop_list = []
f = 0

for shop in all_shops:
    if sum_shop(shop) > f:
        max_shop = shop

for shop in all_shops:
    if sum_shop(max_shop) == sum_shop(shop):
        final_max_shop_list.append([shop[0], sum_shop(shop)])

print(final_max_shop_list)
