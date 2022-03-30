# Searching string t see if it start with "The" and ends with "Ethiopia"
import re
newmsg = "Python is the language i enjoy most in coding "
#newmatch = re.split("\s",newmsg)

# spliting string at first occurence 
#specifiying max split
newmatch = re.split("\s",newmsg,2)
print(newmatch)
newsubs =re.sub("\s", "@ ",newmsg )
print(newsubs)