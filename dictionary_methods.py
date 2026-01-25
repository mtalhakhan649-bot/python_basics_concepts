marks={"AIstudents":"marks",
       "talha":29,
       "sheryar":20,
       "shahid":24,
       "sudais":23,
       "farhan":3,
}
print(marks)
print(marks.items())#it print the indivisual record of every person in '()' brakets.
print(marks.keys()) #it print only the left side data like here students names.
print(marks.values())#it print only the values of the cooresponding students
marks.update({"farhan":3,"khan":30,})#this method/fuction of dict can update the data that is in the dict
print(marks)#also we can add new record like in this khan:30
print(marks,marks.get("talha"))#through this we can print any records of our choice
print(marks,marks.pop("farhan"))#pop method use to delete some record from your  dict
