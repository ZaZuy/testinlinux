class Leetcode4():
    def dayOfYear(self, dd, mm, yy):
        leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        common_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if yy > 0:
            if yy % 4 == 0:
                if mm < 12:
                    if dd <= leap_year[mm - 1]:
                        return dd + leap_year[mm - 1]
                    else:
                        print("Undefined date")
                else:
                    print("Undefined month")
            else:
                if mm < 12:
                    if dd <= common_year[mm - 1]:
                        return dd + common_year[mm - 1]
                    else:
                        print("Undefined date")
                else:
                    print("Undefined month")
        else:
            print("Undefined year")
Leetcode4 = Leetcode4()
print("Day of the Year",Leetcode4.dayOfYear(18,3,2024))