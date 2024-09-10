#pip install folium
import folium
from folium.plugins import MiniMap
from branca.element import Template, MacroElement

#Coordinates and relative informations 
fac = [
	    {'name': 'Ambarlı İleri Biyolojik Atık Su Arıtma Tesisi', 'lat': 40.99000, 'lon': 28.68111, 'detail':400000, 'detail_2':2012},
	    {'name': 'Ataköy İleri Biyolojik Atık Su Arıtma Tesisi', 'lat': 40.97194, 'lon': 28.83639, 'detail':620, 'detail_2':2010},
        {'name': 'Terkos İleri Biyolojik Atık Su Arıtma Tesisi', 'lat': 41.30278, 'lon': 28.67361, 'detail':1.73, 'detail_2':2000},
        {'name': 'Çanta İleri Biyolojik Atık Su Arıtma Tesisi', 'lat': 41.06667, 'lon': 28.09972, 'detail':52, 'detail_2':2016},
        {'name': 'Silivri İleri Biyolojik Atık Su Arıtma Tesisi', 'lat': 41.09167, 'lon': 28.23972, 'detail':36.5, 'detail_2':2016},
        {'name': 'Büyükçekmece İleri Biyolojik Atık Su Arıtma Tesisi', 'lat': 41.04778, 'lon':28.55056 , 'detail':132.16, 'detail_2':2016},
        {'name': 'Selimpaşa İleri Biyolojik Atık Su Arıtma Tesisi', 'lat': 41.0625, 'lon':28.35333 , 'detail':70, 'detail_2':2016},
        {'name': 'Gümüşyaka İleri Biyolojik Atık Su Arıtma Tesisi', 'lat': 41.06694, 'lon': 28.04917, 'detail':4.4, 'detail_2':2007},
        {'name': 'Çatalca Akalan Biyolojik Paket Atık Su Arıtma Tesisi', 'lat': 41.2525, 'lon':28.42222 , 'detail':400, 'detail_2':2008},
        {'name': 'Çatalca Kestanelik Biyolojik Atık Su Arıtma Tesisi', 'lat':41.22556 , 'lon':28.50139 , 'detail':500, 'detail_2':2010},
        {'name': 'Çatalca Yazlık Biyolojik Atık Su Arıtma Tesisi', 'lat':41.29694 , 'lon':28.51194 , 'detail':250, 'detail_2':2012},
        {'name': 'Çatalca Çanakça Biyolojik Atık Su Arıtma Tesisi', 'lat':41.23806 , 'lon':28.50361 , 'detail':500, 'detail_2':2010},
        {'name': 'Çatalca İzzettin Biyolojik Atık Su Arıtma Tesisi', 'lat':41.15639 , 'lon':28.50917 , 'detail':500, 'detail_2':2010},
        {'name': 'Arnavutköy Boyalık Biyolojik Atık Su Arıtma Tesisi', 'lat':41.255 , 'lon':28.62889 , 'detail':250, 'detail_2':2011},
        {'name': 'Çatalca Başakköy Biyolojik Atık Su Arıtma Tesisi', 'lat':41.33472 , 'lon':28.45167 , 'detail':250, 'detail_2':2010},
        {'name': 'Silivri Beyciler Biyolojik Atık Su Arıtma Tesisi', 'lat':41.22722 , 'lon':28.115 , 'detail':1, 'detail_2':2013},
        {'name': 'Arnavutköy Karaburun Biyolojik Atık Su Arıtma Tesisi', 'lat':41.33 , 'lon':28.71278 , 'detail':2, 'detail_2':2014},
        {'name': 'Silivri Çayırdere Biyolojik Atık Su Arıtma Tesisi', 'lat':41.28056 , 'lon':28.13611 , 'detail':500, 'detail_2':2014},
        {'name': 'Silivri Danamandıra Biyolojik Atık Su Arıtma Tesisi', 'lat':41.31417 , 'lon':28.24917 , 'detail':500, 'detail_2':2014},
        {'name': 'Çatalca Hallaçlı Biyolojik Atık Su Arıtma Tesisi', 'lat':41.31389 , 'lon':28.08944 , 'detail':500, 'detail_2':2014},
        {'name': 'Çatalca Aydınlar Biyolojik Atık Su Arıtma Tesisi', 'lat':41.37889 , 'lon':28.20611 , 'detail':500, 'detail_2':2014},
        {'name': 'Arnavutköy Dursunköy Biyolojik Atık Su Arıtma Tesisi', 'lat':41.19611 , 'lon':28.63944 , 'detail':500, 'detail_2':2016},
        {'name': 'Çatalca Hisarbeyli Biyolojik Atık Su Arıtma Tesisi', 'lat':41.3675 , 'lon':28.46694 , 'detail':500, 'detail_2':2016},
        {'name': 'Çatalca Elbasan Biyolojik Atık Su Arıtma Tesisi', 'lat':41.13028 , 'lon':28.41639 , 'detail':50, 'detail_2':2016},
        {'name': 'Arnavutköy Yassıören Biyolojik Atık Su Arıtma Tesisi', 'lat':41.23028 , 'lon':28.59861 , 'detail':550, 'detail_2':2018},
        {'name': 'Arnavutköy Baklalı Biyolojik Atık Su Arıtma Tesisi', 'lat':41.25333 , 'lon':28.65222 , 'detail':250, 'detail_2':2018},
        {'name': 'Silivri Akören Biyolojik Atık Su Arıtma Tesisi', 'lat':41.18333 , 'lon':28.34611 , 'detail':500, 'detail_2':2016},
        {'name': 'Eyüpsultan Akpınar Biyolojik Atık Su Arıtma Tesisi', 'lat':41.2875 , 'lon':28.80861 , 'detail':950, 'detail_2':2018},
        {'name': 'Çatalca Ormanlı Biyolojik Atık Su Arıtma Tesisi', 'lat':41.39528 , 'lon': 28.46111, 'detail':250, 'detail_2':2020},
        {'name': 'Yenikapı Atık Su Ön Arıtma Tesisi', 'lat':41.00278 , 'lon':28.94972 , 'detail':86.4, 'detail_2':1998},
        {'name': 'Baltalimanı Biyolojik Atık Su Arıtma Tesisi', 'lat':41.09944 , 'lon':29.03583 , 'detail':600, 'detail_2':2023},
        {'name': 'Küçükçekmece Atık Su Ön Arıtma Tesisi', 'lat':40.98139 , 'lon':28.75611 , 'detail':354, 'detail_2':2003},
        {'name': 'Tuzla İleri Biyolojik Atık Su Arıtma Tesisi', 'lat':40.82528 , 'lon':29.29278 , 'detail':650, 'detail_2':1998},
        {'name': 'Paşaköy İleri Biyolojik Atık Su Arıtma Tesisi', 'lat':41.0075 , 'lon':29.28083 , 'detail':154, 'detail_2':2000},
        {'name': 'Şile Geredeli Köyü Biyolojik Atık Su Arıtma Tesisi', 'lat':41.12528 , 'lon':29.56861 , 'detail':800, 'detail_2':2013},
        {'name': 'Şile Kabakoz Köyü Biyolojik Atık Su Arıtma Tesisi', 'lat':41.15528 , 'lon':29.70417 , 'detail':250, 'detail_2':2013},
        {'name': 'Şile Sofular Köyü Biyolojik Atık Su Arıtma Tesisi', 'lat':41.18194 , 'lon':29.49806 , 'detail':250, 'detail_2':2013},
        {'name': 'Şile Alacalı Köyü Biyolojik Atık Su Arıtma Tesisi', 'lat':41.18861 , 'lon':29.47611 , 'detail':250, 'detail_2':2013},
        {'name': 'Şile Kurnaköy Köyü Biyolojik Atık Su Arıtma Tesisi', 'lat':41.20833 , 'lon':29.3575 , 'detail':250, 'detail_2':2013},
        {'name': 'Cumhuriyet Biyolojik Ve İleri Biyolojik Atık Su Arıtma Tesisi', 'lat':41.13278 , 'lon':29.27167 , 'detail':1000, 'detail_2':2013},
        {'name': 'Şile Üvezli Köyü Biyolojik Atık Su Arıtma Tesisi', 'lat':41.11583 , 'lon':29.44306 , 'detail':250, 'detail_2':2013},
        {'name': 'Şile Satmazlı İleri Biyolojik Atık Su Arıtma Tesisi', 'lat':41.12528 , 'lon':29.56861 , 'detail': 800, 'detail_2':2013},
        {'name': 'Şile Değirmençayırı Köyü Biyolojik Atık Su Arıtma Tesisi', 'lat':40.98417 , 'lon':29.66778 , 'detail':250, 'detail_2':2013},
        {'name': 'Çekmeköy Ömerli Biyolojik Atık Su Arıtma Tesisi', 'lat':41.08167 , 'lon':29.33417 , 'detail':500, 'detail_2':2008},
        {'name': 'Şile Kömürlük Biyolojik Atık Su Arıtma Tesisi', 'lat':41.07861 , 'lon':29.43306 , 'detail':125, 'detail_2':2008},
        {'name': 'Şile Sahilköy Biyolojik Atık Su Arıtma Tesisi', 'lat':41.20028 , 'lon':29.42889 , 'detail':500, 'detail_2':2011},
        {'name': 'Şile İmrenli Biyolojik Atık Su Arıtma Tesisi', 'lat':41.15722 , 'lon':29.75361 , 'detail': 50, 'detail_2':2012},
        {'name': 'Şile Karakiraz Biyolojik Atık Su Arıtma Tesisi', 'lat':41.18167 , 'lon':29.35111 , 'detail':450, 'detail_2':2012},
        {'name': 'Çekmeköy Koçullu Biyolojik Atık Su Arıtma Tesisi', 'lat':41.08389 , 'lon':29.33556 , 'detail':500, 'detail_2':2012},
        {'name': 'Beykoz Öğümce Biyolojik Paket Atık Su Arıtma Tesisi', 'lat':41.16278 , 'lon':29.26861 , 'detail':200, 'detail_2':2010},
        {'name': 'Çekmeköy Hüseyinli Köyü Biyolojik Atık Su Arıtma Tesisi', 'lat':41.12556 , 'lon':29.28306 , 'detail':2, 'detail_2':2013},
        {'name': 'Çekmeköy Reşadiye Köyü Biyolojik Atık Su Arıtma Tesisi', 'lat':41.10083 , 'lon':29.27972 , 'detail':2, 'detail_2':2013},
        {'name': 'Küçüksu Atık Su Ön Arıtma Tesisi', 'lat':41.06944 , 'lon':29.07444 , 'detail':640, 'detail_2':2004},
        {'name': 'Şile Kumbaba Atık Su Ön Arıtma Tesisi', 'lat':41.16944 , 'lon':29.58028 , 'detail':46, 'detail_2':2008},
        {'name': 'Kadıköy Atık Su Ön Arıtma Tesisi', 'lat':40.98806 , 'lon':29.01944 , 'detail':833, 'detail_2':2003},
        {'name': 'Üsküdar Atık Su Ön Arıtma Tesisi', 'lat':41.06944 , 'lon':29.07444 , 'detail':77.76, 'detail_2':1992},
        {'name': 'Anadolu Feneri İleri Biyolojik Atık Su Arıtma Tesisi', 'lat':41.16278 , 'lon':29.26861 , 'detail':500, 'detail_2':2021},
        {'name': 'Ömerli /Orhaniye İçme Suyu Arıtma Tesisi', 'lat':40.99556 , 'lon':29.32333 , 'detail':550, 'detail_2':1978},
        {'name': 'Kâğıthane/Çelebi Mehmet İçme Suyu Arıtma Tesisi', 'lat':41.0925 , 'lon':28.96583 , 'detail':400, 'detail_2':1978},
        {'name': 'Büyükçekmece İçme Suyu Arıtma Tesisi', 'lat':41.04111 , 'lon':28.59111 , 'detail':400, 'detail_2':1989},
        {'name': 'Elmalı İçme Suyu Arıtma Tesisi', 'lat':41.07417 , 'lon':29.09639 , 'detail':40, 'detail_2':1956},
        {'name': 'İkitelli Fatih Sultan Mehmet İçme Suyu Arıtma Tesisi', 'lat':41.0875 , 'lon':28.76528 , 'detail':'', 'detail_2':1998},
        {'name': 'İkitelli II.Bayezid İçme Suyu Arıtma Tesisi', 'lat':41.0875 , 'lon':28.76528 , 'detail':400, 'detail_2':2003},
        {'name': 'Şile (Darlık) Ultrafiltrasyon Membran İçme Suyu Arıtma Tesisi', 'lat':41.12528 , 'lon':29.56861 , 'detail':20, 'detail_2':2022},
        {'name': 'Şile İçme Suyu Arıtma Tesisi', 'lat':41.15472 , 'lon':29.59611 , 'detail':11, 'detail_2':1994},
        {'name': 'Silivri Danamandıra İçme Suyu Arıtma Tesisi', 'lat':41.27917 , 'lon':28.23389 , 'detail':12, 'detail_2':2003},
        {'name': 'Taşoluk İçme Suyu Arıtma Tesisi', 'lat':41.22028 , 'lon':28.7075 , 'detail':100, 'detail_2':2005},
        {'name': 'Süleymanpaşa Batı İleri Biyolojik Atıksu Arıtma Tesisi', 'lat':40.98389 , 'lon':27.48556 , 'detail':40440, 'detail_2':2017},
        {'name': 'Sultanköy Biyolojik Atıksu Arıtma Tesisi', 'lat':41.02083 , 'lon':27.97778 , 'detail':720, 'detail_2':2012},
        {'name': 'Yeniçiftlik İleri Biyolojik Atıksu Arıtma Tesisi', 'lat':41.00778 , 'lon':27.82917 , 'detail':3000, 'detail_2':2006},
        {'name': 'Yenice Biyolojik Atıksu Arıtma Tesisi', 'lat':41.01583 , 'lon':27.7225 , 'detail':3000, 'detail_2':2003},
        {'name': 'TOKİ Biyodisk Atıksu Arıtma Tesisi', 'lat':41.01583 , 'lon':27.7225 , 'detail':800, 'detail_2':2010},
        {'name': 'Malkara İleri Biyolojik Atıksu Arıtma Tesisi', 'lat':40.89944 , 'lon':26.92306 , 'detail':7320, 'detail_2':2015},
        {'name': 'Saray İleri Biyolojik Atıksu Arıtma Tesisi', 'lat':41.42556 , 'lon':27.90917 , 'detail':7166, 'detail_2':2016},
        {'name': 'Çorlu İleri Biyolojik Atıksu Arıtma Tesisi', 'lat':41.07611 , 'lon':27.76861 , 'detail':60, 'detail_2':2017},
        {'name': 'Çerkezköy-Kapaklı İleri Biyolojik Atıksu Arıtma Tesisi', 'lat':41.26056 , 'lon':27.91944 , 'detail':52800, 'detail_2':2017},
        {'name': 'Marmaraereğlisi İçme Suyu Arıtma Tesisi', 'lat':40.975 , 'lon':27.91556 , 'detail':10000, 'detail_2':2007},
        {'name': 'Yeniçiftlik İçme Suyu Arıtma Tesisi', 'lat':41.00778 , 'lon':27.82917 , 'detail':1500, 'detail_2':2004},
        {'name': 'Tekirdağ İçme Suyu Arıtma Tesisi', 'lat':40.94722 , 'lon':27.44528 , 'detail':30000, 'detail_2':''},
        {'name': 'İzmit Plajyolu İleri Biyolojik Atıksu Arıtma Tesisi', 'lat':40.76111 , 'lon':29.88556 , 'detail':10, 'detail_2':''},
        {'name': 'Körfez Biyolojik Atıksu Arıtma Tesisi', 'lat':40.75389 , 'lon':29.775 , 'detail':45, 'detail_2':2004},
        {'name': 'Gölcük Yeniköy Biyolojik Atıksu Arıtma Tesisi', 'lat':40.7125 , 'lon':29.85556 , 'detail':600, 'detail_2':2004},
        {'name': 'Gebze İleri Biyolojik Atıksu Arıtma Tesisi', 'lat':40.80528 , 'lon':29.34972 , 'detail':2, 'detail_2':2011},
        {'name': 'Kandıra Cebeci İleri Biyolojik Atıksu Arıtma Tesisi', 'lat':41.18417 , 'lon':30.23944 , 'detail':9, 'detail_2':2013},
        {'name': 'Karamürsel Valideköprü Biyolojik Atıksu Arıtma Tesisi', 'lat':40.68417 , 'lon':29.55389 , 'detail':240, 'detail_2':2011},
        {'name': 'Dilovası İleri Biyolojik Atıksu Arıtma Tesisi', 'lat':40.80778 , 'lon':29.53056 , 'detail':25, 'detail_2':2017},
        {'name': 'Dilovası Köseler İleri Biyolojik Atıksu Arıtma Tesisi', 'lat':40.80778 , 'lon':29.53056 , 'detail':1000, 'detail_2':2019},
        {'name': 'Gölcük Siretiye İSU Tip – 200 İçme Suyu Arıtma Tesisi', 'lat':40.64361 , 'lon':29.83056 , 'detail':4800, 'detail_2':2014},
        {'name': 'Kartepe Suadiye İSU Tip – 200 İçme Suyu Arıtma Tesisi', 'lat':40.77278 , 'lon':30.22056 , 'detail':4800, 'detail_2':2013},
        {'name': 'Kartepe Maşukiye İSU Tip – 200 İçme Suyu Arıtma Tesisi', 'lat':40.77278 , 'lon':30.22056 , 'detail':4800, 'detail_2':2014},
        {'name': 'Yuvacık Barajı İçmesuyu Arıtma Tesisi', 'lat':40.67389 , 'lon':29.96917 , 'detail':389, 'detail_2':1999},
        {'name': 'Doğu Atıksu Arıtma Tesisi', 'lat':40.22917 , 'lon':29.08639 , 'detail':240, 'detail_2':2006},
        {'name': 'Batı Atıksu Arıtma Tesisi', 'lat':40.23972 , 'lon':28.91389 , 'detail':87.5, 'detail_2':2017},
        {'name': 'Karacabey Atıksu Arıtma Tesisi', 'lat':40.2225 , 'lon':28.37917 , 'detail':8500, 'detail_2':1993},
        {'name': 'Orhaneli Atıksu Arıtma Tesisi', 'lat':39.91722 , 'lon':28.97583 , 'detail':1000, 'detail_2':2015},
        {'name': 'Dobruca İçmesuyu Arıtma Tesisi', 'lat':40.18861 , 'lon':28.97583 , 'detail':500, 'detail_2':1985},
        {'name': 'Kartepe Avluburun İçmesuyu Arıtma Tesisi', 'lat':40.77278 , 'lon':30.22056 , 'detail':22500, 'detail_2':2003},
        {'name': 'Karamürsel Valideköprü İSU Tip - 100 İçme Suyu Arıtma Tesisi', 'lat':40.60333 , 'lon':29.52972 , 'detail':2400, 'detail_2':2013},
        {'name': 'Yalova İleri Biyolojik Atıksu Arıtma Tesisi', 'lat':40.65444 , 'lon':29.245 , 'detail':15000, 'detail_2':2012},
        {'name': 'Orhangazi Atıksu Arıtma Tesisi', 'lat':40.44444 , 'lon':29.33417 , 'detail':19.2, 'detail_2':2016},
        {'name': 'Karacabey Merkez İçmesuyu Arıtma Tesisi', 'lat':40.2225 , 'lon':28.37917 , 'detail':12.096, 'detail_2':1994},
        {'name': 'Mustafa Kemal Paşa Karadere İçmesuyu Paket Arıtma Tesisi', 'lat':40.01944 , 'lon':28.43417, 'detail':'', 'detail_2':''},
        {'name': 'Çanakale Atıksu Arıtma Tesisi', 'lat':40.14167 , 'lon':26.4725 , 'detail':21750, 'detail_2':''},
        {'name': 'Kepez Belediyesi Atıksu Arıtma Tesisi', 'lat':40.09528 , 'lon':26.38167, 'detail':'', 'detail_2':''},
        {'name': 'Çanakkale İçmesuyu Arıtma Tesisi', 'lat':40.1525 , 'lon':26.44167 , 'detail':100, 'detail_2':''},
        {'name': 'İvrindi Okullar Bölgesi Atıksu Arıtma Tesisi', 'lat':39.47056 , 'lon':27.49222 , 'detail':450, 'detail_2':''},
        {'name': 'Balıkesir Merkez Atıksu Arıtma Tesisi', 'lat':39.62111 , 'lon':27.95167 , 'detail':67117, 'detail_2':''},
        {'name': 'Erdek Ocaklar Atıksu Arıtma Tesisi', 'lat':40.39139 , 'lon':27.79639 , 'detail':2000, 'detail_2':''},
        {'name': 'Havran Büyükdere Atıksu Arıtma Tesisi', 'lat':39.4575 , 'lon':27.05 , 'detail':500, 'detail_2':''},
        {'name': 'Ayvalık Küçükköy Atıksu Arıtma Tesisi', 'lat':39.27722 , 'lon':26.63611 , 'detail':30000, 'detail_2':''},
        {'name': 'Sındırgı Atıksu Arıtma Tesisi', 'lat':39.25722 , 'lon':28.15361 , 'detail':5495, 'detail_2':''},
        {'name': 'Savaştepe Atıksu Arıtma Tesisi', 'lat':39.395 , 'lon':27.63833 , 'detail':3678, 'detail_2':''},
        {'name': 'Gönen Atıksu Arıtma Tesisi', 'lat':40.12389 , 'lon':27.65417 , 'detail':14679, 'detail_2':''},
        {'name': 'Edremit Zeytinli Atıksu Arıtma Tesisi', 'lat':39.56361 , 'lon':26.95694 , 'detail':23760, 'detail_2':''},
        {'name': 'İvrindi Atıksu Arıtma Merkezi', 'lat':39.47056 , 'lon':27.49222 , 'detail':1000, 'detail_2':''},
        {'name': 'İvrindi Büyükyenice Atıksu Arıtma Tesisi', 'lat':39.47111 , 'lon':27.49333 , 'detail':500, 'detail_2':''},
        {'name': 'Balıkesir Merkez İçmesuyu Arıtma Tesisi', 'lat':39.635 , 'lon':27.87194 , 'detail':220000, 'detail_2':''},
        {'name': 'Marmara Avşa Adası İçmesuyu Arıtma Tesisi', 'lat':40.51806 , 'lon':27.4975 , 'detail':6000, 'detail_2':''}

     #Other water related facilities...
]   

