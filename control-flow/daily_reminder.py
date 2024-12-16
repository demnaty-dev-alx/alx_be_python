task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ").lower()

message = ""

match priority:
    case "high" | "medium":
        message += "Reminder: '"
    case "low":
        message += "Note: '"

message += task + "' is a " + priority + " priority task"

if time_bound == "yes":
    message += " that requires immediate attention today!"
elif time_bound == "no":
    message += ". Consider completing it when you have free time."

print(message)
