import os
from urllib.parse import urlparse

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
    )# psycopg2.connect(db_connection)
        # creating the cursor (vessel to the db)
    cursor=connection.cursor()
        # executing the query
    # cursor.execute("SELECT * FROM public.agric_indicator where gs_id<10 ")
#     cursor.execute('''select ppp_sum,(ndvi_jfm+ndvi_amj+ndvi_jas+ndvi_ond)/4,
# (ndwi_jfm+ndwi_amj+ndwi_jas+ndwi_ond)/4,soil_phos,soil_copper,soil_iron,soil_magne,
# rainfall,soil_alumi,soil_potas,(lst_jfm+lst_amj+lst_jas+lst_ond)/4,slope,elevation,
# land_cover, gs_id from public.agric_indicator where gs_id<10 ''')

    cursor.execute('''select ppp_sum,soil_copper,soil_phos,soil_potas,soil_boron,soil_alumi,soil_iron,
    soil_magne,ndwi_jfm,ndwi_amj,ndwi_jas,ndwi_ond,presp_jfm,presp_amj,presp_jas,presp_ond,ndvi_jfm,
    ndvi_amj,ndvi_jas,ndvi_ond,land_cover,slope,elevation,lst_jfm,lst_amj,lst_jas,lst_ond,gs_id from 
    public.agric_indicator''')



    agricRows=cursor.fetchall()


    cursor.close()
    connection.close()
    return Response({'agridata':agricRows})
