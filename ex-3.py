# Kaun Banega Karur Proti


# Capable of displaying questions to the user like KBC(Kon Banega Crore-poti)
# Use List data type to store the questions and their correct answer
# Display the final amount that the person is taking home after playing game


questions = [
            ["Which language was used to create fb?", "Python",
                "Java", "Javscript", "Php", "None", 4],
            ["Which language was used to create fb?", "Python",
                "Java", "Javscript", "Php", "None", 4],
            ["Which language was used to create fb?", "Python",
                "Java", "Javscript", "Php", "None", 4],
            ["Which language was used to create fb?", "Python",
                "Java", "Javscript", "Php", "None", 4],
            ["Which language was used to create fb?", "Python",
                "Java", "Javscript", "Php", "None", 4],
            ["Which language was used to create fb?", "Python",
                "Java", "Javscript", "Php", "None", 4],
            ["Which language was used to create fb?", "Python",
                "Java", "Javscript", "Php", "None", 4],
            ["Which language was used to create fb?", "Python",
                "Java", "Javscript", "Php", "None", 4],
            ["Which language was used to create fb?", "Python",
                "Java", "Javscript", "Php", "None", 4],
            ["Which language was used to create fb?", "Python",
                "Java", "Javscript", "Php", "None", 4],
            ["Which language was used to create fb?", "Python",
                "Java", "Javscript", "Php", "None", 4],
            ["Which language was used to create fb?", "Python",
                "Java", "Javscript", "Php", "None", 4]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000,
          50000, 100000, 500000, 1000000, 5000000, 10000000]
money = 0

for i in range(0, len(questions)):
    question = questions[i]

    print(f"Question for Rs. {levels[i]} : ")
    print(f"{questions[i][0]}")
    print(f"a. {question[1]}       b. {question[2]}")
    print(f"c. {question[3]}       d. {question[4]}")

    reply = int(input("Enter your answer (1-4) or 0 to quit : "))

    if (reply == 0):
        money = levels[i-1]
        break

    if (reply == question[-1]):
        print(f"Correct answer, You have won Rs. {levels[i]}.\n\n")
        if (i == 4):
            money = 10000
        elif (i == 7):
            money = 100000
        elif (i == 9):
            money = 1000000
        elif (i == 11):
            money = 10000000
    else:
        print("Wrong answer.")
        break


print(f"Your take home money is {money}.")
