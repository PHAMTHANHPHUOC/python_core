class Ngay:
    #constructor
    def __init__(self,ngay,thang,nam):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam
    #xác định số ngày của tháng
    @staticmethod
    def soNgayCuaThang(thang,nam):
        if(thang in [1,3,5,7,8,10,12]):
            return 31
        elif(thang in [4,6,9,11]):
            return 30
        elif(thang == 2):
            # return ((nam % 400 == 0)|| (nam%4==0 && nam %100 != 0))?29:28;
            if (nam % 400 == 0 or (nam%4==0 and nam %100 != 0)):
                return 29
            else:
                return 28

    def ngayTrongNam(self):
        giatringaytrongnam = 0
        #tính tổng số lượng ngày của những tháng trước
        for x in range(1,self.thang):
            giatringaytrongnam += self.soNgayCuaThang(x,self.nam)
        # cộng thêm số ngày của tháng hiện tại
        giatringaytrongnam+=self.ngay
        #trả kêt quá
        return giatringaytrongnam
NgayA = Ngay(15,3,2022)
print(NgayA.ngayTrongNam())
