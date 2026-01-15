import socket

# خادم بسيط لاستقبال ضربات الاختبار
def start_target():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 8080)) # سيفتح البورت 8080
    sock.listen(5)
    print("Target Server is Running... Waiting for test hits on port 8080")
    
    while True:
        conn, addr = sock.accept()
        # استقبال البيانات دون معالجتها لإبقاء المعالج مشغولاً
        data = conn.recv(1024)
        conn.close()

if __name__ == "__main__":
    start_target()
