import datetime
import math

def bolehCuti(cuti_bersama, tanggal_join, tanggal_cuti, duration):
    CUTI_KANTOR = 14
    NEW_INVALID = 180
    
    date_format= "%Y-%m-%d"
    date_join = datetime.datetime.strptime(tanggal_join, date_format)
    date_valid = date_join + datetime.timedelta(days = NEW_INVALID)
    date_cuti = datetime.datetime.strptime(tanggal_cuti, date_format)
    #date_31dec = datetime.datetime(datetime.datetime.now().year, 12, 31)
    #alternative to find 31 december of the current year
    #since the question mentions 2021, I had to hardcore 2021 in
    date_31dec = datetime.datetime(2021, 12, 31)

    cuti_pribadi_yearly = CUTI_KANTOR - cuti_bersama
    cuti_pribadi = math.floor(cuti_pribadi_yearly * min((date_31dec-date_valid).days/365, 1))
    #count days from valid day to 31dec of current year
    #if employee has been valid for more than one year, min returns 1, hence cuti_pribadi will be the same as cuti_pribadi_yearly

    if(int((date_cuti-date_valid).days) < 0):
        print("Alasan: Karena belum 180 hari sejak tanggal join karyawan")
        return False
    if(cuti_pribadi < duration):
        print("Alasan: Karena hanya boleh mengambil {} hari cuti".format(cuti_pribadi))
        return False
    if(duration > 3):
        print("Alasan: Cuti pribadi max 3 hari berturutan.")
        return False
    return True

print(bolehCuti(7, "2021-05-01", "2021-07-05", 1))
print(bolehCuti(7, "2021-05-01", "2021-11-05", 3))
print(bolehCuti(7, "2021-01-05", "2021-12-08", 1))
print(bolehCuti(7, "2021-01-05", "2021-12-08", 3))