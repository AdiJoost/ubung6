students = [
    "Herold",
    "Max",
    "Edgar"
]
grades = []
def getGrade(student):
    foundGrade = False
    while not foundGrade:
        userInput = input(f"Geben Sie die Note für {student} ein: ")
        try:
            grade = float(userInput)
            return grade
        except:
            print("Die Eingegebene Note ist nicht gültig")

print("Fügen Sie Noten hinzu")
for student in students:
    grades.append((student, getGrade(student)))
print(f"Ihre eingegebenen Noten: {grades}")
