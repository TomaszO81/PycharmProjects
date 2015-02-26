# -*- coding: utf-8 -*-
__author__ = 'test'


#^[a-z]{1,15}$



'''
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
'''


import re

def main():


   input_str = input('Cześć jestem Zed, a Ty jak masz na imię?')
   if not re.match('^[a-z]*$', input_str.lower()):
      print ('Dozwolne są tylko litery a-z!')

   elif len(input_str) > 15:
      print ('Dozwolnych jest 15 znaków!')

      print ('Naprawde nazwyasz się?:', input_str)

   else:
      print("Super " + input_str.capitalize() + ", miło Cię poznać")





   marki = {}
   marki['yamaha', 'honda', 'suzuki'] ={}

   marki = input('Jaka marką motocykla jeździsz?')
   if marki == 'yamaha':
       print(yamaha())
   else:
       print('Możesz wybrać spośród: yamaha, honda, suzuki')





def yamaha():
   model2 = {}
   model2['yamaha'] = {}
   model2['yamaha']['models']= {

   }




   v1 = input('Jaki rocznik?')

   if v1=='1999':
       pass
   else:
       print('Podaj rocznik od 1999-2015')





   model2['1999'] = {}
   model2['2000'] = {}
   model2['1999']['info'] = 'Yamaha YZF-R6'
   model2['2000']['info'] = 'Yamaha YZF-R6'
   model2['1999']['data'] = model2['2000']['data']= {
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

   model2['2001'] = {}
   model2['2002'] = {}
   model2['2001']['info'] = 'Yamaha YZF-R6'
   model2['2002']['info'] = 'Yamaha YZF-R6'
   model2['2001']['data'] = model2['2002']['data']= {
       'rokProdukcji'          : '2001/2002',
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
       'ukladZaplonowy'        : 'DC-CDI',
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
       'dryWeight'             : '167,5 kg',
       'wetWeight'             : '186 kg',

   }


   model2['2003'] = {}
   model2['2004'] = {}
   model2['2003']['info'] = 'Yamaha YZF-R6'
   model2['2004']['info'] = 'Yamaha YZF-R6'
   model2['2003']['data'] = model2['2004']['data']= {
       'rokProdukcji'          : '2003/2004',
       'oznaczenie'            : 'RJ05/RJ09',
       'typ'                   : 'Rzędowy, 4-suwowy, 4-cylindrowy, chłodzony cieczą, 16-zaworowy DOHC',
       'pojemnoscSkokowa'      : '599,8 cm3',
       'rokprodukcji'          : '2008',
       'srednicaCylindra'      : '65,5 x 44,5 mm',
       'stopienSprezania'      : '12,4 : 1',
       'Moc'                   : '90,5 kW (123 KM) przy 13 000 obr/min z doładowaniem dynamicznym 86,0 kW (117 KM) przy 13 000 obr/min bez doładowania dynamicznego',
       'momentObrotowy'        : '68,5 Nm przy 12 000 obr/min z doładowaniem dynamicznym 66,4 Nm przy 12 000 obr/min bez doładowania dynamicznego',
       'ukladOlejenia'         : 'Z mokrą misą olejową',
       'ukladZasilania'        : 'Wtrysk paliwa',
       'ukladZaplonowy'        : 'DC-CDI',
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
       'rama'                  : 'Aluminiowa, Deltabox III',
       'przednieZawieszenie'   : 'Widelec teleskopowy, Ø 43 mm, regulacja napięcia wstępnego, regulacja tłumienia dobicia, regulacja tłumienia odbicia',
       'skokPrzedniego'        : '130 mm',
       'rozmiarPrzedniejopony' : '120/60 ZR 17',
       'tylneZawieszenie'      : 'Wahacz połączony układem dźwigniowym z elementem resorująco-amortyzującym, regulacja napięcia wstępnego, regulacja tłumienia dobicia, regulacja tłumienia odbicia',
       'skokTylnego'           : '120 mm',
       'rozmiarTylnejopony'    : '180/55 ZR 17',
       'katGlowkiramy'         : '24°',
       'wyprzedzenie'          : '86 mm',
       'przedniHamulec'        : 'Dwutarczowy, Ø 298 mm',
       'tylnyHamulec'          : 'Pojedyncza tarcza, Ø 220 mm',
       'dlugosc'               : '2025 mm',
       'szerokosc'             : '690 mm',
       'height'                : '1090 mm',
       'wysokoscSiedzenia'     : '820 mm',
       'rozstawOsi'            : '1380 mm',
       'przeswitMinimalny'     : '135 mm',
       'pojemnoscZbiornika'    : '17,0 l (3,5 l)',
       'pojemnoscUkladu'       : '3,5 l',
       'dryWeight'             : '162 kg',
       'wetWeight'             : '182 kg',

   }


   model2['2005'] = {}
   model2['2006'] = {}
   model2['2005']['info'] = 'Yamaha YZF-R6'
   model2['2006']['info'] = 'Yamaha YZF-R6'
   model2['2005']['data'] = model2['2006']['data']= {
       'rokProdukcji'          : '2005/2006',
       'oznaczenie'            : 'RJ095',
       'typ'                   : 'Rzędowy, 4-suwowy, 4-cylindrowy, chłodzony cieczą, 16-zaworowy DOHC',
       'pojemnoscSkokowa'      : '599,8 cm3',
       'rokprodukcji'          : '2008',
       'srednicaCylindra'      : '65,5 x 44,5 mm',
       'stopienSprezania'      : '12,4 : 1',
       'Moc'                   : '92,7 kW (126 KM) przy 13 000 obr/min z doładowaniem dynamicznym 88,2 kW (120 KM) przy 13 000 obr/min bez doładowania dynamicznego',
       'momentObrotowy'        : '68,5 Nm przy 12 000 obr/min z doładowaniem dynamicznym 66,4 Nm przy 12 000 obr/min bez doładowania dynamicznego',
       'ukladOlejenia'         : 'Z mokrą misą olejową',
       'ukladZasilania'        : 'Wtrysk paliwa',
       'ukladZaplonowy'        : 'DC-CDI',
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
       'rama'                  : 'Aluminiowa, Deltabox III',
       'przednieZawieszenie'   : 'Odwrócony widelec teleskopowy, Ø 41 mm, regulacja napięcia wstępnego, regulacja tłumienia dobicia, regulacja tłumienia odbicia',
       'skokPrzedniego'        : '120 mm',
       'rozmiarPrzedniejopony' : '120/70 ZR 17',
       'tylneZawieszenie'      : 'Wahacz połączony układem dźwigniowym z elementem resorująco-amortyzującym, regulacja napięcia wstępnego, regulacja tłumienia dobicia, regulacja tłumienia odbicia',
       'skokTylnego'           : '120 mm',
       'rozmiarTylnejopony'    : '180/55 ZR 17',
       'katGlowkiramy'         : '24,5°',
       'wyprzedzenie'          : '95 mm',
       'przedniHamulec'        : 'Dwutarczowy, Ø 310 mm, zaciski radialne',
       'tylnyHamulec'          : 'Pojedyncza tarcza, Ø 220 mm',
       'dlugosc'               : '2045 mm',
       'szerokosc'             : '690 mm',
       'height'                : '1105 mm',
       'wysokoscSiedzenia'     : '830 mm',
       'rozstawOsi'            : '1385 mm',
       'przeswitMinimalny'     : '145 mm',
       'pojemnoscZbiornika'    : '17,0 l (3,5 l)',
       'pojemnoscUkladu'       : '3,5 l',
       'dryWeight'             : '163 kg',
       'wetWeight'             : '183 kg',

   }


   model2['2006'] = {}
   model2['2007'] = {}
   model2['2006']['info'] = 'Yamaha YZF-R6'
   model2['2007']['info'] = 'Yamaha YZF-R6'
   model2['2006']['data'] = model2['2007']['data']= {
       'rokProdukcji'          : '2006/2007',
       'oznaczenie'            : 'RJ11',
       'typ'                   : 'Rzędowy, 4-suwowy, 4-cylindrowy, chłodzony cieczą, 16-zaworowy DOHC',
       'pojemnoscSkokowa'      : '599,4 cm3',
       'rokprodukcji'          : '2008',
       'srednicaCylindra'      : '67,0 x 42,5 mm',
       'stopienSprezania'      : '12,8 : 1',
       'Moc'                   : '97,8 kW (133 KM) przy 14 500 obr/min z doładowaniem dynamicznym 93,4 kW (127 KM) przy 14 500 obr/min bez doładowania dynamicznego',
       'momentObrotowy'        : '68,0 Nm przy 12 000 obr/min z doładowaniem dynamicznym 66,0 Nm przy 12 000 obr/min bez doładowania dynamicznego',
       'ukladOlejenia'         : 'Z mokrą misą olejową',
       'ukladZasilania'        : 'Wtrysk paliwa z YCC-T',
       'ukladZaplonowy'        : 'TCI',
       'sprzeglo'              : 'Wielotarczowe mokre z zabezpieczeniem przed zablokowaniem tylnego koła',
       'przelożenieWstepne'    : '85/41 (2,073)',
       'skrzyniaBiegow'        : '6-biegowa o stałym zazębieniu',
       'przelozenie1biegu'     : '31/12 (2,583)',
       'przelozenie2biegu'     : '32/16 (2,000)',
       'przelozenie3biegu'     : '30/18 (1,667)',
       'przelozenie4biegu'     : '26/18 (1,444)',
       'przelozenie5biegu'     : '27/21 (1,286)',
       'przelozenie6biegu'     : '23/20 (1,150)',
       'napedtylnegokola'      : '#525 łańcuch O-ring',
       'przelozenieNapedu'     : '45/16 (2,813',
       'rama'                  : 'Aluminiowa, Deltabox',
       'przednieZawieszenie'   : 'Odwrócony widelec teleskopowy, Ø 41 mm, regulacja napięcia wstępnego, regulacja tłumienia dobicia niezależnie dla wolnych i szybkich ugięć, regulacja tłumienia odbicia',
       'skokPrzedniego'        : '120 mm',
       'rozmiarPrzedniejopony' : '120/70 ZR 17',
       'tylneZawieszenie'      : 'Wahacz połączony układem dźwigniowym z elementem resorująco-amortyzującym, regulacja napięcia wstępnego, regulacja tłumienia dobicia niezależnie dla wolnych i szybkich ugięć, regulacja tłumienia odbicia',
       'skokTylnego'           : '120 mm',
       'rozmiarTylnejopony'    : '180/55 ZR 17',
       'katGlowkiramy'         : '24°',
       'wyprzedzenie'          : '97 mm',
       'przedniHamulec'        : 'Dwutarczowy, Ø 310 mm, zaciski radialne',
       'tylnyHamulec'          : 'Pojedyncza tarcza, Ø 220 mm',
       'dlugosc'               : '2040 mm',
       'szerokosc'             : '700 mm',
       'height'                : '1100 mm',
       'wysokoscSiedzenia'     : '850 mm',
       'rozstawOsi'            : '1380 mm',
       'przeswitMinimalny'     : '130 mm',
       'pojemnoscZbiornika'    : '17,3 l (3,5 l)',
       'pojemnoscUkladu'       : '3,4 l',
       'dryWeight'             : '161 kg',
       'wetWeight'             : '182 kg',

   }


   model2['2008'] = {}
   model2['2009'] = {}
   model2['2008']['info'] = 'Yamaha YZF-R6'
   model2['2009']['info'] = 'Yamaha YZF-R6'
   model2['2008']['data'] = model2['2009']['data']= {
       'rokProdukcji'          : '2008/2009',
       'oznaczenie'            : 'RJ15',
       'typ'                   : 'Rzędowy, 4-suwowy, 4-cylindrowy, chłodzony cieczą, 16-zaworowy DOHC',
       'pojemnoscSkokowa'      : '599,4 cm3',
       'rokprodukcji'          : '2008',
       'srednicaCylindra'      : '67,0 x 42,5 mm',
       'stopienSprezania'      : '13,1 : 1',
       'Moc'                   : '99,6 kW (135 KM) przy 14 500 obr/min z doładowaniem dynamicznym 94,9 kW (129 KM) przy 14 500 obr/min bez doładowania dynamicznego',
       'momentObrotowy'        : '69,1 Nm przy 11 000 obr/min z doładowaniem dynamicznym 65,8 Nm przy 11 000 obr/min bez doładowania dynamicznego',
       'ukladOlejenia'         : 'Z mokrą misą olejową',
       'ukladZasilania'        : 'Wtrysk paliwa z YCC-T oraz YCC-I',
       'ukladZaplonowy'        : 'TCI',
       'sprzeglo'              : 'Wielotarczowe mokre z zabezpieczeniem przed zablokowaniem tylnego koła',
       'przelożenieWstepne'    : '85/41 (2,073)',
       'skrzyniaBiegow'        : '6-biegowa o stałym zazębieniu',
       'przelozenie1biegu'     : '31/12 (2,583)',
       'przelozenie2biegu'     : '32/16 (2,000)',
       'przelozenie3biegu'     : '30/18 (1,667)',
       'przelozenie4biegu'     : '26/18 (1,444)',
       'przelozenie5biegu'     : '27/21 (1,286)',
       'przelozenie6biegu'     : '23/20 (1,150)',
       'napedtylnegokola'      : '#525 łańcuch O-ring',
       'przelozenieNapedu'     : '45/16 (2,813',
       'rama'                  : 'Aluminiowa, Deltabox',
       'przednieZawieszenie'   : 'Odwrócony widelec teleskopowy, Ø 41 mm, regulacja napięcia wstępnego, regulacja tłumienia dobicia niezależnie dla wolnych i szybkich ugięć, regulacja tłumienia odbicia',
       'skokPrzedniego'        : '115 mm',
       'rozmiarPrzedniejopony' : '120/70 ZR 17',
       'tylneZawieszenie'      : 'Wahacz połączony układem dźwigniowym z elementem resorująco-amortyzującym, regulacja napięcia wstępnego, regulacja tłumienia dobicia niezależnie dla wolnych i szybkich ugięć, regulacja tłumienia odbicia',
       'skokTylnego'           : '120 mm',
       'rozmiarTylnejopony'    : '180/55 ZR 17',
       'katGlowkiramy'         : '24°',
       'wyprzedzenie'          : '97 mm',
       'przedniHamulec'        : 'Dwutarczowy, Ø 310 mm, zaciski radialne',
       'tylnyHamulec'          : 'Pojedyncza tarcza, Ø 220 mm',
       'dlugosc'               : '2040 mm',
       'szerokosc'             : '705 mm',
       'height'                : '1100 mm',
       'wysokoscSiedzenia'     : '850 mm',
       'rozstawOsi'            : '1380 mm',
       'przeswitMinimalny'     : '130 mm',
       'pojemnoscZbiornika'    : '17,3 l (3,5 l)',
       'pojemnoscUkladu'       : '3,4 l',
       'dryWeight'             : '166 kg',
       'wetWeight'             : '185 kg',

   }



   model2['2010'] = {}
   model2['2011'] = {}
   model2['2012'] = {}
   model2['2013'] = {}
   model2['2014'] = {}
   model2['2015'] = {}
   model2['2010']['info'] = 'Yamaha YZF-R6'
   model2['2011']['info'] = 'Yamaha YZF-R6'
   model2['2012']['info'] = 'Yamaha YZF-R6'
   model2['2013']['info'] = 'Yamaha YZF-R6'
   model2['2014']['info'] = 'Yamaha YZF-R6'
   model2['2015']['info'] = 'Yamaha YZF-R6'
   model2['2010']['data'] = model2['2011']= model2['2012']= model2['2013']= model2['2014']= model2['2015']['data']= {
       'rokProdukcji'          : '2010',
       'oznaczenie'            : 'RJ15',
       'typ'                   : 'Rzędowy, 4-suwowy, 4-cylindrowy, chłodzony cieczą, 16-zaworowy DOHC',
       'pojemnoscSkokowa'      : '599,4 cm3',
       'rokprodukcji'          : '2008',
       'srednicaCylindra'      : '67,0 x 42,5 mm',
       'stopienSprezania'      : '13,1 : 1',
       'Moc'                   : '91,0 kW (124 KM) przy 14 500 obr/min',
       'momentObrotowy'        : '65,7 Nm przy 11 000 obr/min',
       'ukladOlejenia'         : 'Z mokrą misą olejową',
       'ukladZasilania'        : 'Wtrysk paliwa z YCC-T oraz YCC-I',
       'ukladZaplonowy'        : 'TCI',
       'sprzeglo'              : 'Wielotarczowe mokre z zabezpieczeniem przed zablokowaniem tylnego koła',
       'przelożenieWstepne'    : '85/41 (2,073)',
       'skrzyniaBiegow'        : '6-biegowa o stałym zazębieniu',
       'przelozenie1biegu'     : '31/12 (2,583)',
       'przelozenie2biegu'     : '32/16 (2,000)',
       'przelozenie3biegu'     : '30/18 (1,667)',
       'przelozenie4biegu'     : '26/18 (1,444)',
       'przelozenie5biegu'     : '27/21 (1,286)',
       'przelozenie6biegu'     : '23/20 (1,150)',
       'napedtylnegokola'      : '#525 łańcuch O-ring',
       'przelozenieNapedu'     : '45/16 (2,813',
       'rama'                  : 'Aluminiowa, Deltabox',
       'przednieZawieszenie'   : 'Odwrócony widelec teleskopowy, Ø 41 mm, regulacja napięcia wstępnego, regulacja tłumienia dobicia niezależnie dla wolnych i szybkich ugięć, regulacja tłumienia odbicia',
       'skokPrzedniego'        : '115 mm',
       'rozmiarPrzedniejopony' : '120/70 ZR 17',
       'tylneZawieszenie'      : 'Wahacz połączony układem dźwigniowym z elementem resorująco-amortyzującym, regulacja napięcia wstępnego, regulacja tłumienia dobicia niezależnie dla wolnych i szybkich ugięć, regulacja tłumienia odbicia',
       'skokTylnego'           : '120 mm',
       'rozmiarTylnejopony'    : '180/55 ZR 17',
       'katGlowkiramy'         : '24°',
       'wyprzedzenie'          : '97 mm',
       'przedniHamulec'        : 'Dwutarczowy, Ø 310 mm, zaciski radialne',
       'tylnyHamulec'          : 'Pojedyncza tarcza, Ø 220 mm',
       'dlugosc'               : '2040 mm',
       'szerokosc'             : '705 mm',
       'height'                : '1100 mm',
       'wysokoscSiedzenia'     : '850 mm',
       'rozstawOsi'            : '1380 mm',
       'przeswitMinimalny'     : '130 mm',
       'pojemnoscZbiornika'    : '17,3 l (3,5 l)',
       'pojemnoscUkladu'       : '3,4 l',
       'dryWeight'             : '166 kg',
       'wetWeight'             : '189 kg',

   }





   try:
      info = model2.get(v1)


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


   except IOError as e:
    print('Tego modelu nie znam ({})'.format(e))





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









