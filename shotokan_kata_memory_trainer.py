import random

# Kata data sourced from The Martial Way
kata_groups = {
    "Heian": {
        "Heian Sho-dan": (9, 17, 21),
        "Heian Ni-dan": (11, 26, 26),
        "Heian San-dan": (10, 20, 20),
        "Heian Yon-dan": (13, 25, 27),
        "Heian Go-dan": (12, 19, 23),
    },
    "Tekki": {
        "Tekki Sho-dan": (15, 29, 29),
        "Tekki Ni-dan": (16, 24, 24),
        "Tekki San-dan": (16, 36, 36),
    },
    "Sentei": {
        "Bassai-Dai": (19, 42, 42),
        "Kanku-Dai": (16, 65, 65),
        "Jion": (17, 47, 47),
        "Empi": (15, 36, 37),
    },
    "Advanced": {
        "Jitte": (13, 24, 24),
        "Gankaku": (28, 42, 42),
        "Hangetsu": (11, 40, 41),
        "Kanku-Sho": (6, 48, 48),
        "Bassai-Sho": (17, 22, 27),
        "Chinte": (28, 32, 32),
        "Nijushiho": (18, 33, 34),
        "Sochin": (30, 41, 41),
        "Unsu": (36, 48, 48),
        "Gojushiho-Sho": (57, 64, 65),
        "Gojushiho-Dai": (59, 66, 67),
        "Meikyo": (32, "-", 33), 
        "Wankan": (24, "-", 24),
        "Jiin": (11, 35, 35),
    }
}

# Translation Dictionary
texts = {
    "en": {
        "title": "SHOTOKAN KATA MEMORY TRAINER",
        "menu_prompt": "\nChoose a Kata Group to practice:\n1. Heian\n2. Tekki\n3. Sentei\n4. Advanced\n5. All Katas\nEnter a number (1-5): ",
        "invalid_menu": "Invalid choice, please enter a number from 1 to 5.",
        "loading": "Loading",
        "q_1st": "1st kiai",
        "q_2nd": "2nd kiai",
        "q_total": "total moves",
        "intro1": "No question repeats until all are used!",
        "intro2": "Type 'quit' anytime to stop.",
        "kata_lbl": "KATA:",
        "question_lbl": "QUESTION:",
        "ans_prompt": "Your answer: ",
        "correct": "✅ Correct!",
        "wrong": "❌ Wrong!",
        "correct_ans": "Correct answer:",
        "score_lbl": "Score:",
        "remaining_lbl": "Questions remaining:",
        "game_over": "GAME OVER",
        "final_score": "Final Score:",
        "completed": "🎉 You completed every question!"
    },
    "fr": {
        "title": "ENTRAÎNEUR DE MÉMOIRE KATA SHOTOKAN",
        "menu_prompt": "\nChoisissez un groupe de Kata à pratiquer :\n1. Heian\n2. Tekki\n3. Sentei\n4. Avancé\n5. Tous les Katas\nEntrez un numéro (1-5) : ",
        "invalid_menu": "Choix invalide, veuillez entrer un nombre de 1 à 5.",
        "loading": "Chargement",
        "q_1st": "1er kiai",
        "q_2nd": "2ème kiai",
        "q_total": "mouvements totaux",
        "intro1": "Aucune question ne se répète avant d'avoir toutes été utilisées !",
        "intro2": "Tapez 'quit' à tout moment pour arrêter.",
        "kata_lbl": "KATA :",
        "question_lbl": "QUESTION :",
        "ans_prompt": "Votre réponse : ",
        "correct": "✅ Correct !",
        "wrong": "❌ Faux !",
        "correct_ans": "Réponse correcte :",
        "score_lbl": "Score :",
        "remaining_lbl": "Questions restantes :",
        "game_over": "FIN DU JEU",
        "final_score": "Score final :",
        "completed": "🎉 Vous avez répondu à toutes les questions !"
    }
}

# 1. Options built directly into the language selection input prompt
while True:
    lang_choice = input("Select Language / Choisissez la langue (en/fr): ").lower()
    if lang_choice in ['en', 'fr']:
        break
    print("Please type 'en' for English or 'fr' for French.")

# Set the active language dictionary
t = texts[lang_choice]

print("===================================")
print(f"   {t['title']}    ")
print("===================================")

# 2. Group menu options placed directly inside the menu input prompt
while True:
    choice = input(t['menu_prompt'])
    if choice in ['1', '2', '3', '4', '5']:
        break
    print(t['invalid_menu'])

# 3. Grab only the katas the user selected
selected_data = {}
if choice == '1':
    selected_data = kata_groups["Heian"]
    print(f"\n{t['loading']} Heian...")
elif choice == '2':
    selected_data = kata_groups["Tekki"]
    print(f"\n{t['loading']} Tekki...")
elif choice == '3':
    selected_data = kata_groups["Sentei"]
    print(f"\n{t['loading']} Sentei...")
elif choice == '4':
    selected_data = kata_groups["Advanced"]
    print(f"\n{t['loading']} Advanced/Avancé...")
elif choice == '5':
    for group in kata_groups.values():
        selected_data.update(group)
    print(f"\n{t['loading']} All/Tous...")

score = 0
rounds = 0

# 4. Create ALL possible questions for the selected list
all_questions = []

for kata, (k1, k2, total) in selected_data.items():

    all_questions.append({
        "kata": kata,
        "type": t['q_1st'],
        "answer": k1
    })

    # Skips the 2nd kiai question if the kata doesn't have one
    if str(k2) != "-":
        all_questions.append({
            "kata": kata,
            "type": t['q_2nd'],
            "answer": k2
        })

    all_questions.append({
        "kata": kata,
        "type": t['q_total'],
        "answer": total
    })

# Shuffle questions
random.shuffle(all_questions)

print(t['intro1'])
print(f"{t['intro2']}\n")

# MAIN LOOP
for q in all_questions:

    print("\n-----------------------------------")
    print(f"{t['kata_lbl']} {q['kata']}")
    print(f"{t['question_lbl']} {q['type']}")

    user = input(t['ans_prompt'])

    if user.lower() == "quit":
        break

    if user == str(q["answer"]):
        print(t['correct'])
        score += 1
    else:
        print(t['wrong'])
        print(f"{t['correct_ans']} {q['answer']}")

    rounds += 1
    remaining = len(all_questions) - rounds

    print(f"\n{t['score_lbl']} {score}/{rounds}")
    print(f"{t['remaining_lbl']} {remaining}")

# END SCREEN
print("\n===================================")
print(f"             {t['game_over']}             ")
print("===================================")
print(f"{t['final_score']} {score}/{rounds}")

if rounds == len(all_questions) and rounds > 0:
    print(t['completed'])
