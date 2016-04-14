grades = {"A": 4.0,
          "A-": 3.7,
          "A+": 4.0,
          "B+": 3.33,
          "B":  3.0,
          "B-": 2.7,
          "C+": 2.33,
          "C": 2.0,
          "C-": 1.7,
          "D+": 1.3,
          "D":  1.0,
          "D-": 0.7,
          "F": 0
          }


input = input().upper()

array = input.split()

total = 0.0
legitSize = 0

for text in array:
    if text in grades:
        total += grades[text]
        legitSize += 1

print( round(total/legitSize, 2) )
