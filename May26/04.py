user_in1 = input("Введите объем флешки в Гб:")
user_in2 = input("Введите объем файла в Мб:")
flash_drive = user_in1 * 1024
#1gb=1024mb
try:
    flash_drive = int(user_in1)
    file_size = int(user_in2)

except ValueError:
    message = "Вы ввели неправильные данные"

else:
    
    result = flash_drive % file_size
    message = " %s копии файла вмещяет эта флешка" % result

print(message)