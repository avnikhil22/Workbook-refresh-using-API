#!/usr/bin/env python
# coding: utf-8

# ########################### Tableau server Datasource refresh using REST API and Python###################################### 

# Requirements:
# 
# pip install tableauserverclient
# 
# pip install tableau_api_lib

# In[ ]:


from tableau_api_lib import TableauServerConnection
import tableauserverclient as TSC
from tableau_api_lib.utils.querying import get_workbooks_dataframe, get_datasources_dataframe
import time

tableau_server_config = {
        'my_env': {
                'server': '',
                'api_version': '',
                'personal_access_token_name': '',
                'personal_access_token_secret': '',
                'site_name': 'Internal',
                'site_url': ''
        }
}
#Signing into Tableau server
conn = TableauServerConnection(tableau_server_config, env='my_env')
conn.sign_in()

#Get datasource function
datasources_df = get_datasources_dataframe(conn)
df = datasources_df

name = input("Enter the datasource name as per Tableau server: \n" )

try:
    id_value = df.loc[df['name'] == name, 'id'].values[0]
    
except Exception as error:
    print('Error: ', str(error))
    print('Value you entered is not found in the code. Please enter a value Tableau datasource name')
    
try: 
    response = conn.update_data_source_now(str(id_value))
    #print('resonse of id =\n')
    #print(response.json())
    
    print('Please wait for a while until extract refresh job is completed \n')
    #The extract refresh job will take 5 minutes to complete extract refresh
    time.sleep(60)
    print('Lets check the status of the job \n')
    #Find the status of your extracts by running these lines of code
    job_id = response.json()['job']['id']
    job_status = conn.query_job(job_id)
    print(job_status.json())
    time.sleep(150)
    print('\n')
    print(job_status.json())
    time.sleep(150)
    print('\n')
    print(job_status.json())
    time.sleep(100)
    print('\n')
    job_id = response.json()['job']['id']
    job_status = conn.query_job(job_id)
    print(job_status.json())
    
    print('\n')
    #Sign out of Tableau server
    conn.sign_out()
    print('Signed out of Tableau server')
except Exception as error:
    print('Error: ', str(error))    


# In[ ]:


conn.sign_out()


# In[ ]:


from tableau_api_lib import TableauServerConnection
import tableauserverclient as TSC
from tableau_api_lib.utils.querying import get_workbooks_dataframe, get_datasources_dataframe
import time

tableau_server_config = {
        'my_env': {
                'server': '',
                'api_version': '3.17',
                'personal_access_token_name': '',
                'personal_access_token_secret': '',
                'site_name': 'Internal',
                'site_url': ''
        }
}
#Signing into Tableau server
conn = TableauServerConnection(tableau_server_config, env='my_env')
conn.sign_in()

#Get datasource function
datasources_df = getDataSourcesTableauServer(conn)
df = datasources_df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




