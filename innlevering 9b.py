#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 08:18:08 2021

@author: sagalabdi
"""

# lag classs
class Question:

    def __init__(self,question='',answer=1,choices=[]):
        self._question=question
        self._answer=answer
        self._choices=choices
    
    def GetQuestion(self):
        print(self._question)
        for i in range(len(self._choices)):
            print(i+1,'. ',self._choices[i])
#riktig svar

    def correct_answer_text(self):
       return self._choices[self._answer-1]

#funksjon for les fil
def read_file(sporsmaalsfil):

    #spørsmåls liste
    questions=[]
    
    #fil objekt
    file = open('sporsmaalsfil.txt','r')
    for line in file:
        line=line.split(':')
        question=line[0];
        answer=int(line[1])
        lst=[]
        for val in line[2].strip('[]').split(","):
            lst.append(val)
            questions.append(Question(question,answer,lst))
        
        file.close()
        return questions
    
  
#main
if __name__=="__main__":
  
    #funkjson for å lese fil
      questions=read_file('sporsmaalsfil.txt')
      player1Score=0
      player2Score=0
      
      #Loop gjennom spørsmål
      for i in range(len(questions)):
          questions[i].GetQuestion()
      
      #få svar fra spiller
      player1=int(input('\nVelg et svaralternativ for spiller 1: '))
      player2=int(input('\nVelg et svaralternativ for spiller 2: '))
     
      #vis riktig svar
      print("\nKorrekt svar: ",questions[i].correct_answer_text())
      
      #sjekk svar
      if player1==questions[i]._answer:
          player1Score+=1
      if player2==questions[i]._answer:
          player2Score+=1
          print()
    
  ##  #Summary report
   ## print("\nSpiller1 fikk ",player1Score,' av  ',len(questions))
  #  print("\nSpiller2 fikk ",player2Score,' av  ',len(questions))
 #   if player1Score>player2Score:
#        print("\nSpiller1 Vinner!!")
   # elif player2Score>player1Score:
    #    print("\nSpiller2 Vinner!!")
  #  else:
   #     print("\nUavgjort!!!")