from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    def pop(self):
        self.container.pop()
    def push(self,val):
        self.container.append(val)
    def is_empty(self):
        return len(self.container) == 0 
    def peak(self):
        return self.container[-1]
    def stack_checker(self,val):
        global is_balanced
        if len(self.container) > 0:
            if self.container[-1] == val:
                self.is_balanced = True
                self.pop()                #pop bracket out
                return self.is_balanced
            else: 
                self.is_balanced = False
                self.container.clear()
                return self.is_balanced
        else: self.is_balanced = False        
        
    def check_brackets(self,string):
        my_string = list(string)
      
        for x in my_string:
            if x == '(':               #push it in the stack
                self.push(x)
            elif x == ')':             #check if bracket at top of stack is the same 
                self.stack_checker('(')
                if self.is_balanced == False:
                    break
            elif x == '{':
                self.push(x)
            elif x == '}':
                self.stack_checker('{')
                if self.is_balanced == False:
                    break
            elif x == '[':
                self.push(x)
            elif x == ']':
                self.stack_checker('[')
                if self.is_balanced == False:
                    break

        return self.is_balanced
s = Stack()
user_string = "({a+b})"
print(user_string, " " , s.check_brackets(user_string))
user_string = "))((a+b}{"
print(user_string," ", s.check_brackets(user_string))
user_string = "((a+b))"
print(user_string," ", s.check_brackets(user_string))
user_string = "))"
print(user_string," ", s.check_brackets(user_string))
user_string = "[a+b]*(x+2y)*{gg+kk}" 
print(user_string," ", s.check_brackets(user_string))
