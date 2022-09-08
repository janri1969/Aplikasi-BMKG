"""
Aplikasi Scrap data BMKG
"""
import requests
from bs4 import BeautifulSoup


def data_extraction():

    content = requests.get("https://bmkg.go.id")
    soup = BeautifulSoup(content.text, "html.parser")

    result = soup.find('ul', {'class' : 'list-unstyled'})
    result = result.findChildren('li')

    i = 0

    time_date = None
    waktu = None
    tanggal = None
    magnitudo = None
    kedalaman = None
    ls = None
    bt = None
    lokasi = None
    dirasakan = None

    for res in result:
        print(i, res)
        if i == 0:
            time_date = res.text.split(', ')
            waktu = time_date[0]
            tanggal = time_date[1]
            print(time_date)
        elif i == 1:
            magnitude = res.text
            print(magnitude)
        elif i == 2:
            kedalaman = res.text
            print(kedalaman)
        elif i == 3:
            koordinat = res.text.split('- ')
            ls = koordinat[0]
            bt = koordinat[1]
            print(koordinat)
        elif i == 4:
            lokasi = res.text
            print(lokasi)
        elif i == 5:
            dirasakan = res.text
            print(dirasakan)
        i = i + 1

    hasil = dict()
    hasil['time_date'] = {'waktu' : waktu, 'tanggal' : tanggal}
    hasil['magnitudo'] = magnitudo
    hasil['kedalaman'] = kedalaman
    hasil['koordinat'] = {'ls' : ls, 'bt' : bt }
    hasil['lokasi'] = lokasi
    hasil['dirasakan'] = dirasakan
    print(hasil)

def data_show(result):

    print("Gempa Terakhir berdasarkan BMKG")
    print(f"Tanggal : {result['time_date']['waktu']}, {result['time_date']['tanggal']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Koordinat : LS = {result['koordinat']['ls']}, BT = {result['koordinat']['bt']}")
    print(f"Lokasi : {result['lokasi']}")
    print(f"{result['dirasakan']}")
    print("data_show")

#data_extraction()
#data_show(result)


