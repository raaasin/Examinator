import csv
import pandas as pd 
df1 = pd.read_csv(r'C:\Users\nisar\Documents\student_reg.csv')
df2= pd.read_csv(r'C:\Users\nisar\Documents\admin_log.csv')
df3= pd.read_csv(r'C:\Users\nisar\Documents\questions.csv')
df4= pd.read_csv(r'C:\Users\nisar\Documents\student_results.csv')
w = input("Hello! welcome to our very own Examination software \nPress y to continue:")
why="y"
if w==why: 
  x = input("Enter your name:")
  print("Hello, " + x,"Please choose from the following options")
  login=int(input("1.Student \n2.Admin \n3.Register \n Enter a number here:"))
  
if login==1:
  studlog= input("Hello Dear Student! \nPlease enter your registration no:")
  studpass= input("Please enter your password:")
  for index,row in df1.iterrows():
    if studlog==row["regid"] and studpass==row["password"]:
      print("you logged in successfully!")
      """def ask_questions():
    	#Displays the question and takes in the answer. Then checks if the given answer is the correct asnwer
	    fh = open('untitled.csv')
	    row_count = len([i for i in fh])
	    questions_needed = 5
	    question_numbers = r.sample(range(1, row_count+1), questions_needed)
	    question_numbers.sort()

	    correct, wrong = 0, 0

	    fh = open('untitled.csv')
	
	    i = 1
    	for line in fh:
		  sl, question, key = line.split(',')
		  key = key.rstrip()

		  sl = int(sl)
		  if sl in question_numbers:
		  	print(i, ". ", question, "\nYour Ans: ", end='')
		  	ans = input().lower()

			if key in ans:
				print("Correct\n")
				correct += 1
			else:
				print("Wrong\n")
				wrong += 1

			i += 1
			del question_numbers[0]

	    print(f"\nCorrect answers: {correct}\nWrong answers: {wrong}\n")


      def main():
	    ask_questions()


       if __name__ == '__main__':
	     main()"""
    
    else:
      print("its wrong password")

if login==2:
  adlog= input("Hello Admin please enter your credentials below! \nPlease enter your username:")
  adpass= input("Please enter your password:")
  for index,row in df2.iterrows():
    if adlog==row["username"] and adpass==row["password"]:
      print("you logged in successfully!")
    else:
      print("its wrong password")

if login==3:
  studlog= input("Dear Student Welcome to Registration \nPlease enter a registration no :")
  studpass= input("Please enter a password:")
  for index,row in df1.iterrows():
    if studlog==row["regid"] :
      studlog= input("Dear Student Please enter a Unique user id this id has already been taken \nPlease enter a registration no :")
    else :
      print("")
