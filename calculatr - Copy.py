import os
c = 'bhanu'
while True:
  if c=='stop':
    break
  s=input("Enter an expression (space separated) to be evaluated or enter any one digit to stop: ")
  if len(s)==1:
    break
  else:
    try:
      l = s.split()
      a=float(l[0])
      b=float(l[2])
      c=l[1]
    except:
      print("ERROR:::probably you forgot to give the space")
      continue
   # print(f"{a} {b} {c}")
    match c:
      case '+':
        ans=a+b
      case '-':
        ans=a-b
      case '*':
        ans=a*b
      case '/':
        try:
          ans=a/b
        except:
          raise ZeroDivisionError('division by zero is not allowed')
    
    print(ans)
    while True:
      print(f"y to carray forward calculation with {ans}, n for a new calculation, write 'stop' to stop:")
      c=input()
      if c=='y':
        s2=input(f"complete the expression as per your wish (space separated): {ans}")
        a2=ans
        #print(s2)
        try:
          l2 = s2.split()
          c2=l2[0]
          b2=float(l2[1])
        except:
          print("ERROR:::probably you forgot to give the space")
          continue
        match c2:
          case '+':
            ans=a2+b2
          case '-':
            ans=a2-b2
          case '*':
            ans=a2*b2
          case '/':
            ans=a2/b2
        print(ans)
      else:
        break
      