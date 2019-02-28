def shop_top3(shop_list):
    shop_list = shop_list[1:]
    shop_list.sort()
    return shop_list[4:7]


shop_1 = ['Shop 1', 5000, 2000, 1000, 1000, 1000, 1000, 1000]
shop_2 = ['Shop 2', 4000, 2000, 1000, 1000, 1000, 1000, 1000]
shop_3 = ['Shop 3', 5000, 2000, 1000, 1000, 1000, 1000, 500]
shop_4 = ['Shop 4', 6000, 2000, 1000, 1000, 1000, 1000, 500]
all_shops = [shop_1, shop_2, shop_3, shop_4]

print('Top 3 best sales of each shop:')
print(shop_1[0], '=', shop_top3(shop_1))
print(shop_2[0], '=', shop_top3(shop_2))
print(shop_3[0], '=', shop_top3(shop_3))
print(shop_4[0], '=', shop_top3(shop_4))