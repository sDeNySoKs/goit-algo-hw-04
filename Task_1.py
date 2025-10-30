def total_salary(path):
    total_sal = 0
    average_sal = 0
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                salary_str = line.strip().split(',')[1]
                total_sal += int(salary_str)
                count += 1
        average_sal = total_sal // count
        return total_sal, average_sal
    
    except FileNotFoundError:
        print("Файл не знайдено")

total, average = total_salary("C:/Users/denis/OneDrive/Desktop/salary_file.txt")
print(f"Загальна сума заробітної плати : {total}, Середня заробітна плата: {average}")
