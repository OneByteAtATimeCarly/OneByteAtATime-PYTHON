#Title: BlackJack (GUI version)
#Author: Carly S. Germany
#Created: 09/08/2022
#Youtube Channel: https://www.youtube.com/c/OneByteAtATime7
#Github Repository: https://github.com/OneByteAtATimeCarly
#Language: Python
#Published: OneByteAtATime © 2023
#Version: 1.0

#Note: In Python, data members of a class declared outside the __init__ method constructor and in side the class are static by default.
# This means they are shared among all instances of a class instead of being different for each instance.
# In this way, Python differs in behavior from Java and C++.
# So the array List CARD_HAND[CARD] is declared and defined in the class CardPlayer. But it's static. It must ALSO be
# initialized inside the __init__ constructor method as self.CARD_HAND = [] so each CardPlayer object can have a separate instance.

from re import L;
import tkinter as tk;
import tkinter.messagebox as MB
from typing import List;
from PIL import ImageTk,Image;
import os;
from playsound import playsound;
import threading;
import random;

#Globals
window = tk.Tk();
window.title("Python tkinter - BLACKJACK - 2022 - Carly Salali Germany");
window_Width = 850;
window_Height = 690;
ScreenWidth = window.winfo_screenwidth();
ScreenHeight = window.winfo_screenheight();
Appear_in_the_Middle = '%dx%d+%d+%d' % (window_Width, window_Height, (ScreenWidth - window_Width) / 2, (ScreenHeight - window_Height) / 2);
window.geometry(Appear_in_the_Middle);
window.resizable(width=False, height=False);
window.configure(bg='black'); 
GUI = None; #pointer that will be used to reference GUI class for functions (instantiated later)


#---Class--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class CARD:

      #--CARD Numerical Values--
      DEUCE = 2;
      THREE = 3;
      FOUR = 4;
      FIVE = 5;
      SIX = 6;
      SEVEN = 7;
      EIGHT = 8;
      NINE = 9;
      TEN = 10;
      JACK = 11;
      QUEEN = 12;
      KING = 13;
      ACE = 14;

      #--CARD Faces--
      SPADES = 0;
      HEARTS = 1;
      DIAMONDS = 2;
      CLUBS = 3;
      
      #--CARD Instances
      TheCard = None;
      TheFace = None;
      PointValue = 0;
      Drawn = False;   

    #---Constructor----------------------------------------------------------------------------    
      def __init__(self, CardNum=DEUCE, CardFace=HEARTS, CardDrawn=False):
          self.TheCard = CardNum;
          self.TheFace = CardFace;
          self.Drawn = CardDrawn;
          self.PointValue = 0;

    #---------------------------------------------------------------------
      def Display_Card(self):
          MESSAGE = "";

          if(self.TheCard == self.DEUCE): MESSAGE += "DEUCE of ";  self.PointValue = 2;
          if(self.TheCard == self.THREE): MESSAGE += "THREE of ";  self.PointValue = 3;
          if(self.TheCard == self.FOUR): MESSAGE += "FOUR of ";    self.PointValue = 4;
          if(self.TheCard == self.FIVE): MESSAGE += "FIVE of ";    self.PointValue = 5;
          if(self.TheCard == self.SIX): MESSAGE += "SIX of ";      self.PointValue = 6;
          if(self.TheCard == self.SEVEN): MESSAGE += "SEVEN of ";  self.PointValue = 7;
          if(self.TheCard == self.EIGHT): MESSAGE += "EIGHT of ";  self.PointValue = 8;
          if(self.TheCard == self.NINE): MESSAGE += "NINE of ";    self.PointValue = 9;
          if(self.TheCard == self.TEN): MESSAGE += "TEN of ";      self.PointValue = 10;
          if(self.TheCard == self.JACK): MESSAGE += "JACK of ";    self.PointValue = 10;
          if(self.TheCard == self.QUEEN): MESSAGE += "QUEEN of ";  self.PointValue = 10;
          if(self.TheCard == self.KING): MESSAGE += "KING of ";    self.PointValue = 10;
          if(self.TheCard == self.ACE): MESSAGE += "ACE of ";      self.PointValue = 11;

          if(self.TheFace == self.SPADES): MESSAGE += "SPADES";
          if(self.TheFace == self.HEARTS): MESSAGE += "HEARTS";
          if(self.TheFace == self.DIAMONDS): MESSAGE += "DIAMONDS";
          if(self.TheFace == self.CLUBS): MESSAGE += "CLUBS";

          return MESSAGE;
#---End Class----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#---Class--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class CardPlayer:
      #Data Members
      NAME = "Anonymous";
      GENDER = "Female";
      Age = 20;
      Money = 100;
      TotalPtsInHand = 0;
      SCORE = 0;
      STAY = False;
      DEALER = False;
      FirstCard = True;
      CARD_HAND = [];      

      def __init__(self, NAM=NAME,GNDR=GENDER,IsDealer=False,Ag=25,Mny=100):
          self.CARD_HAND = [];
          self.NAME = NAM;
          self.GENDER = GNDR;
          self.DEALER = IsDealer;
          self.Age = Ag;
          self.Money = Mny;
          self.TotalPtsInHand = 0;
          self.SCORE = 0;
          self.STAY = False;
          self.FirstCard = True;                        
#---End Class----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




