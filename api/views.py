from rest_framework.response import Response
from rest_framework.decorators import api_view

festivals = [{
    'id':1, 
    'name': 'Dashain',
    'desc': 'festival of joy eta uta',
    'date': 'Ashok 2nd week'
},
{
    'id':2, 
    'name': 'Dashain',
    'desc': 'festival of joy eta uta',
    'date': 'Ashok 2nd week'
},
{
    'id':3, 
    'name': 'Dashain',
    'desc': 'festival of joy eta uta',
    'date': 'Ashok 2nd week'
},
{
    'id':4, 
    'name': 'Dashain',
    'desc': 'festival of joy eta uta',
    'date': 'Ashok 2nd week'
},
{
    'id':5, 
    'name': 'Dashain',
    'desc': 'festival of joy eta uta',
    'date': 'Ashok 2nd week'
},
{
    'id':6, 
    'name': 'Dashain',
    'desc': 'festival of joy eta uta',
    'date': 'Ashok 2nd week'
},
{
    'id':7, 
    'name': 'Dashain',
    'desc': 'festival of joy eta uta',
    'date': 'Ashok 2nd week'
},
{
    'id':8, 
    'name': 'Dashain',
    'desc': 'festival of joy eta uta',
    'date': 'Ashok 2nd week'
},
{
    'id':9, 
    'name': 'Dashain',
    'desc': 'festival of joy eta uta',
    'date': 'Ashok 2nd week'
},
{
    'id':10, 
    'name': 'Dashain',
    'desc': 'festival of joy eta uta',
    'date': 'Ashok 2nd week'
}
]

@api_view(['GET'])
def getFestivals(request):
    return Response(festivals)