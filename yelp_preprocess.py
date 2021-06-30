import json
import matplotlib.pyplot as plt

#=============business_dataset====================
#'yelp_dataset~\yelp_academic_dataset_business.json''s example are berow
# {"business_id":"wvFZ06nmPmQ2-IVoPqVYLA","name":"Painting with a Twist","address":"2164 S Chickasaw Trl","city":"Orlando","state":"FL","postal_code":"32825","latitude":28.5116145,"longitude":-81.2700195,"stars":5.0,"review_count":8,"is_open":0,"attributes":{"DogsAllowed":"False","ByAppointmentOnly":"True","GoodForKids":"True","WiFi":"u'no'"},"categories":"Arts & Entertainment, Paint & Sip, Art Classes, Education","hours":{"Monday":"0:0-0:0","Wednesday":"12:0-17:0","Thursday":"19:0-21:0","Friday":"19:0-21:0","Saturday":"15:30-21:0","Sunday":"16:0-18:0"}}
# {"business_id":"GB75wPibj3IjNauaoCxyGA","name":"Havana Cafe","address":"910 NW 14th St","city":"Portland","state":"OR","postal_code":"97209","latitude":45.5296468,"longitude":-122.6851529,"stars":4.0,"review_count":10,"is_open":1,"attributes":{"RestaurantsTakeOut":"True","RestaurantsDelivery":"True","HasTV":"True"},"categories":"Cuban, Sandwiches, Restaurants, Cafes","hours":null}
# {"business_id":"ngmLL5Y5OT-bYHKU0kKrYA","name":"Zora Grille","address":"1370 E Altamonte Dr","city":"Altamonte Springs","state":"FL","postal_code":"32701","latitude":28.6630471,"longitude":-81.3467284,"stars":4.5,"review_count":82,"is_open":0,"attributes":{"RestaurantsReservations":"True","OutdoorSeating":"True","DogsAllowed":"True","BikeParking":"True","RestaurantsPriceRange2":"2","Alcohol":"u'beer_and_wine'","RestaurantsAttire":"'casual'","RestaurantsGoodForGroups":"True","RestaurantsTableService":"True","BusinessParking":"{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}","WheelchairAccessible":"True","BusinessAcceptsCreditCards":"True","GoodForMeal":"{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': True, 'brunch': False, 'breakfast': False}","Ambience":"{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}","WiFi":"u'free'","NoiseLevel":"'average'","HasTV":"False","RestaurantsTakeOut":"True","GoodForKids":"True","Caters":"True","RestaurantsDelivery":"False"},"categories":"Restaurants, Middle Eastern, Mediterranean, Persian\/Iranian, Salad","hours":{"Tuesday":"17:0-21:0","Wednesday":"17:0-21:0","Thursday":"17:0-21:0","Friday":"17:0-21:0","Saturday":"11:30-21:0","Sunday":"12:0-19:30"}}

#read json line by line by f.readline() and each line convert dict. afterwards we append res
#jsonファイルを一行ずつ読み込んで各行をディクショナリー型にしてそれをresにappendしていく
#len(res)=160585

# json_data = 'yelp_dataset~\yelp_academic_dataset_business.json'
# res = []
# with open(json_data,'r',encoding='utf-8') as f:
#     line = f.readline()
#     while line :
#         d = json.loads(line)
#         res.append(d)
#         line = f.readline()
#=======================================================


#=======pthotos.json=============
#json load
json_data = 'yelp_photos\photos.json'
#photo_list:[{'pthoto_id:4310873dfa,'business_id':489321hfjah,,,},{'photo_id:fkdaj342,'business_id']:fklaj,,,}]
photo_list = []
with open(json_data,'r',encoding='utf-8') as f:
    line = f.readline()
    while line :
        d = json.loads(line)
        photo_list.append(d)
        line = f.readline()

#count of shop:{'N0Y8MQV8_L_9-nnT3jOy8Q'(business_id):4(count of picture各店が何枚写真を持っているか)}
count_shop = {}
for photo_data in photo_list:
    if photo_data['business_id'] not in count_shop:
        count_shop[photo_data['business_id']] = 1
    else:
        count_shop[photo_data['business_id']] += 1
#写真のある店舗数：39438店
# print(len(count_shop))

#photo_distribution{1:13096,6:43141,2:43143}
#写真がkey枚の店はvalue店存在する,ソートされていない
photo_distribution = {}
for key,value in count_shop.items():
    if value not in photo_distribution:
        photo_distribution[value]=1
    else:
        photo_distribution[value]+=1

#photo_distributionをソート:[(1,13096),(2,7150),(3,4409),,,]
pthoto_distribution_sorted = sorted(photo_distribution.items(),key=lambda x:x[0],reverse=False)
# print(pthoto_distribution_sorted)

#写真枚数の分布のグラフ作成
# distribution_list = []
# for data in pthoto_distribution_sorted:
#     distribution_list.append(data[1])

# print(distribution_list)
# x = range(1,31)
# y = distribution_list[:30]
# plt.bar(x,y,label='count photos')
# plt.show()


#ラベルの調査 research of label
#label_dic:{'drink': 40000, 'food': 40000, 'interior': 40000, 'outside': 40000, 'menu': 40000}
#labelがkeyであるものがvalue枚ある　There are value photos whose label is key
# label_dic = {}
# for photo_data in photo_list:
#     if photo_data['label'] not in label_dic:
#         label_dic[photo_data['label']] = 1
#     else:
#         label_dic[photo_data['label']] += 1
# print(label_dic)


#Which label cover stores well どのラベルを使えばより多くの店をカバーできるか

labels = ['drink','food','interior','outside','menu']
for label in labels:
    #uniqueな店の数
    unique_count = 0
    #各店舗が今見ているラベルの写真を何枚持っているか
    each_label_count = {}
    for photo_data in photo_list:
        #photo_dataのラベルが今見ているラベルと一致しているか
        if photo_data['label'] == label:
            if photo_data['business_id'] not in each_label_count:
                each_label_count[photo_data['business_id']] = 1
                unique_count += 1
            else:
                each_label_count[photo_data['business_id']] += 1
    print(label,unique_count)
    # drink 14650
    # food 16978
    # interior 19048
    # outside 18961
    # menu 16840

    # print(each_label_count)


#===============================