#---Class--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class BlackJack_GUI:
      
      DH_Counter = 0;
       
      #Data Members Global to Class
      SOUND_Directory = os.getcwd() + "\\Sounds\\";
      CARD_Directory = os.getcwd() + "\\CARDS\\";
      DEALER_Directory = os.getcwd() + "\\PONIES\\";

      NUMCARDS = 13;
      NUMFACES = 4;
      NUMCARDSINDECK = 52;
      MaxHandSize = 20;
      NumCardsToStartWith = 2;
      HouseLimit = 17;
      MinimumBet = 5;
      MaximumBet = 50;
      ThePot = 0;
      TheBet = 0;
      OUTPUT = " ";
      DisplayAllDealerCards = False;
      CHEAT = False;
      ANIMATECARDS = False;
      DealerPhoto = 1;
      Pre_Bet = True;
      Game_Over = False; 
      Pre_Determine_Win = True;
      Dealt_Initial_Hand = False;

      DeckOfCards = [None];
      PLAYER = CardPlayer("Carly","Female",False);
      DEALER = CardPlayer("Twilight","Female",True);
      Bet_Text = tk.StringVar();

    #IMAGES
      ACE_clubs = Image.open(CARD_Directory +  "ACE_clubs.jpg");
      ACE_diamonds = Image.open(CARD_Directory +  "ACE_diamonds.jpg");
      ACE_hearts = Image.open(CARD_Directory +  "ACE_hearts.jpg");
      ACE_spades = Image.open(CARD_Directory +  "ACE_spades.jpg");
      JACK_clubs = Image.open(CARD_Directory +  "JACK_clubs.jpg");
      JACK_diamonds = Image.open(CARD_Directory +  "JACK_diamonds.jpg");
      JACK_hearts = Image.open(CARD_Directory +  "JACK_hearts.jpg");
      JACK_spades = Image.open(CARD_Directory +  "JACK_spades.jpg");
      QUEEN_clubs = Image.open(CARD_Directory +  "QUEEN_clubs.jpg");
      QUEEN_diamonds = Image.open(CARD_Directory +  "QUEEN_diamonds.jpg");
      QUEEN_hearts = Image.open(CARD_Directory +  "QUEEN_hearts.jpg");
      QUEEN_spades = Image.open(CARD_Directory +  "QUEEN_spades.jpg");
      KING_clubs = Image.open(CARD_Directory +  "KING_clubs.jpg");
      KING_diamonds = Image.open(CARD_Directory +  "KING_diamonds.jpg");
      KING_hearts = Image.open(CARD_Directory +  "KING_hearts.jpg");
      KING_spades = Image.open(CARD_Directory +  "KING_spades.jpg");
      TWO_clubs = Image.open(CARD_Directory +  "TWO_clubs.jpg");
      TWO_diamonds = Image.open(CARD_Directory +  "TWO_diamonds.jpg");
      TWO_hearts = Image.open(CARD_Directory +  "TWO_hearts.jpg");
      TWO_spades = Image.open(CARD_Directory +  "TWO_spades.jpg");
      THREE_clubs = Image.open(CARD_Directory +  "THREE_clubs.jpg");
      THREE_diamonds = Image.open(CARD_Directory +  "THREE_diamonds.jpg");
      THREE_hearts = Image.open(CARD_Directory +  "THREE_hearts.jpg");
      THREE_spades = Image.open(CARD_Directory +  "THREE_spades.jpg");
      FOUR_clubs = Image.open(CARD_Directory +  "FOUR_clubs.jpg");
      FOUR_diamonds = Image.open(CARD_Directory +  "FOUR_diamonds.jpg");
      FOUR_hearts = Image.open(CARD_Directory +  "FOUR_hearts.jpg");
      FOUR_spades = Image.open(CARD_Directory +  "FOUR_spades.jpg");
      FIVE_clubs = Image.open(CARD_Directory +  "FIVE_clubs.jpg");
      FIVE_diamonds = Image.open(CARD_Directory +  "FIVE_diamonds.jpg");
      FIVE_hearts = Image.open(CARD_Directory +  "FIVE_hearts.jpg");
      FIVE_spades = Image.open(CARD_Directory +  "FIVE_spades.jpg");
      SIX_clubs = Image.open(CARD_Directory +  "SIX_clubs.jpg");
      SIX_diamonds = Image.open(CARD_Directory +  "SIX_diamonds.jpg");
      SIX_hearts = Image.open(CARD_Directory +  "SIX_hearts.jpg");
      SIX_spades = Image.open(CARD_Directory +  "SIX_spades.jpg");
      SEVEN_clubs = Image.open(CARD_Directory +  "SEVEN_clubs.jpg");
      SEVEN_diamonds = Image.open(CARD_Directory +  "SEVEN_diamonds.jpg");
      SEVEN_hearts = Image.open(CARD_Directory +  "SEVEN_hearts.jpg");
      SEVEN_spades = Image.open(CARD_Directory +  "SEVEN_spades.jpg");
      EIGHT_clubs = Image.open(CARD_Directory +  "EIGHT_clubs.jpg");
      EIGHT_diamonds = Image.open(CARD_Directory +  "EIGHT_diamonds.jpg");
      EIGHT_hearts = Image.open(CARD_Directory +  "EIGHT_hearts.jpg");
      EIGHT_spades = Image.open(CARD_Directory +  "EIGHT_spades.jpg");
      NINE_clubs = Image.open(CARD_Directory +  "NINE_clubs.jpg");
      NINE_diamonds = Image.open(CARD_Directory +  "NINE_diamonds.jpg");
      NINE_hearts = Image.open(CARD_Directory +  "NINE_hearts.jpg");
      NINE_spades = Image.open(CARD_Directory +  "NINE_spades.jpg");
      TEN_clubs = Image.open(CARD_Directory +  "TEN_clubs.jpg");
      TEN_diamonds = Image.open(CARD_Directory +  "TEN_diamonds.jpg");
      TEN_hearts = Image.open(CARD_Directory +  "TEN_hearts.jpg");
      TEN_spades = Image.open(CARD_Directory +  "TEN_spades.jpg");
      Joker = Image.open(CARD_Directory +  "Joker.jpg");
      BlankCard = Image.open(CARD_Directory +  "BlankCard.jpg"); 

      Dealer_Img_01 = Image.open(DEALER_Directory +  "AppleJack_1.png");
      Dealer_Img_02 = Image.open(DEALER_Directory +  "Fluttershy_1.jpg");
      Dealer_Img_03 = Image.open(DEALER_Directory +  "Pinkie_Pie_2.png");
      Dealer_Img_04 = Image.open(DEALER_Directory +  "Rarity_3.jpg");
      Dealer_Img_05 = Image.open(DEALER_Directory +  "Rainbow_Dash_6.png");
      Dealer_Img_06 = Image.open(DEALER_Directory +  "Twilight_Sparkle_1.jpg");
      Dealer_Img_07 = Image.open(DEALER_Directory +  "AppleJack_3.jpg");  
      Dealer_Img_08 = Image.open(DEALER_Directory +  "Fluttershy_6.jpg"); 
      Dealer_Img_09 = Image.open(DEALER_Directory +  "Pinkie_Pie_3.png"); 
      Dealer_Img_10 = Image.open(DEALER_Directory +  "Rarity_5.jpg"); 
      Dealer_Img_11 = Image.open(DEALER_Directory +  "Rainbow_Dash_3.png"); 
      Dealer_Img_12 = Image.open(DEALER_Directory +  "Twilight_Sparkle_3.jpg"); 
      Dealer_Img_13 = Image.open(DEALER_Directory +  "Twilight_Sparkle_4.jpg"); 

    #SOUNDS
      #Note: To keep game and GUI responsive when you call playsound, you must play each sound in a different thread from mainloop().
      # Also, the new version of playsound is broken and doesn't work right with multi-threading. Old version is better. To remedy this:
      # pip uninstall playsound
      # pip install playsound==1.2.2

    #01.----------------------------------------------------------------------------------------------------------------
      def Sound_Welcome(self): playsound(self.SOUND_Directory + "Welcome.mp3", block=True);

      def Sound_Welcome_Thread(self):
          self.refresh();
          threading.Thread(target=self.Sound_Welcome, name="BG_Sound_Welcome").start();   
    #02.----------------------------------------------------------------------------------------------------------------
      def Sound_Wanna_Play(self): playsound(self.SOUND_Directory + "Wanna_Play_Feeling_Lucky.mp3", block=True);

      def Sound_Wanna_Play_Thread(self):
          self.refresh();
          threading.Thread(target=self.Sound_Wanna_Play, name="BG_Sound_Wanna_Play").start();  
    #03.----------------------------------------------------------------------------------------------------------------
      def Sound_Lets_Make_A_Deal(self): playsound(self.SOUND_Directory + "Lets_Make_a_Deal.mp3", block=True);

      def Sound_Lets_Make_A_Deal_Thread(self):
          self.refresh();
          threading.Thread(target=self.Sound_Lets_Make_A_Deal, name="BG_Sound_Lets_Make_A_Deal").start();                     
    #04.----------------------------------------------------------------------------------------------------------------
      def Sound_Shuffle(self): playsound(self.SOUND_Directory + "Shuffle.au", block=True);

      def Sound_Shuffle_Thread(self):
          self.refresh();
          threading.Thread(target=self.Sound_Shuffle, name="BG_Sound_Shuffle").start();
    #05.----------------------------------------------------------------------------------------------------------------
      def Sound_Shuffle(self): playsound(self.SOUND_Directory + "Shuffle.au", block=True);

      def Sound_Shuffle_Thread(self):
          self.refresh();
          threading.Thread(target=self.Sound_Shuffle, name="BG_Sound_Shuffle").start();          
    #06.----------------------------------------------------------------------------------------------------------------
      def Sound_CallItQuits(self): playsound(self.SOUND_Directory + "Call_It_Quits.mp3", block=True);

      def Sound_CallItQuits_Thread(self):
          self.refresh();
          threading.Thread(target=self.Sound_CallItQuits, name="BG_Sound_CallItQuits").start();
    #07.----------------------------------------------------------------------------------------------------------------
      def Sound_YouWin(self): playsound(self.SOUND_Directory + "YOU_Win.mp3", block=True);

      def Sound_YouWin_Thread(self):
          self.refresh();
          threading.Thread(target=self.Sound_YouWin, name="BG_Sound_YouWin").start();          
    #08.----------------------------------------------------------------------------------------------------------------
      def Sound_Wager(self): playsound(self.SOUND_Directory + "Wager.mp3", block=True);

      def Sound_Wager_Thread(self):
          self.refresh();
          threading.Thread(target=self.Sound_Wager, name="BG_Sound_Wager").start();
    #09.----------------------------------------------------------------------------------------------------------------
      def Sound_HitOrStay(self): playsound(self.SOUND_Directory + "Hit_or_Stay.mp3", block=True);

      def Sound_HitOrStay_Thread(self):
          self.refresh();
          threading.Thread(target=self.Sound_HitOrStay, name="BG_Sound_HitOrStay").start();          
    #10.----------------------------------------------------------------------------------------------------------------
      def Sound_CheatNO(self): playsound(self.SOUND_Directory + "CHEAT_Off.mp3", block=True);

      def Sound_CheatNO_Thread(self):
          self.refresh();
          threading.Thread(target=self.Sound_CheatNO, name="BG_Sound_CheatNO").start();   
    #11.----------------------------------------------------------------------------------------------------------------
      def Sound_CheatYES(self): playsound(self.SOUND_Directory + "CHEAT_On.mp3", block=True);

      def Sound_CheatYES_Thread(self):
          self.refresh();
          threading.Thread(target=self.Sound_CheatYES, name="BG_Sound_CheatYES").start(); 
    #12.----------------------------------------------------------------------------------------------------------------
      def Sound_DEAL(self): playsound(self.SOUND_Directory + "Deal.au", block=True);

      def Sound_DEAL_Thread(self):
          self.refresh();
          threading.Thread(target=self.Sound_DEAL, name="BG_Sound_DEAL").start(); 
    #13.----------------------------------------------------------------------------------------------------------------
      def Sound_NAILSITPLAYER(self): playsound(self.SOUND_Directory + "PLAYER_Nailed_21.mp3", block=True);

      def Sound_NAILSITPLAYER_Thread(self):
          self.refresh();
          threading.Thread(target=self.Sound_NAILSITPLAYER, name="BG_Sound_NAILS_IT_PLAYER").start(); 
    #14.----------------------------------------------------------------------------------------------------------------
      def Sound_NAILSITDEALER(self): playsound(self.SOUND_Directory + "DEALER_Nails_It_21.mp3", block=True);

      def Sound_NAILSITDEALER_Thread(self):
          self.refresh();
          threading.Thread(target=self.Sound_NAILSITDEALER, name="BG_Sound_NAILS_IT_DEALER").start();          
    #15.----------------------------------------------------------------------------------------------------------------
      def Sound_BUSTEDPLAYER(self): playsound(self.SOUND_Directory + "PLAYER_Busted.mp3", block=True);

      def Sound_BUSTEDPLAYER_Thread(self):
          self.refresh();
          threading.Thread(target=self.Sound_BUSTEDPLAYER, name="BG_Sound_BUSTED_PLAYER").start();  
    #16.----------------------------------------------------------------------------------------------------------------
      def Sound_BUSTEDDEALER(self): playsound(self.SOUND_Directory + "Dealer_Busted.mp3", block=True);

      def Sound_BUSTEDDEALER_Thread(self):
          self.refresh();
          threading.Thread(target=self.Sound_BUSTEDDEALER, name="BG_Sound_BUSTED_DEALER").start();
    #17.----------------------------------------------------------------------------------------------------------------
      def Sound_PLAYERWINS(self): playsound(self.SOUND_Directory + "PLAYER_Wins.mp3", block=True);

      def Sound_PLAYERWINS_Thread(self):
          self.refresh();
          threading.Thread(target=self.Sound_PLAYERWINS, name="BG_Sound_PLAYER_WINS").start();
    #18.----------------------------------------------------------------------------------------------------------------
      def Sound_DEALERWINS(self): playsound(self.SOUND_Directory + "DEALER_Wins.mp3", block=True);

      def Sound_DEALERWINS_Thread(self):
          self.refresh();
          threading.Thread(target=self.Sound_DEALERWINS, name="BG_Sound_DEALER_WINS").start();      
    #19.----------------------------------------------------------------------------------------------------------------
      def Sound_TIE(self): playsound(self.SOUND_Directory + "TIE.mp3", block=True);

      def Sound_TIE_Thread(self):
          self.refresh();
          threading.Thread(target=self.Sound_TIE, name="BG_Sound_TIE").start();  

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def refresh(self):
          window.update();
          window.after(1000,self.refresh);

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def Text_Append(self,MESSAGE):
          Previous_Text = self.TXT_Game_Txt_Output.get("0.0",tk.END);
          self.TXT_Game_Txt_Output.delete("1.0", "end");
          self.TXT_Game_Txt_Output.insert("0.0", Previous_Text + MESSAGE);

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def Text_Write(self,MESSAGE):
          self.TXT_Game_Txt_Output.delete("0.0", "end");
          self.TXT_Game_Txt_Output.insert("0.0", "\n " + MESSAGE);         

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def New_Game(self):
          self.Sound_Welcome_Thread(); 
          self.Game_Over = False; 
          self.BTN_Quit["state"] = tk.NORMAL;
          self.BTN_Talk["state"] = tk.NORMAL;
          self.BTN_Deal["state"] = tk.NORMAL;
          self.BTN_Start["state"] = tk.DISABLED;
          self.BTN_Hit["state"] = tk.DISABLED;
          self.BTN_Stay["state"] = tk.DISABLED;
          self.BTN_Bet["state"] = tk.DISABLED;
          self.BTN_Cheat["state"] = tk.NORMAL;
          self.BTN_GO["state"] = tk.DISABLED;  
          self.ThePot = 0;
          self.TheBet = 0;
          self.DisplayAllDealerCards = False;
          self.CHEAT = False;
          self.DealerPhoto = 1; 
          self.PLAYER = CardPlayer("Carly","Female",False); #BUILD a PLAYER
          self.PLAYER.Money = 100;
          self.PLAYER.Score = 0;
          self.DEALER = CardPlayer("Twilight","Female",True); #Build a DEALER
          self.DEALER.Money = 100;
          self.DEALER.Score = 0;
          self.Pre_Bet = True;
          self.Pre_Determine_Win = True;
          self.Update_Holdings();
          self.DeckOfCards.clear();
          self.Build_Deck_of_Cards();
          self.Change_Dealer_Pix();
          self.Name_Window();

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def New_Game_Thread(self):
          self.refresh();
          threading.Thread(target=self.New_Game).start();

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def Initialize_Game(self):
          self.DeckOfCards.clear();
          self.PLAYER.CARD_HAND.clear();
          self.DEALER.CARD_HAND.clear();
          MESSAGE = "\n Click the \"START\" button to begin a new game.";
          self.Text_Write(MESSAGE);
          self.BTN_Start["state"] = tk.NORMAL;
          self.BTN_Talk["state"] = tk.NORMAL;
          self.BTN_Cheat["state"] = tk.DISABLED; 
          self.BTN_Quit["state"] = tk.DISABLED;
          self.BTN_Deal["state"] = tk.DISABLED;
          self.BTN_Hit["state"] = tk.DISABLED;
          self.BTN_Stay["state"] = tk.DISABLED;
          self.BTN_Bet["state"] = tk.DISABLED; 
          self.BTN_GO["state"] = tk.DISABLED;
                       

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def Change_Dealer_Pix(self):    
          Current_Dealer_Pic = None;
          if(self.DealerPhoto == 1): Current_Dealer_Pic = self.Dealer_Img_01.resize((165, 165), Image.ANTIALIAS);
          if(self.DealerPhoto == 2): Current_Dealer_Pic = self.Dealer_Img_02.resize((165, 165), Image.ANTIALIAS);
          if(self.DealerPhoto == 3): Current_Dealer_Pic = self.Dealer_Img_03.resize((165, 165), Image.ANTIALIAS);
          if(self.DealerPhoto == 4): Current_Dealer_Pic = self.Dealer_Img_04.resize((165, 165), Image.ANTIALIAS);
          if(self.DealerPhoto == 5): Current_Dealer_Pic = self.Dealer_Img_05.resize((165, 165), Image.ANTIALIAS);
          if(self.DealerPhoto == 6): Current_Dealer_Pic = self.Dealer_Img_06.resize((165, 165), Image.ANTIALIAS);
          if(self.DealerPhoto == 7): Current_Dealer_Pic = self.Dealer_Img_07.resize((165, 165), Image.ANTIALIAS);
          if(self.DealerPhoto == 8): Current_Dealer_Pic = self.Dealer_Img_08.resize((165, 165), Image.ANTIALIAS);
          if(self.DealerPhoto == 9): Current_Dealer_Pic = self.Dealer_Img_09.resize((165, 165), Image.ANTIALIAS);
          if(self.DealerPhoto == 10): Current_Dealer_Pic = self.Dealer_Img_10.resize((165, 165), Image.ANTIALIAS);
          if(self.DealerPhoto == 11): Current_Dealer_Pic = self.Dealer_Img_11.resize((165, 165), Image.ANTIALIAS);
          if(self.DealerPhoto == 12): Current_Dealer_Pic = self.Dealer_Img_12.resize((165, 165), Image.ANTIALIAS);
          if(self.DealerPhoto == 13): Current_Dealer_Pic = self.Dealer_Img_13.resize((165, 165), Image.ANTIALIAS);

          self.Dealer_Pic = ImageTk.PhotoImage(Current_Dealer_Pic);
          self.LAB_Dealer_Img.configure(image=self.Dealer_Pic);
          #self.TXT_Game_Txt_Output.delete("0.0", "end");
          #self.TXT_Game_Txt_Output.insert("0.0", "\n " + str(self.DealerPhoto));
          self.DealerPhoto += 1;
          if(self.DealerPhoto == 14): self.DealerPhoto = 1;

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def Draw_Blank_Cards(self): 
          Blank_Card = self.BlankCard.resize((85, 130), Image.ANTIALIAS);  
          self.B_Card = ImageTk.PhotoImage(Blank_Card);
          self.LAB_PLAYER_Card_1.configure(image=self.B_Card);
          self.LAB_PLAYER_Card_2.configure(image=self.B_Card);
          self.LAB_PLAYER_Card_3.configure(image=self.B_Card);
          self.LAB_PLAYER_Card_4.configure(image=self.B_Card);
          self.LAB_PLAYER_Card_5.configure(image='');
          self.LAB_PLAYER_Card_6.configure(image='');
          self.LAB_DEALER_Card_1.configure(image=self.B_Card);
          self.LAB_DEALER_Card_2.configure(image=self.B_Card); 
          self.LAB_DEALER_Card_3.configure(image=self.B_Card);
          self.LAB_DEALER_Card_4.configure(image=self.B_Card);
          self.LAB_DEALER_Card_5.configure(image='');
          self.LAB_DEALER_Card_6.configure(image='');

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def Update_Holdings(self):
          self.LAB_Player_Wins_Output["text"] = str(self.PLAYER.SCORE);
          self.LAB_Dealer_Wins_Output["text"] = str(self.DEALER.SCORE);
          self.LAB_Dealer_Cash_Output["text"] = str(self.DEALER.Money);
          self.LAB_Money_In_Pot_Output["text"] = str(self.ThePot);
          self.LAB_Player_Cash_Output["text"] = str(self.PLAYER.Money);
          self.LAB_Current_Bet_Output["text"] = str(self.TheBet);
          self.LAB_PLAYER_Pts_Output["text"] = str(self.PLAYER.TotalPtsInHand); 
          if(self.CHEAT == True):
             self.LAB_DEALER_Pts_Output["text"] = str(self.DEALER.TotalPtsInHand);
          else: self.LAB_DEALER_Pts_Output["text"] = "???"; 

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def Build_Deck_of_Cards(self):     
          #Clear Array List DECK of CARDs if previously populated for a new game
          self.DeckOfCards.clear();
          #Populate the Deck Array List With Card Values
          MESSAGE = "Beginning a NEW game now.\n\n";
          MESSAGE += " ---- Creating 52 CARD Deck ----\n";
             
          CardType = CARD.DEUCE; #Start populating deck with DEUCES

          #Create 52 CARD objects
          CardInDeck = 0;
          while(CardInDeck < self.NUMCARDSINDECK):
                
                #For each CARD type create 4 faces
                CardFace = 0;
                while(CardFace < self.NUMFACES):
                      self.DeckOfCards.append(CARD(CardType,CardFace));
                      CardFace += 1;
                      MESSAGE += "\n ";
                      MESSAGE += self.DeckOfCards[CardInDeck].Display_Card();
                      CardInDeck += 1;

                CardType += 1; #After 4 faces generated for current type move on to next
           
          MESSAGE += "\n\n ---- DONE! ----\n";
          MESSAGE += "\n Total CARDs in DECK Array List = " + str(len(self.DeckOfCards));
          MESSAGE += "\n\n Click the \"DEAL\" button to continue.\n";
          self.Text_Write(MESSAGE);                                

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def New_Hand(self):       
          #Initialize Values for a Round
          self.DEALER.TotalPtsInHand = 0;
          self.PLAYER.TotalPtsInHand = 0;
          self.DEALER.STAY = False;
          self.PLAYER.STAY = False;
          self.DisplayAllDealerCards = False;

          MESSAGE = "\n Placing all CARDs back into the deck.";

          #Remove All CARDs from CardPlayer's HANDS
          MESSAGE += "\n Clearing player's and dealer's hands.\n";
          self.DEALER.CARD_HAND.clear();
          self.PLAYER.CARD_HAND.clear();

          MESSAGE += "\n PLAYER current # CARDs now: " + str(len(self.PLAYER.CARD_HAND));   
          MESSAGE += "\n DEALER current # CARDs now: " + str(len(self.DEALER.CARD_HAND));

          #Reset DeckOfCards
          MESSAGE += "\n\n Resetting deck of CARDs.\n";
          MESSAGE += "\n BEFORE reset:\n";
          for x in range(len(self.DeckOfCards)):
              MESSAGE += "\n   " + str((x+1)) + ". Drawn = " + str(self.DeckOfCards[x].Drawn);           

          for X in self.DeckOfCards:
              X.Drawn = False;

          MESSAGE += "\n\n AFTER reset:\n";
          for x in range(len(self.DeckOfCards)):
              MESSAGE += "\n   " + str((x+1)) + ". Drawn = " + str(self.DeckOfCards[x].Drawn); 

          self.Text_Append(MESSAGE);                     

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def DRAW(self, WHOEVER): 
          #1. Pick a random CARD from the DECK (offset for fencepost) 
          A_Card = random.randint(0,(self.NUMCARDSINDECK-1));

          #2. Keep pulling cards from DECK until find one that's not already DRAWN
          while(self.DeckOfCards[A_Card].Drawn == True):
                A_Card = random.randint(0,(self.NUMCARDSINDECK-1));

          #3. Once CARD is Drawn, set that attribute on it so it's no longer available from DECK
          self.DeckOfCards[A_Card].Drawn = True;

          #4. Display CARD Drawn
          if(WHOEVER.DEALER == True): 
             MESSAGE = " DEALER draws. ";
             if(self.DEALER.FirstCard == True and self.CHEAT == False):
                MESSAGE += "1st CARD is HIDDEN! You can't see it!";
                self.DEALER.FirstCard = False;
             else:   
                  MESSAGE += "CARD drawn was: " + self.DeckOfCards[A_Card].Display_Card();
             self.DEALER.CARD_HAND.append(self.DeckOfCards[A_Card]);
          elif(WHOEVER.DEALER == False): 
               MESSAGE = " PLAYER draws. ";
               MESSAGE += "CARD drawn was: " + self.DeckOfCards[A_Card].Display_Card();
               self.PLAYER.CARD_HAND.append(self.DeckOfCards[A_Card]);
               
          self.Text_Append(MESSAGE);   

    
   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def Bet(self):  
          #Did the PLAYER enter some garbage for the bet?
          if((self.ENT_Betting).get().isdigit()):   
              MESSAGE = "A valid numerical value was entered.";
              self.TheBet = int(self.ENT_Betting.get());
              self.Bet_Text.set("");
              MESSAGE += "\n " + self.PLAYER.NAME + " is betting " + str(self.TheBet) + " dollars!";
              
              if(self.TheBet > self.PLAYER.Money or self.TheBet > self.DEALER.Money):
                      
                 if(self.TheBet > self.PLAYER.Money):
                    MESSAGE += "\n You wish! You don't have that much money, " + self.PLAYER.NAME + "!";
                 elif(self.TheBet > self.DEALER.Money):
                      MESSAGE += "\n The dealer doesn't have that much money!\n Prepare for a beating...";  

                 if(self.PLAYER.Money - 5 > 0 and self.DEALER.Money - 5 > 0):
                    MESSAGE += "\n Making minimum $5 bet that player and dealer can handle. Ante up!";
                    self.TheBet = 5;
                 else: self.TheBet = 0;
              else:
                    self.ThePot += (self.TheBet*2);
                    self.PLAYER.Money -= self.TheBet;
                    self.DEALER.Money -= self.TheBet;
                    self.BTN_Hit["state"] = tk.NORMAL;
                    self.BTN_Stay["state"] = tk.NORMAL;
                    self.BTN_Bet["state"] = tk.DISABLED; 
                    MESSAGE += "\n You and the dealer both bet " + str(self.TheBet) + " dollars.";
                    MESSAGE += "\n Adding $" + str((self.TheBet*2)) + " to the pot.\n";                  

          else:
                 MESSAGE = "Invalid numerical value! That was not a number.";
                 MESSAGE += "\n Enter a valid amount and click \"BET\" to try this again.";
                 self.Pre_Bet = True;

          self.Text_Write(MESSAGE);
          self.Update_Holdings();
                        
          if(self.PLAYER.TotalPtsInHand < 21 and self.DEALER.TotalPtsInHand < 21):   
             self.Deal();

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def Display_Hand(self, WHOEVER):
          self.Card_Instance_Img = None;  
          MESSAGE = "\n---------------------------------------------------------";
          #DEALER
          if(WHOEVER.DEALER == True):
             MESSAGE += "\n " + self.DEALER.NAME + "\'s Hand(DEALER):";
             self.DEALER.TotalPtsInHand = 0; #reset and recalculate
             if(self.DisplayAllDealerCards == True or self.CHEAT == True):
                MESSAGE += "\n CHEATERS never prosper!";
                #1. Since CHEAT active, start at 0 so displays ALL cards
                Card_Img_Count = 0;
                for x in range(0,len(self.DEALER.CARD_HAND)):
                    self.DEALER.TotalPtsInHand += self.DEALER.CARD_HAND[x].PointValue;
                    MESSAGE += "\n A ";
                    MESSAGE += self.DEALER.CARD_HAND[x].Display_Card();
                    Card_Img_Count += 1;
                    self.Display_Card_Image(self.DEALER.CARD_HAND[x],Card_Img_Count,self.DEALER);
                
                self.LAB_DEALER_Pts_Output["text"] = str(self.DEALER.TotalPtsInHand);
                MESSAGE += "\n " + self.DEALER.NAME + "'s total points = " + str(self.DEALER.TotalPtsInHand) + ". Cheater!\n";
             else:
                   #2. Since CHEAT NOT active, start at 1 so 1st CARD stays hidden
                   #Have to recount starting at 0 for TotalPtsInHand
                   for x in range(0,len(self.DEALER.CARD_HAND)):
                       self.DEALER.TotalPtsInHand += self.DEALER.CARD_HAND[x].PointValue;

                   MESSAGE += "\n First CARD is hidden! What could it be???";
                   Card_Img_Count = 1;
                   #Have to recount starting at 1 to hide 1st CARD
                   for x in range(1,len(self.DEALER.CARD_HAND)):
                       MESSAGE += "\n A ";
                       MESSAGE += self.DEALER.CARD_HAND[x].Display_Card();
                       Card_Img_Count += 1;
                       self.Display_Card_Image(self.DEALER.CARD_HAND[x],Card_Img_Count,self.DEALER);

                   self.LAB_DEALER_Pts_Output["text"] = "??? + " + str((self.DEALER.TotalPtsInHand-self.DEALER.CARD_HAND[0].PointValue));
                   MESSAGE += "\n " + self.DEALER.NAME + "'s total points = ???.\n";

          #PLAYER                     
          elif(WHOEVER.DEALER == False):
               MESSAGE += "\n " + self.PLAYER.NAME + "\'s Hand(PLAYER):";
               self.PLAYER.TotalPtsInHand = 0; #reset and recalculate
               Card_Img_Count = 0;
               for x in range(0,len(self.PLAYER.CARD_HAND)):
                   self.PLAYER.TotalPtsInHand += self.PLAYER.CARD_HAND[x].PointValue;
                   MESSAGE += "\n A ";
                   MESSAGE += self.PLAYER.CARD_HAND[x].Display_Card();
                   Card_Img_Count += 1;
                   self.Display_Card_Image(self.PLAYER.CARD_HAND[x],Card_Img_Count,self.PLAYER);
               
               self.LAB_PLAYER_Pts_Output["text"] = str(self.PLAYER.TotalPtsInHand); 
               MESSAGE += "\n " + self.PLAYER.NAME + "'s total points = " + str(self.PLAYER.TotalPtsInHand) + ".\n"; 

          self.Text_Append(MESSAGE);     
          self.Sound_DEAL_Thread();

          #Check for ACEs and adjust points accordingly
          self.Check_For_Aces(WHOEVER);

          if(self.PLAYER.TotalPtsInHand >= 21 or self.DEALER.TotalPtsInHand >= 21 or self.PLAYER.STAY == True):
             if(self.Pre_Determine_Win == True):
                self.Determine_Winner();

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def Check_For_Aces(self, WHOEVER):  
          #self.Text_Append(" INSIDE Check_For_Aces method.");
          MESSAGE = "";
          if(WHOEVER.TotalPtsInHand > 21):
             for x in range(len(WHOEVER.CARD_HAND)):
                 if(WHOEVER.CARD_HAND[x].TheCard == CARD.ACE and WHOEVER.CARD_HAND[x].PointValue != 1):
                    MESSAGE += " Total points in " + WHOEVER.NAME + "'s hand is over 21.";
                    MESSAGE += "\n But an ACE was found! If it hasn't already been converted";
                    MESSAGE +=  "\n to 1 point? We'll convert it from 11 points to 1 point!\n";
                    MESSAGE += "\n Total points BEFORE conversion = " + str(WHOEVER.TotalPtsInHand);
                    WHOEVER.CARD_HAND[x].PointValue = 1;
                    #Reset and re-count Point values of cards after converting ACE
                    WHOEVER.TotalPtsInHand = 0; 
                    for x in WHOEVER.CARD_HAND:
                        WHOEVER.TotalPtsInHand += x.PointValue;
                    MESSAGE += "\n Total points AFTER conversion = " + str(WHOEVER.TotalPtsInHand);
                    self.Text_Append(MESSAGE); 
                    self.BTN_Hit["state"] = tk.NORMAL;
                    self.BTN_Stay["state"] = tk.NORMAL;
                    self.LAB_PLAYER_Pts_Output["text"] = str(self.PLAYER.TotalPtsInHand);
                    if(self.DisplayAllDealerCards == True or self.CHEAT == True):
                       self.LAB_DEALER_Pts_Output["text"] = str(self.DEALER.TotalPtsInHand); 
                    break; #Convert only 1 ACE in hand, 2 conversions not allowed
        
   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def Display_Card_Image(self,The_CARD,CardNum,WHOEVER):
          self.Card_Image = None;
          MESSAGE  = The_CARD.Display_Card();

          #Debugging: Uncomment 2 lines below for console debugging
          #print("CardNum = ",CardNum);
          #print("CARD = ",MESSAGE);

          if(MESSAGE == "ACE of SPADES"): self.Card_Image = BlackJack_GUI.ACE_spades;
          if(MESSAGE == "ACE of HEARTS"): self.Card_Image = BlackJack_GUI.ACE_hearts;
          if(MESSAGE == "ACE of DIAMONDS"): self.Card_Image = BlackJack_GUI.ACE_diamonds;
          if(MESSAGE == "ACE of CLUBS"): self.Card_Image = BlackJack_GUI.ACE_clubs;
          if(MESSAGE == "JACK of SPADES"): self.Card_Image = BlackJack_GUI.JACK_spades;
          if(MESSAGE == "JACK of HEARTS"): self.Card_Image = BlackJack_GUI.JACK_hearts;
          if(MESSAGE == "JACK of DIAMONDS"): self.Card_Image = BlackJack_GUI.JACK_diamonds;
          if(MESSAGE == "JACK of CLUBS"): self.Card_Image = BlackJack_GUI.JACK_clubs;
          if(MESSAGE == "QUEEN of SPADES"): self.Card_Image = BlackJack_GUI.QUEEN_spades;
          if(MESSAGE == "QUEEN of HEARTS"): self.Card_Image = BlackJack_GUI.QUEEN_hearts;
          if(MESSAGE == "QUEEN of DIAMONDS"): self.Card_Image = BlackJack_GUI.QUEEN_diamonds;
          if(MESSAGE == "QUEEN of CLUBS"): self.Card_Image = BlackJack_GUI.QUEEN_clubs;          
          if(MESSAGE == "KING of SPADES"): self.Card_Image = BlackJack_GUI.KING_spades;
          if(MESSAGE == "KING of HEARTS"): self.Card_Image = BlackJack_GUI.KING_hearts;
          if(MESSAGE == "KING of DIAMONDS"): self.Card_Image = BlackJack_GUI.KING_diamonds;
          if(MESSAGE == "KING of CLUBS"): self.Card_Image = BlackJack_GUI.KING_clubs;
          if(MESSAGE == "DEUCE of SPADES"): self.Card_Image = BlackJack_GUI.TWO_spades;
          if(MESSAGE == "DEUCE of HEARTS"): self.Card_Image = BlackJack_GUI.TWO_hearts;
          if(MESSAGE == "DEUCE of DIAMONDS"): self.Card_Image = BlackJack_GUI.TWO_diamonds;
          if(MESSAGE == "DEUCE of CLUBS"): self.Card_Image = BlackJack_GUI.TWO_clubs;
          if(MESSAGE == "THREE of SPADES"): self.Card_Image = BlackJack_GUI.THREE_spades;
          if(MESSAGE == "THREE of HEARTS"): self.Card_Image = BlackJack_GUI.THREE_hearts;
          if(MESSAGE == "THREE of DIAMONDS"): self.Card_Image = BlackJack_GUI.THREE_diamonds;
          if(MESSAGE == "THREE of CLUBS"): self.Card_Image = BlackJack_GUI.THREE_clubs; 
          if(MESSAGE == "FOUR of SPADES"): self.Card_Image = BlackJack_GUI.FOUR_spades;
          if(MESSAGE == "FOUR of HEARTS"): self.Card_Image = BlackJack_GUI.FOUR_hearts;
          if(MESSAGE == "FOUR of DIAMONDS"): self.Card_Image = BlackJack_GUI.FOUR_diamonds;
          if(MESSAGE == "FOUR of CLUBS"): self.Card_Image = BlackJack_GUI.FOUR_clubs; 
          if(MESSAGE == "FIVE of SPADES"): self.Card_Image = BlackJack_GUI.FIVE_spades;
          if(MESSAGE == "FIVE of HEARTS"): self.Card_Image = BlackJack_GUI.FIVE_hearts;
          if(MESSAGE == "FIVE of DIAMONDS"): self.Card_Image = BlackJack_GUI.FIVE_diamonds;
          if(MESSAGE == "FIVE of CLUBS"): self.Card_Image = BlackJack_GUI.FIVE_clubs;
          if(MESSAGE == "SIX of SPADES"): self.Card_Image = BlackJack_GUI.SIX_spades;
          if(MESSAGE == "SIX of HEARTS"): self.Card_Image = BlackJack_GUI.SIX_hearts;
          if(MESSAGE == "SIX of DIAMONDS"): self.Card_Image = BlackJack_GUI.SIX_diamonds;
          if(MESSAGE == "SIX of CLUBS"): self.Card_Image = BlackJack_GUI.SIX_clubs; 
          if(MESSAGE == "SEVEN of SPADES"): self.Card_Image = BlackJack_GUI.SEVEN_spades;
          if(MESSAGE == "SEVEN of HEARTS"): self.Card_Image = BlackJack_GUI.SEVEN_hearts;
          if(MESSAGE == "SEVEN of DIAMONDS"): self.Card_Image = BlackJack_GUI.SEVEN_diamonds;
          if(MESSAGE == "SEVEN of CLUBS"): self.Card_Image = BlackJack_GUI.SEVEN_clubs;     
          if(MESSAGE == "EIGHT of SPADES"): self.Card_Image = BlackJack_GUI.EIGHT_spades;
          if(MESSAGE == "EIGHT of HEARTS"): self.Card_Image = BlackJack_GUI.EIGHT_hearts;
          if(MESSAGE == "EIGHT of DIAMONDS"): self.Card_Image = BlackJack_GUI.EIGHT_diamonds;
          if(MESSAGE == "EIGHT of CLUBS"): self.Card_Image = BlackJack_GUI.EIGHT_clubs; 
          if(MESSAGE == "NINE of SPADES"): self.Card_Image = BlackJack_GUI.NINE_spades;
          if(MESSAGE == "NINE of HEARTS"): self.Card_Image = BlackJack_GUI.NINE_hearts;
          if(MESSAGE == "NINE of DIAMONDS"): self.Card_Image = BlackJack_GUI.NINE_diamonds;
          if(MESSAGE == "NINE of CLUBS"): self.Card_Image = BlackJack_GUI.NINE_clubs;                                     
          if(MESSAGE == "TEN of SPADES"): self.Card_Image = BlackJack_GUI.TEN_spades;
          if(MESSAGE == "TEN of HEARTS"): self.Card_Image = BlackJack_GUI.TEN_hearts;
          if(MESSAGE == "TEN of DIAMONDS"): self.Card_Image = BlackJack_GUI.TEN_diamonds;
          if(MESSAGE == "TEN of CLUBS"): self.Card_Image = BlackJack_GUI.TEN_clubs; 

          #Reset DEALER 1st CARD to BlankCard in case CHEAT activated then deactivated mid-game
          if(self.CHEAT == False):
             self.Blank_CARD  = BlackJack_GUI.BlankCard.resize((85, 130), Image.ANTIALIAS);
             self.Crd_Img_Blank = ImageTk.PhotoImage(self.Blank_CARD);
             self.LAB_DEALER_Card_1.configure(image=self.Crd_Img_Blank);

          self.Card_Image  = self.Card_Image.resize((85, 130), Image.ANTIALIAS);

          if(WHOEVER.DEALER == False):
             if(CardNum==1): 
                             self.Crd_Img_1 = ImageTk.PhotoImage(self.Card_Image);
                             self.LAB_PLAYER_Card_1.configure(image=self.Crd_Img_1);
             if(CardNum==2): 
                             self.Crd_Img_2 = ImageTk.PhotoImage(self.Card_Image);
                             self.LAB_PLAYER_Card_2.configure(image=self.Crd_Img_2);                   
             if(CardNum==3): 
                             self.Crd_Img_3 = ImageTk.PhotoImage(self.Card_Image);
                             self.LAB_PLAYER_Card_3.configure(image=self.Crd_Img_3);
             if(CardNum==4): 
                             self.Crd_Img_4 = ImageTk.PhotoImage(self.Card_Image);
                             self.LAB_PLAYER_Card_4.configure(image=self.Crd_Img_4);
             if(CardNum==5): 
                             self.Crd_Img_5 = ImageTk.PhotoImage(self.Card_Image);
                             self.LAB_PLAYER_Card_5.configure(image=self.Crd_Img_5);
             if(CardNum==6): 
                             self.Crd_Img_6 = ImageTk.PhotoImage(self.Card_Image);
                             self.LAB_PLAYER_Card_6.configure(image=self.Crd_Img_6);

          elif(WHOEVER.DEALER == True):
               if(CardNum==1): 
                               self.Crd_Img_7 = ImageTk.PhotoImage(self.Card_Image);
                               self.LAB_DEALER_Card_1.configure(image=self.Crd_Img_7);
               if(CardNum==2): 
                               self.Crd_Img_8 = ImageTk.PhotoImage(self.Card_Image);
                               self.LAB_DEALER_Card_2.configure(image=self.Crd_Img_8);                   
               if(CardNum==3): 
                               self.Crd_Img_9 = ImageTk.PhotoImage(self.Card_Image);
                               self.LAB_DEALER_Card_3.configure(image=self.Crd_Img_9);
               if(CardNum==4): 
                               self.Crd_Img_10 = ImageTk.PhotoImage(self.Card_Image);
                               self.LAB_DEALER_Card_4.configure(image=self.Crd_Img_10);
               if(CardNum==5): 
                               self.Crd_Img_11 = ImageTk.PhotoImage(self.Card_Image);
                               self.LAB_DEALER_Card_5.configure(image=self.Crd_Img_11);
               if(CardNum==6): 
                               self.Crd_Img_12 = ImageTk.PhotoImage(self.Card_Image);
                               self.LAB_DEALER_Card_6.configure(image=self.Crd_Img_12);    

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def Deal_Out_Initial_Hands(self):  
          self.Game_Over = False;
          self.DisplayAllDealerCards = False;
          self.DEALER.STAY = False;
          self.PLAYER.STAY = False;          
          self.CHEAT = False;   
          self.ThePot = 0;
          self.TheBet = 0;
          self.Pre_Bet = True;
          self.Pre_Determine_Win = True;
          self.Update_Holdings();
          self.Change_Dealer_Pix();

          #CLEAR all arrays/Lists to reset hands and clear main output
          self.Text_Write("\n Clearing PLAYER and DEALER hands.");
          self.PLAYER.CARD_HAND.clear();
          self.DEALER.CARD_HAND.clear();          

          #Dealer and Player Start Hand By Drawing NumCardsToStartWith Cards Each

          for x in range(0,self.NumCardsToStartWith):
              self.DRAW(self.PLAYER);
              self.DRAW(self.DEALER);
                   
          self.Text_Append("\n PLAYER # CARDs: " + str(len(self.PLAYER.CARD_HAND)));   
          self.Text_Append(" DEALER # CARDs: " + str(len(self.DEALER.CARD_HAND)));

          #Display starting hands when 1st draw complete
          self.Display_Hand(self.PLAYER);
          self.Display_Hand(self.DEALER);

          self.Text_Append(" Click the \"GO\" button to continue.\n");
          self.Dealt_Initial_Hand = True;                                                      

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def Deal(self):
          #Player goes 1st, play till PLAYER or DEALER reaches 21, busts or both Player and Dealer decide to STAY  
          if(self.PLAYER.STAY == False and self.PLAYER.TotalPtsInHand < 21):
             MESSAGE = "\n The DEALER, " + self.DEALER.NAME + ", asks:\n";
             MESSAGE += " \"" + self.PLAYER.NAME + ", do you want a HIT or will you STAY?\"\n\n";
             MESSAGE += " Click the \"HIT\" or \"STAY\" buttons to decide...";
             self.Update_Holdings();
             self.Text_Append(MESSAGE); 
             self.Display_Hand(self.PLAYER);
             self.Display_Hand(self.DEALER);
             self.BTN_Hit["state"] = tk.NORMAL;
             self.BTN_Stay["state"] = tk.NORMAL;
             self.Sound_HitOrStay_Thread();  

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def Dealer_Reaction(self):  
          #DEALER only Draw() if PLAYER not busted or gets BlackJack (21).
          #PLAYER or DEALER "stays" by adding or removing those conditions.
          #In this example, only PLAYER can still Draw() if the DEALER stays.
          #But the DEALER may not Draw() if the PLAYER stays.  
          if(self.DEALER.STAY == False):   
             if(self.DEALER.TotalPtsInHand < self.HouseLimit):
                MESSAGE =  "\n DEALER's current hand less than house limit.";
                MESSAGE += "\n So DEALER decides to draw a CARD.\n";
                self.Text_Append(MESSAGE); 
                self.DRAW(self.DEALER);
                self.Display_Hand(self.DEALER);
             else:
                   MESSAGE = "\n At or over house limit so DEALER decides to STAY.\n";
                   self.Text_Append(MESSAGE); 
                   self.DEALER.STAY = True; 
          elif(self.DEALER.STAY == False):
               MESSAGE = "\n DEALER decided to STAY and draws no more CARDs.";
               self.Text_Append(MESSAGE);

          #Check if after STAY or DRAW() DEALER busted or got 21
          if(self.PLAYER.TotalPtsInHand >= 21 or self.DEALER.TotalPtsInHand >= 21 or self.PLAYER.STAY == True):
             if(self.Pre_Determine_Win == True):
                self.Determine_Winner();
          else: 
              self.Deal();            

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def Determine_Winner(self):  
          self.DH_Counter += 1;
          print("Called Determine_Winner " + str(self.DH_Counter ) + " times.");

          if(self.Pre_Determine_Win == True):
             self.BTN_Bet["state"] = tk.DISABLED;
             self.BTN_GO["state"] = tk.NORMAL;
             self.BTN_Hit["state"] = tk.DISABLED;
             self.BTN_Stay["state"] = tk.DISABLED;
             self.BTN_Deal["state"] = tk.DISABLED;
             self.DisplayAllDealerCards = True; #Stop hiding Dealer's CARDs and POINTs
             self.Text_Append("\n Somebody wins!!! Somebody loses!!!\n Click \"GO\" to continue.\n");
             self.Pre_Determine_Win = False;
             self.Pre_Bet = False; #In case PLAYER or DEALER draws 21 with 1st 2 CARDs

          else:
               MESSAGE = "Determining a WINNER ...\n\n";
               self.Text_Write(MESSAGE);
               #1. *****CONDITION 1 = PLAYER or DEALER [NAILED] a perfect 21**********************
               if(self.PLAYER.TotalPtsInHand == 21 or self.DEALER.TotalPtsInHand == 21):
                  #*****1.A: Both PLAYER and DEALER [TIE] in game by both nailing 21. Unlikely, but possible.
                  if(self.PLAYER.TotalPtsInHand == 21 and self.DEALER.TotalPtsInHand == 21):
                     MESSAGE += " Unthinkable! " + self.PLAYER.NAME + "(PLAYER) and ";
                     MESSAGE += self.DEALER.NAME + "(DEALER) both win, NAILing a perfect 21!";
                     self.PLAYER.SCORE += 1;
                     self.DEALER.SCORE += 1;
                     self.PLAYER.Money += (self.ThePot / 2);
                     self.DEALER.Money += (self.ThePot / 2);
                     self.Sound_NAILSITDEALER_Thread();
                     self.Sound_NAILSITPLAYER_Thread();
                  #*****1.B: PLAYER [NAILS] a perfect 21 and wins************************
                  elif(self.PLAYER.TotalPtsInHand == 21):
                       MESSAGE += " " + self.PLAYER.NAME + "(PLAYER) nails a perfect 21 and wins!"
                       MESSAGE += "\n PLAYER receives a BONUS $50 for achieving pure BlackJack.";
                       self.PLAYER.SCORE += 1;
                       self.PLAYER.Money += self.ThePot;
                       self.PLAYER.Money += 50;
                       self.Sound_NAILSITPLAYER_Thread();
                  #*****1.C: DEALER [NAILS] a perfect 21 and wins************************
                  elif(self.DEALER.TotalPtsInHand == 21):
                       MESSAGE += " " + self.DEALER.NAME + "(DEALER) nails a perfect 21 and wins!"
                       MESSAGE += "\n DEALER receives a BONUS $50 for achieving pure BlackJack.";
                       self.DEALER.SCORE += 1;
                       self.DEALER.Money += self.ThePot;
                       self.DEALER.Money += 50;
                       self.Sound_NAILSITDEALER_Thread();

               #2. *****CONDITION 2 = PLAYER or DEALER [BUSTED] losing the game*******************
               elif(self.PLAYER.TotalPtsInHand > 21 or self.DEALER.TotalPtsInHand > 21):
                    #*****2.A: Both PLAYER and DEALER [BUSTED]. Unlikely, but possible.
                    if(self.PLAYER.TotalPtsInHand > 21 and self.DEALER.TotalPtsInHand > 21):
                       MESSAGE += " Insane! Both " + self.PLAYER.NAME + "(PLAYER) and ";
                       MESSAGE += self.DEALER.NAME + "(DEALER) busted!\n Looks like nobody won this hand.";
                       self.PLAYER.Money += (self.ThePot / 2);
                       self.DEALER.Money += (self.ThePot / 2);
                       self.Sound_BUSTEDDEALER_Thread();
                       self.Sound_BUSTEDPLAYER_Thread();
                    #*****2.B: PLAYER [BUSTED]. DEALER wins.  
                    elif(self.PLAYER.TotalPtsInHand > 21 and self.DEALER.TotalPtsInHand <= 21):
                         MESSAGE += " " + self.PLAYER.NAME + "(PLAYER) busted!";
                         MESSAGE += "\n Sorry, you lost this round.";
                         self.Sound_BUSTEDPLAYER_Thread();
                         self.DEALER.SCORE += 1;
                         self.DEALER.Money += self.ThePot;
                    #*****2.C: DEALER [BUSTED]. PLAYER wins.
                    elif(self.DEALER.TotalPtsInHand > 21 and self.PLAYER.TotalPtsInHand <= 21):  
                         MESSAGE += " " + self.DEALER.NAME + "(DEALER) busted!";
                         MESSAGE += "\n Yay! PLAYER won this round.";
                         self.Sound_BUSTEDDEALER_Thread();
                         self.PLAYER.SCORE += 1;
                         self.PLAYER.Money += self.ThePot;

               #3. *****CONDITION 3 = PLAYER decided to [STAY] so calculate who won***************
               elif(self.PLAYER.STAY == True):
                    #*****3.A: PLAYER [STAYS]. Total points identical. Game is a [TIE]
                    if(self.PLAYER.TotalPtsInHand == self.DEALER.TotalPtsInHand):
                       MESSAGE += " Unbelievable! " + self.PLAYER.NAME + "(PLAYER) and ";
                       MESSAGE += self.DEALER.NAME + "(DEALER)\n both match with the same points!\n";
                       MESSAGE += "\n This game is a TIE. Both win, but neither gets the cash."
                       self.PLAYER.SCORE += 1;
                       self.DEALER.SCORE += 1;
                       self.PLAYER.Money += int((self.ThePot / 2));
                       self.DEALER.Money += int((self.ThePot / 2));
                    #*****3.B: PLAYER has more points so wins game   
                    elif(self.PLAYER.TotalPtsInHand > self.DEALER.TotalPtsInHand):
                         MESSAGE += " " + self.PLAYER.NAME + " wins this round with higher points!";
                         self.PLAYER.Money += self.ThePot;
                         self.PLAYER.SCORE += 1;
                         self.Sound_PLAYERWINS_Thread();
                    #*****3.C: DEALER has more points so wins game   
                    elif(self.PLAYER.TotalPtsInHand < self.DEALER.TotalPtsInHand):
                         MESSAGE += " " + self.DEALER.NAME + " wins this round with higher points!";
                         self.DEALER.Money += self.ThePot;
                         self.DEALER.SCORE += 1;
                         self.Sound_DEALERWINS_Thread(); 

               self.TheBet = 0;
               self.ThePot = 0; 
               self.Update_Holdings();
               MESSAGE += "\n\n This round of BlackJack is now complete.\n";
               MESSAGE += "\n Click \"DEAL\" to play a new hand.\n";
               MESSAGE += "\n Closing HANDs:";
               self.Text_Write(MESSAGE); 
               self.Display_Hand(self.PLAYER);
               self.Display_Hand(self.DEALER);
               self.BTN_Deal["state"] = tk.NORMAL;
               self.BTN_GO["state"] = tk.DISABLED;      
          
   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def Hit(self):  
          self.DRAW(self.PLAYER);
          self.Display_Hand(self.PLAYER);
          
          if(self.PLAYER.TotalPtsInHand < 21):
             self.Dealer_Reaction();
          else: 
                if(self.Pre_Determine_Win == True):
                   self.Determine_Winner();   

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def Help(self): 
          The_MESSAGE = " Blackjack is a short, fast card game of luck and skill.";
          The_MESSAGE += "\n The dealer will start you with two cards from the deck.";
          The_MESSAGE += "\n Your goal is to draw cards to get as close to the number";
          The_MESSAGE +="\n 21 as possible. If you go over 21, you are BUSTED. If you";
          The_MESSAGE += "\n get closer to 21 than the dealer but not over, you win.";
          The_MESSAGE += "\n The card values are:\n";
          The_MESSAGE += "\n             DEUCES = 2        EIGHT = 8";
          The_MESSAGE += "\n             THREE = 3           NINE = 9";
          The_MESSAGE += "\n             FOUR = 4            TEN = 10";
          The_MESSAGE += "\n             FIVE = 5               JACK = 10";
          The_MESSAGE += "\n             SIX = 6                 QUEEN = 10";
          The_MESSAGE += "\n             SEVEN = 7           KING = 10";
          The_MESSAGE += "\n\n             ACE =   11 or 1";
          The_MESSAGE += "\n\n Note: ACEs can count as 1 point or 11 points depending";
          The_MESSAGE += "\n on which CARD point value is advantageous to the player.";
          The_MESSAGE += "\n\n Activating the CHEAT allows you to see all the dealer's cards,";
          The_MESSAGE += "\n giving you an unfair advantage. Normally, one of the Dealer's";
          The_MESSAGE += "\n cards is hidden, making the game more challenging.";     
          MB.showinfo(title='Blackjack HELP: ', message=The_MESSAGE); 

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def Cheat(self): 
          if(self.CHEAT == False):
             The_MESSAGE = "Activating CHEAT! Peeking at my cards now?";
             self.CHEAT = True;
             self.Sound_CheatYES_Thread();
          elif(self.CHEAT == True):
               The_MESSAGE = "Deactivating CHEAT! Decided to be honest for a change?";
               self.CHEAT = False; 
               self.Sound_CheatNO_Thread();
          MB.showinfo(title='Cheaters never prosper', message=The_MESSAGE);
          self.TXT_Game_Txt_Output.delete("0.0", "end");
          self.Display_Hand(self.DEALER);
          self.Display_Hand(self.PLAYER); 

   #---FUNCTION----------------------------------------------------------------------------------------------------------------------
      def Name_Window(self): # new window definition
          Nam_Win = tk.Toplevel(window);
          Nam_Win.configure(bg='black'); 
          Nam_Win.title("Please enter your name.");
          Name_Window_Width = 300;
          Name_Window_Height = 150;
          ScreenWidth = Nam_Win.winfo_screenwidth();
          ScreenHeight = Nam_Win.winfo_screenheight();
          Appear_in_the_Middle = '%dx%d+%d+%d' % (Name_Window_Width, Name_Window_Height, (ScreenWidth - Name_Window_Width) / 2, (ScreenHeight - Name_Window_Height) / 2);
          Nam_Win.geometry(Appear_in_the_Middle);
          Nam_Win.resizable(width=False, height=False);
        
          Name_Data = tk.StringVar();

          def SUBMIT_Button_Handler():
              The_Name = Name_Data.get();
              self.PLAYER.NAME = The_Name;
              Nam_Win.destroy();        

          Label_NAM = tk.Label(Nam_Win, text="Please enter your name below, player.", font=('Helvetica 12'), bg='black', fg='white').pack(pady=10);
          Entry_NAM = tk.Entry(Nam_Win, width=25, font=('Helvetica 12'),textvariable=Name_Data).pack(pady=10);
          Button_NAM = tk.Button(Nam_Win, width=15, height=10, font=('Helvetica 11'), text="SUBMIT", bg='red', command=SUBMIT_Button_Handler).pack(pady=10);            

   #---CONSTRUCTOR-------------------------------------------------------------------------------------------------------------------    
      def __init__(self, master=None):

          #Event handlers for File menu items (Note that event handlers don't take the "self" argument like other inline function definitions in a class)
          def File_Menu_NEW_Handler(): self.PLAYER.NAME = MB.askquestion(title='New  Game!', message="What is your name, player?");
          def File_Menu_CLOSE_Handler(): MB.showinfo(title='File CLOSE Menu Event Triggered: ', message="From FILE menu clicked CLOSE"); 
          def File_Menu_CHEAT_Handler(): self.Cheat();


          #Event handlers for View menu items
          def View_Menu_ZOOMIN_Handler(): MB.showinfo(title='Menu Event Triggered: ', message="From VIEW menu clicked ZOOM IN");
          def View_Menu_ZOOMOUT_Handler(): MB.showinfo(title='Menu Event Triggered: ', message="From VIEW menu clicked ZOOM OUT"); 

          #Event handlers for Help menu items
          def Help_Menu_HELP_Handler(): self.Help(); 
          def Help_Menu_ABOUT_Handler(): 
                                         The_MESSAGE = "Python tkinter BlackJack - 2022 - Carly Salali Germany";
                                         MB.showinfo(title='Python tkinter BlackJack ABOUT: ', message=The_MESSAGE);   

          #Event Handlers for Buttons
          def Handle_Button_Start():
              self.New_Game_Thread();

          def Handle_Button_Quit():
              MB.showinfo(title='You\'re a QUITTER now?', message="Quitting game.");
              self.Initialize_Game();            

          def Handle_Button_Talk():
              self.Change_Dealer_Pix(); 
              WhatToSay = random.randint(1,10);
              if(WhatToSay == 1): MB.showinfo(title='TALK Button Event Triggered: ', message=("Hi! How are you, " + self.PLAYER.NAME + "?"));
              if(WhatToSay == 2): MB.showinfo(title='TALK Button Event Triggered: ', message=("Fine weather we seem to be having today ..."));
              if(WhatToSay == 3): MB.showinfo(title='TALK Button Event Triggered: ', message=("Which came first? The chicken or the egg?"));
              if(WhatToSay == 4): MB.showinfo(title='TALK Button Event Triggered: ', message=("Ever wonder about the meaning of it all?\nWhy are we here?"));
              if(WhatToSay == 5): MB.showinfo(title='TALK Button Event Triggered: ', message=("In the event of an emergency exit doors are to the left."));
              if(WhatToSay == 6): MB.showinfo(title='TALK Button Event Triggered: ', message=("Once upon a time in a galaxy far, far away ..."));
              if(WhatToSay == 7): MB.showinfo(title='TALK Button Event Triggered: ', message=(self.PLAYER.NAME + ", how do you deal with the pressure and uncertainty?"));
              if(WhatToSay == 8): MB.showinfo(title='TALK Button Event Triggered: ', message=("I am SOOOO tired. Been on my feet all day. My hooves are killing me."));
              if(WhatToSay == 9): MB.showinfo(title='TALK Button Event Triggered: ', message=("What's your favforite color, " + self.PLAYER.NAME + "? Mine is PURPLE!"));
              if(WhatToSay == 10): MB.showinfo(title='TALK Button Event Triggered: ', message=("In the end - it doesn't even matter."));

          def Handle_Button_Deal():
              self.BTN_Deal["state"] = tk.DISABLED;
              self.BTN_Hit["state"] = tk.DISABLED;
              self.BTN_Stay["state"] = tk.DISABLED;
              self.BTN_Bet["state"] = tk.DISABLED;
              self.Dealt_Initial_Hand = False;
              self.Pre_Bet = True;
              self.Pre_Determine_Win = True;               

              if(self.PLAYER.Money > 0 and self.DEALER.Money > 0):
                 MESSAGE = "\n Let's make a deal, " + self.PLAYER.NAME + "!\n";
                 MESSAGE += "\n Click the \"GO\" button to continue."; 
                 self.Draw_Blank_Cards();
                 self.Text_Write(MESSAGE); 
                 self.Change_Dealer_Pix();
                 self.Sound_Lets_Make_A_Deal_Thread();
                 self.BTN_Start["state"] = tk.DISABLED;
                 self.BTN_Cheat["state"] = tk.NORMAL;
                 self.BTN_GO["state"] = tk.NORMAL;
              elif(self.PLAYER.Money <= 0):
                   MESSAGE = "\n Sorry. " + self.PLAYER.NAME + "(PLAYER) is out of cash.\n";
                   MESSAGE += "\n Click the \"START\" button to begin again.";
                   self.Text_Write(MESSAGE);
                   self.BTN_Start["state"] = tk.NORMAL;
                   self.BTN_Cheat["state"] = tk.DISABLED;
                   self.BTN_GO["state"] = tk.DISABLED; 
              elif(self.DEALER.Money <= 0):
                   MESSAGE = "\n Sorry. " + self.DEALER.NAME + "(DEALER) is out of cash.\n";
                   MESSAGE += "\n Click the \"START\" button to begin again.";
                   self.Text_Write(MESSAGE);
                   self.BTN_Start["state"] = tk.NORMAL;
                   self.BTN_Cheat["state"] = tk.DISABLED;
                   self.BTN_GO["state"] = tk.DISABLED;  

