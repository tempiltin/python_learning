import os
import random
import datetime

# 📂 "python" papkasini yaratish
PYTHON_DIR = "python"
if not os.path.exists(PYTHON_DIR):
    os.makedirs(PYTHON_DIR)

# 📝 Python kod shablonlari (Fibonacci, Sorting, Prime Check va h.k.)
PYTHON_TEMPLATES = [
    """# Fibonacci function
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
n = 10
fibonacci(n)
""",

    """# Prime number checker
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(29))
""",

    """# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(bubble_sort([5, 3, 8, 6, 2]))
""",

    """# Random password generator
import random
import string
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))
print(generate_password())
""",

    """# Matrix multiplication
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))
"""
]

# 📅 2024 yilning barcha kunlari uchun commit qilish (90% faollik)
def get_commit_dates(year, activity_percent=90):
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)
    all_days = [(start_date + datetime.timedelta(days=i)) for i in range((end_date - start_date).days + 1)]
    
    active_days = random.sample(all_days, int(len(all_days) * (activity_percent / 100)))
    return sorted(active_days)

# 📜 Python fayl yaratish
def generate_python_file(file_name):
    code = random.choice(PYTHON_TEMPLATES)
    with open(file_name, "w") as f:
        f.write(code)

# 🟢 Git commit va push qilish
def commit_and_push(date, commit_count):
    for _ in range(commit_count):
        file_name = f"{PYTHON_DIR}/my_script_{random.randint(1, 100)}.py"
        generate_python_file(file_name)

    # Faqat `main.py` ni commit qilmaslik uchun
    os.system("git add --all")
    os.system("git reset main.py")  

    commit_date = date.strftime("%Y-%m-%dT%H:%M:%S")
    os.system(f'git commit --date="{commit_date}" -m "Commit on {commit_date}"')

    os.system("git push")

# 🚀 Asosiy funksiya
def main():
    year = 2024  
    commit_dates = get_commit_dates(year)

    for date in commit_dates:
        commit_count = random.randint(3, 7)  
        commit_and_push(date, commit_count)
        print(f"✅ {date} uchun {commit_count} ta commit qilindi.")

if __name__ == "__main__":
    main()
