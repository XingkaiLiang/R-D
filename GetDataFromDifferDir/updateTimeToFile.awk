#运行前
BEGIN{
    srcFile ="testTime.ph"
    destFile ="result.ini"
    timeData="debug"
    lineStart = 0
    debugFilename="lxk"
    findFlag =0

}
#运行中
{
    #printf "start to process file %s\n",FILENAME
    if($0~"TestTime")
    {
        #get the testtime from source file
        debugFilename = $3
    }

    if($0~"timestamp")
    {
        #find key word in target file
        findFlag =1
        lineStart = FNR + 1
        lintEnd = lineStart +6
        #printf "findFlag = %d linestart = %d\n",findFlag,lineStart
    }

    if(findFlag == 1 && FNR >=lineStart && FNR<= lintEnd)
    {
        temp = $0""debugFilename
        print temp
        if(FNR == lintEnd)
        {
            findFlag = 0
        }
        $0 = temp
    }
    else
    {
        #skip and check next sentence
        next
    }
    if(FILENAME ==srcFile)
    {
        debugFilename = FILENAME
        #printf "start to process file:%s",FILENAME
        if($0~"TestTime")
        {
            timeData = $2
        }
    }

    if(FILENAME ==destFile)
    {
        debugFilename = FILENAME
        if($0~"timestamp")
        {
             lineStart = FNR+1
         }
        #printf "start to process file:%s and startLine = %d",FILENAME,lineStart
    }
    newValue = $0""debugFilename
    $0 = newValue    

}
#运行后
END{
    #printf "at the end debugFilename = %s\n",debugFilename
}


































