import akshare as ak

df = ak.stock_zh_ah_name()
# print(df)
# name_df = df['名称']

# for idx,data in df.iterrows():
#     print("[{}]: {}".format(idx,data['名称']))
#
# for idx,data in df.iteritems():
#     print("[{}]: {}".format(idx,data['名称']))

# for data in df.iterrows():
#     print(type(data))
#
    
    
for colName,data in df.items():
    print("colName:[{}]\ndata:{}".format(colName,data))