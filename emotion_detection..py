import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


apikey = 'vQ9FbrdXQPDc23NEuXDNY_1ixidDp410dEJCJ6lt4SK7'
url = 'https://gateway-lon.watsonplatform.net/tone-analyzer/api'


authenticator = IAMAuthenticator('vQ9FbrdXQPDc23NEuXDNY_1ixidDp410dEJCJ6lt4SK7')
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)

tone_analyzer.set_service_url('https://gateway-lon.watsonplatform.net/tone-analyzer/api')

text = ' am so happy :) '

tone_analysis = tone_analyzer.tone(
    {'text': text},
    content_type='application/json'
).get_result()
print(json.dumps(tone_analysis, indent=2))
if tone_analysis['document_tone']['tones']:
    data = tone_analysis['document_tone']['tones'][0]['tone_name'] 
else:
    data = 'no mood found'

#print(tone_analysis['document_tone']['tones'][0]['tone_name'])
print(data)
