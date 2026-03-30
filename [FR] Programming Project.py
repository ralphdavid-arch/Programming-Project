print("Welcome to Cyber Duel\n")
print("Some random fancy message\n")

print("Hacker Moves Table")
print("Choice   Move           Cost        Effect")
print("1        DDos Attack    15 Energy  Inflicts 20 Damage to the SysAdmin")
print("2        Phising Scam   10 HP      Restores 20 Energy (Capped at 100)")
print("3        Stealth Mode   10 Energy  Blocks SysAdmin's Firewall Purge\n")

print("SysAdmin Moves Table")
print("Choice   Move            Cost        Effect")
print("1        Firewall Purge  15 Energy  Inflicts 20 Damage (Blocked by Stealth)")
print("2        Reboot System   10 HP      Restores 20 Energy (Capped at 100)")
print("3        Trace Route     10 Energy  Inflicts 10 Damage; Bypasses Stealth\n")

Hacker = input("Hacker, who are you? ")
if Hacker == "":
    Hacker = "Neo"

SysAdmin = input("SysAdmin, who are you? ")
if SysAdmin == "":
    SysAdmin = "Agent Smith"

def display_stats(Hname, Hhealth, Henergy, Sname, Shealth, Senergy):
    print("\n==================== Round Stats ====================")
    print(Hname + "          | " + Sname)
    print("Health: " + str(Hhealth) + "    | Health: " + str(Shealth))
    print("Energy: " + str(Henergy) + "    | Energy: " + str(Senergy))
    print("====================================================\n")

def get_move(player):
    while True:
        move = input(player + ", enter your 3-digit move combo (1,2,3 only): ")
        # assign each digit to a separate variable
        m1 = move[0]
        m2 = move[1]
        m3 = move[2]
        if (m1 == "1" or m1 == "2" or m1 == "3") and \
           (m2 == "1" or m2 == "2" or m2 == "3") and \
           (m3 == "1" or m3 == "2" or m3 == "3"):
            return m1, m2, m3
        print("Invalid input! Must be 3 digits using only 1,2,3.\n")

def game():
    Hhealth = 100
    Henergy = 30
    Shealth = 100
    Senergy = 30
    round_count = 1
    stealth_active = False

    while Hhealth > 0 and Shealth > 0:
        print("=============== Round " + str(round_count) + " ===============")

        if round_count % 3 == 0:
            print("Warning: OVERHEAT -10 Health to both players!")
            Hhealth -= 10
            Shealth -= 10

        display_stats(Hacker, Hhealth, Henergy, SysAdmin, Shealth, Senergy)

        h1, h2, h3 = get_move(Hacker)
        s1, s2, s3 = get_move(SysAdmin)

        stealth_active = False
        if h1 == "1" or h2 == "1" or h3 == "1":
            if Henergy >= 15:
                print(Hacker + " used DDos Attack!")
                Henergy -= 15
                Shealth -= 20
            else:
                print(Hacker + " tried DDos Attack but not enough energy!")

        if h1 == "2" or h2 == "2" or h3 == "2":
            print(Hacker + " used Phising Scam!")
            Hhealth -= 10
            Henergy += 20
            if Henergy > 100:
                Henergy = 100

        if h1 == "3" or h2 == "3" or h3 == "3":
            if Henergy >= 10:
                print(Hacker + " used Stealth Mode!")
                Henergy -= 10
                stealth_active = True
            else:
                print(Hacker + " tried Stealth Mode but not enough energy!")

        if s1 == "3" or s2 == "3" or s3 == "3":
            if Senergy >= 10:
                print(SysAdmin + " used Trace Route!")
                Senergy -= 10
                Hhealth -= 10
            else:
                print(SysAdmin + " tried Trace Route but not enough energy!")

        if s1 == "1" or s2 == "1" or s3 == "1":
            if stealth_active:
                print(SysAdmin + "'s Firewall Purge blocked by " + Hacker + "'s Stealth Mode!")
            elif Senergy >= 15:
                print(SysAdmin + " used Firewall Purge!")
                Senergy -= 15
                Hhealth -= 20
            else:
                print(SysAdmin + " tried Firewall Purge but not enough energy!")

        if s1 == "2" or s2 == "2" or s3 == "2":
            print(SysAdmin + " used Reboot System!")
            Shealth -= 10
            Senergy += 20
            if Senergy > 100:
                Senergy = 100

        display_stats(Hacker, Hhealth, Henergy, SysAdmin, Shealth, Senergy)

        if Hhealth <= 0 and Shealth <= 0:
            print("Double K.O! It's a tie!")
            break
        elif Hhealth <= 0:
            print(SysAdmin + " wins!")
            break
        elif Shealth <= 0:
            print(Hacker + " wins!")
            break

        round_count += 1

    choice = input("Do you wish to continue? (1-Rematch / 2-Finish) ")
    if choice == "1":
        game()
    else:
        print("Game Over")

game()