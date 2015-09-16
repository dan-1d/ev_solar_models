import datetime

class solar_config:

#    def __init__(self):
#        '''
#        'data' is a dataframe 
#        '''
#        self.data_df = data

    def ingest_pvwatts(self, data):
        '''
        data must be a dataframe object.
        This function adds a datetime column
        '''
        self.data_df = data
        self.data_df["datetime"] = self.data_df.apply( lambda row:  
                datetime.datetime( year=2016, month=int(row["Month"]), day=int(row["Day"]),
                                hour=int(row["Hour"]) ), axis=1 )

