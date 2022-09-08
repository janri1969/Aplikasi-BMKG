"""
Aplikasi BMKG
"""
from scrap_bmkg import data_extraction, data_show

if __name__ == '__main__':
    print("Aplikasi BMKG")
    result = data_extraction()
    data_show(result)

