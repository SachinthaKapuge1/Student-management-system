

#Student list
ls=[]

###################################################################################################
#creating student class
class Student:
    #Constructor
    def __init__(self,name,index,mark1,mark2):
        self.name=name
        self.index=index
        self.mark1=mark1
        self.mark2=mark2

    #Accepting students
    def inputs(self):
        try:
            name=str(input("NAME="))
            index=int(input("INDEX="))
            mark1=int(input("MARK1="))
            mark2=int(input("MARK2="))
            ob=Student(name,index,mark1,mark2)
            ls.append(ob)
        except:
            print("Warning!!! Please check your inputs")

    #Display a Students
    def displayAll(self,ob):
        print("\n")
        print("Name:",ob.name)
        print("index:",ob.index)
        print("mark1:",ob.mark1)
        print("mark2:",ob.mark2)
        
    #Search
    def search(self,d_index):
        for i in range(len(ls)):
            if ls[i].index==d_index:
                return i

#####################################################################################################
while True:
    print("\nAdd a Student -> 1\nDisplay all Students -> 2\nSearch a Student -> 3\nDelete a Student -> 4\nUpdate a student -> 5\nTerminate the programe -> 6\n")

    try:
        number=int(input("What do you want? -> "))
        if number in [1,2,3,4,5,6]:
            print("")
            
            #print("Please give a correct number!!!")
            #create a initial object
            obj=Student("",0,0,0)

            #Add Objects
            if number==1:
                obj.inputs()
                

            #Display All
            if number==2:
                for i in range(len(ls)):
                    obj.displayAll(ls[i])
                

            #Search
            if number==3:
                s_index=int(input("Enter the Index Number ="))
                k=obj.search(s_index)
                ls[k].displayAll(ls[k])
                
            #Delete
            if number==4:
                d_index=int(input("Enter the index to delete = "))
                j=obj.search(d_index)
                del(ls[j])


            #Update
            if number==5:
                u_index=int(input("Enter the index to update = "))
                l=obj.search(u_index)
                ls[l].name=str(input("Enter the new name = "))
                ls[l].index=int(input("Enter the new index = "))
                ls[l].mark1=int(input("Enter the new mark1 = "))
                ls[l].mark2=int(input("Enter the new mark2 = "))

            #Termination
            if number==6:
                print("We are terminating!!!")
                exit()
        else:
            print("")
            print("The entered number is not valid!!!")
                
            

    except:
        print("")
        print("Please enter a valid number!!!")







        
        
