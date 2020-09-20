# import pychromecast
# import time

# PORT = 8000
# ghome_ip = '192.168.0.7'
# local_ip = '192.168.0.11'
# ghome = pychromecast.Chromecast(ghome_ip)
# print(ghome)
# ghome.wait()

# mc = ghome.media_controller
# mc.play_media(
#     'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', 'video/mp4')
# mc.block_until_active()
# mc.pause()
# time.sleep(5)
# mc.play()


# import pychromecast
# import time
# DISABLE FIREWALL TO WORK PLS
# _chromecast_devices = pychromecast.get_chromecasts()[0]
# chromecasts = []

# for cast in _chromecast_devices:
#     print(cast.name)

# import wikipedia
# python = wikipedia.page('capital of latvia')
# print(python.summary.split('\n')[0])

wiki = 'wikipedia capital of latvia'
