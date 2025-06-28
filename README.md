<div align="center">

  # 🌐 Django Web Project

  <img src="https://github.com/HitDrama/Project-Django-Firstly/blob/master/shopweb/sale/static/imgs/Django%20Web%20Project.png" alt="Banner" style="max-width: 100%; height: auto;"/>

</div>



## 📖 Giới thiệu

Đây là **dự án đầu tiên** được xây dựng bằng **Django**, bao gồm các trang quản lý hệ thống và các chức năng cơ bản của một **website thương mại điện tử**.


## 🎥 Demo
<div align="center">
<a href="https://drive.google.com/file/d/1FDvYllsbow9nXxca2rDr22FKOeO9Gy3T/view?usp=sharing" target="_blank">
  <img src="https://github.com/HitDrama/Project-Django-Firstly/blob/master/shopweb/sale/static/imgs/Django.gif" alt="Xem video demo" style="max-width: 100%; height: auto;"/>
</a>
   <p>📌 *Nhấn vào video demo hoặc liên kết để xem video demo đầy đủ.*</p>
</div>



## 🏗️ Cấu trúc dự án  
### **1. Pages - Trang chính**  
- 🏠 **Home** – Trang chủ  
- 📂 **Cate** – Danh mục sản phẩm  
- 📄 **Detail** – Chi tiết sản phẩm  
- 🛒 **Cart** – Giỏ hàng  

### **2. Secure - Bảo mật & Xác thực**  
- 🔑 **Login** – Đăng nhập  
- 📝 **Register** – Đăng ký  
- ❌ **404** – Trang lỗi  
- 🔃 **Forget** – Quên mật khẩu  

### **3. System - Quản trị hệ thống**  
- 👤 **Account** – Quản lý tài khoản  
- 📂 **Category** – Quản lý danh mục  
- 🛠️ **Manager** – Quản lý hệ thống  
- ⚠️ **Baotri** – Trang bảo trì  
- 📦 **Product** – Quản lý sản phẩm  

## 🚀 Hướng dẫn sử dụng  
Dự án **không bao gồm database**, bạn cần **tạo superuser** để có quyền truy cập hệ thống.  

### 🔧 Tạo tài khoản quản trị  
1️⃣ **Mở terminal hoặc command prompt**, di chuyển vào thư mục dự án Django và chạy lệnh:  
   ```bash
   python manage.py createsuperuser
```
2️⃣ **Nhập thông tin tài khoản quản trị, bao gồm:

Username – Tên đăng nhập
Email – Không bắt buộc
Password – Mật khẩu quản trị
3️⃣ **Sau khi tạo tài khoản, mở database và chỉnh sửa giá trị is_superuser trong bảng auth_user, đặt giá trị là 1 để cấp quyền quản trị.

📩 Liên hệ
Nếu có bất kỳ thắc mắc nào hoặc cần hỗ trợ, vui lòng liên hệ qua:
📧 Email: dangtonhan2002@gmail.com
