

import tornado.ioloop
import tornado.websocket

# Lớp WebSocketClient xử lý kết nối và tương tác với máy chủ WebSocket
class WebSocketClient:
    def __init__(self, io_loop):
        # Biến để lưu trữ đối tượng kết nối WebSocket
        self.connection = None
        # Biến để lưu trữ đối tượng IOLoop của Tornado
        self.io_loop = io_loop

    def start(self):
        """
        Bắt đầu quá trình kết nối với máy chủ WebSocket.
        """
        self.connect_and_read()

    def stop(self):
        """
        Dừng vòng lặp I/O của Tornado, ngắt kết nối client.
        """
        self.io_loop.stop()

    def connect_and_read(self):
        """
        Kết nối với máy chủ WebSocket và bắt đầu lắng nghe tin nhắn.
        Nếu kết nối thất bại, nó sẽ thử lại sau.
        """
        print("Connecting and reading...")
        # Sử dụng websocket_connect để thiết lập kết nối WebSocket
        # url: Địa chỉ máy chủ WebSocket
        # callback: Hàm được gọi khi kết nối hoàn tất (thành công hoặc thất bại)
        # on_message_callback: Hàm được gọi khi nhận được tin nhắn từ máy chủ
        # ping_interval/ping_timeout: Cấu hình giữ kết nối sống (keep-alive)
        tornado.websocket.websocket_connect(
            url="ws://localhost:8888/websocket/",
            callback=self.maybe_retry_connection,
            on_message_callback=self.on_message,
            ping_interval=10,
            ping_timeout=30
        )

    def maybe_retry_connection(self, future) -> None:
        """
        Hàm callback được gọi sau khi cố gắng kết nối.
        Kiểm tra kết quả của tương lai (future) để xác định xem kết nối có thành công không.
        """
        try:
            # Lấy kết quả từ tương lai (nếu thành công, đây là đối tượng kết nối)
            self.connection = future.result()
            print("Successfully connected to WebSocket server.")
        except Exception as e:
            # Nếu kết nối thất bại, in thông báo lỗi và thử lại sau 3 giây
            print(f"Could not reconnect, retrying in 3 seconds... Error: {e}")
            self.io_loop.call_later(3, self.connect_and_read)

    def on_message(self, message):
        """
        Hàm callback được gọi khi nhận được tin nhắn từ máy chủ WebSocket.
        """
        if message is None:
            # Nếu tin nhắn là None, điều đó có nghĩa là máy chủ đã ngắt kết nối
            print("Disconnected, reconnecting...")
            self.connect_and_read() # Cố gắng kết nối lại
            return

        # In tin nhắn nhận được từ máy chủ
        print(f"Received word from server: {message}")

        # Tiếp tục lắng nghe tin nhắn tiếp theo
        # Hàm read_message sẽ gọi lại on_message khi có tin nhắn mới
        self.connection.read_message(callback=self.on_message)

def main():
    """
    Hàm chính để khởi chạy client WebSocket.
    """

    io_loop = tornado.ioloop.IOLoop.current()


    client = WebSocketClient(io_loop)


    io_loop.add_callback(client.start)


    io_loop.start()


if __name__ == "__main__":
    main()
