def sum_shop(shop_list):
    return sum(shop_list[1:])


shop_1 = ['Shop 1', 5000, 2000, 1000, 1000, 1000, 1000, 1000]
shop_2 = ['Shop 2', 5000, 2000, 1000, 1000, 1000, 1000, 1000]
shop_3 = ['Shop 3', 5000, 2000, 1000, 1000, 1000, 1000, 500]
shop_4 = ['Shop 4', 5000, 2000, 1000, 1000, 1000, 1000, 500]
all_shops = [shop_1, shop_2, shop_3, shop_4]

print('Best shop(-s) by total revenue for the week:')

all_shops.sort(key=sum_shop, reverse=True)
max_shop = all_shops[0]
for shop in all_shops:
    if sum_shop(max_shop) == sum_shop(shop):
        print(shop[0], '=', sum_shop(shop))
