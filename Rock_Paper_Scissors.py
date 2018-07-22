q=["Rock", "Paper", "Scissors"]
import random
def rps(c,h):
 if c==h:
  return"Draw"
 elif c=="Rock":
  if h=="Paper":
   return'Human Win'
  elif h=="Scissors":
   return"Computer Win"
 elif c=="Paper":
  if h=="Rock":
   return'Computer Win'
  elif h=="Scissors":
   return'Human Win'
 elif c=="Scissors":
  if h=="Rock":
   return'Human Win'
  elif h=="Paper":
   return"Computer Win"
a=0
b=0
c=0
i=0
win=0
d={}   
while True:
 l= sorted(d.items())
 if i==0 or l[0][1]==l[1][1]==l[2][1]:
  c_choice=random.choice(q)
 else:
  if l[0][1]>l[1][1] and l[0][1]>l[2][1]:
   c_choice="Scissors"
  elif l[1][1]>l[0][1] and l[1][1]>l[2][1]:
   c_choice="Paper"
  elif l[0][1]==l[1][1] and l[0][1]>l[2][1]:
   c_choice=random.choice(["Scissors","Paper"])
  elif l[0][1]==l[2][1] and l[0][1]>l[1][1]:
   c_choice=random.choice(["Scissors","Rock"])
  elif l[1][1]==l[2][1] and l[1][1]>l[0][1]:
   c_choice=random.choice(["Paper","Rock"])
  else:
   c_choice="Rock"
 h_choice=raw_input("Choose Rock, Paper or Scissors to play. Type Quit to stop playing:")
 if h_choice!="Rock" and h_choice!="Paper" and h_choice!="Scissors" and h_choice!="Quit":
  print"Not a valid input"
  continue
 elif h_choice=="Quit":
  print"Games Played:",i
  print"Games won:",win
  quit()
 r=rps(c_choice,h_choice)
 i+=1
 if r=="Draw":
  print"Draw",":",c_choice,"draws with",h_choice
 elif r=="Human Win":
  print"Human Win:",h_choice,"beats",c_choice
  win+=1
 else:
  print"Computer Win:",c_choice,"beats",h_choice
 if h_choice=='Rock':
  a+=1
 elif h_choice=="Paper":
  b+=1
 else:
  c+=1
 d['Rock']=a
 d['Paper']=b
 d['Scissors']=c
 

 
 