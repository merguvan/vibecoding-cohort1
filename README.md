# Proje Adı

vbl1

## Proje Hakkında

Bu proje, çeşitli Python modüllerinden oluşan bir yazılım uygulamasıdır. Projede agent ve asistan dosyaları ile, front-end tarafında ise HTML dosyaları ile kullanıcı ara yüzleri oluşturulmuştur.

## Kurulum

Projeyi çalıştırmak için gereksinim dosyasındakı paketlerin kurulması gerekmektedir. Bunun için:

```
pip install -r requirements.txt
```

komutunu çalıştırarak gerekli tüm bağımlılıkları yükleyebilirsiniz.

## Kullanım

Proje, arka planda `app.py`, `agent.py`, `asistan.py` ve `llm.py` Python dosyaları ve ön yüzde `frontend` klasöründeki HTML dosyaları ile çalışmaktadır. Her bir bileşen spesifik işlemler için tasarlanmıştır.

## Katkıda Bulunma

Katkıda bulunmak isteyenler standart bir pull request süreci üzerinden projeye katkıda bulunabilirler.

## Eklenen Agent Araci

Bu fork'ta `text_insights` adinda yeni bir agent araci eklendi. Agent bu araci kullanarak verilen metindeki kelime sayisini, karakter sayisini, cumle sayisini ve tahmini okuma suresini hesaplayabilir. Arac `backend/tools/` altinda tanimlandi ve `agent.py` icindeki tool-calling dongusune kaydedildi.

## Lisans

Bu projeye ait lisans bilgileri burada yer alacaktır.
