class HinhChuNhat:
    def __init__(self,dai=0.0,rong=0.0):
        self.dai=dai
        self.rong=rong
    
    def set(self,dai,rong): # Dat kich thuoc cho HCN
        self.dai=dai
        self.rong=rong

    def get(self): # Lay kich thuoc HCN
        return 'Chieu dai: '+str(self.dai)+\
               '\nChieu rong: '+str(self.rong)
 
    def dientich(self):
        return self.dai*self.rong

    def chuvi(self):
        return (self.dai+self.rong)*2
   
    def to_string(self):
        s=self.get()
        s=s+'\nChu vi hinh chu nhat: '+str(self.chuvi())+\
            '\nDien tich: '+str(self.dientich())+'\n'
        return s

    # Ghi ra file
    def ghifile(self,tenfile):
        f=open(tenfile,'w')
        f.write(self.to_string())
        f.close()

def HCN():
    dai = float(input("Nhap chieu dai hinh chu nhat:"))
    rong = float(input("Nhap chieu rong hinh chu nhat:"))
    hcn=HinhChuNhat(dai,rong)
    print(hcn.to_string())
    hcn.set(dai,rong)
    print(hcn.to_string())
    hcn.ghifile('D:\Lecture Materials\OOP with Python\Python Practice\Python Class\hcn.txt')

HCN()