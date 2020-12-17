from method import *
optinals = '''
    1. Add student
    2. Remove student
    3. Update student
    4. View all student
    5. View all student after sort by point
    6. Exit
'''

actionOptional = dict()
actionOptional["1"] = ThemSinhvien
actionOptional["2"] = XoaTenMotSinhvien
actionOptional["3"] = CapNhatThongTTSV
actionOptional["4"] = HienThiTTSV
actionOptional["5"] = HienthisauSapxep

print("    CHAO MUNG TOI CHUONG TRINH")
while True:
    print(optinals)
    print("Nhap lua chon: ", end="")
    optinal = input()
    if optinal == "6":
        print("Cam on da su dung")
        break
    if optinal not in actionOptional:
        print("Xin chon lai")
    else:
        actionOptional[optinal]()
