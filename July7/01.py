# myfile = open('text.txt', encoding="utf-8")
# text = myfile.read()
# myfile.close()
#
# print(text)


myfile = open('text.txt', 'a', encoding="utf-8")
myfile.write("\nHello!")
myfile.close()


# myfile = open('text.txt', 'w', encoding="utf-8")
# myfile.write("\nHello!")
# myfile.close()