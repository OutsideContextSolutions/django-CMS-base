from social_core.backends.open_id_connect import OpenIdConnectAuth

class UrlOpenIdConnect(OpenIdConnectAuth):
    name="UrlOpenIdConnect"
    OIDC_ENDPOINT="http://demesne.aura.t8q.org:8000"
    def __init__(self,*args,**kwargs):
        print(args,kwargs)
