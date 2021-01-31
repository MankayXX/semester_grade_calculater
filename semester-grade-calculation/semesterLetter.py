k = False
def letterGrade(a):
    if a >= 90 and a <= 100:
        letterGrade = "AA"
    if a >= 85 and a < 90:
        letterGrade = "BA"
    if a >= 80 and a < 85:
        letterGrade = "BB"
    if a >= 70 and a < 80:
        letterGrade = "CB"
    if a >= 60 and a < 70:
        letterGrade = "CC"
    if a >= 50 and a < 60:
        letterGrade = "DC"
    if a >= 45 and a < 50:
        letterGrade = "DD"
    if a > 0 and a < 45:
        letterGrade = "FF"
    return  letterGrade