#---FUNCTION----------------------------------------------------------------------------------------------------------------------
          def Handle_Button_GO():

              print("\nValue of Dealt_Initial_Hand =",self.Dealt_Initial_Hand);
              print("Value of Pre_Bet =",self.Pre_Bet);
              print("Value of Pre_Determine_Win =",self.Pre_Determine_Win);
              
              #1. 
              if(self.Dealt_Initial_Hand == False and self.Pre_Bet == True and self.Pre_Determine_Win == True):
                 self.BTN_GO["state"] = tk.DISABLED;
                 self.Deal_Out_Initial_Hands();
              
              #2. 
              if(self.Dealt_Initial_Hand == True and self.Pre_Bet == True and self.Pre_Determine_Win == True):
                 self.Sound_Wager_Thread();
                 MESSAGE = "What amount will you wager, " + self.PLAYER.NAME + "?\n";
                 MESSAGE += "\n Enter the amount in the bet box above the \"BET\" button.";
                 MESSAGE += "\n Then click \"BET\" to continue.";
                 self.Text_Write(MESSAGE);
                 self.Pre_Bet = False;
                 self.ENT_Betting.focus();
                 self.BTN_GO["state"] = tk.DISABLED; 
                 self.BTN_Bet["state"] = tk.NORMAL; 
              
              #3.
              if(self.Dealt_Initial_Hand == True and self.Pre_Bet == False and self.Pre_Determine_Win == False):
                 self.TXT_Game_Txt_Output.delete("0.0", "end"); #CLEAR
                 self.Determine_Winner();    

