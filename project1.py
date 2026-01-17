def get_valid_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = int(input(prompt))
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f""n_val} و {max_val}")
                continue
            return val
        except ValueError:
            print("خطأ! يرجى إدخال رقم صحيح.")

def get_student_info():
    name = input("أدخل اسم الطالب: ")
    age = get_valid_int("أدخل عمر الطالب: ", 1, 100)
    scores = []
    for i in range(3):
        score = get_valid_int(f"أدخل درجة المادة {i+1} (من 0 لـ 100): ", 0, 100)
        scores.append(score)
    return name, (age, scores)

def calculate_averages(student_data):
    averages = {}
    for name, info in student_data.items():
        scores = info[1]
        avg = sum(scores) / len(scores)
        averages[name] = avg
    return averages