### First retrieve the HPLC data

#The Spreadsheet ID is: 1NxERFkckKKGi3H737HilHUzYw_qM-mNfVMRPPTj8juU for the entire spreadsheet.
#The Range is defined  by the tab that I need, in this case, 'All Monomers'

#Adapted from https://medium.com/analytics-vidhya/how-to-read-and-write-data-to-google-spreadsheet-using-python-ebf54d51a72c


import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow,Flow
from google.auth.transport.requests import Request
import os
import pickle

%load_ext rpy2.ipython

SCOPES = ['https://www.googleapis.com/auth/spreadsheets'] #this scope allows read/write access to the user's sheet ant their properties

# here enter the id of your google sheet
SAMPLE_SPREADSHEET_ID_input = '1NxERFkckKKGi3H737HilHUzYw_qM-mNfVMRPPTj8juU'
SAMPLE_RANGE_NAME = 'CR_curated' 

def main():
    global values_input, service
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES) # here enter the name of your downloaded JSON file
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result_input = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input, 
                                  
                                range=SAMPLE_RANGE_NAME).execute()
    values_input = result_input.get('values', [])

    if not values_input and not values_expansion:
        print('No data found.')

main()

HPLC_all_monomers=pd.DataFrame(values_input[1:], columns=values_input[0])



#Now let's do the same for the Discovery database.
#The ID of the spreadsheet is: 1FSOVNl2KX875uAgED2fsVUtfdciyZL-6dqDcPw-QWL4

#Let's start by retrieving the Culture data

SAMPLE_SPREADSHEET_ID_input = '1FSOVNl2KX875uAgED2fsVUtfdciyZL-6dqDcPw-QWL4'
SAMPLE_RANGE_NAME = 'Cultures' 


main()

Cultures_data=pd.DataFrame(values_input[1:], columns=values_input[0])

# And now for the samples:

SAMPLE_SPREADSHEET_ID_input = '1FSOVNl2KX875uAgED2fsVUtfdciyZL-6dqDcPw-QWL4'
SAMPLE_RANGE_NAME = 'Samples' 

main()

Samples_data=pd.DataFrame(values_input[1:], columns=values_input[0])

# Join Cultures and Samples

# First pick just the columns we need

Cultures = Cultures_data[['Culture_id', 'Sample_id', 'Batch_number', 'Inoculum_source']]

Samples = Samples_data[['Sample_id', 'Procedence', 'Description']]

# Merge both tables using Sample_id

discovery = Cultures.merge(Samples, on = 'Sample_id')

# First change the name of the first column in the HPLC data so it matches the Discovery tables

HPLC_all_monomers.rename(columns = {'Sample Name':'Culture_id'}, inplace = True)

# Now merge on Culture_id

fulltable = discovery.merge(HPLC_all_monomers, on = 'Culture_id')

# keep only known monomers for now

known_monomers = ['TPA', 'BHET', 'MHET']

fulltable_known = fulltable.loc[fulltable['Monomer'].isin(known_monomers)]

# Push the merged tables to a new Google sheet

# this is the ID of the destination Google Sheet, Discovery_data_aggregate
SAMPLE_SPREADSHEET_ID_input = '1zSfr8qkT---M6zh_FnQmFutwMGssEZSej4eyx50Tj_k'
#worksheet = 'all_data'


#change the range if needed
SAMPLE_RANGE_NAME = 'A1:AA1000'


def Create_Service(client_secret_file, api_service_name, api_version, *scopes):
    global service
    SCOPES = [scope for scope in scopes[0]]
    #print(SCOPES)
    
    cred = None

    if os.path.exists('token_write.pickle'):
        with open('token_write.pickle', 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, SCOPES)
            cred = flow.run_local_server()

        with open('token_write.pickle', 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(api_service_name, api_version, credentials=cred)
        print(api_service_name, 'service created successfully')
        #return service
    except Exception as e:
        print(e)
        #return None
        
# change 'my_json_file.json' by your downloaded JSON file.
Create_Service('client_secret.json', 'sheets', 'v4',['https://www.googleapis.com/auth/spreadsheets'])
    
def Export_Data_To_Sheets():
    response_date = service.spreadsheets().values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
        valueInputOption='RAW',
        range=SAMPLE_RANGE_NAME,
        body=dict(
            majorDimension='ROWS',
            values=fulltable_known.T.reset_index().T.values.tolist())
    ).execute()
    print('Sheet successfully Updated')

Export_Data_To_Sheets()