fac_2 = [
	{'name': 'Kemerburgaz Atık Yakma ve Enerji Üretim Tesisi', 'lat': 41.22444, 'lon': 28.81472},
        {'name': 'Kemerburgaz Biyometaniyonizasyon Tesisi', 'lat': 41.22361 , 'lon': 28.8225},
        {'name': 'Odayeri Enerji Üretim Tesisi', 'lat': 41.21667 , 'lon': 28.85333},
        {'name': 'Seymen Enerji Üretim Tesisi', 'lat': 41.21833, 'lon': 28.16306 },
        {'name': 'Kemerburgaz Atıktan Türetilmiş Yakıt Tesisi', 'lat': 41.22167, 'lon': 28.81917},
        {'name': 'Kemerburgaz Geri Kazanım ve Kompost Tesisi', 'lat': 41.22139 , 'lon': 28.81972},
        {'name': 'Metan Gazından Elektrik Üretim Tesisi', 'lat': 40.18361, 'lon': 29.10333},
        {'name': 'Tehlikeli Atık Yakma Tesisi', 'lat': 40.78722, 'lon': 30.02500},
        {'name': 'Biyogaz Tesisi', 'lat': 40.78778 , 'lon': 30.02639},
        {'name': 'LFG Enerji Üretim Tesisi', 'lat': 40.78889 , 'lon': 30.02583},
        {'name': 'Hidroelektrik Santrali(HES)', 'lat': 40.78972 , 'lon': 30.02583}



    #Other energy related facilities...
]

