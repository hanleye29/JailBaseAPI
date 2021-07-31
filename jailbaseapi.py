import requests

class JailBaseAPI:
        
    def getSources():
        sources_url = 'http://www.JailBase.com/api/1/sources/'
        response = requests.get(sources_url)
        s = response.json()['records']

        sources = []

        for i in range(len(s)):
            sources.append({'city':s[i]['city'],'state':s[i]['state'],'county':s[i]['county'], 'source_id':s[i]['source_id']})

    
        return sources
    
    def getRecent(sources):
        recent_url = 'http://www.JailBase.com/api/1/recent/'
        sources = getSources()
        rec_sources = []

        for i in range(len(sources)):
            source_id = sources[i].get('source_id')
            query = {'source_id':source_id}
            if requests.get(recent_url, params = query).status_code == 500:
                continue
            response = requests.get(recent_url, params = query).json()['records']
            for j in range(len(response)):
                rec = response[j]
                rec.update(sources[i])
                rec_sources.append(rec)
        
        return rec_sources
