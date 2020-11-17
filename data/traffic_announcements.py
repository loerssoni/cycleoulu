import requests
import json 

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
    res = requests.post('https://api.oulunliikenne.fi/proxy/graphql', json={'query': query})
    data = json.loads(res.text)['data']['trafficAnnouncements']
    return data