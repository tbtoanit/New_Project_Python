import re

data= 'A4%'
pt1='[A-Z]' #Kiểm tra chữ hoa
pt2='[0-9]{3}' #Kiểm tra 3 số liên tiếp
pt2_1='[0-9]{1}' #Kiểm tra ít nhất 1 số
pt3='\W' ##Kiểm tra ký tự đặc biệt

a_viet_hoa = re.findall(pt1,data)
a_3_so_lien_tiep= re.findall(pt2,data)
a_chu_so= re.findall(pt2_1,data)
a_ky_tu_dac_biet= re.findall(pt3,data)
if len(a_viet_hoa)==0:
    print('Mật khẩu không có ít nhất một chữ in hoa')
if len(a_ky_tu_dac_biet)==0:
    print('Mật khẩu không có ít nhất một ký tự đặc biệt')
    exit()
if len(a_3_so_lien_tiep)!=0:
    print('Mật có 3 số liên tiếp')
    exit()
elif len(a_chu_so)==0:
    print('Mật khẩu không có số')
    exit()
# print(data) #Removing this code based on the requirement.
#Add the final line
