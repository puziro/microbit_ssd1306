from ssd1306_px import set_px
from kana2 import khenkan

def kana_prt(keta, gyo, km):
    z = 0
    for c in km:
        x = (keta + z) * 6
        y = gyo * 8 + 1
        k = khenkan(c)
        for n in range(0, 5):
            if k[n] == "1":
                set_px(x + n, y, k[n], 0)
        for n in range(5, 10):
            if k[n] == "1":
                set_px(x + n - 5, y + 1, k[n], 0)
        for n in range(10, 15):
            if k[n] == "1":
                set_px(x + n - 10, y + 2, k[n], 0)
        for n in range(15, 20):
            if k[n] == "1":
                set_px(x + n - 15, y + 3, k[n], 0) 
        for n in range(20, 25):
            if k[n] == "1":
                set_px(x + n - 20, y + 4, k[n], 0)                  
        z = z + 1