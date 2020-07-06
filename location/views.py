import os
from urllib.parse import urlparse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
import psycopg2
from rest_framework.response import Response

db_connection = os.getenv('DATABASE_URL')

db_params = urlparse(db_connection)


@api_view(['GET'])
def view(request):
        # establishing a connection
    connection = psycopg2.connect(
        host=db_params.hostname, database=db_params.path[1:],
        user=db_params.username, password=db_params.password
    )
        # creating the cursor (vessel to the db)
    cursor=connection.cursor()
        # executing the query
    cursor.execute("select region,district,rsd_id from public.regional_structure")

    Rows=cursor.fetchall()
    cursor.close()
    connection.close()
    return Response({'data':Rows})
