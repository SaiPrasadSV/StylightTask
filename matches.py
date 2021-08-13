#Step 1: Class "matches" Created to check
class matches:
    result = []
    a = []
    def __init__(self, inputstr):
        self.inputstr = inputstr
        print(type(self.inputstr))
        print(self.inputstr)
        
    def find(self, findstr):
        base = len(findstr)
        self.permute(list(findstr), 0, len(findstr))
        perm = self.result
        print(self.result)
        return list(set(list(self.inputstr)) & set(perm))
    
    def permute(self, data, i, length):
        if i == length:
            self.result.append(''.join(data) )
        else:
            for j in range(i, length):
                # swap
                data[i], data[j] = data[j], data[i]
                self.permute(data, i+1 , length)
                data[i], data[j] = data[j], data[i]
 
input_list =list(map(str, input('Enter input list of strings:').strip('[]').replace('"', '').replace(' ', '').replace("'", '').split(',')))
obj = matches(input_list)
find_str = input('Enter find string in list of stings:')
objresult= obj.find(find_str)
print(objresult)