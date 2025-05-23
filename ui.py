# GOLF SCORECARD #

import db

def display_menu():
    print("MENU OPTIONS")
    print("0 - Menu Options")
    print("1 - Display Golfers Total Scores")
    print("2 - Display Golfer Par/Strokes/Scores")
    print("3 - Add Golfer")
    print("4 - Remove Golfer")
    print("5 - Edit Golfer Stats")
    print("6 - Exit")
    print()

def display_records(golfers):
    if not golfers:
        print("No records available.")
        return
    else:
        print(f"{'':3}{'Golfer':25}{'Total Score'}")
        print("-" * 64)
        for golfer in golfers:
            print(f"{golfer['id']:<3d}{golfer['full_name']:25}{golfer.get('total_score', 'N/A')}")
        print()

def display_ParStrokeScore(golfers):
    if not golfers:
        print("No records available.")
        return
    
    print(f"{'':3}{'Golfer':25}", end="")
    for hole in range(1, 10):
        print(f"Hole {hole}", end="  ")
    print()
    
    print("-" * 100)
    
    for golfer in golfers:
        print(f"{golfer['id']:<3d}{golfer['full_name']:25}", end="")
        
        for i, ((par, strokes), score) in enumerate(zip(golfer['par_strokes'], golfer['score_dif'])):
            print(f"{par}/{strokes}/{score:<4d}", end="")
        
        print()
    
def add_golfer(golfers):
    golfer_id = len(golfers) + 1
    first_name = input("First Name: ").title()
    last_name = input("Last Name: ").title()
    full_name = f"{first_name} {last_name}"
    
    par_strokes = get_par_and_strokes()
    score = get_score(par_strokes)
    total = total_score(score)
  
    new_golfer = {
        "id": golfer_id,
        "full_name": full_name,
        "par_strokes": par_strokes,
        "score_dif": score,
        "total_score": total
    }
    golfers.append(new_golfer)
    db.write_golfers(golfers)
    print(f"Golfer {full_name} added successfully.")

def get_par_and_strokes():
    par_strokes = []
    print("Use / to separate par number from strokes.\nType \"N/A\" to stop.")
    
    for hole in range(1, 10):
        value = input(f"Hole {hole} Par/Strokes: ")
        if value.lower() == "n/a":
            break
        try:
            par, strokes = map(int, value.split("/"))
            par_strokes.append((par, strokes))
        except ValueError:
            print("Invalid input. Please use the format Par/Strokes (e.g., 4/5).")
    return par_strokes

def get_score(par_strokes):
    score = []
    for par, strokes in par_strokes:
        score_dif = strokes - par
        score.append(score_dif)
    return score

def total_score(score):
    return sum(score)

def remove_golfer(golfers):
    try:
        golfer_id = int(input("Enter the ID of the golfer to remove: "))
        for golfer in golfers:
            if golfer["id"] == golfer_id:
                golfers.remove(golfer)
                print(f"Golfer {golfer['full_name']} removed successfully.")
                db.write_golfers(golfers)
                return
        print("Golfer not found.")
    except ValueError:
        print("Invalid ID. Please enter a number.")

def edit_golfer_stats(golfers):
    while True:
        try:
            golfer_id = int(input("Enter the ID of the golfer to edit: "))
            for golfer in golfers:
                if golfer["id"] == golfer_id:
                    print(f"Editing scores for {golfer['full_name']}.")
                    par_strokes = get_par_and_strokes()
                    score = get_score(par_strokes)
                    golfer["par_strokes"] = par_strokes
                    golfer["score_dif"] = score
                    golfer["total_score"] = total_score(score)
                    print(f"Scores updated for {golfer['full_name']}.")
                    db.write_golfers(golfers)
                    return
            print("Golfer not found.")
        except ValueError:
            print("Invalid ID. Please enter a number.")

def main():
    golfers = db.read_golfers()
    display_menu()
    
    while True:
        choice = input("Enter an option (0 for menu): ")
        if choice == "0":
            display_menu()
        elif choice == "1":
            display_records(golfers)
        elif choice == "2":
            display_ParStrokeScore(golfers)
        elif choice == "3":
            add_golfer(golfers)
        elif choice == "4":
            remove_golfer(golfers)
        elif choice == "5":
            edit_golfer_stats(golfers)
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
    
