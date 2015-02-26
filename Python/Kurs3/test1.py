__author__ = 'test'

'''
print("hello word!")

a, b =0,1
if a < b:
    print('a ({}) is less then b ({})'.format(a,b))
else:
    print('a ({}) is not less than b ({})'.format(a,b))

print("foo" if a < b else "bar")

a,b =0,1
while b< 50:
    print(b)
    a,b=b, a+b


fh = open('lines.txt')
for line in fh.readlines():
    print(line)



def isprime(n):
    if n == 1:
        print("1 is special")
        return False
    for x in  range (2,n):
        if n % x == 0:
            print("{} equals {} x {}".format (n, x, n //x))
            return False

    else:
        print(n, " is a prime number")
        return True
for n in range(1,20):
    isprime(n)



def isprime(n):
    if n ==1:
        return False
    for x in range(2,n):
        if n % x ==0:
            return False

    else:
        return True

def primes(n =1):
    while(True):
        if isprime(n): yield n
        n +=1

for n in primes():
    if n > 100: break
    print(n)



class Fibonacci():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while(True):
            yield (self.b)
            self.a, self.b = self.b, self.a + self.b

f = Fibonacci(0,1)
for r in f.series():
    if r > 100: break
    print(r, end=' ')


class AnimalActions:
    def quack(self): return self.strings['quack']
    def feathers(self): return self.strings['feathers']
    def bark(self): return self.strings['bark']
    def fur(self): return self.strings['fur']

class Duck(AnimalActions):
    strings = dict(
        quack = "Quaaaak!",
        feathers =" The duck has gray and white fethers",
        bark = "The duck cannot brak",
        fur = "The duck has no fur"
    )

class Person(AnimalActions):
    strings = dict(
        quack = "The person imitates a duck",
        feathers="The person takes a feather from the ground and shows it",
        bark = "The person puts on a fur coat"
    )

class Dog(AnimalActions):
    strings = dict(
        quack = "The dog cannot quack",
        feathers= "the dog has no feathers",
        bark= "Arf!",
        fur = "The dog has white fur with black spots"
    )

def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())

def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())

def main():
    donald =Duck()
    john = Person()
    fido = Dog()

    print(" - n the forset:")
    for o in ( donald, john, fido):
        in_the_forest(o)

    print(" - In the doghouse: ")
    for o in ( donald, john, fido):
        in_the_doghouse(o)

if __name__ == "__main__": main()


try:
    fh = open ('xlines.txt')
    for line in fh.readlines():
        print(line)
except IOError as e:
    print("something bad happend ({})".format(e))

print("after badness")


#!/usr/bin/python3
def main ():
    print("This is the syntax.py file")
    egg()

def egg():
    print("egg")


if __name__ == '__main__': main ()


def main():
    a, b = 0, 1
    if a < b:
        print("a is less then b")
    elif a> b:
        print("a is geather then b")
    else:
        print("a is equal b")

if __name__ == '__main__': main()




def main():
    a, b = 0, 1
    s = "less than" if a < b else "not less than"
    print(s)

if __name__ == '__main__': main()


def main():
    func(1)
    func(3)
    func(5)

def func(a):
    for i in range(a,10):
        print(i, end=' ')
    print()



if __name__ == '__main__': main()




class Egg:
    def __init__(self, kind = "fride"):
        self.kind =kind
    def whatkind(self):
        return self.kind
def main():
    fride = Egg()
    scramble =Egg('scramble')
    print(fride.whatkind())


if __name__ == '__main__': main()



def main():
    num = round (42 / 9, 2)
    print(type(num), num)

if __name__ == '__main__':
    main()



def main():
    n=42
    s = "This is a {} string!".format(n)
    print(s)

if __name__ == '__main__':
    main()




def main():
    n=42
   s = '''\
#This is a  string!
#dasdasdsdasdsa
#dasdsadasdasdas'''
#    print(s)

#if __name__ == '__main__':
#    main()

