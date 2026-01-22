first_name: str
gpa: float = 0.0

DEAN_LIST: float = 3.5
DEANS_LIST_MSG: str = "You made the Dean's List"
HONOR_ROLL: float = 3.25
HONOR_ROLL_MSG = "You made the Honor Roll"
SENTINEL: str = 'ZZZ'
INPUT_STR: str = 'Enter the first name: '
INPUT_GPA_STR: str = 'Enter the GPA: '


while True:
   first_name = input(INPUT_STR)
   if first_name.upper() != SENTINEL:
      gpa =  float(input(INPUT_GPA_STR))
      if gpa >= DEAN_LIST: 
        print(DEANS_LIST_MSG)
      elif gpa >= HONOR_ROLL:
        print(HONOR_ROLL_MSG)
   else:
      break