import redis

#创建连接 redis 对象

r = redis.Redis(host='127.0.0.1',port=6379,decode_responses=True,db=0)

#decode_responses = True 必须加,任何返回字符串类型的Redis命令都将使用指定编码进行解码.
#db = 0 指定库.默认是 0 号库.

#所有起始指令 都是函数,语句都是参数.

#存储 字符串类型 k-v
#r.set('name','ok')
#获取 
#print(r.get('name'))

#存储 哈希表
#r.hmset('user:1',{'name':'张三','age':20,'sex':'男'})
#获取
#print(r.hgetall('user:1'))

#存储 列表
r.rpush('user:2',1,2,3,4,5)
print(r.lrange('user:2',0,-1))


