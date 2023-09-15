student=int(input("Enter the no of student:"))
for i in range(student):
  SE=int(input('Enter  SE mark:'))
  OS=int(input('Enter  OS mark:'))
  CS=int(input('Enter  CS mark:'))
  tot=(SE+OS+CS)
  print("total value is:",tot)
  a=[SE,OS,CS]
  print(a)
  if SE<35:
        print('The fail subject is SE:',SE)
  elif OS<35:
        print('The fail subject is OS:',OS)
  elif CS<35:
        print('The fail subject is CS:',CS)
  elif SE>35 and OS>35 and SE>35:
         print("PASS")     
  else :
         print("All Fail")           