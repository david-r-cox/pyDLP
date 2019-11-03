def Shanks(g,y,p):
  import math
  import numpy as np
  import pandas as pd
  """
  This Algorithm solves for x given y = g^x (mod p)
  """
  def _create_s_table(g,m,p):
      logs = {}
      for i in range(m+1):
          res = (g**(i*m))%p
          logs.update({i:res})
      return logs

  def _create_t_table(g,y,m,p):
      logs={}
      for j in range(m+1):
          res = (y*g**j)%p
          logs.update({j:res})
      return logs

  def _compare(log1,log2,m,p):
      for i in range(m+1):
          for j in range(m+1):
              if log1[i] == log2[j]:
                  x = (i*m-j)%(p-1)
                  return x, (i,j)
                
  def _plot_tables(baby_steps,giant_steps):
    babys = pd.DataFrame().from_dict(baby_steps, orient='index')
    giant = pd.DataFrame().from_dict(giant_steps, orient='index')
    df = pd.concat([babys,giant],axis=1)
    print(df)
                  
  m = int(np.floor(math.sqrt(p))+1)
  print("m = ",m)
  giant_steps = _create_s_table(g,m,p)
  baby_steps = _create_t_table(g,y,m,p)
  
  x,(index1,index2) = _compare(giant_steps,baby_steps,m,p)
  
  print("x =",x)
  result = (g**x)%p
  print("{}^{}(mod {})".format(g,x,p))
  print("result: ",result)
  _plot_tables(baby_steps,giant_steps)
  print(index2,index1)


def PollardRho(g,y,p):
    import random
    import math

    def get_next_num(num, g, p, y, pow_y, pow_g, set1, set2, set3):
        if num in set1:
            logs.append([num,[pow_y,pow_g]])
            new_num = (y*num)%p
            pow_y += 1
            return new_num, pow_y, pow_g

        elif num in set2:
            logs.append([num,[pow_y,pow_g]])
            new_num = (num**2)%p
            pow_g = pow_g*2
            pow_y = pow_y*2
            return new_num, pow_y, pow_g
        elif num in set3:
            logs.append([num,[pow_y,pow_g]])
            new_num = (g*num)%p
            pow_g += 1
            return new_num, pow_y, pow_g

        else:
            print("No set found. Logic error")

    def getModInverse(a, m):

        if math.gcd(a, m) != 1:
            return None
        u1, u2, u3 = 1, 0, a
        v1, v2, v3 = 0, 1, m

        while v3 != 0:
            q = u3 // v3
            v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
        return u1 % m


    def check_tables(logs, num):
      num1 = 0
      num2 = 0
      for i in range(len(logs)):
        if logs[i][0] == num:
          print("Pair one: ",logs[i])
          print("Pair two: ",logs[-1])
          num1 = logs[i]
          num2 = logs[-1]
          break
      return num1, num2
    
    #alfa = random.randint(1,15)

    alfa = 27
    
    num = (g**alfa)%p
    
    pow_y = 0
    
    pow_g = alfa
    
    mod_set = range(1,p)

    set1 = [x for x in mod_set if x%3 == 0 ]
    set2 = [x for x in mod_set if x%3 == 1 ]
    set3 = [x for x in mod_set if x%3 == 2 ]

    logs = []
    
    search_pair = True
    
    past = []
    num1 = 0
    num2 = 0
    while search_pair:
      past.append(num)
      num, pow_y, pow_g = get_next_num(num, g, p, y, pow_y, pow_g, set1, set2, set3)
      if num in past:
        get_next_num(num, g, p, y, pow_y, pow_g, set1, set2, set3)
        num1, num2 = check_tables(logs,num)
        break  

    def findX(g,y,p,num1,num2):
        foo = 0
        if num2[1][0] % 2 == 1:    
            foo = ((getModInverse(num2[1][0],p-1) * ((num1[1][1]+num1[1][0])-num2[1][1]))%(p-1))
        else:
            cannd = []
            for i in range(p):
                if (( num2[1][0] * i + num2[1][1] ) % (p-1) == num1[1][0] + num1[1][1] ):
                    cannd.append(i)
            for possX in cannd:
                if ((g**possX)%p == y):
                    foo = possX
                    print(foo)
        return foo

    x = findX(g,y,p,num1,num2)
    print("x =",x)
    result = (g**x)%p
    print("{}^{}(mod {})".format(g,x,p))
    print("result: ",result)
    print("\n\n\n")
    print(l qogs)


if __name__ == "__main__":
    g = 5
    y = 3
    p = 2027
    print("SHANKS:\n")
    Shanks(g,y,p)
    print("\n")
    print("POLLARDRHO\n")
    PollardRho(g,y,p)