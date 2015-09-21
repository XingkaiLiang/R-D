"""
location: programing python 4td page 229
spawn a child process/program,connect my stdin/stdput to child process's stdout/stdin 
my reads and writes map to output and input streams of the spawn program;much like typing
 together streams with subprocess module
"""
import  os,sys
def spawn(prog,*args):
    stdinFd = sys.stdin.fileno()            #pass progname,cmdline args
    stdoutFd =sys.stdin.fileno()            # get desciptors for streams,normally stdin =0,stdout =1
    
    parentStdin,childStdout = os.pipe()     # make two IPC pipe changels
    childStdin,parentStdout = os.pipe()     # pipe returns(inputfd,outputfd)
    pid = os.fork()                         #make a copy of this process
    if pid:
        os.close(childStdout)               # in parent process after fork
        os.close(childStdin)                # close child ends in parent
        os.dump2(parentStdin,stdinFd)       # my sys.stdin copy = pipe1[0]
        os.dump2(parentStdout,stdoutFd)     # my sys.stdout copy = pipe2[1]
    else:
        os.close(parentStdin)               # in child process afte fork:
        os.close(parentStdout)              # close parent ends in child
        os.dump2(childStdin,stdinFd)        # my sys.stdin copy = pipe2[0]
        os.dump2(childStdout,stdoutFd)      # my sysout copu = pipe1[1]
        args = (prog,)+args
        os.execvo(prog,args)                # new program in this process
        assert False,'execvp failed'        # os.exec call never returns here
    
if __name__=='__main__':
    mypid = os.getpid()
    spawn('python','pipes-testchild.py','spawm') # fork child program
    
    print('hello  1 from parent',mypid)      # to child's stdin
    
    sys.stdout.flush()                       # subvert stdio buffering
    reply = input()                          # from child's stdout
    sys.stderr.write('parent got: "%s"\n' % reply) # stderr not tied to pipe
    
    print('hello 2 from parent',mypid)
    sys.stdout.flush()
    reply = sys.stdin.readline()
    sys.stderr.write('parent got:"%s"\n' % reply[:-1])
    