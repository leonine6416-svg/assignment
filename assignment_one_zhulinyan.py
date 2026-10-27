"""
Assignment 1: Ultimate Python Showcase (Turtle + Bot + Calculator)
Author: Your Name
Description: A unified terminal program featuring vector graphics, an interactive 
             conditional query bot, and a fully functional calculator using if/elif/else logic.
"""

import turtle

def draw_turtle_star():
    """Module 1: Creates a dynamic geometric star spiral with Turtle graphics."""
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Creative Turtle Drawing - Geometric Star Spiral")

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)

    colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "magenta"]
    total_steps = 120

    print("\n[Turtle Graphic] Drawing star spiral pattern... Close the window when finished.")

    # Structured for loop fulfilling dynamic color, length, and shape requirements
    for i in range(total_steps):
        # 1. Dynamically change color
        t.pencolor(colors[i % len(colors)])
        
        # 2. Dynamically change length
        t.forward(i * 3.5)
        
        # 3. Geometric star rotation angle (144 degrees)
        t.left(144)
        
        # 4. Secondary geometric square accent every 6 steps
        if i % 6 == 0:
            t.circle(i / 3, steps=4)

    t.hideturtle()
    screen.mainloop()


def run_interactive_bot():
    """Module 2: Interactive query bot using keyword matching and if/elif/else logic."""
    print("\n" + "=" * 65)
    print("🤖 Welcome to the HKU AI & Robotics Interactive Bot!")
    print("Ask me anything! Try keywords like: HKU, robot, jetson, ai, human.")
    print("Type 'back' or 'exit' to return to the main menu.")
    print("=" * 65)

    while True:
        query = input("\nYou: ").strip()

        if query.lower() in ["back", "exit", "quit"]:
            print("Bot: Returning to main menu... 👋")
            break

        query_lower = query.lower()

        # Conditional logic matching the 5 required keywords
        if "hku" in query_lower:
            print("\nBot: 🏫 HKU (The University of Hong Kong) is a world-class institution leading cutting-edge research in computer science, AI, and robotics!")
        elif "jetson" in query_lower:
            print("\nBot: ⚡ NVIDIA Jetson is a family of embedded AI computing modules designed for real-time computer vision and autonomous robotics.")
        elif "robot" in query_lower:
            print("\nBot: 🦾 Robots are programmable mechanical systems equipped with sensors, actuators, and smart controllers to carry out complex tasks.")
        elif "ai" in query_lower:
            print("\nBot: 🧠 Artificial Intelligence enables software systems to process visual data, learn from patterns, and make autonomous decisions.")
        elif "human" in query_lower:
            print("\nBot: 👥 Human-Robot Interaction (HRI) focuses on enabling safe, natural, and efficient collaboration between people and robots.")
        else:
            print("\nBot: 🤔 No recognized keyword detected. Please include **HKU**, **robot**, **jetson**, **ai**, or **human** in your question!")


def run_calculator():
    """Module 3: Functional terminal-based calculator using if/elif/else logic."""
    print("\n" + "=" * 55)
    print("      🧮 TERMINAL CALCULATOR")
    print("=" * 55)
    print("Supported operators: +, -, *, /")
    print("Type 'back' at any prompt to return to the main menu.")
    print("=" * 55)

    while True:
        # 1. Prompt for first number
        num1_input = input("\nEnter first number (or 'back'): ").strip()
        if num1_input.lower() == 'back':
            print("Returning to main menu...")
            break
        
        try:
            num1 = float(num1_input)
        except ValueError:
            print("❌ Invalid number! Please enter a valid numeric value.")
            continue

        # 2. Choose operator
        operator = input("Choose operator (+, -, *, /): ").strip()
        if operator.lower() == 'back':
            print("Returning to main menu...")
            break

        # 3. Prompt for second number
        num2_input = input("Enter second number: ").strip()
        if num2_input.lower() == 'back':
            print("Returning to main menu...")
            break

        try:
            num2 = float(num2_input)
        except ValueError:
            print("❌ Invalid number! Please enter a valid numeric value.")
            continue

        # 4. Use if / elif / else for math logic and display clear results
        if operator == "+":
            result = num1 + num2
            print(f"\n✨ Result: {num1} + {num2} = {result}")
        elif operator == "-":
            result = num1 - num2
            print(f"\n✨ Result: {num1} - {num2} = {result}")
        elif operator == "*":
            result = num1 * num2
            print(f"\n✨ Result: {num1} * {num2} = {result}")
        elif operator == "/":
            if num2 == 0:
                print("\n❌ Error: Division by zero is undefined!")
            else:
                result = num1 / num2
                print(f"\n✨ Result: {num1} / {num2} = {result}")
        else:
            print(f"\n❌ Error: '{operator}' is not a valid operator. Please use +, -, *, or /.")


def main():
    """Main program execution loop with top-level if / elif / else routing."""
    while True:
        print("\n" + "=" * 55)
        print("      ASSIGNMENT 1: COMBINED PYTHON PROGRAM")
        print("=" * 55)
        print("  [1] Launch Turtle Graphics Drawing")
        print("  [2] Launch Interactive Keyword Bot")
        print("  [3] Launch Terminal Calculator")
        print("  [4] Exit Program")
        print("=" * 55)
        
        user_choice = input("Select an option (1, 2, 3, or 4): ").strip()

        # Top-level conditional control structure
        if user_choice == "1":
            draw_turtle_star()
        elif user_choice == "2":
            run_interactive_bot()
        elif user_choice == "3":
            run_calculator()
        elif user_choice == "4":
            print("\nExiting program. Good luck with your assignment! 🚀")
            break
        else:
            print("\n❌ Invalid choice! Please enter '1', '2', '3', or '4'.")


if __name__ == "__main__":
    main()
