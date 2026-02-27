# 1. Git vs. GitHub.    version control vs online repository storage
# 2. Terminal vs. Command Line.   command line is text based interface to type instructions, terminal is application that provides access to interface
# 3. Local vs. Remote Repository. A local repository is on my physical computer, while a remote repository is stored on an online server like GitHub
# 4. Version Control. a system that keeps track of changes so versions can be recalled/easy for collaboration
# 5. Staging Area. area to prepare for commiting
# 6. git add. add files to staging area.
# 7. git commit. saves staged changes to local repository with a message.
# 8. git push. uploads local repo commits to remote
# 9. git status. displays files that are staged or not
# 10. git pull. retrieve content from online repository
# 11. pwd prints working directory: path of folder
# 12. ls lists out items in folder
# 13. cd change directory
# 14. nano edit files in terminal
# 15. touch create new empty file
# 16. mv move file
# 17. rm remove file
# 18. cat concatenate: display text content of file

#pwd
#ls
#cd brianna_repo
#git pull
#mv homework.py ../judy_decal/homework
#cd ../judy_decal/homework/
#cat homework.py
#git add
#git commit -m "message"
#git push
#github repo has work that isn't at local repo. to resolve, use git pull
#~/Recent/

def checkDataType(data):
    return str(type(data))

def evenOrOdd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
def sumWithLoop(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def duplicateList(original):
    duplicated = []
    for i in original:
        duplicated.append(i)
        duplicated.append(i)
    return duplicated

def square(num): #orignially missing ":""
    return num * num