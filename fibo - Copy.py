def print_fib(n :int):
  a=0
  b=1
  if n==1:
    print(a)
    return
  elif n==2:
    print(a,b)
    return
  else:
    i=1
    while(i<=n):
      print(a,end=" ")
      a, b = b, a+b
      i+=1

#print_fib(10)

def get_fib(n: int) -> list:
  l = []
  a=0
  b=1
  if n==1:
    l.append(a)
    return l
  elif n==2:
    l.append(a)
    l.append(b)
    return l
  else:
    i=1
    while(i<=n):
      l.append(a)
      a,b = b,a+b
      i+=1
    return l
#l = get_fib(10)
#print(l)
__all__ = ['get_fib']
if __name__ == "__main__":
    import sys
    get_fib(int(sys.argv[1]))   #sys.argv[1] the value that you will enter after entering the running command

 #This statement is often used at the end of a Python script to define a block of code 
 #that should only be executed if the script is being run as the main program, 
 #but not if it is being imported by another module.


