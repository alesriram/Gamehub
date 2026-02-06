import random

gk = "⟦G⟧⟦e⟧⟦n⟧⟦e⟧⟦r⟧⟦a⟧⟦l⟧ ⟦K⟧⟦n⟧⟦o⟧⟦w⟧⟦l⟧⟦e⟧⟦d⟧⟦g⟧⟦e⟧ ⟦Q⟧⟦u⟧⟦i⟧⟦z⟧"

class GeneralKnowledgeQuiz:
    def __init__(self):
        self.questions = [
            "What is the capital of France?",
            "Which planet is known as the Red Planet?",
            "Who painted the Mona Lisa?",
            "What is the largest mammal?",
            "What is the currency of Japan?",
            "What is the chemical symbol for gold?",
            "What is the tallest mountain in the world?",
            "Which gas do plants use for photosynthesis?",
            "What is the smallest prime number?",
            "Who wrote the play 'Romeo and Juliet'?",
            # ADD MORE AS NEEDED ...
        ]
        self.answers = [
            "Paris", "Mars", "Leonardo da Vinci", "Blue whale", "Yen",
            "Au", "Mount Everest", "Carbon dioxide", "2", "William Shakespeare",
            # ADD MORE AS NEEDED ...
        ]

    def play_quiz(self):
        while True:
            print(f"\n\n ------------------ {gk}-------------------")
            if len(self.questions) == 0:
                print("No more questions! Thank you for playing.")
                break
            choice_index = random.randint(0, len(self.questions) - 1)
            print(f"\n\n QUESTION : {self.questions[choice_index]}")
            user = input("\n ANSWER : ").lower().replace(" ", "")
            comp = self.answers[choice_index].lower().replace(" ", "")
            if user == comp:
                print("\n\n CONGRATULATIONS....! CORRECT ANSWER ")
            else:
                print("\n\n SORRY...! WRONG ANSWER ")
            print("\n The Correct Answer : ", self.answers[choice_index])
            self.questions.pop(choice_index)
            self.answers.pop(choice_index)
            print("\n ----------------------------------------------------------------------")
            again = input("\n\n Do you want to play again? (Y/N) : ")
            if again.lower() != 'y':
                print("\n\t\t THANK YOU")
                break

if __name__ == "__main__":
    quiz = GeneralKnowledgeQuiz()
    quiz.play_quiz()
