# main program
# main.py

from pathlib import Path
from participant_pkg.file_ops import save_participant, load_participants

def get_participant_details():
    """
    Collect participant details with input validation
    Returns:
        dict: participant details
    """
    print("\n=== Welcome to Olu.Oludayo Enterprises Workshop ===\n")

    # Ask for name
    name = input("Enter your full name:\n>> ").strip()

    # Validate age (must be a positive integer)
    while True:
        try:
            age = int(input("Enter your age:\n>> "))
            if age <= 0:
                print("⚠️ Age must be positive. Try again.")
                continue
            break  # valid input, break the loop
        except ValueError:
            print("⚠️ Invalid age. Please enter a number.")

    # Ask for phone and track
    phone = input("Enter your phone number:\n>> ").strip()
    track = input("Enter your track (e.g., Data Science, Web Dev, etc.):\n>> ").strip()

    # Return participant details as a dictionary
    return {"name": name, "age": age, "phone": phone, "track": track}


def main():
    # Define CSV file path (participants.csv in the same folder as main.py)
    path = Path("participants.csv")

    while True:
        # Display menu
        print("\n===== MENU =====")
        print("1. Add participant")
        print("2. View all participants")
        print("3. Exit\n")

        # Ask user for choice
        choice = input("Select an option (1-3):\n>> ").strip()

        if choice == "1":
            # Collect participant details and save
            participant = get_participant_details()
            save_participant(path, participant)

        elif choice == "2":
            # Load participants and display
            participants = load_participants(path)
            if participants:
                print("\n=== Participant List ===")
                for i, p in enumerate(participants, start=1):
                    print(f"{i}. {p['name']} \t Age: {p['age']} \t Phone: {p['phone']} \t Track: {p['track']}")
            else:
                print("⚠️ No participants found.")

        elif choice == "3":
            # Exit program
            print("👋 Exiting program. Goodbye!")
            break

        else:
            # Handle invalid input
            print("⚠️ Invalid choice, try again.")


# Run the program only if executed directly
if __name__ == "__main__":
    main()