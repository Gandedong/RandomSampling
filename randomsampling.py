#测试数据，后期直接采用函数调用
fir = 1
last = 50

#返回所需抽样数量sample_number
total_number = last-fir+1 #样本数量
if total_number >= 250:
    sample_number = 25
elif total_number < 250 and total_number >= 100 :
    sample_number = 15
elif total_number < 100 and total_number >= 50 :
    sample_number = 10
elif total_number < 50 and total_number >= 12 :
    sample_number = 4
elif total_number < 12 and total_number >= 4 :
    sample_number = 2
elif total_number < 4 :
    sample_number = 1

#生成随机数
def ransam(fir,last,sample_number):
    from random import seed,sample
    seed() #生成随机种子
    a = sample(list(range(fir,last)),sample_number)
    return(a)

b=ransam(fir,last,sample_number)
print("根据抽样要求，总样本{}个，抽样{}个，样本编号分别为{}".format(total_number,sample_number,b))

