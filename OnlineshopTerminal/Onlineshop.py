from collections import defaultdict

data_product = {
    1: "YSB Alpha Arbutin 3% + Grapeseed", 
    2: "YSB Niacinamide 12% + Centella Asiatica",
    3: "YSB Salyclic Acid 2% + Zinc",
    4: "YSB Marine Collagen 10% + Ginseng Root",
    5: "YSB Ultimate Hyaluron HYACROSS 3% + Green Tea",
    6: "YSB Azeclair 10% + Kombucha 3% + Niacinamide 2,5% Vaccine Serum",
    7: "YSB Lactic Acid 10% + Kiwi Fruit 5% + Niacinamide 2,5% High Dose Serum",
    8: "YSB Vitamin C 3% + Niacinamide 2% + Mandarin Orange Fruit Extract",
    9: "YSB Panthenol 5% + Mugwort + Cica Barrier Hero Serum"
}

daftar_harga = {
    1: 120000, 
    2: 120000, 
    3: 139000,
    4: 120000,
    5: 120000,
    6: 149000,
    7: 129000,
    8: 120000,
    9: 139000
}

data_toko = {
    "nama": "Apotik Marina", 
    "alamat": "jl jaksa", 
    "telp": "1312312"
}


keranjang_belanja_barang = []
keranjang_belanja_jumlah = []
keranjang_belanja_subtotal = []


def nested_dict(n, type):
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: nested_dict(n-1, type))

data_pelanggan = nested_dict(2, float)
data_pesanan = nested_dict(4, float)

def databarang():
    print("Data Barang Yang Tersedia:");
    for i in range(1,9):
        print("NO/ID :",i," Nama Barang : ",data_product[i]," Harga :",daftar_harga[i]);

def datakeranjang():
    lendata=len(keranjang_belanja_barang);
    print("Data Keranjang Barang  :");
    print '-----------------------------------';
    for i in range(0,lendata):
        print(keranjang_belanja_barang[i]," Jumlah :",keranjang_belanja_jumlah[i]," Subtotal :",keranjang_belanja_subtotal[i]);
    
    print '-----------------------------------';


def menu():
    print '-----------------------------------';
    print '          ONLINE SHOP SYSTEM';
    print '-----------------------------------';
    print '1. Print Data Barang ';
    print '2. Pesan Barang/Input Barang ke Keranjang ';
    print '3. Print Data Keranjang Pesanan ';
    print '4. Checkout Keranjang Pesanan ';
    print '5. Print Data Pesanan';
    print '6. Exit';
    print '-----------------------------------';
    return int(raw_input())

loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        databarang();    
    if choice == 2:
        databarang();
        print 'Pilih ID/No Barang Yang di pesan';
        idbarang=int(raw_input());
        if idbarang>0 and idbarang<=9 :
            keranjang_belanja_barang.append(idbarang);
            print "Masukan Jumlah ",data_product[idbarang]," Yang di pesan";
            jumlahbarang=int(raw_input());
            keranjang_belanja_jumlah.append(jumlahbarang);
            hargabarang=daftar_harga[idbarang];
            subtotal=hargabarang*jumlahbarang;
            keranjang_belanja_subtotal.append(subtotal);
            print "Subtotal : ",data_product[idbarang]," Yang di pesan :",subtotal;
            print 'Berhasil Input di Keranjang Belanja';
        else:
            print 'ID/No Barang Tidak Ada';
    if choice == 3:
        datakeranjang();
    if choice == 4:
        print 'Processing Checkout';
        print 'Input Nama Pemesan';
        namapemesan=int(raw_input());  
        print 'Alamat pemesan';
        alamatpemesan=int(raw_input());
        print 'Telp Pemesan';
        telppemesan=int(raw_input()); 
        
        data_pelanggan[namapemesan]['alamat']=

        keranjang_belanja_barang.clear();
        keranjang_belanja_jumlah.clear();
        keranjang_belanja_subtotal.clear();
    elif choice == 6:
        loop = 0
