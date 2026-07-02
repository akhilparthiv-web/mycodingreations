import random

# ONLY up to Kanku-Dai
# Questions NEVER repeat until all have been used

kata_data = {
    "Heian Shodan": (9, 17, 21),
    "Heian Nidan": (11, 26, 26),
    "Heian Sandan": (10, 20, 20),
    "Heian Yondan": (13, 25, 27),
    "Heian Godan": (12, 19, 23),

    "Tekki Shodan": (15, 29, 29),
    "Tekki Nidan": (16, 24, 24),
    "Tekki Sandan": (16, 36, 36),

    "Bassai Dai": (19, 42, 42),
    "Jion": (17, 47, 47),
    "Empi": (15, 36, 37),
    "Kanku Dai": (16, 65, 65)
}

score = 0
rounds = 0

# Create ALL possible questions
all_questions = []

for kata, (k1, k2, total) in kata_data.items():

    all_questions.append({
        "kata": kata,
        "type": "1st kiai",
        "answer": k1
    })

    all_questions.append({
        "kata": kata,
        "type": "2nd kiai",
        "answer": k2
    })

    all_questions.append({
        "kata": kata,
        "type": "total moves",
        "answer": total
    })

# Shuffle questions
random.shuffle(all_questions)

print("===================================")
print(" SHOTOKAN KATA MEMORY TRAINER ")
print("===================================")
print("No question repeats until all are used!")
print("Type 'quit' anytime to stop.\n")

# MAIN LOOP
for q in all_questions:

    print("\n-----------------------------------")
    print(f"KATA: {q['kata']}")
    print(f"QUESTION: {q['type']}")

    user = input("Your answer: ")

    if user.lower() == "quit":
        break

    if user == str(q["answer"]):
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong!")
        print(f"Correct answer: {q['answer']}")

    rounds += 1

    remaining = len(all_questions) - rounds

    print(f"\nScore: {score}/{rounds}")
    print(f"Questions remaining: {remaining}")

# END SCREEN
print("\n===================================")
print(" GAME OVER ")
print("===================================")
print(f"Final Score: {score}/{rounds}")

if rounds == len(all_questions):
    print("🎉 You completed every question!")
