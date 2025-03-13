
#STRINGS INDISE DICTIONARIES

# name_major = {
#               "Ary"    : "Econ" ,
#               "Mridul" : "Phy",
#               "Pratik" : "IT"
#               }

# #iterating through the dictionary and printing it 
# for key, value in name_major.items():
#     print(f"Name is {key} and the major is {value}")

# for name, major in name_major.items():
#     print(f"The name is {name} and the major is {major }")

# for value in name_major.values():
#     print(value)

# for key in name_major.keys():
#     print(key)

# ----------------------------------------------------

#LISTS INSIDE DICTIONARIES

# student_info = {
#               "Ary"    : ["Econ", "prerar2@..."],
#               "Mridul" : ["Phy", "Agramr2@...."],
#               "Pratik" : ["IT" , "shrepra@..."]
#               }


# print(student_info["Ary"][0], ",", student_info ["Ary"][1])

# for key, value in student_info.items():
#     # print(f"The name is {key} and the info is {value[0]}")
#     # print(f"The name is {key} and the info is {value[1]}")
#     print(f"The name is {key} and the info is {value[0]}, {value [1]} ")

#------------------------------------------------------------------------

#DICTIONARIES INSIDE DICTIONARIES

student_info = {
                "Ary" : { "major":"econ" , "email":"emailAry" },
                }

print( student_info ['Ary'] ["major"])
print(student_info ["Ary"] ["email"])

names = [ ["Mridul", "Agrawal"], ["ary", "Prera"], ["Laiba", "Ashfaq"] ]

print( names [1] [1])


