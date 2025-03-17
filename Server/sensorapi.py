from flask import Flask, jsonify
from server import Server

app = Flask(__name__)

server = Server()


@app.route('/get_data', methods=['GET'])
def get_data():
    server.update_psutils()
    metrics = {
        'cpuUsage': server.cpu_usage(),
        'memoryAvailable': server.memory.available,
        'swapAvailable': server.swap.free,
        'diskFree': server.disk.free,
        'ioWriteCount': server.diskIO.write_count,
        'ioReadCount': server.diskIO.read_count,
        'ioReadBytes': server.diskIO.read_bytes,
        'ioWriteBytes': server.diskIO.write_bytes,
        'netSentBytes': server.net.bytes_sent,
        'netRecvBytes': server.net.bytes_recv,
        'netSentPackets': server.net.packets_sent,
        'netRecvPackets': server.net.packets_recv,
        'netErrin': server.net.errin,
        'netErrout': server.net.errout,
    }
    return jsonify(metrics)


@app.route('/get_initial', methods=['GET'])
def get_initial():
    initial = {
        'name' : server.name,
        'cpuCores' : server.cpuCores,
        'memTotal' : server.memory.total,
        'swapTotal' : server.swap.total,
        'diskTotal' : server.disk.total
    }
    return jsonify(initial)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)