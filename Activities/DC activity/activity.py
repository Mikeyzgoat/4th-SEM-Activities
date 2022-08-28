# create exception class for unequal code word lengths
class UnequalLength(Exception) :
    pass

# create exception class for unknown choice input while asking for another time
class UnknownChoice(Exception) :
    pass

# creating an exception for non binary inputs
class NonBinaryinput(Exception):
    pass
# creating a exception for error detection in CRC
class CodewordError(Exception):
    pass

# choice function
def choice():
    while(True) :
        try:
            ch = str(input("Enter\n1. To compute hamming distance\n2. To simulate CRC\n3. To Exit\n"))
            if(ch == "1") :
                hamming()
            elif(ch == "2") :
                crc_sim()
            elif(ch == "3") :
                exit(0)
            else : 
                raise UnknownChoice
            
        except UnknownChoice :
            print("Enter values from 1 to 3 only!!")
        except Exception as e:
            print(f'[ERROR]-{e}')


'''
hamming distance :
1. method apply bitwise xor to both code words and obtain another code.
2. the number of 1's in the new code is the hamming distance.
'''
def hamming():
    flag = True
    while(flag):
        try:
            print("Note : Enter code words such that their length is the same.\n")
            code1 = list(str(input("Enter 1st Code word : ")))
            for i in code1:
                if(i == "1" or i == "0"):
                    continue
                else : raise NonBinaryinput("")
            
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
                        code.append("0")
                        continue;
                    else : 
                        code.append("1")
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


'''
CRC functions:
modulo division
xor operation( dividend / divisor) of codewords
'''
class crc:
    def __init__(self,dataword : str,gen :str):
        self.dataword = dataword
        self.gen = gen.lstrip('0')
        self.crc = 0
        self.remainder = 0
    
    def EncodeDecode(self, mode: str = 'e') -> str:
        GeneratorLen = len(self.gen)
        DatawordLen = len(self.dataword)
        PaddedArray = list(self.dataword + ('0'*(GeneratorLen - 1) if mode == 'e' else self.crc))

        while '1' in PaddedArray[:DatawordLen]:
            ShiftIndex = PaddedArray.index('1')
            for i in range(GeneratorLen):
                PaddedArray[ShiftIndex + i] = str(int(self.gen[i] != PaddedArray[ShiftIndex + i]))

        crc = ''.join(PaddedArray)[DatawordLen:]
        return crc if mode == 'e' else str('1' not in crc)

    def send(self) -> None:
        self.crc = self.EncodeDecode('e')
        self.PrintData('Sender')

    def receive(self) -> None:
        self.remainder = self.EncodeDecode('d')
        self.PrintData('Receiver')

    def BitInvert(self, action: bool = False) -> None:
        if action:
            DatawordList = list(map(int, self.dataword))
            DatawordList[randrange(len(DatawordList) - 1)] ^= 1
            self.dataword = reduce(lambda x, y: x + str(y), DatawordList, '')

    def check(self) -> None:
        try:
            assert self.remainder == 'True'
            print('\nNo Error Detected.')
        except:
            print('\nError, Bit Inversion Detected.')
    
    def PrintData(self, person: str) -> None:
        print(
            f'\n{person} Side:\n'
            f'Dataword: {self.dataword} | Generator: {self.gen}\n'
            f'CRC: {self.crc} | Codeword: {self.dataword + self.crc}'
        )
        print()

# A method to simplify number of statements at choice()        
def crc_sim():
    print("Simulating Sender's end :")
    data = str(input("Enter Dataword : "))
    for i in data:
        if(i == "1" or i=="0"):
            continue
        else :
            raise NonBinaryinput("Input might contain spaces or strings other than 0 or 1. Enter Binary values only!\n")
    gen = str(input("Enter Generator polynomial : "))
    for i in gen:
        if(i=="1" or i == "0"): continue
        else : raise NonBinaryinput("Input might contain spaces or strings other than 0 or 1. Enter Binary values only!\n")
    obj = crc(data,gen)
    obj.send()
    obj.BitInvert(False)
    print("Simulating Receiver's end : ")
    
    obj.receive()
    obj.check()


'''
Stop and Wait protocol
'''    
def stopwait():
    return
'''
Entry point
contains menu for user to choose between
1. Simulation of hamming distance.
2. Simulation of CRC.
3. Simulation of Stop and Wait protocols.
4. A choice to exit.
'''
choice()