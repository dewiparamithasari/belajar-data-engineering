#dewi paramithasari

harga_per_tiket = 5000
jumlah_tiket_terjual = 100
lokasi_pemutaran_film = "Jakarta", "Surabaya"

def informasi_transaksi_bioskop (nama_film, jumlah_tiket_terjual, total_pendapatan, lokasi_pemutaran_film):
    print ("Tiket film", nama_film, "terjual sebanyak", jumlah_tiket_terjual, "dengan total pendapatan Rp", total_pendapatan, "di", lokasi_pemutaran_film)

informasi_transaksi_bioskop ("Spiderman", (jumlah_tiket_terjual), (harga_per_tiket*jumlah_tiket_terjual), (lokasi_pemutaran_film))