'''
def main():
    x = [1,2,3]
    x.append(5)
    x.insert(2,7)
    print(type(x),x)

if __name__ == '__main__':
    main()

def main():
    x = 'string'
    print(type(x), x[2:4])

if __name__ == '__main__':
    main()


def main():
    #d ={ 'one':1, 'two':2, 'three':3, 'four':4, 'five':5 }
    d = dict(
        obe =1, two=2, three=3, four=4, five =5
    )
    d['seven'] =7
    for k in sorted(d.keys()):
     print(k, d[k])

if __name__ == '__main__':
    main()



def main():
    a, b = 2,1
    if False:
        print('this is true')
    elif a<b:
        print(" jest wiekszy")

    else:
        print(" is qual")


if __name__ == '__main__':
    main()

def main():
    v = 'two'
    if v =='one':
        print('v is one')
    elif v == 'two':
        print('v is two')
    elif v== 'three':
        print('v is three')
    else:
        print("dupa zadna z powyzszych")

if __name__ == '__main__':
    main()




def main():
    choices = dict(
        one = 'first',
        two= 'second ',
        three='third',
        four='fourth',
        five='fifth'
    )
    v ='five'
    print(choices.get(v, "other"))


if __name__ == '__main__':
    main()



def main():
    a, b = 0,1
    if a<b:
      v = 'this is true'
    else:
      v = 'this is not true'
    print(v)

if __name__ == '__main__':
    main()

def main():
    a, b = 1,1
    v ='this is true' if a<b else "this is not true"
    print(v)

if __name__ == '__main__':
    main()



def main():
    a, b = 0,1
    while b <50:
        print(b, end=' ')
        a, b = b, a +b

if __name__ == '__main__':
    main()



def main():
   fh=open('lines.txt')
   for line in fh.readlines():
     print(line, end=' ')


if __name__ == '__main__': main()

name = input("Jak masz na imię? ")
print("Miło Cię poznać " + name + "!")
if name =='kasia':
    print('oo kobieta, super:)')
age = input("Ile masz lat? ")
print("Wiec masz " + age + " lata, " + name + "!")


def main():
   fh=open('lines.txt')
   for index, line in enumerate (fh.readlines()):
      print(index, line, end=' ')


if __name__ == '__main__': main()


def main():
    s = 'this is a string'
    for i, c in enumerate(s):
        print(i,c)

if __name__ == '__main__':
    main()




def main():
    s = 'this is a string'
    for i, c in enumerate(s):
        if c == 's': print('index {} is an s'.format(i))

if __name__ == '__main__':
    main()



def main():
    s = 'this is a string'
    for c in s:
        if c == 's': continue
        print(c, end=' ')


if __name__ == '__main__':
    main()


import re

def main():
    fh = open ('raven.txt')
    for line in fh:
        if re.search('(Len|Neverm)ore',line):
            print(line, end=' ')
if __name__ == '__main__':
    main()



import re
def main():
    fh = open ('raven.txt')
    for line in fh:
        match = re.search('(Len|Neverm)ore',line)
        if match:
            print(match.group())

if __name__ == '__main__':
    main()


import re

def main():
    fh = open ('raven.txt')
    for line in fh:
        print(re.sub('(Len|Neverm)ore', '###', line), end=' ')

if __name__ == '__main__':
    main()


import re

def main():
    fh = open ('raven.txt')
    for line in fh:
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(line.replace(match.group(), '###')),


if __name__ == '__main__':
    main()


import re
def main():
    fh = open ('raven.txt')
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
        if re.search(pattern,line):
            print(pattern.sub('###', line), end=' ')

if __name__ == '__main__':
    main()



def main():
    try:
       fh =open ('xlines.txt')
    except:
        print('nie mogę zanleść pliku wróć jutro.')
    else:
        for line in fh: print(line.strip())

if __name__ == '__main__':
    main()



def main():
    try:
       fh =open ('xlines.txt')
    except IOError as e:
        print('nie mogę zanleść pliku', e)
    else:
        for line in fh: print(line.strip())

if __name__ == '__main__':
    main()



def main():
    try:
       fh =open ('xlines.txt')
       for line in fh: print(line.strip())
    except IOError as e:
        print('nie mogę zanleść pliku', e)


if __name__ == '__main__':
    main()

def main():
    try:
       for line in readfile('lines.txt'): print(line.strip())
    except IOError as e:
        print(' cannot read file:', e)
    except ValueError as e:
        print('bad filename' ,e)


def readfile(filename):
    if filename.endswith('.txt'):
      fh = open(filename)
      return fh.readlines()
    else: raise  ValueError('Filename must end with .txt')

if __name__ == '__main__':
     main()



def main():
    testfunc(42)

def testfunc(number, another =None, onemore =75):
    if another is None:
        another=112
    print('This is a test function', number, another ,onemore)

if __name__ == '__main__':
    main()




def main():
    testfunc(1,2,3,42,43,44,45,46)


def testfunc(this, that, other, *args):
    print(this, that, other, args)
    for n in args: print(n, end=' ')

if __name__ == '__main__':
    main()



def main():
    testfunc(5,6,7,8,9,10, one =1, two=2,four=42 )

def testfunc(this, that, other, *args,**kwargs):
    print( ' this is a test function',
           this,that,other,args,
           kwargs['one'], kwargs['two'], kwargs['four'])

if __name__ == '__main__':
    main()




def main():
    for n in testfunc():print(n, end=' ')

def testfunc():
    return range(25)

if __name__ == '__main__':
    main()



def main():
    print("This is the functions.py file")
    for i in range(25):
        print(i, end=' ')

if __name__ == '__main__':
    main()


def main():
    print("This is the functions.py file")
    for i in inclusive_range(0,25,1):
        print(i, end=' ')

def inclusive_range(start, stop, step):
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == '__main__':
    main()


def main():
    print('This is the functions.py file')
    for i in inclusive_range(25):
        print(i, end=' ')

def inclusive_range(*args):
    numargs= len(args)
    if numargs < 1: raise TypeError('requiers at last one argument')
    elif numargs ==1:
        stop =args[0]
        start =0
        step =1
    elif numargs==2:
        (start,stop) =args
        step =1
    elif numargs==3:
        (start, stop, step)
    else: raise TypeError('inclusice_range expacted at most 3 arguments, got {}'.format(numargs))
    i=start
    while i <= stop:
        yield i
        i += step

if __name__ == '__main__':
    main()



class Duck:
    def quack(self):
        print('Quaaaak!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__':
    main()



class Duck:
    def __init__(self, value):
        self._v =value

    def quack(self):
        print('Quaaaak!', self._v)

    def walk(self):
        print('Walks like a duck.',self._v)

def main():
    donald = Duck(57)
    frank=Duck(222)
    donald.quack()
    donald.walk()
    frank.quack()
    frank.walk()

if __name__ == '__main__':
    main()



class Duck:
    def __init__(self, **kwargs):
        self.varialbles = kwargs


    def quack(self):
        print('Quaaaak!')

    def walk(self):
        print('Walks like a duck.')

    def set_varialble (self, k , v):
        self.varialbles[k] =v

    def get_varialble(self,k):
        return self.varialbles.get(k, None)




def main():
    donald = Duck(feet = 2)
    donald.set_varialble('color', 'blue')
    print(donald.get_varialble('feet'))
    print(donald.get_varialble('color'))


if __name__ == '__main__':
    main()




class Animal:
    def talk(self): print(' i have samothing to say')
    def walk(self): print('hay im wolking hear')
    def clothes(self): print('I have nice clothes')


class Duck(Animal):
    def quack(self):
        print('Quaaaak!')

    def walk(self):
        super().walk()
        print('Walks like a duck.')

class Dog(Animal):
    def clothes(self):
        print(' I have brow and white fur')


def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    donald.clothes()

    fido =Dog()
    fido.walk()
    fido.clothes()



if __name__ == '__main__':
    main()


class Duck:
    def quack(self):
        print('Quaaaak!')

    def walk(self):
        print('Walks like a duck.')

    def bark(self):
        print('Duck cannot brak')

    def fur(self):
        print('Duck has feathers')


class Dog:
    def bark(self):
        print('Woof!')

    def fur(self):
        print('The dog has brown and white fur')

    def walk(self):
        print('The dog walks like a dog')

    def quack(self):
        print('Dogs cannot quack')


def main():
    donald = Duck()
    fido=Dog()

    for o in (donald,fido):
        o.quack()
        o.walk()
        o.bark()
        o.fur()


if __name__ == '__main__':
    main()




class Duck:
    def quack(self):
        print('Quaaaak!')

    def walk(self):
        print('Walks like a duck.')

    def bark(self):
        print('Duck cannot brak')

    def fur(self):
        print('Duck has feathers')


class Dog:
    def bark(self):
        print('Woof!')

    def fur(self):
        print('The dog has brown and white fur')

    def walk(self):
        print('The dog walks like a dog')

    def quack(self):
        print('Dogs cannot quack')


def main():
    donald = Duck()
    fido=Dog()
    in_the_forest(donald)
    in_the_pond(fido)

def in_the_forest(dog):
    dog.bark()
    dog.fur()

def in_the_pond(duck):
    duck.quack()
    duck.walk()


if __name__ == '__main__':
    main()



class inclusive_range:
    def __init__(self, *args):
        numargs =len(args)
        if numargs <1: raise TypeError('requiers at Last one argument')
        elif numargs ==1:
            self.stop= args[0]
            self.start=0
            self.step=1
        elif numargs==2:
            (self.start, self.stop) = args
            self.step=1
        elif numargs==3:
            (self.start, self.stop, self.step) =args
        else: raise TypeError('expected at most 3 arguments, got {}'.format(numargs))


    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step


def main():
     o = inclusive_range(25)
     for i in o: print(i, end=' ')

if __name__ == '__main__':
    main()


class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs


    def quack(self):
        print('Quaaaak!')

    def walk(self):
        print('Walks like a duck.')

    def get_properites (self):
        return self.properties

    def get_properyty(self, key):
        return self.properties.get(key, None)

    @property
    def color(self):
        return  self.properties.get('color', None)


    @color.setter
    def color(self, c):
        self.properties['color'] = c

    @color.deleter
    def color(self):
        del self.properties['color']

def main():
    donald = Duck()
    donald.color='blue'
    print(donald.get_properyty('color'))


if __name__ == '__main__':
    main()


##########poza progrogramowo testowanie w pythonie
import unittest

# Here's our "unit".
def IsOdd(n):
    return n % 2 == 1

# Here's our "unit tests".
class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.failUnless(IsOdd(1))

    def testTwo(self):
        self.failIf(IsOdd(2))

def main():
    unittest.main()

if __name__ == '__main__':
    main()


### prosty skrypt selenium
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://seleniumhq.org/')





from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://www.yahoo.com')
assert 'Yahoo!' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()



def main():
    fin  = open('utf8.txt', 'r', encoding='utf_8')
    fout = open('utf8.html', 'w')
    outbytes = bytearray()
    for line in fin:
        for c in line:
            if ord(c) > 127:
                outbytes += bytes ('&#{:04d};'.format(ord(c)), encoding = 'utf_8')
            else: outbytes.append(ord(c))
    outstr =str(outbytes, encoding='utf_8')
    print(outstr, file=fout)
    print(outstr)
    print('Done.')

if __name__ == '__main__':
    main()



def main():
    buffersize = 50000
    infile = open('bigfile.txt', 'r')
    outfile = open('new.txt', 'w')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.', end=' ')
        buffer =infile.read(buffersize)
    print()
    print('Done')


if __name__ == '__main__':
    main()



def main():
    buffersize =50000
    infile = open ('olives.jpg', 'rb')
    outfile = open ('new.jpg', 'wb')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.', end=' ')
        buffer= infile.read(buffersize)
    print()
    print('Done.')


if __name__ == '__main__':
    main()

import  sqlite3

def main():
    db = sqlite3.connect('test.db')
    db.execute('drop table if exists test')
    db.execute('create table test (t1 text, i1 int)')
    db.execute('insert into test (t1, i1) values (?,?)', ('one', 1))
    db.execute('insert into test (t1, i1) values (?,?)', ('two', 2))
    db.execute('insert into test (t1, i1) values (?,?)', ('three', 3))
    db.execute('insert into test (t1, i1) values (?,?)', ('four', 4))
    db.commit()
    cursor = db.execute('select * from test order by t1')
    for row in cursor:
        print(row)

if __name__ == '__main__':
    main()


import sqlite3

def insert(db, row):
    db.execute('insert into test (t1, i1) values (?, ?)', (row['t1'], row['i1']))
    db.commit()

def retrieve(db, t1):
    cursor = db.execute('select * from test where t1 = ?', (t1,))
    return cursor.fetchone()

def update(db, row):
    db.execute('update test set i1 = ? where t1 = ?', (row['i1'], row['t1']))
    db.commit()

def delete(db, t1):
    db.execute('delete from test where t1 = ?', (t1,))
    db.commit()

def disp_rows(db):
    cursor = db.execute('select * from test order by t1')
    for row in cursor:
        print('  {}: {}'.format(row['t1'], row['i1']))

def main():
    db = sqlite3.connect('test.db')
    db.row_factory = sqlite3.Row
    print('Create table test')
    db.execute('drop table if exists test')
    db.execute('create table test ( t1 text, i1 int )')

    print('Create rows')
    insert(db, dict(t1 = 'one', i1 = 1))
    insert(db, dict(t1 = 'two', i1 = 2))
    insert(db, dict(t1 = 'three', i1 = 3))
    insert(db, dict(t1 = 'four', i1 = 4))
    disp_rows(db)

    print('Retrieve rows')
    print(dict(retrieve(db, 'one')), dict(retrieve(db, 'two')))

    print('Update rows')
    update(db, dict(t1 = 'one', i1 = 101))
    update(db, dict(t1 = 'three', i1 = 103))
    disp_rows(db)

    print('Delete rows')
    delete(db, 'one')
    delete(db, 'three')
    disp_rows(db)

if __name__ == "__main__": main()


import sqlite3

class database:
    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename')
        self.table = kwargs.get('table', 'test')

    def sql_do(self, sql, *params):
        self._db.execute(sql, params)
        self._db.commit()

    def insert(self, row):
        self._db.execute('insert into {} (t1, i1) values (?, ?)'.format(self._table), (row['t1'], row['i1']))
        self._db.commit()

    def retrieve(self, key):
        cursor = self._db.execute('select * from {} where t1 = ?'.format(self._table), (key,))
        return dict(cursor.fetchone())

    def update(self, row):
        self._db.execute(
            'update {} set i1 = ? where t1 = ?'.format(self._table),
            (row['i1'], row['t1']))
        self._db.commit()

    def delete(self, key):
        self._db.execute('delete from {} where t1 = ?'.format(self._table), (key,))
        self._db.commit()

    def disp_rows(self):
        cursor = self._db.execute('select * from {} order by t1'.format(self._table))
        for row in cursor:
            print('  {}: {}'.format(row['t1'], row['i1']))

    def __iter__(self):
        cursor = self._db.execute('select * from {} order by t1'.format(self._table))
        for row in cursor:
            yield dict(row)

    @property
    def filename(self): return self._filename

    @filename.setter
    def filename(self, fn):
        self._filename = fn
        self._db = sqlite3.connect(fn)
        self._db.row_factory = sqlite3.Row

    @filename.deleter
    def filename(self): self.close()

    @property
    def table(self): return self._table
    @table.setter
    def table(self, t): self._table = t
    @table.deleter
    def table(self): self._table = 'test'

    def close(self):
            self._db.close()
            del self._filename

def main():
    db = database(filename = 'test.db', table = 'test')

    print('Create table test')
    db.sql_do('drop table if exists test')
    db.sql_do('create table test ( t1 text, i1 int )')

    print('Create rows')
    db.insert(dict(t1 = 'one', i1 = 1))
    db.insert(dict(t1 = 'two', i1 = 2))
    db.insert(dict(t1 = 'three', i1 = 3))
    db.insert(dict(t1 = 'four', i1 = 4))
    for row in db: print(row)

    print('Retrieve rows')
    print(db.retrieve('one'), db.retrieve('two'))

    print('Update rows')
    db.update(dict(t1 = 'one', i1 = 101))
    db.update(dict(t1 = 'three', i1 = 103))
    for row in db: print(row)

    print('Delete rows')
    db.delete('one')
    db.delete('three')
    for row in db: print(row)

if __name__ == "__main__": main()


import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

    import os
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())
    print(os.urandom(25))

    import random
    print(random.randint(1, 1000))
    x = list(range(25))
    print(x)

    import urllib.request
    page = urllib.request.urlopen('http://bw.org')
    for line in page: print (str(line, encoding='utf_8'), end=' ')



if __name__ == '__main__':
    main()



import sys
import time

__version__ = "1.1.0"

class numwords():
    """
        return a number as words,
        e.g., 42 becomes "forty-two"
    """
    _words = {
        'ones': (
            'oh', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
        ), 'tens': (
            '', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
        ), 'teens': (
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
        ), 'quarters': (
            'o\'clock', 'quarter', 'half'
        ), 'range': {
            'hundred': 'hundred'
        }, 'misc': {
            'minus': 'minus'
        }
    }
    _oor = 'OOR'    # Out Of Range

    def __init__(self, n):
        self.__number = n;

    def numwords(self, num = None):
        "Return the number as words"
        n = self.__number if num is None else num
        s = ''
        if n < 0:           # negative numbers
            s += self._words['misc']['minus'] + ' '
            n = abs(n)
        if n < 10:          # single-digit numbers
            s += self._words['ones'][n]
        elif n < 20:        # teens
            s += self._words['teens'][n - 10]
        elif n < 100:       # tens
            m = n % 10
            t = n // 10
            s += self._words['tens'][t]
            if m: s += '-' + numwords(m).numwords()    # recurse for remainder
        elif n < 1000:      # hundreds
            m = n % 100
            t = n // 100
            s += self._words['ones'][t] + ' ' + self._words['range']['hundred']
            if m: s += ' ' + numwords(m).numwords()    # recurse for remainder
        else:
            s += self._oor
        return s

    def number(self):
        "Return the number as a number"
        return str(self.__number);

class saytime(numwords):
    """
        return the time (from two parameters) as words,
        e.g., fourteen til noon, quarter past one, etc.
    """

    _specials = {
        'noon': 'noon',
        'midnight': 'midnight',
        'til': 'til',
        'past': 'past'
    }

    def __init__(self, h, m):
        self._hour = abs(int(h))
        self._min = abs(int(m))

    def words(self):
        h = self._hour
        m = self._min

        if h > 23: return self._oor     # OOR errors
        if m > 59: return self._oor

        sign = self._specials['past']
        if self._min > 30:
            sign = self._specials['til']
            h += 1
            m = 60 - m
        if h > 23: h -= 24
        elif h > 12: h -= 12

        # hword is the hours word)
        if h is 0: hword = self._specials['midnight']
        elif h is 12: hword = self._specials['noon']
        else: hword = self.numwords(h)

        if m is 0:
            if h in (0, 12): return hword   # for noon and midnight
            else: return "{} {}".format(self.numwords(h), self._words['quarters'][m])
        if m % 15 is 0:
            return "{} {} {}".format(self._words['quarters'][m // 15], sign, hword)
        return "{} {} {}".format(self.numwords(m), sign, hword)

    def digits(self):
        "return the traditionl time, e.g., 13:42"
        return "{:02}:{:02}".format(self._hour, self._min)

class saytime_t(saytime):   # wrapper for saytime to use time object
    """
        return the time (from a time object) as words
        e.g., fourteen til noon
    """
    def __init__(self, t):
        self._hour = t.tm_hour
        self._min = t.tm_min

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            test()
        else:
            try: print(saytime(*(sys.argv[1].split(':'))).words())
            except TypeError: print("Invalid time ({})".format(sys.argv[1]))
    else:
        print(saytime_t(time.localtime()).words())

def test():
    print("\nnumbers test:")
    list = (
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 19, 20, 30,
        50, 51, 52, 55, 59, 99, 100, 101, 112, 900, 999, 1000
    )
    for l in list:
        print(l, numwords(l).numwords())

    print("\ntime test:")
    list = (
        (0, 0), (0, 1), (11, 0), (12, 0), (13, 0), (12, 29), (12, 30),
        (12, 31), (12, 15), (12, 30), (12, 45), (11, 59), (23, 15),
        (23, 59), (12, 59), (13, 59), (1, 60), (24, 0)
    )
    for l in list:
        print(saytime(*l).digits(), saytime(*l).words())

    print("\nlocal time is " + saytime_t(time.localtime()).words())

if __name__ == "__main__": main()


class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        if numargs < 1: raise TypeError('Requires at least one argument')
        elif numargs == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            step = 1
        elif numargs == 3:
            (self.start,self.stop,self.step) = args
        else: raise TypeError('inclusiveRange expected at most 3 arguments, got {}'.format(numargs))

    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step

def main():
    o = inclusive_range(4, 25, 3)
    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()


class AnimalActions:
    def bark(self): return self._doAction('bark')
    def fur(self): return self._doAction('fur')
    def quack(self): return self._doAction('quack')
    def feathers(self): return self._doAction('feathers')

    def _doAction(self, action):
        if action in self.strings:
            return self.strings[action]
        else:
            return 'The {} has no {}'.format(self.animalName(), action)

    def animalName(self):
        return self.__class__.__name__.lower()

# -- MODEL --

class Duck(AnimalActions):
    strings = dict(
        quack = "Quaaaaak!",
        feathers = "The duck has gray and white feathers."
    )

class Person(AnimalActions):
    strings = dict(
        bark = "The person says woof!",
        fur = "The person puts on a fur coat.",
        quack = "The person imitates a duck.",
        feathers = "The person takes a feather from the ground and shows it."
    )

class Dog(AnimalActions):
    strings = dict(
        bark = "Arf!",
        fur = "The dog has white fur with black spots.",
    )

# -- VIEW --

def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())

def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())

def main():
    donald = Duck()
    john = Person()
    fido = Dog()

    print("-- In the forest:")
    for o in ( donald, john, fido ):
        in_the_forest(o)

    print("-- In the doghouse:")
    for o in ( donald, john, fido ):
        in_the_doghouse(o)

if __name__ == "__main__": main()



#!/usr/bin/python3
# saytime.py by Bill Weinman [http://bw.org/]
# created for Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC
import sys
import time

__version__ = "1.1.0"

class numwords():
    """
        return a number as words,
        e.g., 42 becomes "forty-two"
    """
    _words = {
        'ones': (
            'oh', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
        ), 'tens': (
            '', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
        ), 'teens': (
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
        ), 'quarters': (
            'o\'clock', 'quarter', 'half'
        ), 'range': {
            'hundred': 'hundred'
        }, 'misc': {
            'minus': 'minus'
        }
    }
    _oor = 'OOR'    # Out Of Range

    def __init__(self, n):
        self.__number = n;

    def numwords(self, num = None):
        "Return the number as words"
        n = self.__number if num is None else num
        s = ''
        if n < 0:           # negative numbers
            s += self._words['misc']['minus'] + ' '
            n = abs(n)
        if n < 10:          # single-digit numbers
            s += self._words['ones'][n]
        elif n < 20:        # teens
            s += self._words['teens'][n - 10]
        elif n < 100:       # tens
            m = n % 10
            t = n // 10
            s += self._words['tens'][t]
            if m: s += '-' + numwords(m).numwords()    # recurse for remainder
        elif n < 1000:      # hundreds
            m = n % 100
            t = n // 100
            s += self._words['ones'][t] + ' ' + self._words['range']['hundred']
            if m: s += ' ' + numwords(m).numwords()    # recurse for remainder
        else:
            s += self._oor
        return s

    def number(self):
        "Return the number as a number"
        return str(self.__number);

class saytime(numwords):
    """
        return the time (from two parameters) as words,
        e.g., fourteen til noon, quarter past one, etc.
    """

    _specials = {
        'noon': 'noon',
        'midnight': 'midnight',
        'til': 'til',
        'past': 'past'
    }

    def __init__(self, h, m):
        self._hour = abs(int(h))
        self._min = abs(int(m))

    def words(self):
        h = self._hour
        m = self._min

        if h > 23: return self._oor     # OOR errors
        if m > 59: return self._oor

        sign = self._specials['past']
        if self._min > 30:
            sign = self._specials['til']
            h += 1
            m = 60 - m
        if h > 23: h -= 24
        elif h > 12: h -= 12

        # hword is the hours word)
        if h is 0: hword = self._specials['midnight']
        elif h is 12: hword = self._specials['noon']
        else: hword = self.numwords(h)

        if m is 0:
            if h in (0, 12): return hword   # for noon and midnight
            else: return "{} {}".format(self.numwords(h), self._words['quarters'][m])
        if m % 15 is 0:
            return "{} {} {}".format(self._words['quarters'][m // 15], sign, hword)
        return "{} {} {}".format(self.numwords(m), sign, hword)

    def digits(self):
        "return the traditionl time, e.g., 13:42"
        return "{:02}:{:02}".format(self._hour, self._min)

class saytime_t(saytime):   # wrapper for saytime to use time object
    """
        return the time (from a time object) as words
        e.g., fourteen til noon
    """
    def __init__(self, t):
        self._hour = t.tm_hour
        self._min = t.tm_min

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            test()
        else:
            try: print(saytime(*(sys.argv[1].split(':'))).words())
            except TypeError: print("Invalid time ({})".format(sys.argv[1]))
    else:
        print(saytime_t(time.localtime()).words())

def test():
    print("\nnumbers test:")
    list = (
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 19, 20, 30,
        50, 51, 52, 55, 59, 99, 100, 101, 112, 900, 999, 1000
    )
    for l in list:
        print(l, numwords(l).numwords())

    print("\ntime test:")
    list = (
        (0, 0), (0, 1), (11, 0), (12, 0), (13, 0), (12, 29), (12, 30),
        (12, 31), (12, 15), (12, 30), (12, 45), (11, 59), (23, 15),
        (23, 59), (12, 59), (13, 59), (1, 60), (24, 0)
    )
    for l in list:
        print(saytime(*l).digits(), saytime(*l).words())

    print("\nlocal time is " + saytime_t(time.localtime()).words())

if __name__ == "__main__": main()


#!/usr/bin/python3
# test-saytime.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import saytime
import unittest

class TestSaytime(unittest.TestCase):
    def setUp(self):
        self.nums = list(range(11))

    def test_numbers(self):
        # make sure the numbers translate correctly
        words = (
            'oh', 'one', 'two', 'three', 'four', 'five',
            'six', 'seven', 'eight', 'nine', 'ten'
        )
        for i, n in enumerate(self.nums):
            self.assertEqual(saytime.numwords(n).numwords(), words[i])

    def test_time(self):
        time_tuples = (
            (0, 0), (0, 1), (11, 0), (12, 0), (13, 0), (12, 29), (12, 30),
            (12, 31), (12, 15), (12, 30), (12, 45), (11, 59), (23, 15),
            (23, 59), (12, 59), (13, 59), (1, 60), (24, 0)
        )
        time_words = (
            "midnight",
            "one past midnight",
            "eleven o'clock",
            "noon",
            "one o'clock",
            "twenty-nine past noon",
            "half past noon",
            "twenty-nine til one",
            "quarter past noon",
            "half past noon",
            "quarter til one",
            "one til noon",
            "quarter past eleven",
            "one til midnight",
            "one til one",
            "one til two",
            "OOR",
            "OOR"
        )
        for i, t in enumerate(time_tuples):
            self.assertEqual(saytime.saytime(*t).words(), time_words[i])

if __name__ == "__main__": unittest.main()

'''

