
array = [1,5,2,6,3,7,5]

commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

answer = []
for arr in commands: # [i,j,k]
    sliced = sorted(array[(arr[0]-1):arr[1]])
    
    answer.append(sliced[arr[2]-1])
        

print(answer)
        

'''
other solution
'''

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


a = list(map(int,input().split()))
