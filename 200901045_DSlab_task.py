#200901045 Faraz Ahmad Qureshi
#Section B BSCS-01
from collections import deque                               #the program first imports deque for making a stack class
class Stack:                                                #then defining stack functions
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
    def stack_checker(self,val):                            #function that checks if the stack is populated, then compare values and see if brackets are balanced
        global is_balanced
        if len(self.container) > 0:
            if self.container[-1] == val:
                self.is_balanced = True                     #if balanced then pop so the next set of brackets in the stack can be tested
                self.pop()
                return self.is_balanced
            else: 
                self.is_balanced = False
                self.container.clear()
                return self.is_balanced
        else: self.is_balanced = False        
        
    def check_brackets(self,string):                        #returns True or False depending on if the bracket is balanced or not
        my_string = list(string)
      
        for x in my_string:                                 #simple loop which is responsible for everything
            if x == '(':               
                self.push(x)                                #if opening bracket then push into the stack
            elif x == ')':             
                self.stack_checker('(')                     #if closing bracket then check/compare with values already in stack
                if self.is_balanced == False:               #if answer is already false then no need to check further
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
s = Stack()                                                 #initializing stack object
user_string = "({a+b})"                                     #storing input expression
print(user_string, " " , s.check_brackets(user_string))     #printing results for each
user_string = "))((a+b}{"
print(user_string," ", s.check_brackets(user_string))
user_string = "((a+b))"
print(user_string," ", s.check_brackets(user_string))
user_string = "))"
print(user_string," ", s.check_brackets(user_string))
user_string = "[a+b]*(x+2y)*{gg+kk}" 
print(user_string," ", s.check_brackets(user_string))
