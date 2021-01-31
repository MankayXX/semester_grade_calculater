import semesterLetter
import lessonLetter

allLessons = []
credit = []
lesson = []
average = 0
letterGrade = ""
totalCredit = 0
k = False
passingGrade = int(input("enter pass grade: "))
manyLessons = int(input("how many lessons do you have? "))

for i in range(manyLessons):
    allLessons.append(input(f"enter the name of the {i + 1}th lesson: "))
    credit.append(int(input(f"enter {allLessons[i]} lesson credit: ")))
    lesson.append(int(input(f"enter the grade for the {allLessons[i]} lesson: ")))
    totalCredit += credit[i]

for i in range(manyLessons):
    average += (credit[i] * lesson[i]) / totalCredit

print("---------------------------------------------")

letters = semesterLetter.letterGrade(average)

if average < passingGrade:
    k = True

if k == False:
    k = "Passed!"
else:
    k = "Couldn't pass!"

for i in range(manyLessons):
    didItPass = False
    lessonLetters = lessonLetter.lessonLetter(lesson[i])
    if lesson[i] < passingGrade:
        didItPass = True
    if didItPass == False:
        didItPass = "Passed the lesson!"
    else:
        didItPass = "Couldn't pass the lesson!"
    print(
        f"credit of {allLessons[i]} course: {credit[i]}, grade: {lesson[i]}, letter grade: {lessonLetters}, {didItPass}")

print("---------------------------------------------")
print(f"average: {average}, letter grade: {letters}, {k}")