fac_3 = [
	{'name': 'Baruthane Aktarma İstasyonu', 'lat': 41.04917, 'lon': 28.96861},
        {'name': 'Yenibosna Aktarma İstasyonu', 'lat': 40.99722, 'lon': 28.82361},
        {'name': 'Silivri Aktarma İstasyonu', 'lat': 41.10111, 'lon': 28.2175},
        {'name': 'Başakşehir Aktarma İstasyonu', 'lat': 41.14639, 'lon': 28.77861},
        {'name': 'Hekimbaşı Aktarma İstasyonu', 'lat': 41.05833, 'lon': 29.1125},
        {'name': 'Aydınlı Aktarma İstasyonu', 'lat': 40.86111, 'lon': 29.34722},
        {'name': 'K.Bakkalköy Aktarma İstasyonu', 'lat': 40.985, 'lon': 29.13056},
        {'name': 'Odayeri Düzenli Depolama Alanı', 'lat': 41.21639, 'lon': 28.85389},
        {'name': 'Silivri Seymen Düzenli Depolama Alanı', 'lat': 41.15639, 'lon': 28.16667},
        {'name': 'Kömürcüada Düzenli Depolma Alanı', 'lat': 41.18167, 'lon': 29.35111},
        {'name': 'Eyüpsultan-Odayeri Entegre Atık Yönetimi Tesisleri', 'lat': 41.21639, 'lon': 28.85389},
        {'name': 'Şile-Kömürcüoda Entegre Atık Yönetimi Tesisleri', 'lat': 41.14194, 'lon': 29.36917},
        {'name': 'Silivri-Seymen Entegre Atık Yönetimi Tesisleri', 'lat': 41.2175, 'lon': 28.14556},
        {'name': 'Asyaport Liman A.Ş. Vahşi Depolama Sahası', 'lat': 40.88194, 'lon': 27.46028},
        {'name': 'Yolaş Madencilik İnş. Taah. İşleri San. ve Tic. A.Ş. Vahşi Depolama Sahası', 'lat': 41.05056, 'lon': 27.41833},
        {'name': 'Kardeşoğulları Hafriyat İnşaat San. ve Tic. Ltd. Şti. Vahşi Depolama Sahası', 'lat': 41.12806, 'lon': 27.46667},
        {'name': 'Baztaş Madencilik İnş. San. Tic. A.Ş.Vahşi Depolama Sahası', 'lat': 41.09222, 'lon': 27.60778},
        {'name': 'Karta Madencilik San. ve Tic. Ltd. Şti. Vahşi Depolama Sahası', 'lat': 41.06889, 'lon': 27.73389},
        {'name': 'Çerkezköy-Veliköy Vahşi Depolama Sahası', 'lat': 41.25778, 'lon': 27.93694},
        {'name': 'Kapaklı-Uzunhancı Köy İçi Yolları Vahşi Depolama Sahası', 'lat': 41.34306, 'lon': 27.83306},
        {'name': 'Asyaport Liman A.Ş. Vahşi Depolama Sahası', 'lat': 40.90139, 'lon': 27.46722},
        {'name': 'Hayrabolu Atık Getirme Merkezi (Aktif)', 'lat': 41.21222, 'lon': 27.10556},
        {'name': 'Şarköy Atık Getirme Merkezi (Aktif)', 'lat': 40.51389, 'lon': 26.90056},
        {'name': 'Süleymanpaşa Atık Getirme Merkezi (Pasif)', 'lat': 40.99889, 'lon': 27.47806},
        {'name': 'Ergene Atık Getirme Merkezi(Aktif)', 'lat': 41.17944, 'lon': 27.76444},
        {'name': 'Çerkezköy Atık Getirme Merkezi(Aktif)', 'lat': 41.28056, 'lon': 27.995},
        {'name': 'Kapaklı Atık Getirme Merkezi(Aktif)', 'lat': 41.33139, 'lon': 27.96472},
        {'name': 'Çayırova,Mustafa Kemal cd. Atık Getirme Merkezi', 'lat': 40.86528, 'lon': 29.375},
        {'name': 'Osmangazi, Aşıroğlu cd.Atık Getirme Merkezi', 'lat': 40.79056, 'lon': 29.37361},
        {'name': 'Derince Atık Getirme Merkezi', 'lat': 40.76333, 'lon': 29.82833},
        {'name': 'Başiskele,Ezgi cd. Atık Getirme Merkezi', 'lat': 40.7375, 'lon': 29.99167},
        {'name': 'Kartepe, Bağdat cd. Atık Getirme Merkezi', 'lat': 40.72944, 'lon': 30.02611},
        {'name': 'Körfez Atık Getirme Merkezi', 'lat': 40.75, 'lon': 29.79528},
        {'name': 'Gebze, Hükümet cd. Atık Getirme Merkezi', 'lat': 40.79861, 'lon': 29.44639},
        {'name': 'İzmit, Çarşıbaşı cd. Atık Getirme Merkezi', 'lat': 40.78917, 'lon': 29.99639},
        {'name': 'Dilovası Düzenli Depolama Sahası', 'lat': 40.79389, 'lon': 29.52111},
        {'name': 'Denizçalı Düzenli Dpolama Sahası', 'lat': 40.63972, 'lon': 29.43167},
        {'name': 'Ambalaj Atığı Toplama Ayırma Tesisi', 'lat': 40.62361, 'lon': 29.27528},
        {'name': 'Tehlikesiz Atık Toplama Ayırma Tesisi', 'lat': 40.62444, 'lon': 29.27667},
        {'name': 'Yenikent Katı Atık Düzenli Depolama Alanı', 'lat': 40.27306, 'lon': 28.97028},
        {'name': 'İnegöl Katı Atık Düzenli Depolama Alanı', 'lat': 40.14778, 'lon': 29.58278},
        {'name': 'Ambalaj Atıkları Toplama Ayırma Tesisi', 'lat': 40.15889, 'lon': 26.43528},
        {'name': 'Çanakkale Katı Atık Düzenli Depolama Tesisi', 'lat': 40.17722, 'lon': 26.54278},
        {'name': 'Ayvalık Aktarma Merkezi', 'lat': 39.32139, 'lon': 26.69778}
       

	    #Other solid waste related facilities...
]


