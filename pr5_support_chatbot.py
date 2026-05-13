import random
import string
from datetime import datetime

# List to store all tickets
tickets = []

def generate_ticket_id():
    chars = string.ascii_uppercase + string.digits
    return "TKT-" + "".join(random.choices(chars, k=6))

def create_ticket(name, email, category, priority, description):
    ticket = {
        "id":          generate_ticket_id(),
        "created_at":  datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "name":        name,
        "email":       email,
        "category":    category,
        "priority":    priority,
        "description": description,
        "status":      "Open"
    }
    tickets.append(ticket)
    return ticket

# Ask a question and keep asking until the answer is valid
def ask(question, is_valid=None):
    while True:
        answer = input(question).strip()
        if is_valid is None or is_valid(answer):
            return answer
        print("  Invalid input. Please try again.")

# Show a numbered menu and return the chosen option label
def pick_option(options):
    for number, label in options.items():
        print("  [" + number + "] " + label)
    valid_keys = list(options.keys())
    choice = ask("Enter your choice: ", lambda x: x in valid_keys)
    return options[choice]

# Main chatbot conversation
def run():
    print("\n" + "=" * 50)
    print("  Support Ticket System")
    print("=" * 50)

    # Step 1: Name
    name = ask("\nYour name: ")
    print("Hello, " + name + "! Let's create a support ticket for you.\n")

    # Step 2: Email
    def valid_email(e):
        return "@" in e and "." in e.split("@")[-1]

    email = ask("Your email: ", valid_email)

    # Step 3: Category
    print("\nWhat is your issue related to?")
    categories = {"1": "Technical", "2": "Billing", "3": "Account", "4": "Other"}
    category = pick_option(categories)

    # Step 4: Priority
    print("\nHow urgent is the issue?")
    priorities = {"1": "Low", "2": "Medium", "3": "High", "4": "Critical"}
    priority = pick_option(priorities)

    # Step 5: Description
    print("\nDescribe your issue below.")
    print("Press Enter on a blank line when done.\n")
    lines = []
    while True:
        line = input()
        if line == "" and len(lines) > 0:
            break
        lines.append(line)
    description = " ".join(lines)

    # Step 6: Show summary and confirm
    print("\n" + "-" * 50)
    print("  Review your details:")
    print("  Name     : " + name)
    print("  Email    : " + email)
    print("  Category : " + category)
    print("  Priority : " + priority)
    print("  Issue    : " + description[:80])
    print("-" * 50)

    confirm = ask("\nSubmit ticket? (y/n): ", lambda x: x.lower() in ("y", "n"))

    if confirm.lower() == "n":
        print("\n  Ticket cancelled.\n")
        return

    # Step 7: Create and show the ticket
    ticket = create_ticket(name, email, category, priority, description)

    sla = {"Low": "48 hours", "Medium": "24 hours", "High": "4 hours", "Critical": "1 hour"}

    print("\n" + "=" * 50)
    print("  Ticket Submitted Successfully!")
    print("=" * 50)
    print("  Ticket ID  : " + ticket["id"])
    print("  Created At : " + ticket["created_at"])
    print("  Status     : " + ticket["status"])
    print("  Response   : Within " + sla[priority])
    print("  We will contact you at: " + email)
    print("=" * 50 + "\n")

# Entry point
while True:
    run()
    again = input("Create another ticket? (y/n): ").strip().lower()
    if again != "y":
        print("\nThank you. Goodbye!\n")
        break
