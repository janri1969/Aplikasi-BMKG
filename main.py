"""
Aplikasi BMKG
"""
from scrap_berita import data_extraction, data_show

if __name__ == '__main__':
#    print("\nScrapping Data from BMKG")
    print("\nScrapping Data from Detik.com")
    result = data_extraction()
    data_show(result)

