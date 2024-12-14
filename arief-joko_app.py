''' 
=================================================

Nama  : Arief Joko Wicaksono

Program ini adalah program shoping cart yang dapat digunakan oleh user untuk menambah, menghapus, dan melihat barang di keranjang belanja (cart) mereka. Tiap barang memiliki informasi nama barang dan harganya. User juga bisa melihat total harga belanjanya.
=================================================
'''

def management_cart():
    '''
    Program ini digunakan untuk mengelola keranjang belanja oleh user. Di dalam program user dapat menambah, menghapus, menampilkan isi keranjang belanja serta dapat mengetahui total harga barang yang sudah masuk dalam keranjang
    '''
    print('\nSelamat Datang di Keranjang Belanja Toko Makmur!')
    list_keranjang = []
    def input_barang(teks):
        '''
        fungsi ini digunakan untuk mengambil input user berupa nama barang. fungsi ini memiliki argumen berupa teks sebagai perlakuan terhadap nilai input dari user apakah input akan ditambah atau dihapus. fungsi akan menjalakan code untuk meminta input dari user , dan nilai input akan di return oleh fungsi. Argumen dalam fungsi ini digunakan untuk pembeda kalimat perintah untuk user.
        '''
        if teks == 'tambah':
            barang =''
            while not barang: #kode ini mencegah user tidak memasukkan nama barang, akan berulang sampai nama barang diinput
                barang = input('Masukkan nama barang: ')
            if not barang: #alert jika tidak ada input 
                print('Anda belum memasukan nama barang')
            return barang
        elif teks == 'hapus':
            barang =''
            while not barang: #kode ini mencegah user tidak memasukkan nama barang, akan berulang sampai nama barang diinput
                barang = input('Masukan nama barang yang ingin dihapus ')
            if not barang: #alert jika tidak ada input 
                print('Anda belum memasukan nama barang')
            return barang
    def input_harga():
        '''
        fungsi ini berguna untuk mendapatkan nilai input data dari user dan akan memvalidasi apakah harga yang dimasukkan sudah benar berupa angka
        '''
        harga = ''
        while not harga: #kode ini mencegah user tidak memasukkan harga, akan berulang sampai harga diinput
            harga = input(f"Masukkan harga: ")
            if not harga: #alert jika tidak ada input dari user
                print('Anda belum memasukan harga')
            elif not harga.isdigit(): #pengecekan apakah harga inpun benar berupa angka kalau salah akan mengulang lagi
                print('Harga yang anda masukkan salah')
                harga ='' #mengembalikan harga ke nilai semula agar program diulang
        harga=int(harga)
        return harga
    def mengecek_keranjang_kosong(list):
        '''
        fungsi ini digunakan untuk mengecek apakah sebuah list memiliki isi atau tidak. fungsi menerima input berupa list, lalu output akan berupa boolean yang akan digunakan untuk step code setelahnya
        '''
        if not list:
            print('\nBelum ada barang di dalam keranjang') 
            input('\nPress enter to return home')
            return True  #menyatakan keranjang kosong
        return False  #menyatakan keranjang isi
    def menghapus_barang(barang,list):
        '''
        fungsi ini bertujuan untuk menghapus data yang berada disuatu list. fungsi ini menerima argument berupa barang sebagai data yang akan dihapus dan juga list. data barang akan dicek apakah berada dalam list atau tidak, jika ada maka barang akan dihapus dari list. jika tidak fungsi akan mereturn boolean untuk alrt 
        '''
        for data in list: #iterasi data dalam list
            if data['nama_barang']==barang: #mengecek apakah data input berada dalam list keranjang dengan key berupa nama barang.
                return list.remove(data) #menggunakan method remove pada list untuk data yang sesuai
        return True
    def melihat_isi_keranjang(list):
        '''
        fungsi ini digunakan untuk menampilakan isi list supaya dapat terbaca dengan mudah oleh user. fungsi memiliki argument input berupa list.
        '''
        i=0
        for data in list: #iterasi data dalam list
            print(f"{i}. {data['nama_barang'].capitalize()} - Rp {data['harga']}.00")
            i+=1
    def menghitung_total_harga(list):
        '''
        fungsi ini digunakan untuk mencari harga total dari barang barang yang sudah user tambahkan ke dalam keranjang. fungsi memiliki argument berupa list dari keranjang
        '''
        total_harga = 0
        for data in list_keranjang:#iterasi data
            total_harga += data['harga'] #menjumlah harga
        return total_harga

    while True: #kode ini digunakan untuk menampilkan menu utama berulang hingga user ingin keluar (braek)
        #menu utama aplikasi
        print('\nMenu:')
        print('1. Menambah Barang')
        print('2. Hapus Barang')
        print('3. Tampilkan Barang di Keranjang')
        print('4. Lihat Total Belanja')
        print('5. Exit\n')

        pilihan = input('Pilihan : ')#mengambil input user untuk pilihan di menu utama
        
        if pilihan == '1':
            barang = input_barang('tambah') #memanggil fungsi input barang sebagi tembah
            harga = input_harga()
            list_keranjang.append({'nama_barang':barang,'harga':harga})#menambahkan barang dan harganya ke dalam list keranjang, ditambahkan dalam bentuk dictionary
            print(f'Barang "{barang.capitalize()}" berhasil dimasukkan ke keranjang')
            
        elif pilihan == '2':
            if mengecek_keranjang_kosong(list_keranjang): #menampilkan pesan jika keranjang masih kosong.
                continue
            barang = input_barang('hapus') #memanggil fungsi input barang sebagai penghapus
            if not menghapus_barang(barang, list_keranjang): #memanggil fungsi menghapus_barang sekaligus conditional pesan ke user apakah penghapusan berhasil atau tidak
                print(f'Barang "{barang.capitalize()}" berhasil dihapus di keranjang belanja.')
            else:
                print(f'Tidak ada {barang} di dalam keranjang')
            
        elif pilihan == '3':
            if mengecek_keranjang_kosong(list_keranjang):#pengecekan dan pemberitahuan kepada user jika keranjang masih kosong
                continue
            print('Barang di Keranjang')
            melihat_isi_keranjang(list_keranjang)#memanggil fungsi melihat_isi_keranjang

        elif pilihan == '4':
            total_harga = 0
            if mengecek_keranjang_kosong(list_keranjang):#pengecekan dan pemberitahuan kepada user jika keranjang masih kosong
                continue
            total_harga=menghitung_total_harga(list_keranjang)#memnggil fungsi menghitung total dan menyimpan ke dalam variable
            print(f'Total belanja: Rp. {total_harga}.00')
        
        elif pilihan == '5':
            print("Sampai Jumpa! Terima kasih sudah belanja di Toko Makmur.")
            break
        
        else: #digunakan jika input user tidak sesuai atau salah
            print('Pilihannya salah. Coba lagi ya.')

if __name__ == "__main__":
    management_cart()