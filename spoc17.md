（spoc)了解race condition. 进入race-condition代码目录。

执行 ./x86.py -p loop.s -t 1 -i 100 -R dx， 请问dx的值是什么？
   -1
   
执行 ./x86.py -p loop.s -t 2 -i 100 -a dx=3,dx=3 -R dx ， 请问dx的值是什么？
  两个线程dx的初始值均为3，而切换中断为100，所以先运行线程1，结束后运行线程2。两个线程中的dx都减为－1时退出
  
执行 ./x86.py -p loop.s -t 2 -i 3 -r -a dx=3,dx=3 -R dx， 请问dx的值是什么？
  两个线程dx的初始值均为3，而切换中断为3，但是两个线程有各自的dx值，不会互相影响，所以两个线程中的dx都为－1.
  
变量x的内存地址为2000, ./x86.py -p looping-race-nolock.s -t 1 -M 2000, 请问变量x的值是什么？
  1
  
变量x的内存地址为2000, ./x86.py -p looping-race-nolock.s -t 2 -a bx=3 -M 2000, 请问变量x的值是什么？为何每个线程要循环3次？
  为6
 循环3次，每次将内存加一。因为在线程1运行之前切换时栈会保存寄存器的值，在切换之后栈会对寄存器的值进行恢复，所以第二个线程中bx的值也为3
  
  
变量x的内存地址为2000, ./x86.py -p looping-race-nolock.s -t 2 -M 2000 -i 4 -r -s 0， 请问变量x的值是什么？
  x的值为1或2。这里会产生冲突，因为线程的切换时间随机，所以当两个线程互斥地访问时会得到结果2，如果冲突，那么得到结果1。
  
变量x的内存地址为2000, ./x86.py -p looping-race-nolock.s -t 2 -M 2000 -i 4 -r -s 1， 请问变量x的值是什么？
  1或2
  
变量x的内存地址为2000, ./x86.py -p looping-race-nolock.s -t 2 -M 2000 -i 4 -r -s 2， 请问变量x的值是什么？
  1或2
  
变量x的内存地址为2000, ./x86.py -p looping-race-nolock.s -a bx=1 -t 2 -M 2000 -i 1， 请问变量x的值是什么？
  1 ，两个线程的第一句汇编指令都讲内存中的值取出，值为0，增加之后再储存都为1。
  
  
（spoc） 了解software-based lock, hardware-based lock, software-hardware-lock代码目录

理解flag.s,peterson.s,test-and-set.s,ticket.s,test-and-test-and-set.s 请通过x86.py分析这些代码是否实现了锁机制？请给出你的实验过程和结论说明。能否设计新的硬件原子操作指令Compare-And-Swap,Fetch-And-Add？

flag.s没有实现好，“./x86.py -p flag.s -t 2 -i 1 -c -M count”的结果，count最后为1，说明没有锁好。
peterson.s没有实现好，“./x86.py -p peterson.s -t 2 -i 1 -c -M count”的结果，count最后为1，说明没有锁好。
test-and-set.s,ticket.s ,test-and-test-and-set.s是锁好的。
