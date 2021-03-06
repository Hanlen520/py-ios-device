import time
"""
获取单应用的网络信息
"""
from ios_device.servers.Instrument import InstrumentServer


def netstat(rpc, pid):
    rpc.start()
    channel = "com.apple.xcode.debug-gauge-data-providers.NetworkStatistics"
    attr = {}
    print("start", rpc.call(channel, "startSamplingForPIDs:", {pid}).parsed)
    ret = rpc.call(channel, "sampleAttributes:forPIDs:", attr, {pid})
    print(ret.parsed)
    rpc.stop()


if __name__ == '__main__':
    rpc = InstrumentServer().init()
    netstat(rpc, 261)
    rpc.deinit()
