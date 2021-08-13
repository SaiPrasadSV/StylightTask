# Stylight - SEO Software Engineer Task

## What is the Task ? 
Python class which takes a list of strings in the constructor. This class will then have another function called find which takes a string to be matched. In the
end this find function will return all the strings from the list which contain the EXACT same characters and number of characters as our given string.

## Prerequisites to do this task 
To run this program below tools/libraries are needed
1) Python 3.8 or higher 
2) unitest library is needed
3) Any IDE tool can run this code and i have used visual Studio code to develop this 

## Solution of this taks/Approach to solve this task 
This solution has One class with constructor and two methods. One method is Static recursive method and another method find method which used to call to find the list of matched strings.

1) Read the input list of strings : One input is list of strings and other input is findSting. 
   a) There are so many ways we can pass input the created class. It can be passed via input method or it can be passed via other class.
   b) If we pass input details via input method then values will be in string because input method will read all the details as string format, so i have converted input string       to list by using below following code. 
     
     **self.inputstr = list(map(str, inputstr.strip('[]').replace('"', '').replace(' ', '').replace("'", '').split(',')))**
     Strip function will remove the braces and replace fucntion will remove unnecessary spaces or qutations. 
     Via input method class details are given in matches1.py file. 
     
   c) If input is getting from other calling application or program then it will verify given data is list or not.
   d) If input details are other than list or string then will throw error that User given invalid input details.

2) Once successfully read the both input details then :
   a) Intialize the class constructor with Input list of strings:
**      class matches:
          result = []
          def __init__(self, inputstr):
              if type(inputstr) ==str:
                  self.inputstr = list(map(str, inputstr.strip('[]').replace('"', '').replace(' ', '').replace("'", '').split(',')))
              elif type(inputstr) ==list:
                  self.inputstr = inputstr
              else:
                  self.inputstr = ' '**
                  
    b) Call the "find" method by using findString to check whether input list of string having any matching.
    
    b) To check exact same chantcter string available in given input list of string , first find the permutations of findString and check whether any permutations are available        in given input list of string. 
    
    c) To find the permutations of given findString created new permutations recursive function :
            def permute(self, data, i, length):
                if i == length:
                    self.result.append(''.join(data) )
                else:
                    for j in range(i, length):
                        data[i], data[j] = data[j], data[i]
                        self.permute(data, i+1 , length)
                        data[i], data[j] = data[j], data[i]
                        
    d) Variable **result** has been declared as global variable and it can be used self.result which will have all the permutations
    
    e) To match given input list of strings and list of permutations strings below simple set logic can be used :
         **list(set(list(self.inputstr)) & set(self.result))**
         
 3) Above set logic will return the list of matched stings and it will return in find function 


## Efficiency of the above task 
  Efficiency can be mesured by time complexity and results achieved by the above approach 
  
  1) **Time-Complexity** : Code logic having most of lines of code written single line and it will take time O(1) and which can be ignored as per BIG O principle. 
      Only logic which takes more time is Permutations function and this function time complexity is O(n) (n is number of charcters). Time complexity of set logic of n elements 
      O(n^k+1) , here k is number of sets. Hence overall time complexity of given logic is O(n^k+2).
    
  2) If we give more string length then efficiency will decreases , but it is quite low compare to other logic as we are using set logic which is more speed than other data structures 
  3) If find requests are more then Performance may decreases , but it is quite good than other logics which have been tested. 
  4) Rethink/Reconstruct approach : We can find permutations by itertator tools and it gives better results, but i did not use as it is build-in libraries. Please find the simple below logic to find the permutations. 
            
**                from itertools import permutations
                  l = list(permutations(range(1, 4)))
                  print l**
 
 6) Pros : 
      a) Have been covered different set of imput values, please find the test cases for more details 
      
      b) Have been used set logic to compare two given list 
      
      c) Very less number of lines without using build-in libraries and it gives good performance.
      
      d) Easy logic and it is covered most of python code logics like map, set, input ,static method etc 
     
     cons:
     
     a) Performance may decreases if we use large string in findString, but it can cover by using itertools as mentioned above.
