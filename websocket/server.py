# server.py

import random
import tornado.ioloop
import tornado.web
import tornado.websocket

# Lớp WebSocketServer xử lý các kết nối WebSocket
class WebSocketServer(tornado.websocket.WebSocketHandler):
    # Tập hợp (set) để lưu trữ tất cả các client đang kết nối
    clients = set()

    # Phương thức được gọi khi một kết nối WebSocket mới được mở
    def open(self):
        # Thêm client hiện tại vào tập hợp các client đang kết nối
        WebSocketServer.clients.add(self)
        print(f"Client connected. Total clients: {len(WebSocketServer.clients)}")

    # Phương thức được gọi khi một kết nối WebSocket bị đóng
    def on_close(self):
        # Xóa client hiện tại khỏi tập hợp các client đang kết nối
        WebSocketServer.clients.remove(self)
        print(f"Client disconnected. Total clients: {len(WebSocketServer.clients)}")

    # Phương thức tĩnh để gửi tin nhắn đến tất cả các client đang kết nối
    @classmethod
    def send_message(cls, message: str):
        print(f"Sending message '{message}' to {len(cls.clients)} client(s).")
        # Duyệt qua tất cả các client và gửi tin nhắn
        for client in cls.clients:
            client.write_message(message)

# Lớp RandomWordSelector để chọn ngẫu nhiên một từ từ danh sách
class RandomWordSelector:
    def __init__(self, word_list):
        self.word_list = word_list

    def sample(self):
        # Chọn ngẫu nhiên một từ từ danh sách
        return random.choice(self.word_list)

# Hàm chính để khởi chạy máy chủ WebSocket
def main():
    # Khởi tạo ứng dụng Tornado Web
    app = tornado.web.Application(
        [
            (r"/websocket/", WebSocketServer)  # Định tuyến URL "/websocket/" đến WebSocketServer
        ],
        # Cấu hình tùy chọn cho WebSocket
        websocket_ping_interval=10,  # Gửi ping mỗi 10 giây để giữ kết nối sống
        websocket_ping_timeout=30,   # Đóng kết nối nếu không nhận được pong trong 30 giây
    )

    # Lắng nghe các kết nối trên cổng 8888
    app.listen(8888)
    print("WebSocket server started on ws://localhost:8888/websocket/")

    # Lấy vòng lặp I/O hiện tại của Tornado
    io_loop = tornado.ioloop.IOLoop.current()

    # Khởi tạo bộ chọn từ ngẫu nhiên với danh sách các từ
    word_selector = RandomWordSelector(['apple', 'banana', 'orange', 'grape', 'melon'])

    # Thiết lập một callback định kỳ để gửi tin nhắn ngẫu nhiên
    # Hàm lambda gọi WebSocketServer.send_message với một từ ngẫu nhiên
    # Mỗi 3000 mili giây (3 giây)
    periodic_callback = tornado.ioloop.PeriodicCallback(
        lambda: WebSocketServer.send_message(word_selector.sample()), 3000
    )
    # Bắt đầu callback định kỳ
    periodic_callback.start()

    # Bắt đầu vòng lặp I/O của Tornado (duy trì máy chủ chạy)
    io_loop.start()

# Điều này đảm bảo rằng hàm main() chỉ được gọi khi tập lệnh được thực thi trực tiếp
if __name__ == "__main__":
    main()
