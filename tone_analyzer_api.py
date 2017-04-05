import json
from watson_developer_cloud import ToneAnalyzerV3


tone_analyzer = ToneAnalyzerV3(
    username='73e4df16-f9d8-42f0-99aa-5e483c931b62',
    password='rdhhib0xtnry' ,
    version='2016-02-11')

print(json.dumps(tone_analyzer.tone(text='I am very happy'), indent=2))