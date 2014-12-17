__author__ = 'test'

#^[a-z]{1,15}$




import re

def main():


   input_str = input('Cześć jestem Zed, a Ty jak masz na imię?')
   if not re.match('^[a-z]*$', input_str.lower()):
      print ('Dozwolne są tylko litery a-z!')

   elif len(input_str) > 15:
      print ('Dozwolnych jest 15 znaków!')

      print ('Naprawde nazwyasz się?:', input_str)

   else:
      print("Super " + input_str + ", miło Cię poznać")

   '''
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
   '''



   marki = ['yamaha', 'suzuki','honda']



   model2 = {}
   model2['yamaha'] = {}
   model2['yamaha']['models'] = {

   }


   model2['r6'] = {}
   model2['r6']['info'] = 'Yamaha YZF-R6'
   model2['r6']['data'] = {
       'rokProdukcji'          : '1999/2000',
       'oznaczenie'            : 'RJ03',
       'typ'                   : 'Rzędowy, 4-suwowy, 4-cylindrowy, chłodzony cieczą, 16-zaworowy DOHC',
       'pojemnoscSkokowa'      : '599,8 cm3',
       'rokprodukcji'          : '2008',
       'srednicaCylindra'      : '65,5 x 44,5 mm',
       'stopienSprezania'      : '12,4 : 1',
       'Moc'                   : '88,2 kW (120 KM) przy 13 000 obr/min',
       'momentObrotowy'        : '68,1 Nm przy 11 500 obr/min',
       'ukladOlejenia'         : 'Z mokrą misą olejową',
       'ukladZasilania'        : '37 mm Keihin CVRD37 z systemem Throttle Position Sensor',
       'ukladZaplonowy'        : 'CDI',
       'sprzeglo'              : 'Wielotarczowe mokre',
       'przelożenieWstepne'    : '86/44 (1,955)',
       'skrzyniaBiegow'        : '6-biegowa o stałym zazębieniu',
       'przelozenie1biegu'     : '37/13 (2,846)',
       'przelozenie2biegu'     : '37/19 (1,947)',
       'przelozenie3biegu'     : '28/18 (1,556)',
       'przelozenie4biegu'     : '32/24 (1,333)',
       'przelozenie5biegu'     : '25/21 (1,190)',
       'przelozenie6biegu'     : '26/24 (1,083)',
       'napedtylnegokola'      : '#532 łańcuch O-ring',
       'przelozenieNapedu'     : '48/16 (3,000)',
       'rama'                  : 'Aluminiowa, Deltabox II',
       'przednieZawieszenie'   : 'Widelec teleskopowy, Ø 43 mm, regulacja napięcia wstępnego, regulacja tłumienia dobicia, regulacja tłumienia odbicia',
       'skokPrzedniego'        : '130 mm',
       'rozmiarPrzedniejopony' : '120/60 ZR 17',
       'tylneZawieszenie'      : 'Wahacz połączony układem dźwigniowym z elementem resorująco-amortyzującym, regulacja napięcia wstępnego, regulacja tłumienia dobicia, regulacja tłumienia odbicia',
       'skokTylnego'           : '120 mm',
       'rozmiarTylnejopony'    : '180/55 ZR 17',
       'katGlowkiramy'         : '24°',
       'wyprzedzenie'          : '81 mm',
       'przedniHamulec'        : 'Dwutarczowy, Ø 298 mm',
       'tylnyHamulec'          : 'Pojedyncza tarcza, Ø 220 mm',
       'dlugosc'               : '2025 mm',
       'szerokosc'             : '690 mm',
       'height'                : '1105 mm',
       'wysokoscSiedzenia'     : '820 mm',
       'rozstawOsi'            : '1380 mm',
       'przeswitMinimalny'     : '135 mm',
       'pojemnoscZbiornika'    : '17,0 l (3,5 l)',
       'pojemnoscUkladu'       : '3,5 l',
       'dryWeight'             : '169 kg',
       'wetWeight'             : '188 kg',

   }

   v1 = input('Jakim motocyklem jezdzisz?')

   try:
      info = model2.get(v1.lower())

      print(info['info'])

      print('Rok Produkcji: '+ info['data']['rokProdukcji'])
      print('Oznaczenie: '+ info['data']['oznaczenie'])
      print('Typ: '+ info['data']['typ'])
      print('Pojemność skokowa: '+ info['data']['pojemnoscSkokowa'])
      print('Średnica cylindra x Skok tłoka: '+ info['data']['srednicaCylindra'])
      print('Stopień sprężania: '+ info['data']['stopienSprezania'])
      print('Moc: '+ info['data']['Moc'])
      print('Moment obrotowy: '+ info['data']['momentObrotowy'])
      print('Układ olejenia: '+ info['data']['ukladOlejenia'])
      print('Układ zasilania: '+ info['data']['ukladZasilania'])
      print('Układ zapłonowy: '+ info['data']['ukladZaplonowy'])
      print('Sprzęgło: '+ info['data']['sprzeglo'])
      print('Przełożenie wstępne (silnik - skrzynia biegów): '+ info['data']['przelożenieWstepne'])
      print('Skrzynia biegów: '+ info['data']['skrzyniaBiegow'])
      print('Przełożenie 1. biegu: '+ info['data']['przelozenie1biegu'])
      print('Przełożenie 2. biegu: '+ info['data']['przelozenie2biegu'])
      print('Przełożenie 3. biegu: '+ info['data']['przelozenie3biegu'])
      print('Przełożenie 4. biegu: '+ info['data']['przelozenie4biegu'])
      print('Przełożenie 5. biegu: '+ info['data']['przelozenie5biegu'])
      print('Przełożenie 6. biegu: '+ info['data']['przelozenie6biegu'])
      print('Napęd tylnego koła: '+ info['data']['napedtylnegokola'])
      print('Przełożenie napędu tylnego koła: '+ info['data']['przelozenieNapedu'])
      print('Rama: '+ info['data']['rama'])
      print('Przednie zawieszenie: '+ info['data']['przednieZawieszenie'])
      print('Skok przedniego zawieszenia: '+ info['data']['skokPrzedniego'])
      print('Rozmiar przedniej opony: '+ info['data']['rozmiarPrzedniejopony'])
      print('Tylne zawieszenie: '+ info['data']['tylneZawieszenie'])
      print('Skok tylnego zawieszenia: '+ info['data']['skokTylnego'])
      print('Rozmiar tylnej opony: '+ info['data']['rozmiarTylnejopony'])
      print('Kąt główki ramy: '+ info['data']['katGlowkiramy'])
      print('Wyprzedzenie: '+ info['data']['wyprzedzenie'])
      print('Przedni hamulec: '+ info['data']['przedniHamulec'])
      print('Tylny hamulec: '+ info['data']['tylnyHamulec'])
      print('Długość: '+ info['data']['dlugosc'])
      print('Szerokość: '+ info['data']['szerokosc'])
      print('Wysokość: '+ info['data']['height'])
      print('Wysokość siedzenia: '+ info['data']['wysokoscSiedzenia'])
      print('Rozstaw osi: '+ info['data']['rozstawOsi'])
      print('Prześwit minimalny: '+ info['data']['przeswitMinimalny'])
      print('Pojemność zbiornika paliwa (rezerwa): '+ info['data']['pojemnoscZbiornika'])
      print('Pojemność układu olejenia: '+ info['data']['pojemnoscUkladu'])
      print('Waga na sucho: '+ info['data']['dryWeight'])
      print('Waga na mokro: '+ info['data']['wetWeight'])

   except:
      print("tego modelu nie znam")


# import  sqlite3

'''wykomentowane dziala ale nie urzyte
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
        #print('  {}: {}'.format(row['model'], row['marka']))
'''

if __name__ == '__main__':
      main()









