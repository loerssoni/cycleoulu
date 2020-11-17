import requests
import json
import pandas as pd
from datetime import datetime

query = """query GetAllTrafficAnnouncements { 
   trafficAnnouncements {
     announcementId
     title {
       fi
     }
     description {
       fi
     }
     severity
     status
     startTime
     endTime
     geojson
     modesOfTransport
     class {
       class
       subclass
     }
     trafficDirectionFreeText {
       fi
     }
     temporarySpeedLimit
     duration
     additionalInfo
     detour
     oversizeLoad
     vehicleSizeLimit
     url
     imageUrls
   }
}"""

def get_traffic_announcements():
    now = datetime.now()
    res = requests.post('https://api.oulunliikenne.fi/proxy/graphql', json={'query': query})
    data = pd.DataFrame(json.loads(res.text)['data']['trafficAnnouncements'])
    data = data[~(pd.to_datetime(data.endTime) <= now)]
    data['descriptions'] = data.apply(lambda x: '<p>Severity: ' + x['severity'] + \
       '.</p><p>'+ x['title']['fi'], 1)
    data = list(data.T.to_dict().values())
    for feat in data:
      feat['geojson']['features'][0]['properties'] = {}
      feat['geojson']['features'][0]['properties']['description'] = feat['descriptions']
    return data