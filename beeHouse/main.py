#https://www.acmicpc.net/problem/2292
class BeeHouse:
    def func(self,n):
        return int(3*(n**2-n))+1
    def start(self,N):
        if 1 <= N <= 1000000000:
            i=1
            while True:
                if N<=self.func(i):
                    return i
                i+=1
        else:
            return("올바르지 않은 값.")

if __name__ == '__main__':
    beeHouse = BeeHouse()
    print(beeHouse.start(int(input())))