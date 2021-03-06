'''
입력으로 주어진 종이의 한 변의 길이 N과 각 정사각형칸의 색(하얀색 또는 파란색)이 주어질 때 
잘라진 하얀색 색종이와 파란색 색종이의 개수를 구하는 프로그램을 작성하시오.


첫째 줄에는 전체 종이의 한 변의 길이 N이 주어져 있다. N은 2, 4, 8, 16, 32, 64, 128 중 하나이다.
색종이의 각 가로줄의 정사각형칸들의 색이 윗줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다.
하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1로 주어지며, 각 숫자 사이에는 빈칸이 하나씩 있다.

첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고, 둘째 줄에는 파란색 색종이의 개수를 출력한다.

'''

import sys 
input = sys.stdin.readline 
# sys.setrecursionlimit(1000000)

white = 0
blue = 0 

def paperCount(x,y,n): 
    
    global white 
    global blue 

    check = paper[x][y] 

    for i in range(x,x+n):
        for j in range(y,y+n): 
            if paper[i][j] != check: # 하나라도 다른게 나오면 4등분 

                for k in range(2):
                    for l in range(2):
                        paperCount(x+((n//2)*k),y+((n//2)*l),n//2)

                    # paperCount(x,y,n//2)
                    # paperCount(x,y+(n//2),n//2)
                    # paperCount(x+(n//2),y,n//2)
                    # paperCount(x+(n//2),y+(n//2),n//2)
                return
                
    
    if check == 1: # 파란색 
        blue += 1

    elif check == 0:
        white += 1 

n = int(input()) 
paper = list() 

for _ in range(n): 
    paper.append(list(map(int,input().split()))) 

paperCount(0,0,n) 

print(white)
print(blue)