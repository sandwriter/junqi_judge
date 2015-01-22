#!/usr/bin/python

# import modules used here -- sys is a very standard one
import os
import sys

from termcolor import colored, cprint

SYMBOL = {
  0: "Gongbing",
  1: "Pai",
  2: "Lian",
  3: "Ying",
  4: "Tuan",
  5: "Lv",
  6: "Shi",
  7: "Jun",
  8: "Siling",
  9: "DiLei",
  10: "Zhadan",
  11: "Junqi",
  }


def Input(player, color):
  for key, role in SYMBOL.iteritems():
    print "%02d\t%s" % (key, role)
  print colored("%s player" % player, color, "on_white", attrs=["bold", "blink"]), "please input now."
  
  while True:
    try:
      key = int(raw_input("Please input the number(two digits) to the left of your role: "))
      if key <0 or key > 11:
        print "Invalid input."
        continue

      # clear the screen so the other party doesn't see what last player inputted.
      os.system("clear")
      
      return key      
    except ValueError:
      print "Invalid input." 
  

def Compare():
  red_key = Input("Red", "red")
  black_key = Input("Black", "blue")

  # Gongbin - Siling should just compare rank.
  if red_key >= 0 and red_key <= 8 and black_key >= 0 and red_key <= 8:
    return red_key - black_key
  # If any one is zhadan, both died.
  if red_key == 10 or black_key == 10:
    return 0
  # Only gongbin win dilei, everything else died.
  if red_key == 9:
    if black_key == 0:
      return -1
    else:
      return 1
  if black_key == 9:
    if red_key == 0:
      return 1
    else:
      return -1
  

def JunQi():
  while True:
    os.system("clear")
    result = Compare()
    if result > 0:
      print "Red Win"
    elif result == 0:
      print "Both Died"
    else:
      print "Black Win"

    raw_input("Press RETURN to start next round...")

# Gather our code in a main() function
def main():
  JunQi()
  # Command line args are in sys.argv[1], sys.argv[2] ..
  # sys.argv[0] is the script name itself and can be ignored

if __name__ == '__main__':
  main()
