from rest_framework.response import Response
from rest_framework.decorators import api_view

festivals = [{
    'name': 'Dashain',
    'desc': 'festival of joy eta uta',
    'date': 'Ashok 2nd week'
},
{
    'name': 'Dashain',
    'desc': 'festival of joy eta uta',
    'date': 'Ashok 2nd week'
}]

@api_view(['GET'])
def getFestivals(request):
    return Response(festivals)