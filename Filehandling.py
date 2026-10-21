# Task 1: Create student.txt and write student details
with open("student.txt", "w") as f:
    f.write("Name: John Doe\nRoll Number: 101\nBranch: Computer Science\nSemester: 4\n")

# Task 2: Open a text file and display its complete contents
with open("student.txt", "r") as f:
    print("--- Task 2: File Contents ---")
    print(f.read())

# Task 3: Append additional student information without deleting previous contents
with open("student.txt", "a") as f:
    f.write("Email: john.doe@university.edu\n")

# Task 4: Read a text file line by line and display each line separately
with open("student.txt", "r") as f:
    print("--- Task 4: Line by Line ---")
    for line in f:
        print(line.strip())

# Task 5: Count and display the total number of lines present in a text file
with open("student.txt", "r") as f:
    lines = f.readlines()
    print(f"--- Task 5: Total Lines ---\n{len(lines)}")

# Task 6: Count the total number of words present in a text file
with open("student.txt", "r") as f:
    words = f.read().split()
    print(f"--- Task 6: Total Words ---\n{len(words)}")

# Task 7: Count the total number of characters in a text file, including spaces
with open("student.txt", "r") as f:
    text = f.read()
    print(f"--- Task 7: Total Characters ---\n{len(text)}")

# Task 8: Read a text file and display its lines in reverse order
with open("student.txt", "r") as f:
    lines = f.readlines()
    print("--- Task 8: Reverse Order ---")
    for line in reversed(lines):
        print(line.strip())

# Task 9: Read a text file and count the number of vowels and consonants
with open("student.txt", "r") as f:
    content = f.read().lower()
    vowels = sum(1 for char in content if char in "aeiou")
    consonants = sum(1 for char in content if char.isalpha() and char not in "aeiou")
    print(f"--- Task 9 ---\nVowels: {vowels}, Consonants: {consonants}")

# Task 10: Read a text file and calculate alphabets, digits, spaces, and special characters
with open("student.txt", "r") as f:
    content = f.read()
    alphabets = sum(1 for c in content if c.isalpha())
    digits = sum(1 for c in content if c.isdigit())
    spaces = sum(1 for c in content if c.isspace())
    special = len(content) - (alphabets + digits + spaces)
    print(f"--- Task 10 ---")
    print(f"Alphabets: {alphabets}, Digits: {digits}, Spaces: {spaces}, Special Characters: {special}")

# Task 11: Read a text file and find the longest word present in the file
with open("student.txt", "r") as f:
    words = f.read().split()
    longest_word = max(words, key=len) if words else ""
    print(f"--- Task 11: Longest Word ---\n{longest_word}")

# Task 12: Read a text file, count word occurrences, and display using a dictionary
with open("student.txt", "r") as f:
    words = f.read().split()
    word_count = {word: words.count(word) for word in set(words)}
    print(f"--- Task 12: Word Count Dictionary ---\n{word_count}")

# Task 13: Search for a specific word, display occurrences and line numbers
search_word = "John"
occurrences = 0
line_numbers = []
with open("student.txt", "r") as f:
    for idx, line in enumerate(f, 1):
        if search_word in line:
            occurrences += line.count(search_word)
            line_numbers.append(idx)
print(f"--- Task 13: Search '{search_word}' ---")
print(f"Occurrences: {occurrences}, Line Numbers: {line_numbers}")

# Task 14: Replace all occurrences of a specified word with another word and save
with open("student.txt", "r") as f:
    content = f.read()
modified_content = content.replace("John", "Jonathan")
with open("student_modified.txt", "w") as f:
    f.write(modified_content)
print("--- Task 14: Replaced 'John' with 'Jonathan' in 'student_modified.txt' ---")

# Task 15: Read a Python source file and create another file after removing single-line comments
with open("script.py", "w") as f:
    f.write("# This is a sample comment\nx = 10\n# Another comment\ny = 20\n")
with open("script.py", "r") as src, open("script_no_comments.py", "w") as dest:
    for line in src:
        if not line.strip().startswith("#"):
            dest.write(line)
print("--- Task 15: Created 'script_no_comments.py' without single-line comments ---")

# Task 16: Read a text file and create another file containing the same text in uppercase
with open("student.txt", "r") as src, open("student_upper.txt", "w") as dest:
    dest.write(src.read().upper())
print("--- Task 16: Created 'student_upper.txt' with uppercase text ---")

# Task 17: Student records operations (Display all, highest marks, average marks, > 80 marks)
with open("records.csv", "w") as f:
    f.write("RollNo,Name,Marks\n101,Amit,85\n102,Priya,92\n103,Rahul,78\n")
