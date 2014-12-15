__author__ = 'test'

#^[a-z]{1,15}$

import re

def main():


   input_str = input('Cześć jestem Zed, a Ty jak masz na imię?')
   if not re.match('^[a-z]*$', input_str.lower()):
      print ('Dozwolne są tylko litery a-z!')

      #sys.exit()
   elif len(input_str) > 15:
      print ('Dozwolnych jest 15 znaków!')
     #sys.exit()

      print ('Naprawde nazwyasz się?:', input_str)

   else:
      print("Super " + input_str + ", miło Cię poznać")

   choices = dict(
        r6 = 'Yamaha, Super moja ulubiona marka',
        yamaha = 'Yamaha, Super moja ulubiona marka',
        gsxr= 'Suzuki, Miałem kiedys GS500F 2005r',
        suzuki = 'Suzuki, Miałem kiedys GS500F 2005r',
        cbr='Honda, podobno najlatwiejszy motocykl do jazdy',
        honda='Honda, podobno najlatwiejszy motocykl do jazdy',
        hp4='BMW 1000RR HP4, motocykl marzenie',

        dukat='Ducatti paniagale, pozazdroscic',
        Ducatti='Ducatti paniagale, pozazdroscic',
   )
   v = input('Jakim motocyklem jezdzisz?')
   print(choices.get(v.lower(), "tego nie znam"))

if __name__ == '__main__':
    main()



'''
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


'''
