def solution(new_id):
    new_id = new_id.lower() # 1-step
    
    del_char = "~!@#$%^&*()=+[{]}:?,<>/" 
    new_id = ''.join(x for x in new_id if x not in del_char) # 2-step
    
    # 3-step
    
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    
    
    # 4-step
    if new_id[0] == '.' and len(new_id)>1:
        new_id = new_id[1:]
    if new_id[-1] == '.' :
        new_id = new_id[:-1]
        
    #5-step
    if not new_id:
        new_id = 'a'
    
    #6-step
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
            
    #7-step
    
    if len(new_id) <=2:
        while len(new_id) < 3:
            new_id += new_id[-1]
            
    
    answer = new_id

    
    return answer


'''
#정규식
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
    
'''