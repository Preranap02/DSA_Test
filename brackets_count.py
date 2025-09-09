def bracket(s):
   stack=[]
   brackets={'}':'{',']':'[',')':'('}
   for i in s:
    if i in brackets.values():
        stack.append(i) 
    elif i in brackets:          
        if not stack or stack.pop()!= brackets[i]:
            return "NO"
   return "YES"  
print(bracket("()[]{}")) 
print(bracket(")[]")) 
