#main.py

#First We Will calculate The Grade with User defined Function
def grade(avg) :
    # There Is Used the if....elif
    if 91 <= avg <= 100 :
        #defining The Local Variable Of Grade
        Grade="A++"
    elif 81 <= avg <= 90:
        Grade="A"
    elif 71 <= avg <= 80:
        Grade="B++"
    elif 61 <= avg <= 70:
        Grade="B"
    elif 51 <= avg <= 60:
        Grade="C"
    elif 33 <= avg <= 50:
        Grade="D"
    else :
        Grade="FF"
    #returning The local Variable Grade
    #The Value Of Grade Will be Changed According To condition parsing stage
    return Grade  
    #print(grade(95))
   
try: 
    name=(input("Enter The Name Of Student ::"))
    #There are Created Two empty Dictionary Created
    student={} ;    marks={}
    # the marks variable will Store marks
    #The student Variable will Store the nested dict of name and marks
    marks_list=["Maths","English","Science","Social.Science","Sanskrit","Gujarati"]

    total=0
    for i in marks_list:
        m=int(input(f"Enter {i} Marks Out Of 100 :"))
        if m < 0 or m > 100:
                raise ValueError(f"❌❌ Marks for {i} must be between 0 and 100.")
        marks[i]=m
        total+=m
    #Attatching The marks into student Dictionary
    student[name]=marks
    #Printing The All Data Of student
    print("Total Marks :",total)
    print("Average Marks : :",total/6)
    print("Grade :",grade(total/6))
    print(student)
    
    #Serializing The data
    import pickle as p
    #opening binary file of data
    with open("data","wb") as f:
        #Using Dump Method To Store data into binary format
        p.dump(student,f)
except ValueError as V:
    print("❌❌Please enter valid Marks")
    print(V)
except TypeError as V:
    #This Block Will Handle The type error if another data type entered
    print("❌❌Please enter valid Marks")
else:
    print("You Data Is Successfully Stored..")
finally :
    #This Block Used To Ensure there is no error occured
   
    print("-->>Program Executed<<--")

