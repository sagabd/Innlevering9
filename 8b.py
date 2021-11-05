#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 23:56:19 2021

@author: sagalabdi
"""

#b)

# Spørsmål tester ut kommit3
#hvis stud ass
#ny

class flervalgspors():
    def __init__(self, spors, valg, riktig):
        self.spors = spors
        self.valg = valg
        self.riktig = riktig
        
    def __str__(self):
        spors = self.spors + '\n'
        for i in range(len(self.valg)):
            spors += '{}. {}\n'.format(i + 1, self.valg[i])
        return spors

    def check_answer(self, user_choice):
        if user_choice == self.riktig:
            return True
        else:
            return False

def main():
    q1 = flervalgspors("Hvor mange kommmuner er det i Rogaland?", [13, 23, 56, 400], 2)
    q2 = flervalgspors("Hvor mange kommuner er det i Norge", [743, 426, 356, 19], 3)
    sporsmaal = [q1, q2]
    for q in sporsmaal:
        
        print(q)
        user_answer = int(input("Skriv ditt svar her: "))
        if q.check_answer(user_answer):
            print("Ditt svar er riktig!\n")
        else:
            print("Ditt svar er ikke riktig!\n")

main()

#    score = 0
 #   flervalg = input("Hvor mange kommuner er det i Rogaland? \n1. 13 \n2. 23 \n3. 56 \nSvar: ")
  #  if flervalgspors == "2" or flervalgspors == "Somalia":
   #     score =+ 1
    #    print("Riktig!")
     #   print("Score: ", score)
      #  print("\n")
   # else:
    #    print("Feil! Det riktige svaret var Somalia. ")
     #   print("Score: ", score)
      #  print("\n")
