#!/usr/bin/env python
# coding: utf-8

# Here is the first class used on this project which reprsent the side of the river:

# In[294]:


import copy
#deep copy will be used later in successor generation

#CLASS REPRESENT THE SIDE OF THE RIVER
class Side:
    mis=0
    can=0
    #mis for missionaries and cin for cannibals counting in each side.
    
    #constructor
    def __init__(self,m=0,c=0):
        self.mis=m
        self.cin=c
    
    #rewriting on the opreators to work with Side opjects
    def __add__(self,copy):
        self.mis += copy.mis
        self.cin += copy.cin
        return self 
    
    def __sub__(self,copy):
        self.mis -= copy.mis
        self.cin -= copy.cin
        return self
    
    #rewritting str to print the Side object when needed
    def __str__(self):
        if self.mis<10 and self.cin<10:
            return f"0{self.mis}:Mis|0{self.cin}:Cin"
        if self.mis>=10 and self.cin<10:
            return f"{self.mis}:Mis|0{self.cin}:Cin"
        if self.mis<10 and self.cin>=10:
            return f"0{self.mis}:Mis|{self.cin}:Cin"
        
        return f"{self.mis}:Mis|{self.cin}:Cin"
    
    #checks if this side is allowed under the constrains
    #1.for both banks and the boat, that the missionaries present cannot be
    #outnumbered by cannibals unless missionaries are 0.

    def allowed(self):
        return (self.mis>=0 and self.cin>=0 and
                (self.mis==0 or(self.mis>=self.cin)))


# now the second class which represent the state

# In[295]:


class State:
    left=None
    right=None
    #left and right reprsent both banks
    onleft=True
    #onleft reprsent the bot loction True for left and False for right
    lastCross=None
    #LastCross used in back tracking the solution path
    
    #constructor
    def __init__(self,l=Side(),r=Side()):
        self.left=l
        self.right=r
        
    #rewritting str to print the State object when needed
    def __str__(self):
        return f"{'L:'if self.onleft else 'R:'}left={str(self.left)}|right={str(self.right)}"

        
    #calls allowd function on each side to check the constrains
    def allowed(self):
        return self.left.allowed() and self.right.allowed()
    
    #goal test function
    def goalTest(self):
        return (not self.onleft) and (self.left.mis==0 and self.left.cin==0)
    
    #the function to move from side to another
    def cross(self,group):
        self.lastCross=group
        if self.onleft:
            self.left -= group
            self.right += group
        else:
            self.right -= group
            self.left += group
        self.onleft= not self.onleft
    
    
        


# In[296]:


from timeit import default_timer as timer
def BFS(m,n,b):
    
    initState=State(Side(m,n))
    if not initState.allowed():
        print("No Solution, your input is not correct since m<c.")
        return
    #insert intial state in fringe(queue)
    queue=deque([initState])
    #saves previuos states to avoid repetition
    prevs={}
    prevs[str(initState)]=True
    #start the seaerch
    count=1
    while len(queue)>0:
        current=queue[0]
        del queue[0]
        #call goal test to check for goal and stop loop if goal is found
        if current.goalTest():
            break
        #edit.
        #if not goal then add it to prevs dictionary 
        #prevs[str(current)]=True
        
        #now we should generate the seccassors to the current
        for m in range(b+1):
            s=1 if m==0 else 0
            for c in range(s,b-m+1):
                newcopy=copy.deepcopy(current)
                newcopy.parent=current
                newcopy.cross(Side(m,c))
                if newcopy.allowed() and not ((str(newcopy)) in prevs):
                    count=count+1;
                    prevs[str(newcopy)]=True
                    queue.append(newcopy)
        #print('nodes generated so far:',count)
        #print('queue length ',len(queue))
        #for i in range(len(queue)):
        #    print(queue[i])
    
    if not current.goalTest():
        print("The problem can not be solved on this input")
        return
        
    path = ""
    i=0
    while current is not None:
        path = f" action:{current.lastCross}\n   {current}{path}"
        try:
            current = current.parent
            i=i+1
        except AttributeError:
            current = None
            
    #first one has no action so we skip this part.
    path = path[13:]


    print ("Breadth-First Search Solution:")
    print (path)
    print ("solution cost : %s steps." % str(i))
    #print len(path)

    print ("\n\n")

start = timer()
BFS(10,10,4)
end = timer()
print(end - start)


# In[305]:


from collections import deque
def IDS(m,n,b,k):
    #IMPORTANT I used deque here because its optimied with O(1) pop/push opretions both sides.
    initState=State(Side(m,n))
    #insert intial state at the top of fringe(stack) 
    stack=deque([initState])
    #saves previuos states to avoid repetition
    prevs={}
    prevs[str(initState)]=True
    counter=0
    while len(stack)>0 and k>=counter:
        current=stack[0]
        del stack[0]
        #call goal test to check for goal and stop loop if goal is found
        if current.goalTest():
            break
        #edit.
        #if not goal then add it to prevs dictionary 
        #prevs[str(current)]=True
        
        #now we should generate the seccassors to the current
        for m in range(b+1):
            s=1 if m==0 else 0
            for c in range(s,b-m+1):
                newcopy=copy.deepcopy(current)
                newcopy.parent=current
                newcopy.cross(Side(m,c))
                if newcopy.allowed() and not ((str(newcopy)) in prevs):
                    prevs[str(newcopy)]=True
                    stack.appendleft(newcopy)
        counter+=1            
    if not current.goalTest():
        print("no solution so far...")
        return False
    
    path = ""
    i=0
    while current is not None:
        path = f" action:{current.lastCross}\n   {current}{path}"
        try:
            current = current.parent
            i=i+1
        except AttributeError:
            current = None
            
    #first one has no action so we skip this part.
    path = path[13:]


    print ("Breadth-First Search Solution:")
    print (path)
    print ("solution cost : %s steps." % str(i))
    return True           
                    

start = timer()
for k in range(100):
    if IDS(10,10,4,k):
        break;

end = timer()
print(end - start)
#we need to add depth to the node...


# In[ ]:





# In[ ]:





# In[ ]:




