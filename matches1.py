#This program is given for test the input method. Input values given by user
#Class "matches" having constructor and find function which matches the exact string chars in given list oif strings
class matches:
    result = []
    def __init__(self, inputstr):  #Constructor 
        if type(inputstr) ==str:
            self.inputstr = list(map(str, inputstr.strip('[]').replace('"', '').replace(' ', '').replace("'", '').split(',')))
        elif type(inputstr) ==list:  
            self.inputstr = inputstr
        else:                      
            self.inputstr = ' '

    def find(self, findstr):    #Find function 
        if self.inputstr == ' ':     
            return 'User should enter valid input list of string details'

        if type(findstr) ==str:
            findstr = findstr.strip('[]').replace('"', '').replace(' ', '').replace("'", '')
        else: 
            return 'User should enter valid find string details'
            
        self.permute(list(findstr), 0, len(findstr))
        return list(set(list(self.inputstr)) & set(self.result))  #match the string by set logic 
    
    def permute(self, data, i, length):  #permutation function 
        if i == length:
            self.result.append(''.join(data) )
        else:
            for j in range(i, length):
                #Swap logic 
                data[i], data[j] = data[j], data[i]
                self.permute(data, i+1 , length)
                data[i], data[j] = data[j], data[i]
 
input_list =input('Enter input list of strings:')
obj = matches(input_list)
find_str = input('Enter find string in list of stings:')
objresult= obj.find(find_str)
print(objresult)