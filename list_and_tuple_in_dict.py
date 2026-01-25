#list in dictionary tuple in dictionary

dic={"idno":232508,
     "dept":"ai",
     "subject":["c++","java","python"],
        12:"is my fvrt",
        "my hobbies":("movies","sex",23532,"bas")
}

print(type(dic))
print(dic)
print(dic["subject"])#we can access dictionary through key elements
                     #their is no indexs in dict
                     
#mutibility
dic["idno"]=2374
print(dic["idno"])