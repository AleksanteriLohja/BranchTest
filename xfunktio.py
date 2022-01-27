# X-funktio tarkistaa onko kulma suora

def suorakulma(sivuA, sivuB, lavistaja):
    """Tarkistaa suorakulmaisuuden kayttaen Pythagoraan lausetta

    Args:
        sivuA ([float]): Ensimmäisen sivun pituus
        sivuB ([float]): Toisen sivun pituus
        lavistaja ([float]): Lavistajan pituus

    Returns:
        boolean: TRUE -> suorakulma
    """
    A_nelio = sivuA * sivuA
    B_nelio = sivuB * sivuB
    l_nelio = lavistaja * lavistaja
    
    if A_nelio + B_nelio == l_nelio:
      suora = True
    else:
        suora = False
    return  suora

# Testataan, että toimii, poista tämä myöhemmin
vastaus = suorakulma(3, 4, 5)
print(vastaus)