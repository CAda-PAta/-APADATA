import random as rd
import csv 
cumlist=[]
def kayit(data,isim):
    with open(f'{isim}.csv', 'w', newline='', encoding='utf-8') as dosya:
        writer = csv.writer(dosya)
        # Başlıkları yaz
        writer.writerow(["kelimeler", 0])
        # Verileri yaz
        writer.writerows(data)

isimler=['kağıt','kalem','at','minibüs','taşıt','kamyon','kafa','yat']
zamir=['sen','o','biz','siz','onlar']
kufur=[]
dosya_yolu = 'ekufur.csv'
with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
    # Satırları döngü ile okuyarak listeye ekleyin
    for satir in dosya:
        kelime = satir.strip()  # Satırdaki boşlukları temizleyin
        kufur.append(kelime)
isfiilleri = []
hakaretler=[]
dosya_yolu = 'genel_is_fiileri.csv'
with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
    # Satırları döngü ile okuyarak listeye ekleyin
    for satir in dosya:
        kelime = satir.strip()  # Satırdaki boşlukları temizleyin
        isfiilleri.append(kelime)

dosya_yolu = 'ARGO_SÖZLER.csv'
with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
    # Satırları döngü ile okuyarak listeye ekleyin
    for satir in dosya:
        kelime = satir.strip()  # Satırdaki boşlukları temizleyin
        hakaretler.append(kelime)
dt= [
    'Ali', 'Ev', 'Okul', 'Yardım', 'Arkadaş', 'Kapı', 'Yatak', 'Masa', 'Köşe', 'Araba',
    'Sokak', 'Bahçe', 'İş', 'Köy', 'Şehir', 'Dağ', 'Göl', 'Deniz', 'Park', 'Ekmek',
    'Kitap', 'Kardeş', 'Anne', 'Baba', 'Güzel', 'Hastane', 'Dışarı', 'Eğitim', 'Üniversite',
    'Kış', 'Yaz', 'Sonbahar', 'Bahar', 'Yol', 'Gölge', 'Sınıf', 'Bilgi', 'Ders', 'Çalışma',
    'Gün', 'Saat', 'Zaman', 'Evde', 'Kapalı', 'Oyun', 'Kampüs', 'Koca', 'Tezgah', 'Tiyatro',
    'Film', 'Dış', 'İç', 'Sahne', 'Bina', 'Hava', 'Su', 'Hediye', 'Çay', 'Kahve', 'Yemek',
    'Pazar', 'Alışveriş', 'Gıda', 'Et', 'Balık', 'Tavuk', 'Şehirler', 'Ülkeler', 'Yatak',
    'Dışarıda', 'Üzerinde', 'Yanında', 'Önünde', 'Arkada', 'İçinde', 'Ötesinde', 'Sahip',
    'Orman', 'Müzik', 'Konser', 'Resim', 'Düşünce', 'Kardeşler', 'Sahip', 'Gece', 'Eğlence',
    'Köylü', 'Çiftçi', 'Fırsat', 'Köyde', 'Üniversiteler', 'Dünya', 'Kıta', 'Ay', 'Yıl',
    'Çim', 'Zemin', 'Pencere', 'Yüksek', 'Fırın', 'Oda', 'Bölüm', 'Kütüphane', 'Ebeveyn',
    'İnternet', 'Kütüphaneler', 'Sokaklar', 'Köyler', 'Ülkeler', 'Şehirler', 'Kasaba', 'Lise',
    'Sınıflar', 'Açık', 'Saklı', 'Eğitimler', 'Söyleşi', 'Konferans', 'Çalışanlar', 'Seminer',
    'Tarih', 'Tatil', 'Küçük', 'Büyük', 'Yük', 'Konaklama'
]


baglac=['ve','ile',]
nitsifatlari = [
    'güzel', 'sarı', 'mavi', 'büyük', 'küçük', 'hızlı', 'düz',
    'harika', 'çekici', 'parlak', 'neşeli', 'eğlenceli', 'temiz', 'sağlam',
    'modern', 'renkli', 'ilginç', 'sevimli', 'şık', 'zarif', 'neat', 'etkileyici',
    'kapsamlı', 'uyumlu', 'rahat', 'yeni', 'prestijli', 'üstün', 'göz alıcı',
    'muazzam', 'olağanüstü', 'mükemmel', 'sıcak', 'tatlı', 'gelişmiş', 'verimli',
    'keyifli', 'huzurlu', 'estetik', 'akıllı', 'nazik', 'güvenilir', 'profesyonel',
    'ikna edici', 'yaratıcı', 'çarpıcı', 'sade', 'hoş', 'canlı', 'dinamik',
    'özgün', 'kapsayıcı', 'pratik', 'fonksiyonel', 'geliştirici', 'detaylı', 'ilham verici',
    'temiz', 'gelişmiş', 'etkili', 'akıcı', 'açık', 'samimi', 'hoş'
]

