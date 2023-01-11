from rest_framework import renderers 
import json
from django.core.serializers.json import DjangoJSONEncoder

class CustomRenderer(renderers.JSONRenderer):
    
    charset = "utf-8"
    
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ""

        if "ErrorDetail" in str(data):
            response = json.dumps(
                                    {
                                        "status": "Error",
                                        "data": data,
                                    }
                                 )
        else:
            response = json.dumps(
                                    {
                                        "status": "Successful",
                                        "data": data,
                                    },
                                    cls=DjangoJSONEncoder
                                 )
        return response