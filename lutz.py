import os 
import math

#4. sqrt
def TestSqrt(x):
  #4
  if x == None or x == 0:
    x = 1
  print("sqrt       : ", math.sqrt(x))
  print("pow(x,0.5) : ", pow(x,0.5))
  print("x ** 0.5   : ", x**0.5)
  #6
  print(int(12.32))
  #7
  print(float(1))
  #8
  print(bin(12))
  print(hex(23))
  print(oct(12))
  #9
  print(bin( int( 'C16' , 16) ).replace('0b', ''))

def WorkMulti(inName):
  print("Multi")
  engineers = {'bob', 'sue', 'ann', 'vic'}
  managers = {'tom', 'sue'}
  try:
    # page 189
    if inName in engineers:
      print(inName, " is engineer")
    else:
      print(inName, " is not engineer")
    #
    print("two vacancy: ",engineers & managers)
    print("all vacs: ",engineers | managers)
    print("all manag: ",engineers - managers)
    print("all engin: ",managers - engineers)
     #
  except KeyError:
    print("Error: input")
    raise KeyError
  except OSError:
    print("Error: other problem")
  finally:
    print("work with multipl is end")

if __name__ == '__main__':
  print("start main")
  #TestSqrt(8)
  inMess = 'test'
  while inMess != 'quit':
    inMess = input("input: ")
    WorkMulti(inMess)