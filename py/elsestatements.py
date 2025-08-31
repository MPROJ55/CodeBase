user_choice_0 = int(input("What is your favorite number? "))

if user_choice_0 < 100: 
    print("small number")
elif 100 <= user_choice_0 <= 500:
    print("large number")
else: 
    print("Massive number")
