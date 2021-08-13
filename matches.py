#Step 1: Class "matches" 
class matches:
    result = []
    def __init__(self, inputstr):
        if type(inputstr) ==str:
            self.inputstr = list(map(str, inputstr.strip('[]').replace('"', '').replace(' ', '').replace("'", '').split(',')))
        elif type(inputstr) ==list:
            self.inputstr = inputstr
        else:
            self.inputstr = ' '

    def find(self, findstr):
        if self.inputstr == ' ':
            return 'User should enter valid input list of string details'

        if type(findstr) ==str:
            findstr = findstr.strip('[]').replace('"', '').replace(' ', '').replace("'", '')
        else: 
            return 'User should enter valid find string details'
            
        self.permute(list(findstr), 0, len(findstr))
        return list(set(list(self.inputstr)) & set(self.result))
    
    def permute(self, data, i, length):
        if i == length:
            self.result.append(''.join(data) )
        else:
            for j in range(i, length):
                data[i], data[j] = data[j], data[i]
                self.permute(data, i+1 , length)
                data[i], data[j] = data[j], data[i]
 
