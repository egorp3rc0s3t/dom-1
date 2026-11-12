print("добро пожаловать")
name= input("введите ваше имя: ")
print("Hello,",name)
bet = input("Enter your bet:")
print("Your bet is: ", bet)
bet = int(bet)
number = input("Enter a number between 1 and 10: ")
number = int(number)
import random
random_number = random.randint(1, 10)
if number == random_number:
    win_amout = bet * 2
    print("you win: ", win_amout) 
    
if number != random_number:
    print("you looser")
print("ваше число: ", number)
print("правильное число: ", random_number)