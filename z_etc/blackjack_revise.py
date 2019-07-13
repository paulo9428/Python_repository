import random

class Deck:                                       
    
    def __init__(self):
        self.deck = []
        
    
    def make_deck(self):                               ## deck 을 만든다
        
        shape = ["S","D","H","C"]
        number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
       
        for i in range (0,4):
            res_shape = shape[i]
            for n in range (0, 13):
                res_number = number[n]

                card = res_shape + res_number
                
                self.deck.append(card)
        
    def shuffle(self):                                 ## deck 을 섞는다

        random.shuffle(self.deck)
        
        
###########---------------------------------------------------------------

class Participant:
    
    def __init__(self):

        self.received_card = []

    
    def sum(self):

        self.sum_result = 0
        

        for i in self.received_card:                                    #### j,q,k 결정
            if i[1] == 'J' or  i[1] =='Q' or  i[1] =='K':
                
                self.sum_result += 10
            elif i[1] == 'A' and self.sum_result + 11 > 21:                    ### a 결정
                
                self.sum_result += 1

            elif i[1] == 'A' and self.sum_result + 11 <= 21:
                
                self.sum_result += 11

            else: 
                self.sum_result += int(i[1:])                                   ## 문자열 숫자를 정수화해서 더해준다

    
    def double_hit(self):                   ##2장 hit 하는 것
        
        for i in range(0,2):
            
            card = dk.deck.pop()            ###밑줄의 self 와 다르다?? 플레이어와 딜러 덱을 따로써야하나?
            self.received_card.append(card)
        
    def hit(self):                             ## 한장 hit 하는거
        
        card = dk.deck.pop()
        self.received_card.append(card)
        
        

            
                
class Player(Participant):

    def __init__(self):

        
        super().__init__() 
        self.name = 'player'
    
    
        
class Dealer(Participant):
    
    def __init__(self):

        super().__init__() 
        self.name = 'dealer'

    def machine_hit(self):

        while self.sum_result < 17:
            self.hit()
    


        
##----------------------main flow----------------------------------       
            
p = Player()
d = Dealer()
dk = Deck()    
        

dk.make_deck()
dk.shuffle()

# print(dk.deck)



p.double_hit()                                                  ### 시작하면 2장씩 준다
print("P>>>", p.received_card)

d.double_hit() 
print("D>>>", d.received_card[0])                               ### 딜러의 카드는 2장 중 한장만 보여준다.
                                                         




while True:

    

    choice = input("카드를 한장 더 받으시겠습니까? yes / no\n")

    if choice == "yes":                                                 ## 각자 한장씩 hit 하는 것

        p.hit()
        print("P>>>", p.received_card)
        print("D>>>", d.received_card[0])

        continue
        

    elif choice == "no":

        

        d.sum()
        d.machine_hit()                                           ## 딜러가 sum이 17이상 될때가지 hit 한다
        
        p.sum()
        d.sum()
        
        print(p.received_card)
        print(d.received_card)
        print("P SCORE>>>", p.sum_result)
        print("D SCORE>>>", d.sum_result)
        
        if p.sum_result > 21 and d.sum_result > 21:
            print("Play again!")
        elif d.sum_result > 21:
            print("Player win~")
        elif p.sum_result > 21:
            print("Player lose~")  
        elif p.sum_result - d.sum_result> 0:
            print("You win!!")
        elif p.sum_result - d.sum_result == 0:
            print("Draw!!")
        else:
            print("You lose~")
        

        

        



        
        

        
        

        break

        

        
            
 


        


    
        
        
        
        
    
    
    
    

    

        

   

       
        
        
        
    
    

            

