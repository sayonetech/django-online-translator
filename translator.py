# -*- coding: utf-8 -*-
import urllib
import requests
from xml.dom.minidom import parseString

class BingTranslator(object):
    def __init__(self, clientID, clientSecret):
        self.client_id = clientID
        self.client_secret = clientSecret

    def tranlsate(self, text, from_language, to_language):
        """
        Translates given text from source language code to target language code.
        text : Text string to be translated.
        from_language : Source language code.
        to_language   : Target language code.

        See http://msdn.microsoft.com/en-us/library/hh456380.aspx for Bing supported laguage codes.
        """
        
        access_token = self.generate_access_token()
        translate_url = 'http://api.microsofttranslator.com/V2/Http.svc/Translate?text=%s&from=%s&to=%s'%(text ,from_language,to_language)
        auth_header = "Bearer " + str(access_token)
        r = requests.get(translate_url, headers={'Authorization':auth_header})
        response = r.content

        value = None

        try:

            dom = parseString(response)

            value = dom.getElementsByTagName('string')[0].childNodes[0].data
        except Exception as e:
            print e

        return value


    def generate_access_token(self):
        """
        Generates Access Token (validity 10 minutes).
        """
        method = "POST"

        token_url = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'
        data = urllib.urlencode(
                                {'client_id':self.client_id,
                                 'client_secret':self.client_secret,
                                 'scope':'http://api.microsofttranslator.com',
                                 'grant_type':'client_credentials'
                                 }
                                )
        access_token = None
        try:
            r = requests.post(token_url, data=data)
            response = r.json()
            access_token = response['access_token']
        except Exception as e:
            print e

        return access_token
