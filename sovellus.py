# PÄÄOHJELMA

# KIRJASTOJEN JA MODULIEN LATAUS

# Otetaan käyttöön Windows-äänikirjasto (pythonin sisäänrakennettu kirjasto)
import winsound

# Otetaan käyttöön oma funktiomoduli
import funktio_moduli


def select_case(sanakirja, avain, oletus):
    """Muiden ohjelmointikielten Select-Case-rakennetta vastaava funktio

    Args:
        sanakirja (dict): Avain-arvo-parit
        avain (any): hakuavain
        oletus (any): arvo, jos hakuavainta ei loydy

    Returns:
        any: Hakuavainta vastaava arvo tai oletus, mikali hakuavainta ei loytynyt
    """
    arvo = sanakirja.get(avain, oletus)
    return arvo


# Varsinainen pääohjelma alkaa tästä
huoneraja_arvot = {'MH': 30, 'K': 20, 'KPH': 5, 'WC': 5, 'OH': 20}

# Lista mittaustuloksista, tyhjä ennen silmukkaa
mittaustulokset = []

# Ikuinen silmukka
while True:
    # Tätä toistetaan kunnes käyttäjä sulkee ohjelman
    seina1 = float(input('Anna ensimmaisen seinan pituus: '))
    seina2 = float(input('Anna toisen seinan pituus: '))
    lavistaja = float(input('Anna ristimitta: '))
    # TODO: Lisää tähän kysymys mikä huonetyyppi on kyseessä
    mittaustulokset.append(seina1)
    mittaustulokset.append(seina2)
    mittaustulokset.append(lavistaja)

    # TODO: Muuta, siten, että kertoo onko huonekohtaisten rajojen sisällä
    # Kerrotaan onko tila suorakulmainen
    print('Nurkka suorakulmainen', funktio_moduli.suorakulma(
        seina1, seina2, lavistaja))

    # Kysytään käyttäjältä haluaako jatkaa
    lopetetaan = input('Paina L, jos haluat lopettaa: ').upper()

    if lopetetaan == 'L':
        break

# Ohjelman suoritus päättyy

# Kysytään mittaajan työmaan tiedot
tyomaa = input(
    'Minka tyyppinen tyomaa oli (kerrostalo, rivitalo tai OK-talo): ').lower()

# Ilmoitetaan montako senttiä mittauksessa saa olla virheitä IF-rakenteen avulla

if tyomaa == 'kerrostalo':
    print('Maksimivirhe saa olla 10 mm')
elif tyomaa == 'rivitalo':
    print('Maksimivirhe saa olla 20 mm')
else:
    print('Maksimivirhe saa olla 50 mm')

# Kysytään huonetyyppi
    huone = input('mika huone? ').upper()

# Haetaan raja-arvo sanakirjasta, oletus 50 mm
raja_arvo = select_case(huoneraja_arvot, huone, 50)

print('Maksimiero', huone, 'on', raja_arvo, 'mm')

mittauksia = len(mittaustulokset)
print('Kiitos tasta paivasta, teit', mittauksia, 'mittausta')

# Tulostetaan ruudulle kaikki mittaustulokset
print('Paivan mittaukset alla: ')
for mittaus in mittaustulokset:
    print(mittaus)
