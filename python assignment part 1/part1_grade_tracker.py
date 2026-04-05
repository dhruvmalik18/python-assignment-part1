# -----------------------------
# STUDENT DATA CLEANING
# -----------------------------

students_data = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma", "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": " Priya Nair ", "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA", "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ", "roll": "105", "marks_str": "75, 80, 70, 68, 85"}
]

clean_list = []

print("Name Validation:\n")

for item in students_data:
    # clean name
    fixed_name = item["name"].strip().title()

    # convert roll
    roll_no = int(item["roll"])

    # convert marks string to list
    marks_list = [int(x) for x in item["marks_str"].split(",")]

    # check if valid name
    valid_flag = True
    for word in fixed_name.split():
        if not word.isalpha():
            valid_flag = False

    if valid_flag:
        print(f"{fixed_name} -> Valid")
    else:
        print(f"{fixed_name} -> Invalid")

    clean_list.append({
        "name": fixed_name,
        "roll": roll_no,
        "marks": marks_list
    })


# -----------------------------
# PROFILE DISPLAY
# -----------------------------

print("\nStudent Profiles:\n")

for stu in clean_list:
    print("-" * 25)
    print(f"Student Name : {stu['name']}")
    print(f"Roll Number  : {stu['roll']}")
    print(f"Marks List   : {stu['marks']}")
    print("-" * 25)


# special case (roll 103)
for stu in clean_list:
    if stu["roll"] == 103:
        print("\nSpecial Case Output:")
        print("UPPER:", stu["name"].upper())
        print("lower:", stu["name"].lower())


# -----------------------------
# TASK 2 - MARKS ANALYSIS
# -----------------------------

stud_name = "Ayesha Sharma"
subs = ["Math", "Physics", "CS", "English", "Chemistry"]
marks_val = [88, 72, 95, 60, 78]

def grade_calc(m):
    if m >= 90:
        return "A+"
    elif m >= 80:
        return "A"
    elif m >= 70:
        return "B"
    elif m >= 60:
        return "C"
    else:
        return "F"

print("\nSubject Report:\n")

for i in range(len(subs)):
    print(f"{subs[i]} : {marks_val[i]} -> {grade_calc(marks_val[i])}")


# calculations
total_marks = sum(marks_val)
avg_marks = round(total_marks / len(marks_val), 2)

print("\nTotal Marks:", total_marks)
print("Average:", avg_marks)

# highest & lowest
max_marks = max(marks_val)
min_marks = min(marks_val)

print("Highest:", subs[marks_val.index(max_marks)], max_marks)
print("Lowest:", subs[marks_val.index(min_marks)], min_marks)


# adding new subjects
added = 0

while True:
    new_sub = input("Enter subject (done to stop): ")

    if new_sub.lower() == "done":
        break

    try:
        new_marks = int(input("Enter marks: "))

        if 0 <= new_marks <= 100:
            subs.append(new_sub)
            marks_val.append(new_marks)
            added += 1
        else:
            print("Marks should be between 0-100")

    except:
        print("Invalid input, try again")

print("\nSubjects added:", added)
print("New Average:", round(sum(marks_val)/len(marks_val), 2))


# -----------------------------
# TASK 3 - CLASS SUMMARY
# -----------------------------

class_info = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma", [55, 68, 49, 72, 61]),
    ("Priya Nair", [91, 85, 88, 94, 79]),
    ("Karan Mehta", [40, 55, 38, 62, 50]),
    ("Sneha Pillai", [75, 80, 70, 68, 85])
]

print("\nClass Performance:\n")
print("Name | Avg | Result")

pass_no = 0
fail_no = 0
top_name = ""
top_avg = 0

all_avg = []

for name, marks in class_info:
    avg = round(sum(marks)/len(marks), 2)

    if avg >= 60:
        status = "Pass"
        pass_no += 1
    else:
        status = "Fail"
        fail_no += 1

    if avg > top_avg:
        top_avg = avg
        top_name = name

    all_avg.append(avg)

    print(f"{name} | {avg} | {status}")

print("\nPassed:", pass_no)
print("Failed:", fail_no)
print("Topper:", top_name, top_avg)
print("Class Avg:", round(sum(all_avg)/len(all_avg), 2))


# -----------------------------
# TASK 4 - STRING OPERATIONS
# -----------------------------

essay = " python is a versatile language. it supports object oriented, fun "

clean_txt = essay.strip().lower()

print("\nClean Text:", clean_txt)
print("Title:", clean_txt.title())

word_count = clean_txt.count("python")
print("Word 'python' count:", word_count)

new_txt = clean_txt.replace("python", "Python 🚀")
print("Updated Text:", new_txt)

sent_list = clean_txt.split(". ")

print("\nSentence List:", sent_list)

print("\nNumbered Sentences:")
for idx, line in enumerate(sent_list, start=1):
    if not line.endswith("."):
        line += "."
    print(f"{idx}. {line}")