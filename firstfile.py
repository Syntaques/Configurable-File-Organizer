
import os
import os.path
import numpy as np
from tkinter import Tk #shamelessly stole this and the next line from stackoverflow
from tkinter.filedialog import askdirectory
#this is still important

# #lmg1.jpg is visible
# statcheck = os.stat(r"C:\Users\rosha\Downloads\TESTFOLDER\lmg3.jpg").st_file_attributes
# print(statcheck) # prints out 
# #lmg2.jpg is hidden AND READ ONLY(by windows attribute)
# statcheck = os.stat(r"C:\Users\rosha\Downloads\TESTFOLDER\lmg2.jpg").st_file_attributes
# print(statcheck == 34) # prints out 34

#end important zone


# Query Start (so much room for optimization, using tricks that I don't know yet)

UserExclusions = []
imgExtensions = ['tiff','png','jpg','jpeg','webp']
videoExtensions = ['mp4','mkv','mov']
audioExtensions = ['wav','flac','mp3','m4a','aac']
installerExtensions = ['']
specialExtensions = []
UserInclusions = []

inclusionsStatus = 0

cutoff = 100000
maxsize = 10
filtersmade = 0



# while True:
#      if len(UserInclusions) != 0:
#           break
#      choice = input("Do you want to the results to only include certain filetypes?").lower()
#      if choice == 'y':
#           print('Ok! enter every extension you want to be included, without the dot (and with no spaces too!)\n please do not include any extensions that you said to include before ;(\n type ""STOP"" when finished!')
#           while True:
#                choice = input('GO! :)\n').lower()
#                if choice == 'stop':
#                     break
#                else:
#                     inclusionsStatus = 1
#                     UserInclusions.append(choice)
#      if choice == 'n':
#           break

# while inclusionsStatus == 0:
#     choice = input('Do you want to exclude image files? Y or N\n').lower()
#     if choice == 'n':
#          break
#     if choice == 'y':
#           UserExclusions.extend(imgExtensions)
#           break
# while inclusionsStatus == 0:
#     choice = input('Do you want to exclude video files? Y or N:\n').lower()
#     if choice == 'n':
#          break
#     if choice == 'y':
#           UserExclusions.extend(videoExtensions)
#           break
# while inclusionsStatus == 0:
#     choice = input('Do you want to exclude audio files? Y or N:\n').lower()
#     if choice == 'n':
#          break
#     if choice == 'y':
#           UserExclusions.extend(audioExtensions)
#           break
# while inclusionsStatus == 0:
#     choice = input('Do you want to exclude installer files? Y or N:\n').lower()
#     if choice == 'n':
#          break
#     if choice == 'y':
#           UserExclusions.extend(installerExtensions)
#           break
# while inclusionsStatus == 0:
#     if len(specialExtensions) != 0:
#          UserExclusions.extend(specialExtensions)
#          break
#     choice = input('Finally, are there any files you personally want excluded? Y or N\n').lower()
#     if choice == 'y':
#          print('Ok! enter every extension you want excluded, without the dot (and with no spaces too!). type ""STOP"" when you are finished!! :D\n')
#          while True:
#           choice = input('GO! :)\n').lower()
#           if choice == 'stop':
#               break
#           else:
#                specialExtensions.append(choice)
#     if choice == 'n':
#          break
               


        
         
# TO TEST: size equivalence against windows to
# make sure this is actually scanning every file
    

path = askdirectory(title='Select Folder!!!!!!!! :D') # shows dialog box and return the path
print(path)
list = os.walk(path) 

paths = [] 
for root, dirs, files in list:
      for file in files:
          if len(file) == 0: # if there is no file (happens when searching empty folders) also NEW!!! delete if needed
               continue
          else:
            #print("joining!" + str(root)+ " "+ str(file))
            paths.append(os.path.join(root,file))

file_extensions = []
for string in paths:
    letter_box = []
    for i,elem in enumerate(string):
        if string[-1-i] == '.':
            complete_string = "".join(str(ele) for ele in letter_box) #joins individual letters into a string
            complete_string = complete_string[::-1] #reverse a string!!
            file_extensions.append(complete_string)
            break
        if len(letter_box) == 8: #NEW!!!! delete if needed
           complete_string = 'default'
           file_extensions.append(complete_string)
           break
        temp = string[-1-i] # what is this doing
        letter_box.append(temp)
     
pathsizes = []
for path in paths:
     pathsize =  os.stat(path).st_size
     #if pathsize < cutoff:
         #continue
     #else:
     pathsizes.append(pathsize)


     
# when we do this numpy business everything becomes
# a numpy.str object... convert to int later or now...
     
infostack = np.column_stack((paths, file_extensions, pathsizes))

print('passed!')

# Begin data discrimination (broken)



# delRows = 0

