__author__ = 'test'

#^[a-z]{1,15}$

import re

def main():


   input_str = input('Cześć jestem Zed, a Ty jak masz na imię1?')
   if not re.match('^[a-z]*$', input_str.lower()):
      print ('Dozwolne są tylko litery a-z!')

      #sys.exit()
   elif len(input_str) > 15:
      print ('Dozwolnych jest 15 znaków!')
     #sys.exit()

      print ('Naprawde nazwyasz się?:', input_str)

   else:
      print("Super " + input_str + ", miło Cię poznać")

   model = dict(
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
   print(model.get(v.lower(), "tego modelu nie znam"))


import  sqlite3

def main1():
    db = sqlite3.connect('moto.db')
    db.execute('drop table if exists moto')
    db.execute('create table moto (i1 int, model text, marka text, rocznik int, moc int)')
    db.execute('insert into moto (i1, model, marka, rocznik, moc) values (?,?,?,?,?)', (1, 'r6', 'yamaha', 2008, 135))
    db.execute('insert into moto (i1, model, marka, rocznik, moc) values (?,?,?,?,?)', (2, 'zx6r', 'kawasaki', 2009, 124))
    db.execute('insert into moto (i1, model, marka, rocznik, moc) values (?,?,?,?,?)', (3, 'gsxr', 'suzuki', 2006, 116))
    db.execute('insert into moto (i1, model, marka, rocznik, moc) values (?,?,?,?,?)', (4, 'cbr', 'honda', 2010, 140))
    db.commit()
    cursor = db.execute('select * from moto order by i1')
    for row in cursor:
        print(row)


if __name__ == '__main__':
    main()
    main1()




