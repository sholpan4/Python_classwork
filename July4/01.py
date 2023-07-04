name = ""
a = name.casefold() #приводит в единый "наименование"
name = "шубадуба   \n"
a = name.replace("дуб", "береза", 1)

#a = name.split("дуб")
#a = name.partition("дуб")

a = name.strip()

name = name.encode('koi8-r')



print(a)