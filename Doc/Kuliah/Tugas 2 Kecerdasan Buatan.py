graph = {
	             'Pinrang': ['Alacalimpo'],
	             'Alacalimpo': ['Tiroang'],
	             'Tiroang ': ['Marawi'],
	             'Marawi': ['Arassie'],
	             'Arassie': ['Wattang Simpo'],
	             'Wattang Simpo': ['Simpo'],
	             'Simpo': ['Padacenga'],
	             'Padacenga': ['Sidrap'],        
	        }
	

	def rutepalingpendek(graph, lokasi_awal, lokasi_tujuan, rute=[]):
	        rute = rute + [lokasi_awal]
	        if lokasi_awal == lokasi_tujuan:
	            return rute
	            if not graph.has_key(lokasi_awal):
	                    return None
	        rutependek = None
	        for node in graph[lokasi_awal]:
	            if node not in rute:
	                rutebaru = rutepalingpendek(graph, node, lokasi_tujuan, rute)
	                if rutebaru:
	                    if not rutependek or len(rutebaru) < len(rutependek):
	                        rutependek = rutebaru
	        return rutependek
	print("Rute Jalan Raya Pinrang sampai Sidrap")
	print("(Pinrang-Alacalimpo-Tiroang-Marawi-Arassie-Wattang-Simpo-Simpo-Padacenga)")
	print("Muh Akbar Tamrin-1144012")
	print("\n")
	lokasi_awal = raw_input("Masukan Lokasi Awal : ")
	lokasi_tujuan = raw_input("Masukan Lokasi Tujuan : ")
	hasilnya = rutepalingpendek(graph, lokasi_awal, lokasi_tujuan, rute=[])
	print "Rute Terpendek", hasilnya ,".",

