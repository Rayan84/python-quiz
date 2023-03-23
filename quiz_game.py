from termcolor import colored
print("""
 _____                             _              _____                   _             _                   
/  __ \                           | |            |_   _|                 (_)           | |                  
| /  \/ ___  _ __ ___  _ __  _   _| |_ ___ _ __    | | ___ _ __ _ __ ___  _ _ __   ___ | | ___   __ _ _   _ 
| |    / _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__|   | |/ _ \ '__| '_ ` _ \| | '_ \ / _ \| |/ _ \ / _` | | | |
| \__/\ (_) | | | | | | |_) | |_| | ||  __/ |      | |  __/ |  | | | | | | | | | | (_) | | (_) | (_| | |_| |
 \____/\___/|_| |_| |_| .__/ \__,_|\__\___|_|      \_/\___|_|  |_| |_| |_|_|_| |_|\___/|_|\___/ \__, |\__, |
                      | |                                                                        __/ | __/ |
                      |_|                                                                       |___/ |___/ 
""")

playing = input("Do you want to play? ")

print("")

if playing.lower() != "yes":
    quit()
print("Ok! Let's play :) ")


def result(val):
    print("")
    if val >= 10:
        print(colored("Success! You got " + str(val / 20 * 100) + "%", "green"))
    else:
        print(colored("Fail! You got " + str(val / 20 * 100) + "%", "red"))


def main():
    print("main running")
    score = 0
    question = ["What does CPU stand for?", "What does GPU stand for?", "What does RAM stand for?", "What does DDR stand for?", "What does DV stnad for? ", "What does DVD stand for?", "What does DVD+R stand for? ", "What does DVD-RAM stand for? ", "What does DVI stand for? ", "What does HDD stand for? ",
                "What does HDMI stand for? ", "What does I/O stand for? ", "What does MAC Address stand for? ", "What does PCI stand for? ", "What does PROM stand for? ", "What does SRAM stand for? ", "Whad does SSD stand for? ", "What does FSB stand for? ", "What does UPS stand for? ", "What does USB stand for? "]
    correct_answer = ["Central Processing Unit", "Graphics Processing Unit", "Random Access Memory", "Double Data Rate", "Digital Video", "Digital Versatile Disc", "Digital Versatile Disc Recordable", "Digital Versatile Disc Random Access Memory", "Digital Video Interface", "Hard Disk Drive",
                      "High-Definition Multimedia Interface", "Input/Output", "Media Access Control Address", "Peripheral Component Interconnect", "Programmable Read-Only Memory", "Static Random Access Memory", "Solid State Drive", "Front Side Bus", "Uninterruptible Power System", "Universal Serial Bus"]
    i = 0
    while i < 20:
        print("")
        print(question[i])
        user_answer = input()
        if user_answer.title() == correct_answer[i]:
            print(colored("Correct!", "green"))
            score += 1
        else:
            print(colored("Wrong!, the correct answer is: " +
                  str(correct_answer[i]), "red"))
        i += 1
    result(score)


main()
