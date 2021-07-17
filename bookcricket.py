mport random
import pandas as pd
import copy


class book_cricket:
    def player_name(self):
        d = []
        w={}
        n = int(input("number of players:-"))
        for u in range(1, n+1):
            self.name= input("enter the player name:-")
            w.update({"players{}".format(u):self.name})
        print(w)
        h={"players":w.keys(),"names":w.values()}
        s= pd.DataFrame(h)
        print(s)
        x=list(w.values())
        print(x)
        return n,x
    def play(self,c1):
        s=0
        d=0
        for i in range(1.c1.x):
            print('{} is playing'.format(c1.y)
            while(i>0):
                f=random.randint(0,100)
                d=f%10
                if(d==0):
                    print("u r out ")
                else:
                    s=s+d
                    print(s)













c1 = book_cricket()
c1.player_name()

#c2 = book_cricket()
#3 = book_cricket()
#c1.player_name()
#c2.playing_game(c1)
#c3.result(c2)









