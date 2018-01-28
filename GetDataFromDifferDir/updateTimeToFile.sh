pattern1="uts"
pattern2="uos"
keyword="TestTime"
keyword2="="
FilePath=".\\GitHub\\folly\\"
filename=$1
filename2=$2
echo $FilePath
echo $filename2
filename2=$(echo $FilePath$2)
echo $filename2
#1.取时间戳数据
#get timeData
timeValue=$(sed -n "/$keyword/p" $filename)

#get substring from specific location：7
timeValue3=$(echo ${timeValue:16})
#timeValue4=$(echo ${timeValue:0-13:10})

#2.操作.ini文件，保存数据

#在行尾添加数据
#sed -i "3,8s/$/$ti..meValue3/" $filename

#取要插入的数据
timeValue4=$(echo $keyword2$timeValue3)
echo $keyword2
echo $timeValue3
echo $timeValue4
#把=后面的替换成新词
sed  "s/\=/$timeValue3/" $filename

#把数据替换到.ini文件中
sed  -i "s/\=/$timeValue4/" $filename2
#sed -i "2,7s/$pattern2/$pattern1/" $filename
#sed -i 's/uts/uos/' $filename
#sed -e '1,10c/I can do it' file

#替换脚本
#http://wiki.jikexueyuan.com/project/shell-learning/sed-search-and-replace.html
#详细例子
#https://jingyan.baidu.com/article/22fe7cedce9e3d3003617f45.html