with open("records.csv", "r") as f:
    records = [line.strip().split(",") for line in f.readlines()[1:]]
    print("--- Task 17: Student Records Operations ---")
    print("All Records:", records)
    highest_student = max(records, key=lambda x: int(x[2]))
    print(f"Highest Marks: {highest_student[1]} ({highest_student[2]})")
    avg_marks = sum(int(r[2]) for r in records) / len(records)
    print(f"Average Marks: {avg_marks:.2f}")
    above_80 = [r[1] for r in records if int(r[2]) > 80]
    print(f"Scored > 80: {above_80}")

# Task 18: Employee record functions (Display, highest-paid, average salary, above salary)
with open("emp.csv", "w") as f:
    f.write("ID,Name,Department,Salary\n1,Alice,HR,50000\n2,Bob,IT,75000\n3,Charlie,Sales,60000\n")
with open("emp.csv", "r") as f:
    emp_data = [line.strip().split(",") for line in f.readlines()[1:]]
    print("--- Task 18: Employee Operations ---")
    print("All Employees:", emp_data)
    highest_paid = max(emp_data, key=lambda x: int(x[3]))
    print(f"Highest-Paid: {highest_paid[1]} ({highest_paid[3]})")
    avg_sal = sum(int(e[3]) for e in emp_data) / len(emp_data)
    print(f"Average Salary: {avg_sal:.2f}")
    above_threshold = [e[1] for e in emp_data if int(e[3]) > 55000]
    print(f"Earning > 55000: {above_threshold}")

# Task 19: Attendance percentage calculation and display students below 75%
with open("attendance.csv", "w") as f:
    f.write("Name,TotalClasses,Attended\nJohn,100,80\nEmma,100,70\nLiam,100,90\n")
with open("attendance.csv", "r") as f:
    print("--- Task 19: Students Below 75% Attendance ---")
    for line in f.readlines()[1:]:
        name, total, attended = line.strip().split(",")
        percentage = (int(attended) / int(total)) * 100
        if percentage < 75:
            print(f"{name}: {percentage:.2f}%")

# Task 20: Deposit/Withdrawals calculations (Total deposits, withdrawals, balance, largest transaction)
with open("transactions.csv", "w") as f:
    f.write("Type,Amount\nDeposit,5000\nWithdrawal,1200\nDeposit,3000\nWithdrawal,500\n")
deposits = withdrawals = largest = 0
with open("transactions.csv", "r") as f:
    for line in f.readlines()[1:]:
        t_type, amt = line.strip().split(",")
        amt = float(amt)
        if t_type.lower() == "deposit":
            deposits += amt
        elif t_type.lower() == "withdrawal":
            withdrawals += amt
        if amt > largest:
            largest = amt
final_balance = deposits - withdrawals
print("--- Task 20: Bank Transaction Summary ---")
print(f"Total Deposits: {deposits}, Total Withdrawals: {withdrawals}")
print(f"Final Balance: {final_balance}, Largest Transaction: {largest}")

# Task 21: Book records management system (Add, Search, Issue, Return, Display available)
with open("books.csv", "w") as f:
    f.write("ID,Title,Author,Status\n1,Python,Guido,Available\n2,Java,Gosling,Issued\n")
print("--- Task 21: Available Books ---")
with open("books.csv", "r") as f:
    for line in f.readlines()[1:]:
        b_id, title, author, status = line.strip().split(",")
        if status.lower() == "available":
            print(f"- {title} by {author}")

# Task 22: Read two text files and create a third file containing contents of both
with open("file1.txt", "w") as f:
    f.write("Content of File 1.\n")
with open("file2.txt", "w") as f:
    f.write("Content of File 2.\n")
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("file3.txt", "w") as f3:
    f3.write(f1.read() + f2.read())
print("--- Task 22: Created 'file3.txt' combining file1 and file2 ---")

# Task 23: Compare two text files for identity or find the first line where they differ
with open("file_a.txt", "w") as f:
    f.write("Line one\nLine two\nLine three\n")
with open("file_b.txt", "w") as f:
    f.write("Line one\nLine X\nLine three\n")
with open("file_a.txt", "r") as f1, open("file_b.txt", "r") as f2:
    f1_lines = f1.readlines()
    f2_lines = f2.readlines()
print("--- Task 23: File Comparison ---")
if f1_lines == f2_lines:
    print("Files are identical.")
else:
    for idx, (l1, l2) in enumerate(zip(f1_lines, f2_lines), 1):
        if l1 != l2:
            print(f"Files differ at line {idx}:")
            print(f"File A: {l1.strip()}")
            print(f"File B: {l2.strip()}")
            break    