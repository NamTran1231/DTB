# Danh sách sinh viên và điểm các môn
sinh_vien = ["John", "Bjonn", "Steves", "Wolfgang"]
diem_toan = [7, 8, 9, 10]
diem_ly = [6.5, 7.5, 9.5, 6.7]
diem_hoa = [5, 6, 7, 8]

# Lấy tên sinh viên thứ 3
name = sinh_vien[2]
print("Tên sinh viên thứ 3:", name)

# In tên sinh viên thứ 4 và điểm hóa của họ
print(f"{sinh_vien[3]} có điểm Hóa: {diem_hoa[3]}")

# Tính và in điểm trung bình của sinh viên thứ nhất
dtb = (diem_toan[0] + diem_ly[0] + diem_hoa[0]) / 3
print(f"Điểm trung bình của {sinh_vien[0]}: {dtb:.2f}")

# In danh sách sinh viên cùng điểm các môn
for i in range(len(sinh_vien)):
    dtb = (diem_toan[i] + diem_ly[i] + diem_hoa[i]) / 3
    print(f"{sinh_vien[i]} có điểm Toán: {diem_toan[i]}, Lý: {diem_ly[i]}, Hóa: {diem_hoa[i]} và điểm trung bình: {dtb:.2f}") #2f de in 2 chu so sau dau phay
