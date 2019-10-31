import csv
import os
import requests
import re

# definiratje URL glavne strani bolhe za oglase z mačkami
viski_frontpage_url = 'http://whiskyadvocate.com/ratings-reviews/?search=&submit=+&brand_id=0&rating=0&price=0&category=0&styles_id=0&issue_id=103'
# mapa, v katero bomo shranili podatke
viski_directory = 'viski_out'
# ime datoteke v katero bomo shranili glavno stran
frontpage_filename = 'index.html'
# ime CSV datoteke v katero bomo shranili podatke
csv_filename = 'viski_csv'

def download_url_to_string(url):
    """Funkcija kot argument sprejme niz in puskuša vrniti vsebino te spletne
    strani kot niz. V primeru, da med izvajanje pride do napake vrne None.
    """
    try:
        # del kode, ki morda sproži napako
        page_content = requests.get(url)
    except Exception as e:
        # koda, ki se izvede pri napaki
        # dovolj je če izpišemo opozorilo in prekinemo izvajanje funkcije
        print(e)
    # nadaljujemo s kodo če ni prišlo do napake
    return page_content.text

def save_string_to_file(text, directory, filename):
    """Funkcija zapiše vrednost parametra "text" v novo ustvarjeno datoteko
    locirano v "directory"/"filename", ali povozi obstoječo. V primeru, da je
    niz "directory" prazen datoteko ustvari v trenutni mapi.
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None


# Definirajte funkcijo, ki prenese glavno stran in jo shrani v datoteko.


def save_frontpage(page, directory, filename):
    """Funkcija shrani vsebino spletne strani na naslovu "page" v datoteko
    "directory"/"filename"."""

    page_data = download_url_to_string(page)
    save_string_to_file(page_data, directory, filename)






def main(redownload=True, reparse=True):
    """Funkcija izvede celoten del pridobivanja podatkov:
    1. Oglase prenese iz bolhe
    2. Lokalno html datoteko pretvori v lepšo predstavitev podatkov
    3. Podatke shrani v csv datoteko
    """
    # Najprej v lokalno datoteko shranimo glavno stran
    for i in range(10):
        viski_frontpage_url = 'http://whiskyadvocate.com/ratings-reviews/?search=&submit=+&brand_id=0&rating=0&price=0&category=0&styles_id=0&issue_id={}'.format(103-i)
        print(viski_frontpage_url)
        frontpage_filename = 'index{}.html'.format(i)
        save_frontpage(viski_frontpage_url, viski_directory, frontpage_filename)
    ## Iz lokalne (html) datoteke preberemo podatke
#
    #content = read_file_to_string(cat_directory, frontpage_filename)
#
    ## Podatke prebermo v lepšo obliko (seznam slovarjev)
    #print(ads_from_file(frontpage_filename, cat_directory))
#
    #print(ads_from_file)
#
    ## Podatke shranimo v csv datoteko
#
    ## Dodatno: S pomočjo parameteov funkcije main omogoči nadzor, ali se
    ## celotna spletna stran ob vsakem zagon prense (četudi že obstaja)
    ## in enako za pretvorbo





if __name__ == '__main__':
    main()

