'''
# 2.) python program to determine ifthe given sets arw Disjointor not without using inbuilt-in Functions


  sets = {'python', 'java', 'data science'}
  sets2 = {'ML','AI','R Language', 'python'}
  sewt3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
  c = 0
  flag= 0
 for val in range(3):
     c= c+1
     if c==1:
         for val in set1:
             if val in set2 or val in set3:
                 flag=1
                 break
     if c==2:
         for val in set2:
             if val in set1 or val in set3:
                 flag=1
                 break
     if c==3:
         for val in set3:
             if val in set2 or val in set1:
                 flag=1
                 break


  if flag==0:
      print('Disjoint')
    else:
        print("joint")
             
             
# 3.)
  list1 = ["M", "na", "i","ke"]
  list2 = ["y", "me","s","lly"]

# 13 = []
  for val in range(len(list1)):
      ans = list1[val]+ list2[val]
      l3. append(ans)
   print(l3)


  i = 0
  while i<len(list1):
      l3.append(list1[i]+list2[i])
      i+=1
   print(l3)   
     

# Hacker rank ---> caesar cipher


# ! Functions
# DEF
  Function is a block of code which is used to perform a specific functionality
  Function can be created using def keyword

''' 
  Function has 3 parts
 1.) Function declaration
 2.) Function defination
 3.)  Function calleg:1
def greet():
     print("Welcome user!!")

greet()    
()    
greet()
greet()
greet()
greet()
greet()
greet()
greet()
greet() # function calling



# ! Eg:2
# ? Function with parameter 
 def greeting(name): # name is parameter
     print("Welcome",name)

 for val in range(3):
     username  = input("Enter the name:")
     greeting(username) # user name is arguement


# ! Eg:3
 def profile(name,age,place):
     print(name,age,place)
 profile("sid",29,"cbe")    
     

























     




          
