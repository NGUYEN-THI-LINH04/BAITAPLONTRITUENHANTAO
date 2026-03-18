# BAITAPLONTRITUENHANTAO
# Link youtube
https://youtu.be/X1LCfPGrDl4
# HƯỚNG DẪN CÀI ĐẶT VÀ CHẠY CHƯƠNG TRÌNH
### 🔹 Bước 1: Cài đặt Anaconda
- Truy cập: https://www.anaconda.com
- Tải và cài đặt Anaconda
- Sau khi cài xong, mở Anaconda Prompt
### 🔹 Bước 2: Tạo môi trường Python 3.10
- Nhập lệnh sau:
- conda create -n ai_env python=3.10
→ Nhấn y để xác nhận cài đặt
### 🔹 Bước 3: Kích hoạt môi trường
- conda activate ai_env
→ Nếu thấy (ai_env) phía trước dòng lệnh là thành công
### 🔹 Bước 4: Cài đặt các thư viện cần thiết
- Nhập lần lượt các lệnh:
<pre>'''pip install tensorflow
pip install flask
pip install pillow
pip install numpy
pip install matplotlib
pip install seaborn
pip install scikit-learn '''</pre>

### 🔹 Bước 5: Mở thư mục chứa project
- Ví dụ project nằm ở ổ D:
- cd D:\Phanloaichomeo
### Hướng dẫn chạy chương trình 
### Bước 1: Vào Pycharm chọn vào new project rồi đặt tên và chọn conda rồi chọn môi trường ai_env
<img width="1263" height="899" alt="image" src="https://github.com/user-attachments/assets/6ea5dd7f-cf54-4f28-9b51-4d6d63ccb7d7" />

### 🔹 Bước 6: Tạo thư mục dataset và cho ảnh mèo và cho vào từng thư mục của mỗi ảnh 
- Đảm bảo thư mục dataset có dạng:
<pre>''' dataset/
 ├── train/
 │    ├── cats/
 │    └── dogs/
 ├── validation/
      ├── cats/
      └── dogs/''' </pre>     
      
### 🔹 Bước 2: Huấn luyện mô hình (train model)
- Chạy lệnh:
- python src/train.py
→ Sau khi chạy xong sẽ tạo file:
- models/mobilenet_dog_cat.h5
  
### 🔹 Bước 3: Tạo thư mục lưu ảnh upload
- mkdir static/uploads
  
### 🔹 Bước 4: Chạy chương trình
- python main.py
→ Nếu thành công sẽ hiển thị:
- Running on http://127.0.0.1:5000/
  
### 🔹 Bước 5: Mở trình duyệt và sử dụng
- Truy cập: http://127.0.0.1:5000/
- → Thực hiện:
- Upload ảnh
- Nhận kết quả phân loại (Chó / Mèo)
- Xem lịch sử
