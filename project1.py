def get_valid_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = int(input(prompt))
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"Error: Value must be between {min_val} and {max_val}.")
            else:
                return val
        except ValueError:
            print("Error: Please enter a valid number.")


def get_student_info():
    name = input("Enter student name: ")
    age = get_valid_int(f"Enter age for {name}: ", 1, 100)
    scores = []
    for i in range(1, 4):
        score = get_valid_int(f"Enter score {i} (0-100) for {name}: ", 0, 100)
        scores.append(score)
    return name, age, scores


def calculate_averages(student_data):
    averages = {}
    for name, data in student_data.items():
        avg = sum(data[1]) / len(data[1])
        averages[name] = avg
    return averages


def save_to_file(filename, student_data):
    try:
        with open(filename, 'w') as f:
            for name, data in student_data.items():
                age = data[0]
                scores = data[1]
                scores_str = f"{scores[0]},{scores[1]},{scores[2]}"
                f.write(f"{name}|{age}|{scores_str}\n")
        print("Data saved successfully.")
    except Exception as e:
        print("Error saving to file:", e)


def read_from_file(filename):
    data = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split('|')
                if len(parts) != 3:
                    continue
                name = parts[0]
                age = int(parts[1])
                scores = [int(s) for s in parts[2].split(',')]
                data[name] = (age, scores)
        print("Data loaded successfully.")
    except Exception as e:
        print("File not found or empty:", e)
    return data


def main():
    student_data = {}

    while True:
        print("\n1. Add student\n2. Show averages\n3. List students above average\n4. Save to file\n5. Read from file\n6. Exit")
        choice = get_valid_int("Enter choice: ", 1, 6)

        if choice == 1:
            name, age, scores = get_student_info()
            student_data[name] = (age, scores)

        elif choice == 2:
            avgs = calculate_averages(student_data)
            for name, avg in avgs.items():
                print(f"{name}: Average = {avg:.2f}")

        elif choice == 3:
            limit = get_valid_int("Enter minimum average: ", 0, 100)
            avgs = calculate_averages(student_data)
            for name, avg in avgs.items():
                if avg > limit:
                    print(f"{name} has {avg:.2f}")

        elif choice == 4:
            save_to_file("students.txt", student_data)

        elif choice == 5:
            student_data = read_from_file("students.txt")

        elif choice == 6:
            break


if __name__ == "__main__":
    main()