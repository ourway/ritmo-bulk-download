#!/usr/bin/env python



__author__ = 'Farsheed Ashouri'
__version__ = '0.0.1'

__description__ = '''
Download tracks info from ritmo.ir API
base url is http://api.ritmo.media/api/tracks/{trackId}/details?format=json
Total tracks number at the time of development is 11202, so we need to update
info later.
This command:
	http "http://hamrahang.aban.io:8000/aban-platform/api/1/content/purchase?contentId=17622" X-Auth-Token:at9re6g99tomtm2g13lqta5teh2pcff8
purchases a track in hamarang platform.


'''

import ujson
import requests
import os


TRACK_COUNT = 11202
API = 'http://api.ritmo.media/api/tracks/{trackId}/details?format=json'


def getTrackInfo(trackId):
	'''Get Track Info and return json file
	'''
	_url = API.format(trackId=trackId)
	r = requests.get(_url)
	if r.status_code == 200:
		return ujson.loads(r.content)


def saveTrackInfo(trackId):
	fp = 'ritmo.ir/tracks/%s.json'%trackId
	if not os.path.isfile(fp):
		with open(fp, 'w') as f:
			data = getTrackInfo(trackId)
			ujson.dump(data, f)
			print('\tTrack %s saved.'%trackId)
	else:
			print('\tTrack %s is already available.'%trackId)






if __name__ == '__main__':
	for track in xrange(1, TRACK_COUNT):
		saveTrackInfo(track)
