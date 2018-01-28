import os
import sys
def updateDestFile(filename,keyword,timeData):
    fileData = ""
    with open(filename,"r") as f:
        for line in f:
            if keyword in line:
                #partOne = line[0:line.rfind('=',1)+1].rstrip()
                #line = partOne+timeData
                partOne = line.rstrip().split('=')[0]
                line=partOne+'='+timeData + '\n'
            fileData += line
    with open(filename,'w+') as f:
        f.writelines(fileData)


def getTimeStamp(filename,keyword):
    #.1.get abs path if neccessaly

    #2.find keyword and get the data
    with open(filename,'r') as f:
        for line in f:
            if keyword in line:
                timedata = line.split()[2].rstrip()

    return timedata


if __name__ == '__main__':
    #1.get source data from .ph file
    temp1File = "F:\\GitHub\\R-D\\test\\testtime.ph"
    temp2File = "F:\\GitHub\\folly\\result.ini"
    filePath1 = "\\folly\\"
    sourceFile = sys.argv[1]
    destFile = sys.argv[2]
    
    filePath0 = "\\R-D\test\\"
    filePath2 = ".\build\script\\"
    
    sourcekeyword = 'TestTime'
    currentDir = os.getcwd()
    sourceFileFullPath = currentDir+filePath1+sourceFile

    destkeyword = "="
    #timedata = getTimeStamp(sourceFileFullPath,keyword)
    testdata = getTimeStamp(temp1File,sourcekeyword)
    print testdata
    
    #2.update the destination file with time data
    updateDestFile(temp2File,destkeyword,testdata)
    
