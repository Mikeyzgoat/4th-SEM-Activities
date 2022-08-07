# create exception class for unequal code word lengths
class UnequalLength(Exception) :
    pass

# create exception class for unknown choice input while asking for another time
class UnknownChoice(Exception) :
    pass

# creating an exception for non binary inputs
class NonBinaryinput(Exception):
    pass

# choice function
def choice():
    while(True) :
        try:
            ch = int(input("Enter\n1. To compute hamming distance\n2. To Exit\n"))
            if(ch == 1) :
                hamming()    
            elif(ch == 2) :
                exit(0)
            else : 
                raise UnknownChoice
            
        except UnknownChoice :
            print("Enter either 1 or 2 !!")
    
# compute hamming distance
def hamming():
    flag = True
    while(flag):
        try:
            print("Note : Enter code words such that their length is the same.\n")
            code1 = list(str(input("Enter 1st Code word : ")))
            for i in code1:
                if(i == "1" or i == "0"):
                    continue
                else : raise NonBinaryinput
            
            code2 = list(str(input("Enter 2nd Code word : ")))
            for i in code2 :
                if(i == "1" or i == "0"):
                    continue
                else : raise NonBinaryinput
            
            k=0
            code = [] #empty list to append code word after xor
            hamdist = 0
            if(len(code1) == len(code2)) :
                for i in range(len(code1)):
                    if(code1[i] == code2[i]) : 
                        code.append(0)
                        continue;
                    else : 
                        code.append(1)
                        hamdist += 1
                        continue;
            else :
                raise UnequalLength
            
            print("\nAfter XOR operation : ")
            for i in code:
                print(str(i),end = " ")
            print("\nHamming Distance : "+str(hamdist)) 
            flag = False
            
        except UnequalLength :
            print("Code word's length did not match. Enter code words again!.\n")
        

        except NonBinaryinput :
            print("Input might contain spaces or strings other than 0 or 1. Enter Binary values only!\n")

def crc():
    
    return            


# driving code
choice()