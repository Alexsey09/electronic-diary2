
FILLNAME = "directory.txt"

def load_diary():
    try:
        with open(FILLNAME, encoding="utf8") as f:
            lines = []
            for i in f:
                i = i.strip()
                if i != "":
                    lines.append(i)
    except FileNotFoundError:
        print("Файл дневника не найден!")
        return None 
    
    diary = {}
    grades = {}

    for line in lines:
        if line.startswith("ФИО: "):
                diary["ФИО"] = line.split(":",1)[1].strip() 

        elif  line.startswith("Класс: "):
            diary["Класс"] = line.split(":", 1)[1].strip()
        else:
            subject_and_marks = line.split(":")
            subject = subject_and_marks[0].strip()
            marks_str = subject_and_marks[1].strip().split(",")
            marks = []
            for i in marks_str:
                digit = int(i)
                marks.append(digit)
            grades[subject] = marks
            

    diary["Оценки"] = grades
    return diary

def show_diary(diary):
    print(f"\nОценки ученика {diary["ФИО"]} {diary["Класс"]}:")
    
    for i in diary["Оценки"]:
        marks = diary["Оценки"][i]
        avg = round(sum(marks) / len(marks),2)
        print(f"{i}: {marks} - средний балл {avg}")


def medium_all_marks(diary):
    total_marks = 0
    long_marks = 0

    for i in diary["Оценки"].values():
        total_marks += sum(i)
        long_marks += len(i)
        avg_all_marks = round(total_marks / long_marks,2)


    print(f"Средний балл ученика {diary["ФИО"]} - {avg_all_marks}")
        
def count_marks(diary):
    min_marks = ""
    max_marks = ""
    max_avg = 0
    min_avg = 5
    
    for marks,grade in diary["Оценки"].items():

        avg = sum(grade) / len(grade)

        if avg > max_avg:
            max_avg = avg
            max_marks = marks
            
        if avg < min_avg:
            min_avg = avg
            min_marks = marks
        
    rounds_max = round(max_avg,2)
    rounds_min = round(min_avg,2)

    print(f"Предмет с самым большим средним баллом: {max_marks} ({rounds_max})")
    print(f"Предмет с самым низким средним баллом: {min_marks} ({rounds_min})")
        
def main():
    diary = load_diary()
    print(f"\nДобро пожаловать, {diary["ФИО"]} из {diary["Класс"]}")
    
    while True:
        print("\nМеню")
        print("1 - Показать оценки по каждому предмету")
        print("2 - Общий балл всех оценок")
        print("3 - Узнать самый низкий и максимальный балл")
        print("0 - Выход")

        choice = input("Выбери пункт меню: ")

        if choice == "1":
            show_diary(diary)
        elif choice == "2":
            medium_all_marks(diary)
        elif choice == "3":
            count_marks(diary)
        elif choice == "0":
            print("Пока!")
            break
        else:
            print("Введиите 0\1\2\3")

main()
