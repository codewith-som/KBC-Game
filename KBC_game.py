import random
import time
import threading
import sys
import os

# ---------------- QUESTIONS ----------------
questions = [
["Which of the following states doesn’t share its boundary with Gujarat?",
 ["Maharashtra","Rajasthan","Madhya Pradesh","Goa"], 4],

["Kans, brother of Devaki, ruled which city?",
 ["Mathura","Dwarka","Indraprastha","Ujjain"], 1],

["Who wrote Romeo and Juliet?",
 ["Oscar Wilde","William Shakespeare","Jane Austen","Scott Fitzgerald"], 2],

["Which state is called Dev Bhoomi?",
 ["Uttarakhand","Rajasthan","Himachal Pradesh","Arunachal Pradesh"], 1],

["Most ODI centuries?",
 ["Sachin Tendulkar","Virat Kohli","Rohit Sharma","Rahul Dravid"], 2],

["Who wrote Jana Gana Mana?",
 ["Bankim Chandra","Rabindranath Tagore","Iqbal","Sarojini Naidu"], 2],

["Which PM was born in Gujarat?",
 ["Charan Singh","Gulzarilal Nanda","Morarji Desai","Nehru"], 3],

["Who lives in Mannat?",
 ["Salman Khan","Aamir Khan","Amitabh Bachchan","Shah Rukh Khan"], 4],

["Who said 'Kitne Aadmi The?'",
 ["Veeru","Gabbar Singh","Jai","Thakur"], 2],

["Author of The God of Small Things?",
 ["R.K. Narayan","Rushdie","Jhumpa Lahiri","Arundhati Roy"], 4],

["Teacher of Kauravas & Pandavas?",
 ["Dronacharya","Karna","Krishna","Bhishma"], 1],

["DDLJ famous dialogue?",
 ["Rishte mein...","Mere paas maa hai",
  "Bade bade deshon mein...","Baazigar..."], 3],

["National animal of India?",
 ["Peacock","Tiger","Lion","Elephant"], 2],

["Full form of URL?",
 ["User Response Level","Updated Research Library",
  "Uniform Resource Locator","Universal Random Language"], 3],

["First Indian Olympic gold?",
 ["Mary Kom","Sushil Kumar","Neeraj Chopra","Abhinav Bindra"], 4],

["WC 2023 Player of Tournament?",
 ["Virat Kohli","Rohit Sharma","Pat Cummins","Zampa"], 1],

["App with disappearing photos?",
 ["Snapchat","TikTok","WhatsApp","Instagram"], 1]
]

# ---------------- MONEY LADDER ----------------
levels = [1000,2000,3000,5000,10000,20000,40000,80000,
          160000,320000,640000,1250000,2500000,
          5000000,7500000,10000000,70000000]

# Safe levels (milestones)
safe_levels = {4:10000, 9:320000, 14:7500000}

# ---------------- TIMER ----------------
timer_up = False

def timer(seconds):                             #Timer countdown
    global timer_up
    time.sleep(seconds)
    timer_up = True

def timed_input(prompt, sec=60):                
    global timer_up
    timer_up = False

    t = threading.Thread(target=timer, args=(sec,))
    t.start()

    ans = input(prompt)
    if timer_up:
        print("⏰ Time Up!")
        return None
    return ans

# ---------------- LIFELINE ----------------
def fifty_fifty(options, correct):
    wrong = [i for i in range(1,5) if i != correct]
    remove = random.sample(wrong,2)

    print("\n⚡ 50-50 Lifeline:")
    for i in range(1,5):
        if i not in remove:
            print(f"{i}. {options[i-1]}")

# ---------------- HIGH SCORE ----------------
def save_score(score):
    with open("highscore.txt","a") as f:
        f.write(str(score)+"\n")

def get_highscore():
    if not os.path.exists("highscore.txt"):
        return 0
    with open("highscore.txt","r") as f:
        scores = [int(x.strip()) for x in f.readlines()]
    return max(scores) if scores else 0

# ---------------- GAME ----------------
def play():
    money = 0
    lifeline = False

    print("\n🎮 WELCOME TO KBC PRO 🎮")
    print(f"🏆 Highest Score: Rs {get_highscore()}")

    for i in range(len(questions)):
        q, opts, correct = questions[i]

        print("\n" + "="*60)
        print(f"💰 Question for Rs {levels[i]}")
        print(q)

        for j,opt in enumerate(opts,1):
            print(f"{j}. {opt}")

        print("="*60)

        # Lifeline
        if not lifeline:
            use = input("Use 50-50? (y/n): ").lower()
            if use == 'y':
                fifty_fifty(opts, correct)
                lifeline = True

        ans = timed_input("👉 Answer (1-4) within 60 sec: ")

        if ans is None:
            break

        try:
            ans = int(ans)
        except:
            print("❌ Invalid input!")
            break

        if ans == correct:
            print(f"✅ Correct! You won Rs {levels[i]}")
            money = levels[i]

            if i in safe_levels:
                money = safe_levels[i]

        else:
            print("❌ Wrong Answer!")
            break

    print("\n" + "="*60)
    print(f"🏆 Take Home Money: Rs {money}")
    print("="*60)

    save_score(money)

# ---------------- MENU ----------------
while True:
    print("\n1. Play Game")
    print("2. High Score")
    print("3. Exit")

    ch = input("Choose: ")

    if ch == "1":
        play()
    elif ch == "2":
        print(f"🏆 Highest Score: Rs {get_highscore()}")
    elif ch == "3":
        sys.exit()
    else:
        print("❌ Invalid choice")