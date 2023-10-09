variabel = []
mitt_nummer = 10


def lägg_till_sak_till_variabel(sak, min_lista):
    variabel.append(sak)
    min_lista = [100]
    min_lista.append(sak)
    print(mitt_nummer)

def main():
    min_lista = []
    lägg_till_sak_till_variabel('Hej', min_lista)
    lägg_till_sak_till_variabel('Då', min_lista)
    lägg_till_sak_till_variabel(42, min_lista)

    # print(variabel)
    print(min_lista)
    # print(min_lista == variabel)
    return min_lista

if __name__ == '__main__':
    min_lista = main()

    print(min_lista)