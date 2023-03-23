from termcolor import colored
print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
score = 0

if playing.lower() != "yes":
    quit()
print("Ok! Let's play :) ")


answer = input("What does CPU stand for? ")
correct_answer = "Central Processing Unit"
if answer.title() == correct_answer:
    print("Correct!")
    score += 1
else:
    print("Wrong! the correct answer is " + str(correct_answer))

print("")
answer = input("What does GPU stand for? ")
correct_answer = "Graphics Processing Unit"
if answer.title() == correct_answer:
    print('Correct!')
    score += 1
else:
    print("Wrong! the correct answer is " + str(correct_answer))

print("")
answer = input("What does RAM stand for? ")
correct_answer = "Random Access Memory"
if answer.title() == correct_answer:
    print('Correct!')
    score += 1
else:
    print("Wrong! the correct answer is " + str(correct_answer))


print("")
answer = input("What does DDR stand for? ")
correct_answer = "Double Data Rate"
if answer.title() == correct_answer:
    print('Correct!')
    score += 1
else:
    print("Wrong! the correct answer is " + str(correct_answer))

print("")
answer = input("What does DV stnad for? ")
correct_answer = "Digital Video"
if answer.title() == correct_answer:
    print('Correct!')
    score += 1
else:
    print("Wrong! the correct answer is " + str(correct_answer))

print("")
answer = input("What does DVD stand for? ")
correct_answer = "Digital Versatile Disc"
if answer.title() == "Digital Versatile Disc":
    print('Correct!')
    score += 1
else:
    print("Wrong! the correct answer is " + str(correct_answer))

print("")
answer = input("What does DVD+R stand for? ")
correct_answer = "Digital Versatile Disc Recordable"
if answer.title() == correct_answer:
    print('Correct!')
    score += 1
else:
    print("Wrong! the correct answer is " + str(correct_answer))

print("")
answer = input("What does DVD-RAM stand for? ")
correct_answer = "Digital Versatile Disc Random Access Memory"
if answer.title() == correct_answer:
    print('Correct!')
    score += 1
else:
    print("Wrong! the correct answer is " + str(correct_answer))

print("")
answer = input("What does DVI stand for? ")
correct_answer = "Digital Video Interface"
if answer.title() == correct_answer:
    print('Correct!')
    score += 1
else:
    print("Wrong! the correct answer is " + str(correct_answer))

print("")
answer = input("What does HDD stand for? ")
correct_answer = "Hard Disk Drive"
if answer.title() == correct_answer:
    print('Correct!')
    score += 1
else:
    print("Wrong! the correct answer is " + str(correct_answer))

print("")
answer = input("What does HDMI stand for? ")
correct_answer = "High-Definition Multimedia Interface"
if answer.title() == correct_answer:
    print('Correct!')
    score += 1
else:
    print("Wrong! the correct answer is " + str(correct_answer))

print("")
answer = input("What does I/O stand for? ")
correct_answer = "Input/Output"
if answer.title() == correct_answer:
    print('Correct!')
    score += 1
else:
    print("Wrong! the correct answer is " + str(correct_answer))

print("")
answer = input("What does MAC Address stand for? ")
correct_answer = "Media Access Control Address"
if answer.title() == correct_answer:
    print('Correct!')
    score += 1
else:
    print("Wrong! the correct answer is " + str(correct_answer))

print("")
answer = input("What does PCI stand for? ")
correct_answer = "Peripheral Component Interconnect"
if answer.title() == correct_answer:
    print('Correct!')
    score += 1
else:
    print("Wrong! the correct answer is " + str(correct_answer))

print("")
answer = input("What does PROM stand for? ")
correct_answer = "Programmable Read-Only Memory"
if answer.title() == correct_answer:
    print('Correct!')
    score += 1
else:
    print("Wrong! the correct answer is " + str(correct_answer))

print("")
answer = input("What does SRAM stand for? ")
correct_answer = "Static Random Access Memory"
if answer.title() == correct_answer:
    print('Correct!')
    score += 1
else:
    print("Wrong! the correct answer is " + str(correct_answer))

print("")
answer = input("Whad does SSD stand for? ")
correct_answer = "Solid State Drive"
if answer.title() == correct_answer:
    print('Correct!')
    score += 1
else:
    print("Wrong! the correct answer is " + str(correct_answer))

print("")
answer = input("What does FSB stand for? ")
correct_answer = "Front Side Bus"
if answer.title() == correct_answer:
    print('Correct!')
    score += 1
else:
    print("Wrong! the correct answer is " + str(correct_answer))

print("")
answer = input("What does UPS stand for? ")
correct_answer = "Uninterruptible Power System"
if answer.title() == correct_answer:
    print('Correct!')
    score += 1
else:
    print("Wrong! the correct answer is " + str(correct_answer))

print("")
answer = input("What does USB stand for? ")
correct_answer = "Universal Serial Bus"
if answer.title() == correct_answer:
    print('Correct!')
    score += 1
else:
    print("Wrong! the correct answer is " + str(correct_answer))

print("")
if score >= 10:
    print(colored("You got " + str(score / 20 * 100) + "%", "green"))
else:
    print(colored("You got " + str(score / 20 * 100) + "%", "red"))
