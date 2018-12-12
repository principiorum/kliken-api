import re
from pandas import Timestamp

bulan = {'Januari': 1,'Februari': 2, 'Maret':3, 'April':4, 'Mei':5, 'Juni': 6, 'Juli': 7, 'Agustus':8, 'September':9, 'Oktober':10, 'November': 11, 'Desember':12}
bulan2 = {'Jan': 1,'Feb': 2, 'Mar':3, 'Apr':4, 'Mei':5, 'Jun': 6, 'Jul': 7, 'Agu':8, 'Sep':9, 'Okt':10, 'Nov': 11, 'Des':12}
hari = ['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu']
hari2 = ['Monday','Thursday', 'Wednesday','Tuesday', 'Friday','Saturday', 'Sunday']
hari3 = ['Mon','Thu', 'Wed','Tue', 'Fri','Sat', 'Sun']

def cln(tm):
	tm = re.sub('[,|]','',tm)
	at1 = tm.replace('WIB', '').strip()
	at2 = ' '.join([i for i in at1.split() if i not in hari and hari2 and hari3])
	at3 = ' '.join(str(bulan.get(word, word)) for word in at2.split())
	at4 = ' '.join(str(bulan2.get(word, word)) for word in at3.split())
	return str(Timestamp(at4))