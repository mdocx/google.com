from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def log_ip():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    with open('ip_log.txt', 'a') as f:
        f.write(f"{ip} - {user_agent}\n")
    return "IP logged. Thank you."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
