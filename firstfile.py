
import os
import os.path
import numpy as np

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




while True:
     if len(UserInclusions) != 0:
          break
     choice = input("Do you want to the results to only include certain filetypes?").lower()
     if choice == 'y':
          print('Ok! enter every extension you want to be included, without the dot (and with no spaces too!)\n please do not include any extensions that you said to include before ;(\n type ""STOP"" when finished!')
          while True:
               choice = input('GO! :)\n').lower()
               if choice == 'stop':
                    break
               else:
                    inclusionsStatus = 1
                    UserInclusions.append(choice)
     if choice == 'n':
          break







while inclusionsStatus == 0:
    choice = input('Do you want image files? Y or N\n').lower()
    if choice == 'y':
         break
    if choice == 'n':
          UserExclusions.extend(imgExtensions)
          break
while inclusionsStatus == 0:
    choice = input('Do you want video files? Y or N:\n').lower()
    if choice == 'y':
         break
    if choice == 'n':
          UserExclusions.extend(videoExtensions)
          break
while inclusionsStatus == 0:
    choice = input('Do you want audio files? Y or N:\n').lower()
    if choice == 'y':
         break
    if choice == 'n':
          UserExclusions.extend(audioExtensions)
          break
while inclusionsStatus == 0:
    choice = input('Do you want installer files? Y or N:\n').lower()
    if choice == 'y':
         break
    if choice == 'n':
          UserExclusions.extend(installerExtensions)
          break
while inclusionsStatus == 0:
    if len(specialExtensions) != 0:
         UserExclusions.extend(specialExtensions)
         break
    choice = input('Finally, are there any files you personally do not want included? Y or N\n').lower()
    if choice == 'y':
         print('Ok! enter every extension you want excluded, without the dot (and with no spaces too!). type ""STOP"" when you are finished!! :D\n')
         while True:
          choice = input('GO! :)\n').lower()
          if choice == 'stop':
              break
          else:
               specialExtensions.append(choice)
    if choice == 'n':
         break
               



# for i in UserExclusions:
#      for k in UserInclusions:
#           if i==k:
#                print("you fucked up buddy")




     

        
         

# TO TEST: size equivalence against windows to
# make sure this is actually scanning every file
list = os.walk(r"C:\Users\rosha\Downloads\TESTFOLDER") 

paths = [] 
for root, dirs, files in list:
      for file in files:
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
        temp = string[-1-i]
        letter_box.append(temp)
     
pathsizes = []
for path in paths:
     pathsize =  os.stat(path).st_size
     pathsizes.append(pathsize)


     
# when we do this numpy business everything becomes
# a numpy.str object... convert to int later or now...
     
infostack = np.column_stack((paths, file_extensions, pathsizes))


# Begin data discrimination



delRows = 0

for index, val in np.ndenumerate(infostack):
     #print(index,val)
    # print(index[1])
     if index[1] == 2: #what is this doing  (if we're in the correct column) index[1] gives the second digit in the coordinate pair that describes everything. if that second digit is a 2, we know that it is our data column)
          #print('woo hoo')
          #print('this is the filesize: ' + val)
          if int(val) == 1: # !!! TODO: MAKE MODULAR
              #print('gotcha: your row is:' + str(index[0]))
              #print('gotcha: your EFFECTIVE row is:' + str(index[0]-i))
              infostack = np.delete(infostack,(index[0]-delRows),0) #should remove the entire row
              #print(infostack) 
              #print('\n')
              delRows = delRows+1
     if index[1] == 1 and (len(UserInclusions) == 0): #this is our second column, our file extension. IF NO inclusions have been made, exclusions have been made. But what if both are empty? well, then all files are free, and a given value doesn't get scanned at all. hooray
          if val in UserExclusions: #if the file extension being questioned is in the naughty list
               infostack = np.delete(infostack,(index[0]-delRows),0) #same logic as before
               delRows = delRows+1
     if index[1] == 1 and (len(UserExclusions) == 0):
          if val not in UserInclusions:
               infostack = np.delete(infostack,(index[0]-delRows),0)
               delRows = delRows+1
     # if index[1] == 0: #this is our first column, our path
     #      if val in UserAttExlusions:
     #           infostack = # fill out with same logic
        
print(infostack)

# End data discrimination
              
#extracting top whatever
               

top2 = infostack[0:2:]
print(top2)




        











