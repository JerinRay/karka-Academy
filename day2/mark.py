tamil = float(input("Enter marks for Tamil: "))
english = float(input("Enter marks for English: "))
maths = float(input("Enter marks for Maths: "))
science = float(input("Enter marks for Science: "))
social = float(input("Enter marks for Social: "))
total_marks = tamil + english + maths + science + social
average_marks = total_marks / 5
print("\n--- Mark Summary ---")
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)