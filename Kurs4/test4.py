__author__ = 'test'





def main():

    name = input("Cześć jestem Zed, jak masz na imię? ")
    print("Super " + name + ", miło Cię poznać")

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
    print(choices.get(v, "tego nie znam"))

if __name__ == '__main__':
    main()




