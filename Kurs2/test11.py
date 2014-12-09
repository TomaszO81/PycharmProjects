__author__ = 'test'


'''
def  main ():
    x, y =1000, 1000

    if (x < y):
        st= "x is less then y"

    elif ( x == y):
        st="sa takie same"
    else:
        st= "x is greater then y"

    print(st)

if __name__ == '__main__':
 main()

def main():
  x=0
  while (x <5):
      print(x)
      x= x+1

if __name__ == "__main__":
    main()

for x in range(5,10):
    print(x)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for d in days:
    print(d)

for x in range(5,10):
 # if (x == 7): break
  if (x % 2 ==0): continue

  print(x)


days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for i, d in enumerate(days):
    print(i, d)


class myClass():
  def method1(self):
    print("myClass method1")

  def method2(self, someString):
    print("myClass method2: " +someString)

class anatherClass(myClass):
  def method2(self):
      print("anotherClass method2")

  def method1(self):
    myClass.method1(self);
    print ("anotherClass method1")


def main():
  c=myClass()
  c.method1()
  c.method2("Th1s is a string")
  c2=anatherClass()
  c2.method1()
  c2.method2()

if __name__ == "__main__":
    main()



from datetime import date
from datetime import time
from datetime import datetime

def main():

  #today =date.today()
  #print("Today's date is ", today)

  #print("Date Componets: ", today.day, today.month, today.year)
  #today =datetime.now()
  #print("The corruent date and time is ", today)

  #t =datetime.time(datetime.now())
  #print("The current time is ", t)

  today =datetime.now()
  wd =date.weekday(today)
  days =["monday", "tusday", "wednsday", "czwartek", "piatek", "sobota", "niedziela"]
  print ("Today is day number %d" % wd)
  print("With is a " + days[wd])


if __name__ == '__main__':
  main();


from datetime import datetime

def main():
    now = datetime.now()
   #print(now.strftime("%Y"))
   #print(now.strftime("%a, %d, %B, %y"))

   #print(now.strftime("%c"))
   #print(now.strftime("%x"))
   #print(now.strftime("%X"))

    print(now.strftime("%I:%H:%S %p"))
    print(now.strftime("%H:%M"))

if __name__ == '__main__':

main();



from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


print(timedelta(days=365, hours=5, minutes=1))
print("today is: " + str(datetime.now()))
print("One year from now will be a: " + str(datetime.now() + timedelta(365)))

t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A, %B, %d, %Y")
print("one week ago it was " +s)

#if __name__ == '__main__':
#  main();



import calendar

c =calendar.TextCalendar(calendar.SUNDAY)
#str =c.formatmonth(2014, 1, 0, 0)
#print(str)

#hc= calendar.HTMLCalendar(calendar.SUNDAY)
#str = hc.formatmonth(2014, 1)
#print(str)

#for i in c.itermonthdates(2014, 8):
#   print (i)

#for name in calendar.month_name:
#    print (name)

#for day in calendar.day_name:
#    print (day)

for m in range(1,13):
    cal = calendar.monthcalendar(2014 ,m)
    weekone = cal[0]
    weektow = cal[1]

    if weekone[calendar.FRIDAY] !=0:
        meetday =weekone[calendar.FRIDAY]
    else:meetday=weektow[calendar.FRIDAY]
    print("%10s %2d" % (calendar.month_name[m], meetday))



def main():
   # f = open ("textfile7.txt", "w+")
   # f =open ("textfile7.txt", "a+")
    #for i in range(10):
    #    f.write("This is line dupa %d\r\n" % (i+1))
    #f.close()

 f =open ("textfile7.txt", "r")
 if f.mode == 'r':
   #contents =f.read()
   #print(contents)
   fl =f.readlines()
   for x in fl:
    print(x)

if __name__ == '__main__':
  main()



import os
from os import  path
import datetime
from datetime import date, time, timedelta
import time

def main():
  #print (os.name);
  #print("Item exists: " + str(path.exists("textfile7.txt")))
  #print("Item is a file: " + str(path.isfile("textfile7.txt")))
  #print("Item is a directory: " + str(path.isdir("textfile7.txt")))

  #print("Item's path: " + str(path.realpath("textfile7.txt")))
  #print("Item paty name is : " + str(path.split(path.realpath(("textfile7.txt")))))
  #t = time.ctime(path.getatime("textfile7.txt"))
  #print (t)
  #print (datetime.datetime.fromtimestamp(path.getatime("textfile7.txt")))

  td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getatime("textfile7.txt"))
  print("It has been " + str(td) + "the file was modified")
  print("Or, " + str(td.total_seconds()) + " seconds")

if __name__ == '__main__':
  main()


import os
import shutil
from os import path
from shutil import  make_archive
from zipfile import ZipFile


def main():

   if path.exists("newfile.txt"):
    src = path.realpath("newfile.txt");
#   head, tail = path.split(src)
#   print("path: " + head)
#   print("file: " + tail)

#   dst = src + ".bak"
#   shutil.copy(src,dst)
#   shutil.copystat(src,dst)
#    os.rename("textfile7.txt", "newfile.txt")
#    root_dir, tail =path.split(src)
#    shutil.make_archive("archive", "zip", root_dir)

    with ZipFile("testzip", "w") as newzip:
     newzip.write("newfile.txt")
     newzip.write("textfile7.txt.bak")

if __name__ == '__main__':
  main()


import urllib.request as urllib2

def main():
  webUrl = urllib2.urlopen("http://joemarini.com")
  print("resul code: " + str(webUrl.getcode()))
  data =webUrl.read()
  print(data)




if __name__ == '__main__':
  main()

import urllib.request as urllib2
import json

def printResults(data):
    theJSON = json.loads(data)
    if "title" in theJSON["metadata"]:
      print (theJSON["metadata"] ["title"])
    count = theJSON["metadata"]["count"];
    print(str(count) + " events recorded")
    for i in theJSON["features"]:
      print( i ["properites"]["place"])



def main():
  urlData ="http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson"
  webUrl= urllib2.urlopen(urlData)
  print (webUrl.getcode())
  if (webUrl.getcode() == 200):
    data = webUrl.read()
    print(data)
  else:
    printResults(" Otrzymalem blad z serwera, connato retrive results ")


if __name__ == '__main__':
  main()



from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):


  def handle_starttag(self, tag, attrs):

      pos = self.getpos()
      print(" At line: ", pos [0], " position", pos[1])
      if attrs.__len__>0:
          print("\tAttributes:")
          for a in attrs:
              print("\t", a[0], "=",a[1])

  def handle_endtag(self, tag):
      print("Encountred an end tag: ", tag)
      pos = self.getpos()
      print ("At line: ", pos [0], " position ",pos[1])


  def handle_data(self, data):
      print ("Encountred some data: ", data)
      pos = self.getpos()
      print ("At line: ",pos[0], " postion ", pos[1])






  def handle_comment(self, data):
     print("Encountered comment: ", data)
     pos = self.getpos()
     print("At line: ", pos[0], "position ", pos[1])

def main():
    parser = MyHTMLParser()
    f =open ("samplehtml.html")
    if f.mode == "r":
        contents = f.read()
        parser.feed(contents)



if __name__ == '__main__':
  main()
  '''
