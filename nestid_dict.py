student={"name":"talha",
    "roll_no":23452,
    "subjects":{"c++":97,
    "python":87,
    "ai":98}
}
#nestid dictionary
print(student)
print(student["subjects"])
print(student["subjects"]["c++"])
#type casting 
print(list(student.keys()))
print(tuple(student.values()))
print(set(student.keys()))


