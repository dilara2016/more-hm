#if tey have a medical cause
medical_cause=input("did you have a medical cause Y or N")
#if no medical cause
atten = int(input("enter the attendance for student: "))
#is attendace hige ?
if medical_cause == 'Y':#checking attendance
 print ("You are allowed")
else:
 if atten>97: #checking attendance 2
  print("Allowed")
 else:
  print("Not allowed")