zt = [
    'dün', 'yarın', 'ertesi gün', 'bahar', 'pzt gün', 'salı gün',
    'bugün', 'önceki gün', 'geçen hafta', 'gelecek hafta', 'bu sabah', 'akşam',
    'gece', 'öğlen', 'öğleden sonra', 'bu gece', 'dün gece', 'bu hafta',
    'önceki hafta', 'sonraki hafta', 'bu yıl', 'geçen yıl', 'gelecek yıl',
    'bu ay', 'geçen ay', 'gelecek ay', 'ilkbahar', 'yaz', 'sonbahar', 'kış',
    'erken', 'geç', 'sabah', 'öğle', 'akşam', 'gece', 'hafta sonu',
    'bu akşam', 'daha önce', 'yakında', 'uzun süre', 'bir süre', 'hemen',
    'şimdi', 'büyük ihtimalle', 'şu anda', 'eski', 'günümüzde', 'esasında',
    'genelde', 'sıklıkla', 'ara sıra', 'daha sonra'
]
zt.extend([
    'bazen', 'sık sık', 'her zaman', 'nadiren', 'hiç', 'zaman zaman', 
    'daha önce', 'son zamanlarda', 'yakın zamanda', 'önümüzdeki günlerde', 
    'uzun zamandır', 'kısa bir süre', 'şu sıralar', 'bir müddet', 'şu anda', 
    'gelişen günlerde', 'gelecek günlerde', 'son birkaç gün', 'önceki aylarda', 
    'geçen yıl', 'yakın tarihlerde', 'önümüzdeki yıllarda', 'bu saatlerde', 
    'geçmişte', 'yakın geçmişte', 'önceki yıllarda', 'bu dönem', 'geçmiş dönem', 
    'uzun bir süre önce', 'geçmiş zamanlarda', 'şu günlerde', 'şu andan itibaren', 
    'önceki haftalarda', 'son günlerde', 'yakın dönemde', 'eski dönemlerde', 
    'günümüzde', 'yakın tarihte', 'gelecek tarihlerde', 'son saatlerde', 
    'önceki saatlerde', 'yakın saatlerde', 'geçmiş saatlerde', 'bu günlerde'
])
saysifatlari = [
    'bir', 'iki', 'üç', 'dört', 'beş', 'altı', 'yedi', 'sekiz', 'dokuz', 'on',
    'onbir', 'oniki', 'onüç', 'ondört', 'onbeş', 'onaltı', 'onyedi', 'onsekiz', 'ondokuz',
    'yirmi', 'yirmibir', 'yirmiiki', 'yirmiüç', 'yirmidört', 'yirmibeş', 'yirmialtı', 'yirmiyedi', 'yirmisekiz', 'yirmidokuz',
    'otuz', 'otuzbir', 'otuziki', 'otuzüç', 'otuzdört', 'otuzbeş', 'otuzaltı', 'otuzyedi', 'otuzsekiz', 'otuzdokuz',
    'kırk', 'kırkbir', 'kırkiki', 'kırküç', 'kırkdört', 'kırkbeş', 'kırkaltı', 'kırkyedi', 'kırksekiz', 'kırkdokuz',
    'elli', 'ellibir', 'elliiki', 'elliüç', 'ellidört', 'ellibeş', 'ellialtı', 'elliyedi', 'ellisekiz', 'ellidokuz',
    'altmış', 'altmışbir', 'altmışiki', 'altmışüç', 'altmışdört', 'altmışbeş', 'altmışaltı', 'altmışyedi', 'altmışsekiz', 'altmışdokuz',
    'yetmiş', 'yetmişbir', 'yetmişiki', 'yetmişüç', 'yetmişdört', 'yetmişbeş', 'yetmişaltı', 'yetmişyedi', 'yetmişsekiz', 'yetmişdokuz',
    'seksen', 'seksenbir', 'sekseniki', 'seksenüç', 'seksenört', 'seksenbeş', 'seksenalti', 'seksenyedi', 'seksensekiz', 'seksen dokuz',
    'doksan', 'doksanbir', 'doksaniki', 'doksanüç', 'doksandört', 'doksanbeş', 'doksanalti', 'doksanyedi', 'doksansekiz', 'doksandokuz'
]



for i in range(500000):
	#sorsifat=['hangi','kaç','nasıl']
	a=[]
	hakdeger=0
	if rd.randint(0,5)<3:
		a.append(rd.choices(zamir))
	for i in range(1):
		if i>0:
			a.append(rd.choices(baglac))
		try:

			c=''
			if rd.randint(0,5)<3:
				for b in range(rd.randint(0,3)):	
					if b>0:
						a.append(['ve'])
					elif rd.randint(0,5)<4:
						a.append(rd.choices(zt))
						a.append(rd.choices(dt))
						if rd.randint(0,5)>3:
							a.append(rd.choices(saysifatlari))

					b=rd.choices(nitsifatlari)
					if c==b:
						break
					a.append(b)
					c=b
			if rd.randint(0,5)<3:
				for b in range(rd.randint(0,2)):	
					if b>0:
						a.append(['ve'])
						hakdeger-=0.1
					hakdeger+=0.2
					b=rd.choices(hakaretler)
					if c==b:
						break
					a.append(b)
					c=b
			if rd.randint(0,5)<3:
				for b in range(rd.randint(0,2)):	
					if b>0:
						a.append(['ve'])
						hakdeger-=0.3
					b=rd.choices(kufur)
					hakdeger+=0.5
					if c==b:
						break
					a.append(b)
					c=b
					
		finally:
			a.append(rd.choices(isimler))
	a.append(rd.choices(isfiilleri))
	cumle=''
	for i in a:
		cumle=cumle+' '+i[0]
	
	# print('cümle = ',cumle)
	# print('hakaret değeri = ', hakdeger)
	cumlist.append([cumle,hakdeger])
kayit(cumlist,'cumle_seti')
	
