#dewi paramithasari

bulan_hari = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

bulan_hari_kabisat = {
    1:31,
    2:29,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

tahun1,bulan1,tanggal1 = input().split("-")
tahun1,bulan1,tanggal1 = int(tahun1),int(bulan1),int(tanggal1)
tahun2,bulan2,tanggal2 = input().split("-")
tahun2,bulan2,tanggal2 = int(tahun2),int(bulan2),int(tanggal2)


## kondisi 1: tahun1 dan tahun2 adalah tahun kabisat ##
if (tahun1 % 4 == 0) and (tahun2 % 4 == 0):
    bulan1_ke_tanggal1 = int()
    bulan2_ke_tanggal2 = int()
    for i in range(1,bulan1):
        bulan1_ke_tanggal1 += bulan_hari_kabisat[i]
    for j in range(1,bulan2):
        bulan2_ke_tanggal2 += bulan_hari_kabisat[j]
    total1 = bulan1_ke_tanggal1 + tanggal1
    total2 = bulan2_ke_tanggal2 + tanggal2
    
    selisih = total2 - total1
    print(selisih,"hari")

if (tahun1 % 4 != 0) and (tahun2 % 4 != 0):
    bulan1_ke_tanggal1 = int()
    bulan2_ke_tanggal2 = int()
    for i in range(1,bulan1):
        bulan1_ke_tanggal1 += bulan_hari[i]
    for j in range(1,bulan2):
        bulan2_ke_tanggal2 += bulan_hari[j]
    total1 = bulan1_ke_tanggal1 + tanggal1
    total2 = bulan2_ke_tanggal2 + tanggal2
    
    selisih = total2 - total1
    print(selisih,"hari")