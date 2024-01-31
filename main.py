import csv


with open("students.csv", encoding="UTF-8") as file:
    rdr = csv.reader(file, delimiter=",", quotechar='"')
    df = list(rdr)[1:]
    sum_grade = {}
    count_grade = {}

    for ID, name, project, grade, score in df:
        if score == "None":
            count_grade[grade] = 0
            sum_grade[grade] = 0
    for ID, name, project, grade, score in df:
        if score != "None":
            if grade in count_grade.keys():
                count_grade[grade] += 1
                sum_grade[grade] += int(score)
    for i in range(len(df)):
        if df[i][-1] == "None":
            df[i][-1] = round(sum_grade[df[i][-2]]/count_grade[df[i][-2]], 2)

    print(count_grade, sum_grade)

    for ID, name, project, grade, score in df:
        if "Хадаров Владимир" in name:
            print(f"Ты получил оценку {score} за проект {project}, Хадаров Владимир")

    with open("students_new.csv", "w", newline="", encoding="UTF-8") as target:
        wrtr = csv.writer(target)
        wrtr.writerow(["id", "Name", "titleProject_id", "class", "score"])
        wrtr.writerows(df)



