hour = float(input("Hora:"))
minute = float(input("minuto:"))
second = float(input("segundo:"))
last_midnight = (hour * 3600) + (minute * 60) + second
next_midnight = 86400 - last_midnight
print("han pasado" ,  last_midnight , "segundos desde la última medianoche y quedan" , next_midnight , "para la siguiente medianoche")