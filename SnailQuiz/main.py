#https://www.acmicpc.net/problem/2869
import re
import math

class Snail:
    def start(self, abvValue):
        A, B, V = map(int, str(abvValue).split(' '))
        if 1 <= B < A <= V <= 10 ** 9:
            temp = math.ceil((V-A)/(A-B))
            return temp+1
        else:
            return "올바르지 않은 값"


if __name__ == '__main__':
    snail = Snail()
    inputData = input()
    if re.compile('^\d+\s+\d+\s+\d+$').match(inputData):
        print(snail.start(inputData))
    else:
        print("올바르지 않은 값")
