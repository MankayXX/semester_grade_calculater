def lessonLetter(x):
    if x > 100 and x < 110:
        letterGrades = "A+"
    if x >= 90 and x <= 100:
        letterGrades = "AA"
    if x >= 85 and x < 90:
        letterGrades = "BA"
    if x >= 80 and x < 85:
        letterGrades = "BB"
    if x >= 70 and x < 80:
        letterGrades = "CB"
    if x >= 60 and x < 70:
        letterGrades = "CC"
    if x >= 50 and x < 60:
        letterGrades = "DC"
    if x >= 45 and x < 50:
        letterGrades = "DD"
    if x > 0 and x < 45:
        letterGrades = "FF"
    return letterGrades