# 质数因子求解
import time, math

# 判断一个数是否为质数
def is_prime(n):
    # for i in range(2, n):
    # for i in range(2, n//2+1):
    # for i in range(3, n//2+1, 2):
    loop = int(math.sqrt(n))+1  # 任何一个数，其因子只需要找小于其开根号的整数即可，
    for i in range(2, loop):
        if n % i == 0:
            return False
    return True


# 给定一个数，求其乘积因子，并确保一定是质数
def prime_pq(n):
    start = time.time()
    for p in range(1, n):
        for q in range(1, n):
            # 如果找到因子且两个因子均为质数，则可以直接得出结论，不需要继续循环
            if p * q == n and is_prime(p) and is_prime(q):
                print(p, q)
                end = time.time()
                print(end-start)
                exit(0)


# 第一轮算法优化：p和q的循环次数减半
def prime_01(n):
    start = time.time()
    for p in range(1, n//2+1):
        for q in range(1, n//2+1):
            # 如果找到因子且两个因子均为质数，则可以直接得出结论，不需要继续循环
            if p * q == n and is_prime(p) and is_prime(q):
                print(p, q)
                end = time.time()
                print(end-start)
                exit(0)

# 第二轮：优化一下 is_prime()
def prime_02(n):
    start = time.time()
    for p in range(1, n//2+1):
        for q in range(1, n//2+1):
            # 如果找到因子且两个因子均为质数，则可以直接得出结论，不需要继续循环
            if p * q == n and is_prime(p) and is_prime(q):
            # if is_prime(p) and is_prime(q) and p * q == n:
                print(p, q)
                end = time.time()
                print(end-start)
                exit(0)


if __name__ == '__main__':
    # prime_pq(5687)
    # prime_pq(3233)
    # prime_pq(99400891)
    # prime_pq(9943081)
    # prime_pq(967381)
    # prime_pq(967381)
    # prime_pq(1964681)     # 38秒
    # prime_01(1964681)       # 18秒
    prime_02(1964681)       # 18秒



n = 1230186684530117755130494958384962720772853569595334792197322452151726400507263657518745202199786469389956474942774063845925192557326303453731548268507917026122142913461670429214311602221240479274737794080665351419597459856902143413
