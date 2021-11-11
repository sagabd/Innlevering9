#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 08:18:08 2021

@author: sagalabdi
"""
#Oppgave9&10

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
        for val in line[2].strip('[] ').split(","):
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


class Player:
    
   
    def __init__(self, name='',score=0,guess=0):
        self._name = name
        self._score = score
        self._guess = guess
    
    # return player name    
    def getName(self):
        return self._name
    
    # return player score
    def getScore(self):
        return self._score
    
    # return player svar    
    def getGuess(self):
        return self._guess

# få spiller info
def getPlayers():
    
    player_list = []
    
    # antall spillere
    n = int(input("Skriv inn antall spillere: "))
    
    # spiller navn og poeng
    for i in range(n):
        name = input("Antall spillere " + str(i+1) + " navn: ")
        player_list.append(Player(name, 0))
    return player_list
    

# Main
if __name__=="__main__":
    
   
    questions = read_file('sporsmaalsfil.txt')
    
    # spiller detaljer
    player_list = getPlayers()
    
    # print score for alle spillere
    print()
    for player in player_list:
        print(" Score for " + player.getName() + " er 0")
    print()
    
    # Loop gjennom spørsmålene
    for i in range(len(questions)):
        questions[i].GetQuestion()
        
        # svar fra spillere
        print()
        for player in player_list:
            player._guess = int(input('Svar til Spiller '+ player.getName() + ' : '))

        # riktig svar visst frem
        print("\nKorrekt Svar: ",questions[i].correct_answer_text())
        
        # sjekk svar
        for player in player_list:
            if player._guess == questions[i]._answer:
                player._score += 1
        print()
    
    # spiller med høyest score
    mostScoredPlayer = None
    maxScore = 0
    
    # oppsummering
    for player in player_list:
        print(player.getName(), "scoret", player.getScore(), 'av', len(questions))
        if player.getScore() > maxScore:
            mostScoredPlayer = player
            maxScore = player.getScore()
    
    # vinner detaljer
    print()
    print("Spiller " + mostScoredPlayer.getName() + " fikk flest poeng som er " + str(mostScoredPlayer.getScore()) + ' av ' + str(len(questions)))
