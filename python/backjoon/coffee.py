DictData= {'아메리카노': 2.0, '헤이즐럿': 2.5, '콜드브루': 3.3 }
for index, (key, elem) in enumerate(DictData.items()):
    print(index+1, key, elem)
goodsIdx = int(input("Select Item(1-3) = "))
print(goodsIdx)
print(list(DictData.values()))
print("Total Price : {} ".format(list(DictData.values())[goodsIdx-1]))