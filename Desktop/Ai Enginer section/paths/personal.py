#===== MENU =====
# 1. Add participant
# 2. View all participants
# 3. Exit

# Select an option (1-3):
# >> 1

# Enter your full name: >> Oludayo Oluwole
# Enter your age:>> 48
# Enter your phone number:>> 08030704503
# Enter your track (e.g., Python, Ai Engineering, etc.):
# >> Ai engineering

#  Participant 'Oludayo Oluwole' saved successfully!

# === Participant List ===
# 1. Oludayo Oluwole     Age: 48     Phone: 087030704503     Track: Ai Engineering

# # Example participant dictionary:
# {"name": "Oludayo Oluwole", "age": 48, "phone": "08030704503", "track": "Ai Engineering"}


# participant_pkg/file_ops.py

# participant_pkg/file_ops.py

import csv
from pathlib import Path

def save_participant(path, participant_dict):
    """
    Save a participant's details into a CSV file.
    
    Args:
        path (Path): Path to the CSV file
        participant_dict (dict): Dictionary with participant info
                                 keys: name, age, phone, track
    """
    try:
        # Check if the file already exists
        file_exists = path.exists()

        # Open file in append mode ("a") so we can add participants one by one
        with path.open(mode="a", newline="", encoding="utf-8") as csvfile:
            # Define the column headers
            fieldnames = ["name", "age", "phone", "track"]

            # Create a DictWriter object (writes dictionary rows into CSV)
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # If the file is new, write the header row first
            if not file_exists:
                writer.writeheader()

            # Write participant details as one row
            writer.writerow(participant_dict)

        print(f"✅ Participant '{participant_dict['name']}' saved successfully!\n")

    except Exception as e:
        # Catch any error (e.g., file permission issues) and print it
        print(f"❌ Error saving participant: {e}")


def load_participants(path):
    """
    Load all participants from a CSV file.

    Args:
        path (Path): Path to the CSV file
    
    Returns:
        list[dict]: List of participant dictionaries
    """
    participants = []
    try:
        # If the file does not exist, return an empty list
        if not path.exists():
            print("⚠️ No participant file found yet.")
            return participants

        # Open the file in read mode
        with path.open(mode="r", newline="", encoding="utf-8") as csvfile:
            # DictReader converts each row into a dictionary
            reader = csv.DictReader(csvfile)

            # Add each row (dictionary) to the participants list
            for row in reader:
                participants.append(row)

        return participants

    except Exception as e:
        print(f"❌ Error loading participants: {e}")
        return participants


# Example participant dictionary:
# {"name": "Oludayo Oluwole", "age": 34, "phone": "08012345678", "track": "Cybersecurity"}