#---------------------------------------------------------------------------------------------------------------------------------
          def Handle_Button_Hit():
              self.TXT_Game_Txt_Output.delete("0.0", "end");
              self.Change_Dealer_Pix();
              self.BTN_Hit["state"] = tk.DISABLED;
              self.BTN_Stay["state"] = tk.DISABLED;
              MESSAGE = self.PLAYER.NAME + " requests a HIT!";
              self.Text_Write(MESSAGE);
              self.Hit();

          def Handle_Button_Stay():
              self.TXT_Game_Txt_Output.delete("0.0", "end");
              self.Change_Dealer_Pix();   
              self.BTN_Hit["state"] = tk.DISABLED;
              self.BTN_Stay["state"] = tk.DISABLED;
              self.PLAYER.STAY = True;
              MESSAGE = self.PLAYER.NAME + " requests to STAY.";
              self.Text_Write(MESSAGE);
              self.Dealer_Reaction();                              

          def Handle_Button_Bet():
              self.Bet();
              self.ENT_Betting.focus();

          def Handle_Button_Cheat(): self.Cheat();             
     
    #---A. Frame: Main Window -------------------------------------------------------------
          self.FRM_Main_Window = tk.Frame(master);
          self.FRM_Main_Window.configure(height=690, width=850, borderwidth=3, relief="flat", background="#006400");
          self.FRM_Main_Window.place(anchor="nw", height=710, width=850, x=0, y=0);

          self.Dealer_Img_01 = self.Dealer_Img_01.resize((165, 165), Image.ANTIALIAS);
          self.Dealer_Pic = ImageTk.PhotoImage(self.Dealer_Img_01);
          self.LAB_Dealer_Img = tk.Label(self.FRM_Main_Window);
          self.LAB_Dealer_Img.configure(image=self.Dealer_Pic, borderwidth=3, relief="ridge", text="Dealer Pix", background="#000000");
          self.LAB_Dealer_Img.place(anchor="nw", height=183, width=183, x=658, y=498);          

    #---B. Create main Menu Bar-------------------------------------------------------   
          self.master = master;
          self.Main_Menu_Bar = tk.Menu(self.master);
          self.master.config(menu = self.Main_Menu_Bar);

          #File Menu
          self.File_Menu = tk.Menu(self.Main_Menu_Bar, tearoff=0);
          self.File_Menu.add_command(label="New", command=File_Menu_NEW_Handler);
          self.File_Menu.add_command(label="Close", command=File_Menu_CLOSE_Handler); 
          self.File_Menu.add_command(label="CHEAT", command=File_Menu_CHEAT_Handler);   
          self.File_Menu.add_separator(); # Add separator line to menu
          self.File_Menu.add_command(label="Exit", command=window.quit); #built-in method closes window
          self.Main_Menu_Bar.add_cascade(label="File", menu=self.File_Menu); #adds menu File_Menu to Main_Menu_Bar             
     
          #View Menu
          self.View_Menu = tk.Menu(self.Main_Menu_Bar, tearoff=0);
          self.View_Menu.add_command(label="Zoom In +", command=View_Menu_ZOOMIN_Handler);
          self.View_Menu.add_command(label="Zoom Out -", command=View_Menu_ZOOMOUT_Handler);
          self.Main_Menu_Bar.add_cascade(label="View", menu=self.View_Menu); #adds menu File_Menu to Main_Menu_Bar    

          #Help Menu
          self.Help_Menu = tk.Menu(self.Main_Menu_Bar, tearoff=0);
          self.Help_Menu.add_command(label="Help", command=Help_Menu_HELP_Handler);
          self.Help_Menu.add_command(label="About", command=Help_Menu_ABOUT_Handler);
          self.Main_Menu_Bar.add_cascade(label="Help", menu=self.Help_Menu); #adds menu File_Menu to Main_Menu_Bar                 

    #---B. Frame: Player ---------------------------------------------------
          self.LAB_FRM_Player = tk.LabelFrame(self.FRM_Main_Window);
          self.LAB_FRM_Player.configure(height=400, width=410, background="#006400", foreground="#FFFFFF", borderwidth=3, relief="sunken", text="PLAYER");    
          self.LAB_FRM_Player.place(anchor="nw", height=345, width=410, x=10, y=5);
                               
          Player_Card_IMAGE_1 = Image.open(self.CARD_Directory + "ACE_hearts.jpg");
          Player_Card_IMAGE_1 = Player_Card_IMAGE_1.resize((85, 130), Image.ANTIALIAS);
          self.Player_Card_1 = ImageTk.PhotoImage(Player_Card_IMAGE_1);
          self.LAB_PLAYER_Card_1 = tk.Label(self.LAB_FRM_Player);
          self.LAB_PLAYER_Card_1.configure(image=self.Player_Card_1, borderwidth=3, relief="ridge", text="Card 1");
          self.LAB_PLAYER_Card_1.place(anchor="nw", height=150, width=100, x=25, y=5);
                     
          Player_Card_IMAGE_2 = Image.open(self.CARD_Directory + "KING_diamonds.jpg");
          Player_Card_IMAGE_2 = Player_Card_IMAGE_2.resize((85, 130), Image.ANTIALIAS);
          self.Player_Card_2 = ImageTk.PhotoImage(Player_Card_IMAGE_2);
          self.LAB_PLAYER_Card_2 = tk.Label(self.LAB_FRM_Player);
          self.LAB_PLAYER_Card_2.configure(image=self.Player_Card_2, borderwidth=3, relief="ridge", text="Card 2");
          self.LAB_PLAYER_Card_2.place(anchor="nw", height=150, width=100, x=150, y=5);
                         
          Player_Card_IMAGE_3 = Image.open(self.CARD_Directory + "QUEEN_hearts.jpg");
          Player_Card_IMAGE_3 = Player_Card_IMAGE_3.resize((85, 130), Image.ANTIALIAS);
          self.Player_Card_3 = ImageTk.PhotoImage(Player_Card_IMAGE_3);
          self.LAB_PLAYER_Card_3 = tk.Label(self.LAB_FRM_Player);
          self.LAB_PLAYER_Card_3.configure(image=self.Player_Card_3, borderwidth=3, relief="ridge", text="Card 3");
          self.LAB_PLAYER_Card_3.place(anchor="nw", height=150, width=100, x=280, y=5);

          Player_Card_IMAGE_4 = Image.open(self.DEALER_Directory + "Twilight_Sparkle_3.jpg");
          Player_Card_IMAGE_4 = Player_Card_IMAGE_4.resize((85, 130), Image.ANTIALIAS);
          self.Player_Card_4 = ImageTk.PhotoImage(Player_Card_IMAGE_4);
          self.LAB_PLAYER_Card_4 = tk.Label(self.LAB_FRM_Player)
          self.LAB_PLAYER_Card_4.configure(image=self.Player_Card_4, borderwidth=3, relief="ridge", text="Card 4");
          self.LAB_PLAYER_Card_4.place(anchor="nw", height=150, width=100, x=25, y=165);

          Player_Card_IMAGE_5 = Image.open(self.DEALER_Directory + "Fluttershy_3.jpg");
          Player_Card_IMAGE_5 = Player_Card_IMAGE_5.resize((85, 130), Image.ANTIALIAS);
          self.Player_Card_5 = ImageTk.PhotoImage(Player_Card_IMAGE_5);
          self.LAB_PLAYER_Card_5 = tk.Label(self.LAB_FRM_Player);
          self.LAB_PLAYER_Card_5.configure(image=self.Player_Card_5, borderwidth=3, relief="ridge", text="Card 5");
          self.LAB_PLAYER_Card_5.place(anchor="nw", height=150, width=100, x=150, y=165);

          Player_Card_IMAGE_6 = Image.open(self.DEALER_Directory + "Rainbow_Dash_6.png");
          Player_Card_IMAGE_6 = Player_Card_IMAGE_6.resize((85, 130), Image.ANTIALIAS);
          self.Player_Card_6 = ImageTk.PhotoImage(Player_Card_IMAGE_6);
          self.LAB_PLAYER_Card_6 = tk.Label(self.LAB_FRM_Player);
          self.LAB_PLAYER_Card_6.configure(image=self.Player_Card_6, borderwidth=3, relief="ridge", text="Card 6");
          self.LAB_PLAYER_Card_6.place(anchor="nw", height=150, width=100, x=280, y=165);

    #---C. Frame: Dealer ---------------------------------------------------        
          self.LAB_FRM_Dealer = tk.LabelFrame(self.FRM_Main_Window);
          self.LAB_FRM_Dealer.configure(height=400, width=410, background="#006400", foreground="#FFFFFF", borderwidth=3, relief="sunken", text="DEALER");
          self.LAB_FRM_Dealer.place(anchor="nw", height=345, width=410, x=430, y=5);        

          Dealer_Card_IMAGE_1 = Image.open(self.CARD_Directory + "SEVEN_hearts.jpg");
          Dealer_Card_IMAGE_1 = Dealer_Card_IMAGE_1.resize((85, 130), Image.ANTIALIAS);
          self.Dealer_Card_1 = ImageTk.PhotoImage(Dealer_Card_IMAGE_1);
          self.LAB_DEALER_Card_1 = tk.Label(self.LAB_FRM_Dealer);
          self.LAB_DEALER_Card_1.configure(image=self.Dealer_Card_1, borderwidth=3, relief="ridge", text="Card 1");
          self.LAB_DEALER_Card_1.place(anchor="nw", height=150, width=100, x=25, y=5);

          Dealer_Card_IMAGE_2 = Image.open(self.CARD_Directory + "JACK_diamonds.jpg");
          Dealer_Card_IMAGE_2 = Dealer_Card_IMAGE_2.resize((85, 130), Image.ANTIALIAS);
          self.Dealer_Card_2 = ImageTk.PhotoImage(Dealer_Card_IMAGE_2);
          self.LAB_DEALER_Card_2 = tk.Label(self.LAB_FRM_Dealer);
          self.LAB_DEALER_Card_2.configure(image=self.Dealer_Card_2, borderwidth=3, relief="ridge", text="Card 2");
          self.LAB_DEALER_Card_2.place(anchor="nw", height=150, width=100, x=150, y=5);

          Dealer_Card_IMAGE_3 = Image.open(self.CARD_Directory + "SEVEN_diamonds.jpg");
          Dealer_Card_IMAGE_3 = Dealer_Card_IMAGE_3.resize((85, 130), Image.ANTIALIAS);
          self.Dealer_Card_3 = ImageTk.PhotoImage(Dealer_Card_IMAGE_3);
          self.LAB_DEALER_Card_3 = tk.Label(self.LAB_FRM_Dealer);
          self.LAB_DEALER_Card_3.configure(image=self.Dealer_Card_3, borderwidth=3, relief="ridge", text="Card 3");
          self.LAB_DEALER_Card_3.place(anchor="nw", height=150, width=100, x=280, y=5);

          Dealer_Card_IMAGE_4 = Image.open(self.DEALER_Directory + "AppleJack_6.jpg");
          Dealer_Card_IMAGE_4 = Dealer_Card_IMAGE_4.resize((85, 130), Image.ANTIALIAS);
          self.Dealer_Card_4 = ImageTk.PhotoImage(Dealer_Card_IMAGE_4);
          self.LAB_DEALER_Card_4 = tk.Label(self.LAB_FRM_Dealer);
          self.LAB_DEALER_Card_4.configure(image=self.Dealer_Card_4, borderwidth=3, relief="ridge", text="Card 4");
          self.LAB_DEALER_Card_4.place(anchor="nw", height=150, width=100, x=25, y=165);

          Dealer_Card_IMAGE_5 = Image.open(self.DEALER_Directory + "Rarity_3.jpg");
          Dealer_Card_IMAGE_5 = Dealer_Card_IMAGE_5.resize((85, 130), Image.ANTIALIAS);
          self.Dealer_Card_5 = ImageTk.PhotoImage(Dealer_Card_IMAGE_5);
          self.LAB_DEALER_Card_5 = tk.Label(self.LAB_FRM_Dealer);
          self.LAB_DEALER_Card_5.configure(image=self.Dealer_Card_5, borderwidth=3, relief="ridge", text="Card 5");
          self.LAB_DEALER_Card_5.place(anchor="nw", height=150, width=100, x=150, y=165);

          Dealer_Card_IMAGE_6 = Image.open(self.DEALER_Directory + "Pinkie_Pie_6.png");
          Dealer_Card_IMAGE_6 = Dealer_Card_IMAGE_6.resize((85, 130), Image.ANTIALIAS);
          self.Dealer_Card_6 = ImageTk.PhotoImage(Dealer_Card_IMAGE_6);
          self.LAB_DEALER_Card_6 = tk.Label(self.LAB_FRM_Dealer);
          self.LAB_DEALER_Card_6.configure(image=self.Dealer_Card_6, borderwidth=3, relief="ridge", text="Card 6");
          self.LAB_DEALER_Card_6.place(anchor="nw", height=150, width=100, x=280, y=165);

    #---D. Frame: Game Actions ---------------------------------------------------     
          self.LAB_FRM_Game_Actions = tk.LabelFrame(self.FRM_Main_Window);
          self.LAB_FRM_Game_Actions.configure(height=155, width=230, background="#006400", foreground="#FFFFFF", borderwidth=3, relief="sunken", text="Game Actions");
          self.LAB_FRM_Game_Actions.place(anchor="nw", height=130, width=230, x=10, y=355);

          self.BTN_Start = tk.Button(self.LAB_FRM_Game_Actions, command=Handle_Button_Start);
          self.BTN_Start.configure(height=30, width=100, justify="center", text="START", background="#FFFFFF", foreground="#FF0000");
          self.BTN_Start.place(anchor="nw", height=30, width=100, x=10, y=5);

          self.BTN_Quit = tk.Button(self.LAB_FRM_Game_Actions, command=Handle_Button_Quit)
          self.BTN_Quit.configure(height=30, width=100, justify="center", text="QUIT", background="#FFFFFF", foreground="#FF0000");
          self.BTN_Quit.place(anchor="nw", height=30, width=100, x=10, y=40);

          self.BTN_Talk = tk.Button(self.LAB_FRM_Game_Actions, command=Handle_Button_Talk)
          self.BTN_Talk.configure(height=30, width=100, justify="center", text="TALK", background="#FFFFFF", foreground="#FF0000");
          self.BTN_Talk.place(anchor="nw", height=30, width=100, x=10, y=75);

          self.BTN_Deal = tk.Button(self.LAB_FRM_Game_Actions, command=Handle_Button_Deal);
          self.BTN_Deal.configure(height=30, width=100, justify="center", text="DEAL", background="#FFFFFF", foreground="#FF0000");
          self.BTN_Deal.place(anchor="nw", height=30, width=100, x=115, y=5);

          self.BTN_Hit = tk.Button(self.LAB_FRM_Game_Actions, command=Handle_Button_Hit);
          self.BTN_Hit.configure(height=30, width=100, justify="center", text="HIT", background="#FFFFFF", foreground="#FF0000");
          self.BTN_Hit.place(anchor="nw", height=30, width=100, x=115, y=40);

          self.BTN_Stay = tk.Button(self.LAB_FRM_Game_Actions, command=Handle_Button_Stay);
          self.BTN_Stay.configure(height=30, width=100, justify="center", text="STAY", background="#FFFFFF", foreground="#FF0000");
          self.BTN_Stay.place(anchor="nw", height=30, width=100, x=115, y=75);

    #---E. Frame: Betting ---------------------------------------------------    
          self.LAB_FRM_Betting = tk.LabelFrame(self.FRM_Main_Window);
          self.LAB_FRM_Betting.configure(height=130, width=110, background="#006400", foreground="#ffffff", borderwidth=3, relief="sunken", text="Betting");
          self.LAB_FRM_Betting.place(anchor="nw", height=130, width=170, x=250, y=355);

          self.ENT_Betting = tk.Entry(self.LAB_FRM_Betting,textvariable=self.Bet_Text);
          self.ENT_Betting.configure(width=125, justify="center", relief="sunken", state="normal"); #Note: To mask, use show='*'
          self.ENT_Betting.place(anchor="nw", height=30, width=125, x=20, y=5);

          self.BTN_Bet = tk.Button(self.LAB_FRM_Betting, command=Handle_Button_Bet);
          self.BTN_Bet.configure(height=25, width=125, justify="center", text="BET", background="#FF0000", foreground="#FFFFFF");
          self.BTN_Bet.place(anchor="nw", height=25, width=125, x=20, y=45);

          self.BTN_GO = tk.Button(self.LAB_FRM_Betting, command=Handle_Button_GO);
          self.BTN_GO.configure(height=25, width=60, justify="center", text="GO", background="#FFFFFF", foreground="#FF0000");
          self.BTN_GO.place(anchor="nw", height=25, width=60, x=21, y=80);

          self.BTN_Cheat = tk.Button(self.LAB_FRM_Betting, command=Handle_Button_Cheat);
          self.BTN_Cheat.configure(height=25, width=55, justify="center", text="CHEAT", background="#FFFFFF", foreground="#FF0000");
          self.BTN_Cheat.place(anchor="nw", height=25, width=55, x=90, y=80);

    #---F. Frame: Game Stats ---------------------------------------------------    
          self.LAB_FRM_Game_Stats = tk.LabelFrame(self.FRM_Main_Window);
          self.LAB_FRM_Game_Stats.configure(height=130, width=410, background="#006400", foreground="#FFFFFF", borderwidth=3, relief="sunken", text="Game Stats");
          self.LAB_FRM_Game_Stats.place(anchor="nw", height=130, width=410, x=430, y=355);

          self.LAB_Player_Wins = tk.Label(self.LAB_FRM_Game_Stats);
          self.LAB_Player_Wins.configure(justify=tk.LEFT, anchor="w", background="#006400", foreground="#FFFFFF", text="Player Wins:");
          self.LAB_Player_Wins.place(anchor="w", width=75, x=3, y=12);

          self.LAB_Player_Wins_Output = tk.Label(self.LAB_FRM_Game_Stats);
          self.LAB_Player_Wins_Output.configure(justify=tk.CENTER, borderwidth=3, relief="sunken", takefocus=False);
          self.LAB_Player_Wins_Output.place(anchor="w", width=100, x=83, y=12);

          self.LAB_Player_Cash = tk.Label(self.LAB_FRM_Game_Stats);
          self.LAB_Player_Cash.configure(justify=tk.LEFT, anchor="w", background="#006400", foreground="#FFFFFF", text="Player Cash:");
          self.LAB_Player_Cash.place(anchor="w", width=75, x=3, y=40);

          self.LAB_Player_Cash_Output = tk.Label(self.LAB_FRM_Game_Stats);
          self.LAB_Player_Cash_Output.configure(justify=tk.CENTER, borderwidth=3, relief="sunken", takefocus=False);
          self.LAB_Player_Cash_Output.place(anchor="w", width=100, x=83, y=40);

          self.LAB_PLAYER_Pts = tk.Label(self.LAB_FRM_Game_Stats);
          self.LAB_PLAYER_Pts.configure(justify=tk.LEFT, anchor="w", background="#006400", foreground="#FFFFFF", text="Player Points:");
          self.LAB_PLAYER_Pts.place(anchor="w", width=75, x=3, y=68);

          self.LAB_PLAYER_Pts_Output = tk.Label(self.LAB_FRM_Game_Stats);
          self.LAB_PLAYER_Pts_Output.configure(justify=tk.CENTER, borderwidth=3, relief="sunken", takefocus=False);
          self.LAB_PLAYER_Pts_Output.place(anchor="w", width=100, x=83, y=68);          

          self.LAB_Current_Bet = tk.Label(self.LAB_FRM_Game_Stats);
          self.LAB_Current_Bet.configure(justify=tk.LEFT, anchor="w", background="#006400", foreground="#FFFFFF", text="Current Bet:");
          self.LAB_Current_Bet.place(anchor="w", width=75, x=3, y=97);

          self.LAB_Current_Bet_Output = tk.Label(self.LAB_FRM_Game_Stats);
          self.LAB_Current_Bet_Output.configure(justify=tk.CENTER, borderwidth=3, relief="sunken", takefocus=False);
          self.LAB_Current_Bet_Output.place(anchor="w", width=100, x=83, y=96);

          self.LAB_Dealer_Wins = tk.Label(self.LAB_FRM_Game_Stats);
          self.LAB_Dealer_Wins.configure(justify=tk.LEFT, anchor="w", background="#006400", foreground="#FFFFFF", text="Dealer Wins:");
          self.LAB_Dealer_Wins.place(anchor="nw", width=80, x=205, y=0);

          self.LAB_Dealer_Wins_Output = tk.Label(self.LAB_FRM_Game_Stats);
          self.LAB_Dealer_Wins_Output.configure(justify=tk.CENTER, borderwidth=3, relief="sunken");
          self.LAB_Dealer_Wins_Output.place(anchor="nw", width=100, x=295, y=0);

          self.LAB_Dealer_Cash = tk.Label(self.LAB_FRM_Game_Stats);
          self.LAB_Dealer_Cash.configure(justify=tk.LEFT, anchor="w", background="#006400", foreground="#FFFFFF", text="Dealer Cash:");
          self.LAB_Dealer_Cash.place(anchor="nw", width=84, x=205, y=29);

          self.LAB_Dealer_Cash_Output = tk.Label(self.LAB_FRM_Game_Stats);
          self.LAB_Dealer_Cash_Output.configure(justify=tk.CENTER, borderwidth=3, relief="sunken");
          self.LAB_Dealer_Cash_Output.place(anchor="nw", width=100, x=295, y=28);

          self.LAB_DEALER_Pts = tk.Label(self.LAB_FRM_Game_Stats);
          self.LAB_DEALER_Pts.configure(justify=tk.LEFT, anchor="w", background="#006400", foreground="#FFFFFF",text="Dealer Points:");
          self.LAB_DEALER_Pts.place(anchor="nw", width=80, x=205, y=56);

          self.LAB_DEALER_Pts_Output = tk.Label(self.LAB_FRM_Game_Stats);
          self.LAB_DEALER_Pts_Output.configure(justify=tk.CENTER, borderwidth=3, relief="sunken", takefocus=False);
          self.LAB_DEALER_Pts_Output.place(anchor="nw", width=100, x=295, y=56); 

          self.LAB_Money_In_Pot = tk.Label(self.LAB_FRM_Game_Stats);
          self.LAB_Money_In_Pot.configure(justify=tk.LEFT, anchor="w", background="#006400", foreground="#FFFFFF",text="Money in Pot:");
          self.LAB_Money_In_Pot.place(anchor="nw", width=80, x=205, y=85);

          self.LAB_Money_In_Pot_Output = tk.Label(self.LAB_FRM_Game_Stats);
          self.LAB_Money_In_Pot_Output.configure(justify=tk.CENTER, borderwidth=3, relief="sunken", takefocus=False);
          self.LAB_Money_In_Pot_Output.place(anchor="nw", width=100, x=295, y=85);          

    #---G. Frame: Game Text Output Window -------------------------------------------------------------
          self.LAB_FRM_Game_Txt_Output = tk.LabelFrame(self.FRM_Main_Window);
          self.LAB_FRM_Game_Txt_Output.configure(height=190, width=640, background="#006400", foreground="#FFFFFF", borderwidth=3, relief="sunken", text="Game Text output");    
          self.LAB_FRM_Game_Txt_Output.place(anchor="nw", height=190, width=640, x=10, y=491);

          self.SB_Vert_TXT_Main_Output = tk.Scrollbar(self.LAB_FRM_Game_Txt_Output, orient = tk.VERTICAL);
          self.SB_Vert_TXT_Main_Output.pack(side=tk.RIGHT, fill=tk.Y);

          self.TXT_Game_Txt_Output  = tk.Text(self.LAB_FRM_Game_Txt_Output);
          self.TXT_Game_Txt_Output.configure(height=160, width=605, background="#000000", foreground="#ffffff", borderwidth=3, relief="sunken", font="{Courier} 12 {}");
          self.TXT_Game_Txt_Output.place(anchor="nw", height=160, width=605, x=5, y=5);

          self.SB_Vert_TXT_Main_Output.config(command=self.TXT_Game_Txt_Output.yview); #set scrollbar behavior    
          
    #--- Default Load Settings -------------------------------------------------------------          
          self.Initialize_Game();    

#---End Class----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-----Invocations-----
GUI = BlackJack_GUI(window); #instantiate GUI class

#---Launch Main Window---
window.mainloop();

    