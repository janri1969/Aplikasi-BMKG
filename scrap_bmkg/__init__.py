"""
Aplikasi Scrap data BMKG
"""
import requests
from bs4 import BeautifulSoup


def data_extraction():
#   print("\nData Mentah dari BMKG")
    content = requests.get("https://bmkg.go.id")
    soup = BeautifulSoup(content.text, "html.parser")

    result = soup.find('ul', {'class' : 'list-unstyled'})
    result = result.findChildren('li')

    i = 0

    waktu = None
    tanggal = None
    magnitudo = None
    kedalaman = None
    ls = None
    bt = None
    lokasi = None
    dirasakan = None

    for res in result:
        if i == 0:
            time_date = res.text.split(', ')
            waktu = time_date[1]
            tanggal = time_date[0]
#            print(time_date)
        elif i == 1:
            magnitudo = res.text
#            print(magnitudo)
        elif i == 2:
            kedalaman = res.text
#            print(kedalaman)
        elif i == 3:
            koordinat = res.text.split('- ')
            ls = koordinat[0]
            bt = koordinat[1]
#            print(koordinat)
        elif i == 4:
            lokasi = res.text
#            print(lokasi)
        elif i == 5:
            dirasakan = res.text
#            print(dirasakan)
        i = i + 1

    hasil = dict()
    hasil['time_date'] = {'waktu' : waktu, 'tanggal' : tanggal}
    hasil['magnitudo'] = magnitudo
    hasil['kedalaman'] = kedalaman
    hasil['koordinat'] = {'ls' : ls, 'bt' : bt }
    hasil['lokasi'] = lokasi
    hasil['dirasakan'] = dirasakan
    return hasil

def data_show(result):

    print("\nGempa Terakhir berdasarkan BMKG")
    print(f"Waktu : {result['time_date']['waktu']}")
    print(f"Tanggal : {result['time_date']['tanggal']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Koordinat : LS = {result['koordinat']['ls']}, BT = {result['koordinat']['bt']}")
    print(f"Lokasi : {result['lokasi']}")
    print(f"{result['dirasakan']}")

