"""
PYTHON ADVANCED FEATURES QUIZ
==============================

This quiz tests your understanding of Python decorators and advanced features.
Answer each question by typing the letter (a, b, c, or d) of your choice.

Good luck! 🎓
"""

import sys


class Quiz:
    """A simple quiz application for testing Python knowledge."""
    
    def __init__(self):
        """Initialize the quiz with questions and track score."""
        self.score = 0
        self.total_questions = 0
        self.questions = self.create_questions()
    
    def create_questions(self):
        """
        Create the quiz questions.
        
        Returns:
            list: List of question dictionaries
        """
        return [
            {
                "question": "What is the main purpose of a decorator in Python?",
                "options": {
                    "a": "To delete functions",
                    "b": "To modify or extend the behavior of functions without changing their code",
                    "c": "To create new classes",
                    "d": "To import modules"
                },
                "correct": "b",
                "explanation": "Decorators wrap functions to add functionality without modifying the original function code."
            },
            {
                "question": "Which decorator allows you to call a method without parentheses (person.name instead of person.name())?",
                "options": {
                    "a": "@staticmethod",
                    "b": "@classmethod",
                    "c": "@property",
                    "d": "@abstractmethod"
                },
                "correct": "c",
                "explanation": "@property allows you to call a method without parentheses, making it accessible like an attribute."
            },
            {
                "question": "What is the first parameter of a @classmethod?",
                "options": {
                    "a": "self",
                    "b": "cls",
                    "c": "class",
                    "d": "instance"
                },
                "correct": "b",
                "explanation": "@classmethod receives 'cls' (the class itself) as the first parameter, not 'self' (instance)."
            },
            {
                "question": "When should you use @staticmethod?",
                "options": {
                    "a": "When you need to access instance variables",
                    "b": "When you need to modify class variables",
                    "c": "When you need a utility function that doesn't access instance or class data",
                    "d": "When you want to create abstract methods"
                },
                "correct": "c",
                "explanation": "@staticmethod is for utility functions that don't need access to self or cls."
            },
            {
                "question": "What happens if you try to instantiate a class with @abstractmethod methods?",
                "options": {
                    "a": "It works fine",
                    "b": "Python raises a TypeError",
                    "c": "The abstract methods are automatically implemented",
                    "d": "The class becomes final"
                },
                "correct": "b",
                "explanation": "You cannot instantiate a class that has unimplemented abstract methods - Python raises TypeError."
            },
            {
                "question": "What is the purpose of @property with @setter?",
                "options": {
                    "a": "To make variables constant",
                    "b": "To add validation logic when setting attribute values",
                    "c": "To delete attributes",
                    "d": "To create static methods"
                },
                "correct": "b",
                "explanation": "@setter allows you to add validation and logic when assigning values to properties."
            },
            {
                "question": "In which order are stacked decorators applied?\n\n@decorator1\n@decorator2\ndef func():\n    pass",
                "options": {
                    "a": "decorator1 first, then decorator2",
                    "b": "decorator2 first, then decorator1",
                    "c": "They are applied simultaneously",
                    "d": "Only the top decorator is applied"
                },
                "correct": "b",
                "explanation": "Decorators are applied bottom-up: the decorator closest to the function is applied first."
            },
            {
                "question": "What does the @final decorator indicate?",
                "options": {
                    "a": "The method or class should not be overridden/subclassed",
                    "b": "The method is the last one in the class",
                    "c": "The class is complete and ready to use",
                    "d": "The method will be called last"
                },
                "correct": "a",
                "explanation": "@final indicates that a method should not be overridden or a class should not be subclassed."
            },
            {
                "question": "What is a common use case for @classmethod?",
                "options": {
                    "a": "Creating utility functions",
                    "b": "Creating alternative constructors (factory methods)",
                    "c": "Making methods private",
                    "d": "Preventing inheritance"
                },
                "correct": "b",
                "explanation": "@classmethod is commonly used for alternative constructors like Date.from_string()."
            },
            {
                "question": "What does the @override decorator help with?",
                "options": {
                    "a": "It makes methods run faster",
                    "b": "It prevents methods from being called",
                    "c": "It helps catch errors when you think you're overriding a parent method but aren't",
                    "d": "It automatically implements abstract methods"
                },
                "correct": "c",
                "explanation": "@override explicitly marks that you're overriding a parent method, helping type checkers catch mistakes."
            }
        ]
    
    def display_question(self, question_num, question_data):
        """
        Display a single question with its options.
        
        Args:
            question_num (int): The question number
            question_data (dict): Dictionary containing question details
        """
        print(f"\n{'='*70}")
        print(f"Question {question_num}/{len(self.questions)}")
        print(f"{'='*70}")
        print(f"\n{question_data['question']}\n")
        
        for option, text in sorted(question_data['options'].items()):
            print(f"  {option}) {text}")
        print()
    
    def get_answer(self):
        """
        Get the user's answer.
        
        Returns:
            str: The user's answer (a, b, c, or d)
        """
        while True:
            answer = input("Your answer (a/b/c/d): ").strip().lower()
            if answer in ['a', 'b', 'c', 'd']:
                return answer
            print("❌ Invalid input. Please enter a, b, c, or d.")
    
    def check_answer(self, user_answer, question_data):
        """
        Check if the user's answer is correct.
        
        Args:
            user_answer (str): The user's answer
            question_data (dict): Dictionary containing question details
            
        Returns:
            bool: True if correct, False otherwise
        """
        correct = question_data['correct']
        is_correct = user_answer == correct
        
        if is_correct:
            print("\n✅ Correct! Well done!")
            self.score += 1
        else:
            print(f"\n❌ Incorrect. The correct answer is: {correct}")
        
        print(f"💡 Explanation: {question_data['explanation']}")
        return is_correct
    
    def display_results(self):
        """Display the final quiz results."""
        percentage = (self.score / self.total_questions) * 100
        
        print("\n" + "="*70)
        print("QUIZ COMPLETED!")
        print("="*70)
        print(f"\nYour Score: {self.score}/{self.total_questions} ({percentage:.1f}%)")
        
        # Provide feedback based on score
        if percentage == 100:
            print("\n🌟 Perfect score! You're a Python decorator master! 🌟")
        elif percentage >= 80:
            print("\n🎉 Excellent work! You have a strong understanding!")
        elif percentage >= 60:
            print("\n👍 Good job! Review the tutorial for topics you missed.")
        elif percentage >= 40:
            print("\n📚 Keep learning! Go through the tutorial again.")
        else:
            print("\n💪 Don't give up! Study the tutorial and try again.")
        
        print("\n" + "="*70)
    
    def run(self):
        """Run the quiz."""
        print("\n" + "="*70)
        print("PYTHON ADVANCED FEATURES QUIZ")
        print("="*70)
        print("\nThis quiz will test your understanding of Python decorators")
        print("and advanced features covered in the tutorial.")
        print(f"\nTotal Questions: {len(self.questions)}")
        print("\nLet's begin!\n")
        
        input("Press Enter to start... ")
        
        self.total_questions = len(self.questions)
        
        for i, question_data in enumerate(self.questions, 1):
            self.display_question(i, question_data)
            user_answer = self.get_answer()
            self.check_answer(user_answer, question_data)
            
            if i < self.total_questions:
                input("\nPress Enter to continue to the next question... ")
        
        self.display_results()


def main():
    """Main function to run the quiz."""
    quiz = Quiz()
    
    try:
        quiz.run()
    except KeyboardInterrupt:
        print("\n\n⚠️  Quiz interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        sys.exit(1)
    
    # Ask if they want to try again
    print("\nWould you like to take the quiz again?")
    retry = input("Enter 'yes' to retry or anything else to exit: ").strip().lower()
    
    if retry == 'yes':
        print("\n" * 2)
        main()
    else:
        print("\n👋 Thanks for taking the quiz! Keep learning Python! 🐍")


if __name__ == "__main__":
    main()

