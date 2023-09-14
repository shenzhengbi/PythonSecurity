import math
import time
# 装饰器函数，用于测量函数执行时间
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 记录开始时间
        result = func(*args, **kwargs)  # 执行原始函数
        end_time = time.time()  # 记录结束时间
        elapsed_time = end_time - start_time  # 计算执行时间
        print(f"{func.__name__} 执行时间：{elapsed_time} 秒")
        return result
    return wrapper


def is_prime(n):
    loop = int(math.sqrt(n))+1  #判断一个数是不是质数，只需要判断其开根号取整数的值是不是其的乘积因子就好了
    for i in range(2,n):
        if n%i==0:
            return False
    return True

#找出一个数的乘积因子，并且确保是质数
@measure_time
def prime_pq(n):
    # time.sleep(10)
    # for q in range(1,n//2+1):
    #     for p in range(1,n//2+1):
    #         if q*p==n and is_prime(q) and is_prime(p):
    #             print(q,p)
    #             exit(0)

    #优化
    max = int(math.sqrt(n))+1
    for p in range(2,max):
        if is_prime(p) and n%p==0 and is_prime(n//p):
            print(f"{p}*{n//p}={n}")

if __name__ == '__main__':

    prime_pq(99460729)