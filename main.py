# Author: Ojas Gupta oqg5053@psu.edu    
def digit_sum(n):
  if (n<= 0):
    return n
  else:
    return n%10 + digit_sum(int(n//10))

def run ():
  numbers = int(input("Enter an int: "))
  print (f"sum of digits of {numbers} is {digit_sum(numbers)}.")

if __name__ == "__main__":
  run()