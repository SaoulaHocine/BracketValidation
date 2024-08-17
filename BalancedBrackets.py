

arr1 = ["[", "(", "{"]
arr2 = ["]", ")", "}"]

FileDattent=[];

def IsColsed(char1,char2):
  return arr1.index(char1) == arr2.index(char2)

def CheckTxt(txt,index):
  if(index==len(txt)):
    return True

  if(txt[index] in (arr1+arr2)):
    if(txt[index] in arr2):
      if len(FileDattent)>0:
        if( IsColsed(FileDattent[-1],txt[index])):
          FileDattent.pop()
          return CheckTxt(txt,index+1)
        else:
         return False
      else:
        FileDattent.append("-1")
        return False

      
    else:
      FileDattent.append(txt[index])
      return CheckTxt(txt,index+1)
  else:
    return CheckTxt(txt,index+1)
  return False


txt=input("Enter your txt : ")
CheckTxt(txt,0)



print("Phrase Corect : ",len(FileDattent)==0)