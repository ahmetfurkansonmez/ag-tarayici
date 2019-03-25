import scapy.all as scapy
# network aglari icin ozellestirilmis paketler uretmemiz icin kullandigimiz kutuphane
import optparse # kullanicidan girdiler alabilmek icin kullandigimiz kutuphane

# kullanicidan ip adresini almak icin kullannacagimiz fonksiyon

def kullanici_girdisi():
    parse_object = optparse.OptionParser() # obje olusturduk
    parse_object.add_option("-i","--ipadress",dest="ip_address",help="IP adresi giriniz")
# objemize ip adresi secenegini ekleyip dest ve help degerlerini atadik
    (girdiler,arguments)= parse_object.parse_args()
# alinan degerleri girdiler adli degiskene atadik.
    if not girdiler.ip_address:
# eger ip adresi girilmediyse ekrana mesaj veren kosul yapisi
        print("ip adresi gir!!!")
# alinan degerleri donduruyoruz
    return girdiler

# icinde belirtilen ip'yi tarayack program

def agi_tara(ip):
    istek_paketi = scapy.ARP(pdst=ip)
# agda istek yapmak icin ARP metodunu kullaniyoruz. metodun icine ip adresini(pdst) ye atiyoruz
    yayin_paketi = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
# agda yayin icin Ether ozelliginin icine default mac adresi giriyoruz
    kombine_paket = yayin_paketi/istek_paketi
# iki paketi birlestirip kombine_paket adli bir degiskene atiyoruz
    (cevaplar, cevapsizlar) = scapy.srp(kombine_paket, timeout=1)
# paketleri srp ozelligiyle gonderip alinan sonuclari cevaplar adli bir degiskene kaydediyoruz.
# #(timeout ozelligi cevap almadigi zaman 1 saniye bekleye ayarliyoruz)
    cevaplar.summary() # cevaplarin ozetini cikar

kullanici_ip_adresi = kullanici_girdisi()
# kullanicidan alinan ip adresini kullanici_ip_adresi adli bir degiskene atadik
agi_tara(kullanici_ip_adresi.ip_address)

# kullanim = python ag-tarayici.py -i {ip adresi}
# ornek = python ag-tarayici.py -i 10.0.2.1/24
#--------------------ahmetfurkansonmez12@gmail.com--------------------