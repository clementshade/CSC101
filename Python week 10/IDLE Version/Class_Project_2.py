# List to hold questions and answers
que = ["Which part of the computer displays visual information?",
       "What is the largest computer network",
       "Who is the known as the Father of computers",
       '''Complete this sentencs.
          input,_____, processing, storage
        ''',
       "The part of the computer that acts as the brain is?",
       '''which of these is an example of early thinking machine
        Mouse, Calculator, Abacus, Fish counter''',
       "Code to display hello world",
       "Full meaning of ICT",
       "______ is the ability of a computer to do task that require human intelligence",
       "Who invented python?(Full Name)"]
ans = ["MONITOR","INTERNET","CHARLES BABBAGE","OUTPUT",
       "central processing unit","Abacus","print(\"hello world\")",
       "INFORMATION AND COMMUNICATION TECHNOLOGIES","ARTIFICIAL INTELLIGENCE",
       "GUIDO VAN ROSSUM"]

# Game variables
point = 0
chance = 3
question = 10
Q = 1
cor = 0


#Start

   
while Q < 11:
# Question to answer
        print(que[Q-1])
        #cor is the answer in respect to the number of question
        cor = (ans[Q-1])
        chance -= 1
        A = (input("What is your answer: "))

        
        
# Correct  Answer
        if chance != 0:
                if A.replace(" ","").lower() == (cor.replace(" ","").lower()):
                    print("Correct")
                    point += 1
                    Q += 1
                    chance = 3
                    continue
# Wrong Answer    
                else:
                   print("Wrong")

                   continue
        if chance == 0:
                print("out of chances. Next question")
                Q += 1
                chance = 3
                pass
                
                   

        
#Game Over
        if Q == 11:
                print("You've answered all the questions")
                input("...")
        #Score
                if point == 10:
                        print("Congratulations, You got",point,"points out of 10 correct")
                elif point >= 1:
                        print("Nice try, You got",point,"points out of 10 correct")
                elif point == 0 :
                        print("Are you even trying, Zero points!")
                else:
                        pass
                pass
                input("...")
                print("Game over")
        #Retry?        
                R = input("Do u wanna play again(y/n): ")
                if R.lower() == "y":
                        Q = 1
                        chance = 3                
                        point = 0
                        continue
                
                if R.lower() == "n":
                        input("See you next time...")
                        
                      
                else:
                        pass

        
   
    

