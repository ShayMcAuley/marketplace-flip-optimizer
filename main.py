def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("=== Marketplace Flip Optimizer ===")
    
    starting_capital = get_positive_number("Enter your starting capital: $")
    target_profit_goal = get_positive_number("Enter your target profit goal: $")
    
    print(f"\nStarting Capital: ${starting_capital:.2f}")
    print(f"Target Profit Goal: ${target_profit_goal:.2f}")

if __name__ == "__main__":
    main()
