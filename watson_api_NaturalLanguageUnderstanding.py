import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features


natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='a7b3f980-a181-4cbf-9f80-51eb10a79b9f',
    password='eFJQNjG8LoZs')

response = natural_language_understanding.analyze(
    text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
         'Superman fears not Banner, but Wayne.',
    features=[features.Entities(), features.Keywords()])

print(json.dumps(response, indent=2))


###more exampels:  https://github.com/watson-developer-cloud/python-sdk/tree/master/examples