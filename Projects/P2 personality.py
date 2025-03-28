# Beginning: create variables 
salty_points = 0
sweet_points = 0

#Middle:Ask questions 
        #question 1:
answer = input ("Would you rather A) eat popcorn all day, or B) eat ice cream all day")
if answer == "A":
        salty_points += 1
elif answer == "B":
        sweet_points += 1

        #question 2:
answer = input ("Would you rather A) eat chips all day, or B) eat candy all day")
if answer == "A":
        salty_points+= 1
elif answer == "B":
        sweet_points+= 1

        #question 3:
answer = input ("Would you rather A) eat salty seaweed all day, or B) eat sweet seaweed all day") 
if answer == "A":
        salty_points+= 1
elif answer == "B":
        sweet_points+= 1
        #question 4:
answer = input ("Would you rather A) eat pretzel all day, or B) eat chocolate all day")
if answer == "A":
        salty_points+= 1
elif answer == "B":
        sweet_points+= 1
        #question 5:
answer = input ("Would you rather A) eat fries all day, or B) eat doughnuts all day")
if answer == "A":
        salty_points+= 1
elif answer == "B":
        sweet_points+= 1
#end of quiz
if salty_points > sweet_points:
        print ("You are a salty person")
elif sweet_points > salty_points:
        print ("You are a sweet person")