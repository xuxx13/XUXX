from optparse import OptionParser
import random

parser = OptionParser()
parser.add_option("-j", "--jobs", default = 3, help = "numbers of jobs in system",action="store", type = "int", dest = "jobs")
parser.add_option("-s", "--seed", default=0, help="the random seed",action="store", type="int", dest="seed")
parser.add_option("-m", "--maxlen", default=10, help="max length of job",action="store", type="int", dest="maxlen")


(options, args) = parser.parse_args()

random.seed = options.seed

print 'Here is the job list, with the run time of each job: '

joblist = []
for jobnum in range(0,options.jobs):
    runtime = int(options.maxlen * random.random()) + 1
    joblist.append([jobnum, runtime])
    print '  Job', jobnum, '( length = ' + str(runtime) + ' )'
print '\n'

lists = []
for i in range(0,4):
    lists.append([])

base = 1.0
quantum = []
for i in range(0,4):
    quantum.append(base)
    base *= 2.0

for job in joblist:
    lists[0].append(job)

jobcount = 0
for somelist in lists:
    jobcount += len(somelist)


turnaround = {}
response = {}
lastran = {}
wait = {}
for i in range(0,jobcount):
    lastran[i] = 0.0
    wait[i] = 0.0
    turnaround[i] = 0.0
    response[i] = -1

print 'Execution trace:'
thetime = 0.0
while jobcount > 0:
    for priority in range(0,4):
        if len(lists[priority]) > 0:
            job = lists[priority].pop(0)
            jobnum  = job[0]
            runtime = float(job[1])
            if response[jobnum] == -1:
                response[jobnum] = thetime
            currwait = thetime - lastran[jobnum]
            wait[jobnum] += currwait
            ranfor = 0

            if runtime > quantum[priority]:
                ranfor = quantum[priority]
                runtime -= ranfor
                print '  [ time %3d ] Run job %3d for %.2f secs, priority: %3d' % (thetime, jobnum, ranfor, priority)
                if priority == 3:
                    nextpriority = 3
                else:
                    nextpriority = priority + 1

                lists[nextpriority].append([jobnum,runtime])
            else:
                ranfor = runtime
                print '  [ time %3d ] Run job %3d for %.2f secs ( DONE at %.2f ), priority: %3d' % (thetime, jobnum, ranfor, thetime + ranfor, priority)
                turnaround[jobnum] = thetime + ranfor
                jobcount -= 1
            thetime += ranfor
            lastran[jobnum] = thetime
            break

print '\nFinal statistics:'
turnaroundSum = 0.0
waitSum       = 0.0
responseSum   = 0.0
for i in range(0,len(joblist)):
    turnaroundSum += turnaround[i]
    responseSum += response[i]
    waitSum += wait[i]
    print '  Job %3d -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f' % (i, response[i], turnaround[i], wait[i])
count = len(joblist)

print '\n  Average -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f\n' % (responseSum/count, turnaroundSum/count, waitSum/count)
