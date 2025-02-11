🌐 Django Web Project
📖 Giới thiệu
Đây là dự án đầu tiên được xây dựng bằng Django, bao gồm các trang quản lý hệ thống và chức năng cơ bản của một website thương mại điện tử.

🏗️ Cấu trúc dự án
1. Pages - Trang chính
Home – Trang chủ
Cate – Danh mục sản phẩm
Detail – Chi tiết sản phẩm
Cart – Giỏ hàng
2. Secure - Bảo mật & Xác thực
Login – Đăng nhập
Register – Đăng ký
404 – Trang lỗi
Forget – Quên mật khẩu
3. System - Quản trị hệ thống
Account – Quản lý tài khoản
Category – Quản lý danh mục
Manager – Quản lý hệ thống
Baotri – Trang bảo trì
Product – Quản lý sản phẩm
🚀 Hướng dẫn sử dụng
Dự án không bao gồm database, bạn cần tự tạo superuser để truy cập hệ thống.

Tạo tài khoản quản trị
Mở terminal hoặc command prompt, di chuyển vào thư mục dự án Django và chạy lệnh:
python manage.py createsuperuser

Nhập thông tin tài khoản quản trị, bao gồm:

Username (tên đăng nhập)
Email (không bắt buộc)
Password (mật khẩu)
Sau khi tạo tài khoản, mở database và chỉnh sửa giá trị is_superuser trong bảng auth_user, đặt giá trị là 1 để cấp quyền quản trị.
📩 Liên hệ
Nếu có bất kỳ thắc mắc nào hoặc cần hỗ trợ, vui lòng liên hệ qua:

Email: dangtonhan2002@gmail.com
