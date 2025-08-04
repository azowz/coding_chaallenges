total_mimutes =  input("please type the number of minutes: \n")

hours = int(total_mimutes)// 60
minutes = int(total_mimutes) % 60
socentd = int(minutes) % 60

print("this coures is " + str(hours) +" hours and " + str(minutes) 
      +" minutes and "+str(socentd) + "seconds")