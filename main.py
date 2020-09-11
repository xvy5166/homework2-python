# Author: xvy5166@psu.edu

def getGradePoint(grade):
  if grade == "A":
    return 4.0
  elif grade == "A-":
    return 3.67
  elif grade == "B+":
    return 3.33
  elif grade == "B":
    return 3.0
  elif grade == "B-":
    return 2.67
  elif grade == "C+":
    return 2.33
  elif grade == "C":
    return 2.0
  elif grade == "D":
    return 1.0
  else:
    return 0.0
  
def run():
  grade1 = input("Enter your course 1 letter grade: ")
  credit1 = float(input("Enter your course 1 credit: "))
  if grade1 == "A":
    gradepoint1 = 4.0
    print (f"Grade point for course 1 is: 4.0")
  elif grade1 == "A-":
    gradepoint1 = 3.67
    print (f"Grade point for course 1 is: 3.67")
  elif grade1 == "B+":
    gradepoint1 = 3.33
    print(f"Grade point for course 1 is: 3.33")
  elif grade1 == "B":
    gradepoint1 = 3.0
    print(f"Grade point for course 1 is: 3.0")
  elif grade1 == "B-":
    gradepoint1 = 2.67
    print(f"Grade point for course 1 is: 2.67")
  elif grade1 == "C+":
    gradepoint1 = 2.33
    print(f"Grade point for course 1 is: 2.33")
  elif grade1 == "C":
    gradepoint1 = 2.0
    print(f"Grade point for course 1 is: 2.0")
  elif grade1 == "D":
    gradepoint1 = 1.0
    print(f"Grade point for course 1 is: 1.0")
  else:
    gradepoint1 = 0.0
    print(f"Grade point for course 1 is: 0.0")
  grade2 = input("Enter your course 2 letter grade: ") 
  credit2 = float(input("Enter your course 2 credit: "))
  if grade2 == "A":
    gradepoint2 = 4.0
    print (f"Grade point for course 2 is: 4.0")
  elif grade2 == "A-":
    gradepoint2 = 3.67
    print (f"Grade point for course 2 is: 3.67")
  elif grade2 == "B+":
    gradepoint2 = 3.33
    print(f"Grade point for course 2 is: 3.33")
  elif grade2 == "B":
    gradepoint2 = 3.0
    print(f"Grade point for course 2 is: 3.0")
  elif grade2 == "B-":
    gradepoint2 = 2.67
    print(f"Grade point for course 2 is: 2.67")
  elif grade2 == "C+":
    gradepoint2 = 2.33
    print(f"Grade point for course 2 is: 2.33")
  elif grade2 == "C":
    gradepoint2 = 2.0
    print(f"Grade point for course 2 is: 2.0")
  elif grade2 == "D":
    gradepoint2 = 1.0
    print(f"Grade point for course 2 is: 1.0")
  else:
    gradepoint2 = 0.0
    print(f"Grade point for course 2 is: 0.0")
  grade3 = input("Enter your course 3 letter grade: ")
  credit3 = float(input("Enter your course 3 credit: "))
  if grade3 == "A":
    gradepoint = 4.0
    print ("Grade point for course 3 is: 4.0")
  elif grade3 == "A-":
    gradepoint3 = 3.67
    print ("Grade point for course 3 is: 3.67")
  elif grade3 == "B+":
    gradepoint3 = 3.33
    print("Grade point for course 3 is: 3.33")
  elif grade3 == "B":
    gradepoint3 = 3.0
    print("Grade point for course 3 is: 3.0")
  elif grade3 == "B-":
    gradepoint3 = 2.67
    print("Grade point for course 3 is: 2.67")
  elif grade3 == "C+":
    gradepoint3 = 2.33
    print("Grade point for course 3 is: 2.33")
  elif grade3 == "C":
    gradepoint3 = 2.0
    print("Grade point for course 3 is: 2.0")
  elif grade3 == "D":
    gradepoint3 = 1.0
    print("Grade point for course 3 is: 1.0")
  else:
    gradepoint3 = 0.0
    print("Grade point for course 3 is: 0.0")
  GPA = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3)
  print(f"Your GPA is: {GPA}")


if __name__ == "__main__":
  run()