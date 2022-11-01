from collector import Model
import time
import schedule


MODEL_TYPE = 'online'
TOKEN = "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"
REPOSITORY_NAME = 'sdp-sig/sdp-sig.github.io'

if __name__ == '__main__':
    collector = Model(TOKEN, REPOSITORY_NAME)
    if MODEL_TYPE == 'offline':
        collector.get_offline_data()
    elif MODEL_TYPE == 'online':
        schedule.every().hour.do(collector.get_online_data_per_hour)
        while True:
            schedule.run_pending()

    # timestamp = 1667253727.0
    #
    # #转换成localtime
    # time_local = time.localtime(timestamp)
    # #转换成新的时间格式(2016-05-05 20:28:54)
    # dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    # print(dt)
