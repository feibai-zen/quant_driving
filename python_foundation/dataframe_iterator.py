import akshare as ak

# https://zhuanlan.zhihu.com/p/339744795


df = ak.stock_zh_ah_name()
# print(df.to_string())
# name_df = df['名称']



# 1) 按行遍历
# 通过for迭代df.iterrows()接口，idx是输出DataFrame内部的索引值,data输出每行单元格的值
# for idx,data in df.iterrows():
#     print("[{}]: {}".format(idx,data['名称']))
#     print("[{}]: {}".format(idx,data[2]))



# 2) 按行优先的遍历方式，它将返回一个生成器，该生成器以元组生成行值
# for data in df.itertuples():
#     print(data)
# for data in df.itertuples(index=False):
#     print(data)
# for data in df.itertuples(index=False,name='Drama'):
#     print(data)
# for data in df.itertuples(index=False,name='Drama'):
#     print(data[1])


# 3) 按照列遍历
for colName,data in df.items():
    print("colName:[{}]\ndata:{}".format(colName,data))

# for colName,data in df.():
#     print("colName:[{}]\ndata:{}".format(colName,data[1]))
