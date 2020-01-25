import requests
import xml.etree.ElementTree as xml

TRAFFIC_API = 'api/monitoring/traffic-statistics'
STATUS_API = 'api/monitoring/status'

class InvalidSessionIDError(Exception):
    '''Raised when SessionID being used is invalid
        Args:
            msg (str): Human readable string describing the exception

        Attributes:
            msg (str): Human readable string describing the exception
    '''
    
    def __init__(self, msg):
    
        self.msg


class Response():
    pass

class HuaweiApi():

    def __init__(self, session_id, base_url='http://192.168.8.1/'):
        self._session_id = session_id
        self.base_url = base_url
        self.session = requests.Session()
        self.session.cookies.update({'SessionID': session_id})

    def __str__(self):
        return self.session.cookies
        
    @property
    def session_id(self):
        return None
    @session_id.setter
    def session_id(self, id):
        self._session_id = id

    def get(self, api):
        '''Get response from the api
            Args:
                api (str): API to get response from

            Raises:
                InvalidSessionIDError: Invalid/Unusable Session ID was provided

            Returns:
                response (Response): Contains meta of requested API
        
        '''
        response = Response()
        try:
            resp = self.session.get(self.base_url + api)
            if resp.ok: 
                root = xml.fromstring(resp.text)

                for child in root:
                    setattr(response, child.tag, child.text)
                return response
        except:
            raise InvalidSessionIDError