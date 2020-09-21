next=True
while next==True:
    print('''
    1.Aries
    2.Tauras
    3.Gemini
    4.Cancer
    5.Leo
    6.Virgo
    7.Libra
    8.Scorpio
    9.Capricorn
    10.Sagittarius
    11.Aquarius
    12.Pisces''')
    s=int(input("pick your no and press enter\n"))
    if s==1:
        print(" This is not the day to either sell or buy property. Your reluctance in spending money on something you accord a lower priority may not be right. A new project will proceed smoothly as you get help from all quarters. Good will power in sticking to the exercise regime will help you in coming back in shape.")
    elif s==2:
        print("Your mood swings can make you miss a profitable opportunity, so do something about it. You will be able to put across your points effectively on the professional front. Be considerate of a family member in all your domestic decisions. Tread carefully while discussing a property issue. ")
    elif s==3:
        print("Be careful with whom you associate romantically as a two-timing individual may prove disastrous for your peace of mind.")
    elif s==4:
        print("You may find yourself in romantic mood today, so make the most of it!")
    elif s==5:
        print("A family youngster may make you proud by his or her achievement. This is a favourable day to seal a property deal. Your professional skills are likely to be acknowledged at work. ")
    elif s==6:
        print("It is time you turned your attention to saving by becoming more careful of your spending. You will be able to give a good account of yourself by solving workplace problems. A few new exercises will benefit those trying to bring specific body parts in shape.")
    elif s==7:
        print("An outdoor activity is likely to give you a chance for sweating out. A child may need guidance, so spare some time for him or her. You are likely to burn the bridges by a few wrong professional moves, if you are not careful.")
    elif s==8:
         print("A new source of income is likely to make your financial worries disappear. A change of medication will save those unwell from side effects.")
    elif s==9:
          print("Chance to earn big money may present itself to those running their own business. ")  
    elif s==10:
          print(" On the financial front, a new source of income is likely to be tapped soon that may get your coffers brimming! Successfully completing an assigned job will give you the edge at work.") 
    elif s==11:
          print("You may choose to wait for better investment options, before committing your money. New dimensions open up on the professional front as you handle more than one project.")
    elif s==12:
          print("Financially, your position remains sound and opportunities to earn materialise. Adopting a disciplined life and change in lifestyle will help in restoring energy and health.")
    else:
        print("hey you sure about the number")
    next=True if input ("shall we do again\n (y/n)")=="Y" else False 
        
