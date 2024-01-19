#!/home/alex/.local/lib/python3.6/ # specify python installation on server
# -*- coding: utf-8 -*-
# version 1.0.0

# This code reads in the 'raw' SQL database for Stephanie stations connected to
# SWARM satellite system and if the latest record is not on the 'clean' SQL 
# database, it pushes the new data to appropriate 'clean' SQL database 
# for VIU-Hydromet. 
# Written by J. Bodart

import pandas as pd 
import numpy as np
from datetime import datetime

# Establish a connection with MySQL database 'viuhydro_wx_data_v2'
# Server log-in details stored in config file
import config
engine = config.main_sql()

# check both 'raw' and 'clean' for each wx station and push if necessary
cains = ['cainridgerun','lowercain'] # the number associated with the stephanie stations connected to GOES
for i in range(len(cains)):  
    while True:
        print('Checking for new data from satellite for: %s' %(cains[i])) 
        
        # note Steph 9 is Upper Russell here
        if cains[i] == 'cainridgerun':
            sql_file_raw_orig = pd.read_sql_query(sql="SELECT * FROM raw_%s ORDER BY DateTime DESC LIMIT 100" %(cains[i]), con = engine)
            sql_file_raw = pd.read_sql_query(sql="SELECT * FROM raw_Ttherm_test_%s ORDER BY DateTime DESC LIMIT 100" %(cains[i]), con = engine)
        else:
            sql_file_raw_orig = pd.read_sql_query(sql="SELECT * FROM raw_%s ORDER BY DateTime DESC LIMIT 100" %(cains[i]), con = engine)
            sql_file_raw = pd.read_sql_query(sql="SELECT * FROM raw_Ttherm_test_%s ORDER BY DateTime DESC LIMIT 100" %(cains[i]), con = engine)
        
        # get datetime for both clean and raw sql databases
        last_dt_sql_raw_orig = sql_file_raw_orig['DateTime'].iloc[0]
        last_dt_sql_raw = sql_file_raw['DateTime'].iloc[0]
        
        # if the last row in raw matches last row in clean SQL database 
        # (i.e. no new data to write), then exit and don't write new data
        check = last_dt_sql_raw_orig == last_dt_sql_raw    
        if check:
            print('No new data detected - check satellite transmission?')  
            
            # write current time for sanity check and exit loop
            current_dateTime = datetime.now()
            print("Done at:", current_dateTime, '- refreshing in 1 hour...')
            break
    
        # else if new data on raw which is not yet written to clean, write it
        else:
            print('New satellite data detected - writing to raw_Ttherm_test database') 
            
            # calculate latest SQL entry and assess how many new 
            # satellite data to write to SQL database
            last_dt_sql_idx = int(np.flatnonzero(last_dt_sql_raw == sql_file_raw_orig['DateTime']))
            last_idx = last_dt_sql_idx
            
            # only keep new data that needs added to sql database
            missing_data_df = sql_file_raw_orig.iloc[:-last_idx]
            missing_data_dt = sql_file_raw_orig['DateTime'].iloc[:-last_idx]   

            # calculate water year for Stephanies (new year starts on 10.01.YYYY). 
            # If months are before October, do nothing. Else add +1
            WatYrs = []
            for j in range(len(missing_data_df)):
                if int(str(missing_data_dt.iloc[j]).split('-')[1]) < 10:
                    WatYr = int(str(missing_data_dt.iloc[j]).split('-')[0])
                else:
                    WatYr = int(str(missing_data_dt.iloc[j]).split('-')[0])+1
                WatYrs.append(WatYr)
            
            # export new data to last row of SQL database  
            # No data values will automatically be added in SQL database as 
            # 'NULL'
            # for cainridgerun
            if cains[i] == 'cainridgerun':     
                # write to SQL
                missing_data_df.insert(loc = 1,
                          column = 'WatYr',
                          value = WatYrs)
                
                # write new data to MySQL database
                #missing_data_df.to_sql(name='raw_Ttherm_test_%s' %cains[i], con=engine, if_exists = 'append', index=False)
            
            # for lowercain
            else:
                # write to SQL
                missing_data_df.insert(loc = 1,
                          column = 'WatYr',
                          value = WatYrs)
                # write new data to MySQL database
                #missing_data_df.to_sql(name='raw_Ttherm_test_%s' %cains[i], con=engine, if_exists = 'append', index=False)
            
            # write current time for sanity check and exit loop
            current_dateTime = datetime.now()
            print("Done at:", current_dateTime, '- refreshing in 1 hour...')