#Pivot this table to have the monomers in their own columns.
#I ended up resorting to R to do this because Panda's handling of index columns did not give me the results that I wanted. Luckily Jupyter Notebooks allow running R in a separate cells using the rmagic extension called rpy2. This library needs to be installed separately through pip, and you need a working version of R in your system.

#I know this will complicate taking this to production, but it works until I figure out how to do it completely in Pandas.

%%R -i fulltable_known

library(tidyverse)
library(tidyr)

# change class of 'Area' from string to float

fulltable_known$Area = as.numeric(fulltable_known$Area)

# pivot the table and collapse by Culture Id



fulltable_wide = 
fulltable_known %>%
select(-Height) %>%
#filter(Area >= 10) %>% # keep only hits with HPLC integrated area > 10
filter(grepl("TUB",Culture_id)) %>%  # keep only the tubes
group_by(Culture_id, Sample_id, Batch_number, Inoculum_source, Procedence, Description) %>%
mutate(row = row_number()) %>% # this is to create a unique index, otherwise the pivot doesn't work
pivot_wider(names_from = "Monomer",
              values_from = "Area")%>%
select(-row) %>% # now we don't need it anymore so out with it
summarise(TPA = sum(TPA, na.rm = T), # the pivot produces 3 different lines for each of the monomers, this summarizes
              BHET = sum(BHET, na.rm = T), # all three into one line
              MHET = sum(MHET, na.rm = T))


%%R -i fulltable -w 10 -h 3 --units in -r 250

library(ggplot2)
library(RColorBrewer)

fulltable_original_samples = 
fulltable %>%
filter(Inoculum_source == 'original sample' & Batch_number !=7)

fulltable_original_samples$Area = as.numeric(fulltable_original_samples$Area)
fulltable_original_samples$Batch_number = as.numeric(fulltable_original_samples$Batch_number)

#print(fulltable_original_samples)

ggplot(fulltable_original_samples, aes(x = Culture_id, y = Area, fill = Monomer)) + 
geom_bar(stat = "identity") +
theme_bw() +
scale_fill_brewer(palette = "Spectral") +
#scale_y_discrete(breaks=seq(1,300,by=25)) +
theme(axis.text.x = element_text(angle = 90, vjust = 1, hjust=1, size=6),
      axis.text.y = element_text(size=6),
      legend.text = element_text(size = 6),
      legend.title = element_text(size = 8),
      axis.ticks = element_line(size = .1)) +
facet_grid(.~Batch_number, scales = 'free', space = 'free')

# export the pivoted table back to the python environment (this goes alone in its own cell)

%R -o fulltable_wide


# Add hit flags

fulltable_wide['TPA_hit'] = ''
fulltable_wide['MHET_BHET_hit'] = ''

hit_minimum_area = 10.0

for i in range(len(fulltable_wide['TPA'])):
    if fulltable_wide['TPA'][i] >= hit_minimum_area:
        fulltable_wide['TPA_hit'][i] = 'yes'
    if (fulltable_wide['MHET'][i] or fulltable_wide['BHET'][i]) > hit_minimum_area:
        fulltable_wide['MHET_BHET_hit'][i] = 'yes'
        
    
# Push pivoted table to a different tab in the same spreadsheet

# this is the ID of the destination Google Sheet, Discovery_data_aggregate
SAMPLE_SPREADSHEET_ID_input = '1zSfr8qkT---M6zh_FnQmFutwMGssEZSej4eyx50Tj_k'
#worksheet = SAMPLE_SPREADSHEET_ID_input[1]

#change the range if needed
SAMPLE_RANGE_NAME = 'data_pivot'

def Create_Service(client_secret_file, api_service_name, api_version, *scopes):
    global service
    SCOPES = [scope for scope in scopes[0]]
    #print(SCOPES)
    
    cred = None

    if os.path.exists('token_write.pickle'):
        with open('token_write.pickle', 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, SCOPES)
            cred = flow.run_local_server()

        with open('token_write.pickle', 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(api_service_name, api_version, credentials=cred)
        print(api_service_name, 'service created successfully')
        #return service
    except Exception as e:
        print(e)
        #return None
        
# change 'my_json_file.json' by your downloaded JSON file.
Create_Service('client_secret.json', 'sheets', 'v4',['https://www.googleapis.com/auth/spreadsheets'])
    
def Export_Data_To_Sheets():
    response_date = service.spreadsheets().values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
        valueInputOption='RAW',
        range=SAMPLE_RANGE_NAME,
        body=dict(
            majorDimension='ROWS',
            values=fulltable_wide.T.reset_index().T.values.tolist())
    ).execute()
    print('Sheet successfully Updated')

Export_Data_To_Sheets()    