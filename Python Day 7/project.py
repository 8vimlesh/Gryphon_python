import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Students"
ws.append(["Name", "Math", "Science", "English", "Computer"])
ws.append(["Rahul", 85, 90, 78, 92])
ws.append(["Priya", 90, 85, 88, 95])
ws.append(["Rohan", 60, 55, 70, 65])
ws.append(["Sneha", 78, 82, 85, 80])
ws.append(["Amit", 45, 50, 55, 48])
ws.append(["Pooja", 92, 88, 90, 94])
ws.append(["Vikas", 35, 40, 38, 42])
ws.append(["Neha", 88, 92, 85, 90])
wb.save("Students.xlsx")
print("Excel file created!")

df = pd.read_excel("Students.xlsx")

df["Average"] = df[["Math", "Science", "English", "Computer"]].mean(axis=1)

df["Result"] = df["Average"].apply(
    lambda x: "pass" if x >= 60 else "fail")

print("\n--- Student Results ---")
print(df[["Name", "Average", "Result"]])

print(f"\nTopper :{df.loc[df['Average'].idxmax()]["Name"]}")
print(f"\nLowest :{df.loc[df['Average'].idxmin()]["Name"]}")
print(f"\nClass Average : {df['Average'].mean():.2f}")

plt.figure(figsize=(10, 6))
plt.bar(df["Name"], df["Average"], color="skyblue")
plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.axhline(y=60, color="red", linestyle="--", label="Pass")
plt.legend()
plt.show()

df.to_excel("results.xlsx", index=False)
print("\n Results saved!")