#Creating the map
marmara_region_map = folium.Map(location=[40.63, 28.12], tiles='Cartodb Positron', zoom_start=8)

#Add minimap
MiniMap(toggle_display=True).add_to(marmara_region_map)

#Setting the boundaries
bounds = [[40.0, 26.5], [41.5, 30.0]]
marmara_region_map.fit_bounds(bounds)

#Adding first type of facilities to the marmara region map
for facility in fac:
    folium.Marker(
        location=[facility['lat'], facility['lon']],
        #popup=folium.Popup(facility['detail'], max_width=200),  #Balloon that opens when clicked
        popup=folium.Popup(f"<b>{facility['name']}</b><br><b>Kapasite:</b> {str(facility['detail'])} (m<sup>3</sup>/gün)<br><b>Hizmete Giriş Yılı:</b> {facility['detail_2']}", max_width=200), #Balloon that opens when clicked
        icon=folium.Icon(color = 'blue', icon = 'tint', prefix = 'glyphicon'),
        tooltip=facility['name'],  #Note balloon that appears when hovering over it with the mouse
    ).add_to(marmara_region_map)

#Adding second type of facilities to the marmara region map
for fa in fac_2:
    folium.Marker(
        location=[fa['lat'], fa['lon']],
        #popup=folium.Popup(fa['detail'], max_width=200),  #Balloon that opens when clicked
        icon=folium.Icon(color = 'lightgray', icon = 'info-sign', prefix = 'glyphicon'),
        tooltip=fa['name'],  #Note balloon that appears when hovering over it with the mouse
    ).add_to(marmara_region_map)

#Adding third type of facilities to the marmara region map
for f in fac_3:
    folium.Marker(
        location=[f['lat'], f['lon']],
        #popup=folium.Popup(f['detail'], max_width=200),  #Balloon that opens when clicked
        icon=folium.Icon(color= 'green', icon = 'trash', prefix = 'glyphicon'),
        tooltip=f['name'],  #Note balloon that appears when hovering over it with the mouse
    ).add_to(marmara_region_map)

# Creating a custom legend
legend_html = '''
<div style="position: fixed;
            top: 25px; right: 25px; width: 250px; height: 80px;
            background-color: white; z-index:9999; font-size:10px;
            border:2px white; padding: 10px;">
    <i class="fa fa-tint" style="color:blue"></i> Atıksu ve İçme Suyu Arıtma Tesisleri<br>
    <i class="fa fa-trash" style="color:green"></i> Atık Yönetimi Tesisleri<br>
    <i class="fa fa-info-circle" style="color:lightgray"></i> Enerji Üretimi Tesisleri
</div>
'''
marmara_region_map.get_root().html.add_child(folium.Element(legend_html))

#Saving the map
marmara_region_map.save("marmara_waste_facilities_map.html")