# for index, val in np.ndenumerate(infostack):
#      #print(index,val)
#     # print(index[1])
#      if index[1] == 2: #what is this doing  (if we're in the correct column) index[1] gives the second digit in the coordinate pair that describes everything. if that second digit is a 2, we know that it is our data column)
#           #print('woo hoo')
#           # print('this is the filesize: ' + val)
#           # print(int(val) == 1)
#           if False == True: # !!! TODO: MAKE MODULAR
#               print('fuck my roommate 1')
#               infostack = np.delete(infostack,(index[0]-delRows),0) #should remove the entire row
#               delRows = delRows+1
#      if index[1] == 1 and (len(UserInclusions) == 0): #this is our second column, our file extension. IF NO inclusions have been made, exclusions have been made. But what if both are empty? well, then all files are free, and a given value doesn't get scanned at all. hooray
#           if val in UserExclusions: #if the file extension being questioned is in the naughty list
#                print('fuck my roommate 2')
#                infostack = np.delete(infostack,(index[0]-delRows),0) #same logic as before
#                delRows = delRows+1
#      if index[1] == 1 and (len(UserExclusions) == 0):
#           if val not in UserInclusions:
#                print('fuck my roommate 1')
#                infostack = np.delete(infostack,(index[0]-delRows),0)
#                delRows = delRows+1
#      # if index[1] == 0: #this is our first column, our path
#      #      if val in UserAttExlusions:
#      #           infostack = # fill out with same logic

# end stupid shit


# begin filtering process
print('begin filtering! :)')
# we want this entire rigmarole to be skipped if user has made NO exlcusions
if filtersmade == 1:
     delRows = 0
     for index, val in np.ndenumerate(infostack):
          print('STILLLL working')
          if index[1] == 2:
               if int(val) <= 100000:
                    #print('fuck1')
                    # print(val)
                    # print(delRows)
                    infostack = np.delete(infostack,(index[0]-delRows),0) #deletes a row
                    delRows = delRows +1 
          if index[1] == 1 and (len(UserExclusions) > 1):
               if val in UserExclusions:
                    #print('fuck2')
                    infostack = np.delete(infostack,(index[0]-delRows),0)
                    delRows = delRows + 1
          if index[1] == 1 and (len(UserInclusions) > 1):
               if val not in UserInclusions:
                    #print('fuck3')
                    infostack = np.delete(infostack,(index[0]-delRows),0) 
                    delRows = delRows +1
          #if index[1] == 0 || file attribute filtering
               
#end filtering process

print('end filtering!')

# begin sorting algo (mergesort)

def mergesort(array):
  if len(array) <= 1:
    return array
  leftarr = mergesort(array[0:(round(len(array)/2))])
  rightarr = mergesort(array[(round(len(array)/2)):len(array)])
  mergearr = []
  while (len(leftarr) + len(rightarr)) != 0: #jobs not finished
    if len(leftarr) < 1:
      mergearr.extend(rightarr)
      break
    if len(rightarr) < 1: #change to elif maybe 
       mergearr.extend(leftarr)
       break
    if leftarr[0] < rightarr[0]:
      mergearr.append(leftarr[0])
      leftarr.pop(0)
    elif rightarr[0] < leftarr[0]:
       mergearr.append(rightarr[0])
       rightarr.pop(0)
    elif rightarr[0] == leftarr[0]: #since they're the same it makes no sense to append both sides but this is more of a readability thing
      mergearr.append(rightarr[0])
      mergearr.append(leftarr[0])
      rightarr.pop(0)
      leftarr.pop(0)
  return mergearr



# end sorting algo (mergesort)

def topgetter(numpyarray,maxsize):
     delRows = 0
     sizes = []
     for index, val in np.ndenumerate(numpyarray):
          if index[1] == 2:
               sizes.append(int(val))
     sizes = mergesort(sizes)
     topsizes = sizes[len(sizes)-1:len(sizes)-maxsize-1:-1]
     topsizes = [int(i) for i in topsizes]
     for index, val in np.ndenumerate(numpyarray):
         if index[1] == 2:
          val = int(val)
          if val not in topsizes:
               numpyarray = np.delete(numpyarray,(index[0]-delRows),0)
               delRows = delRows +1
     # print(np.shape(numpyarray)[0])
     # print(type(np.shape(numpyarray)[0]))
     while np.shape(numpyarray)[0] != int(maxsize):
         #print(np.shape(numpyarray)[0]-1)
         numpyarray = np.delete(numpyarray,np.shape(numpyarray)[0]-1,0)

     X_1 = np.array([[x,y,int(z)] for x,y,z in numpyarray],dtype='O') #makes the third column ints instead of whatever the fuck they were before. (numpy.str objects) stolen from stackoverflow
     numpyarray = X_1[X_1[:,2].argsort()[::-1]] # I deserve to use this I literally coded 2 different algos by hand in prep for this step. stolen from stackoverflow
     return numpyarray


print('begin sorting and extracting!')
print(topgetter(infostack,maxsize))
print(":D")


        











