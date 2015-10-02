import datetime
import pandas as pd

class solar_data:

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

    def ingest_pvwatts_csv(self, filename):
        df = pd.read_csv(filename,thousands=',')
        self.ingest_pvwatts(df)


    def export_kwatts_for_elect_rates(self):
        df = pd.DataFrame()
        df["datetime"] = self.data_df["datetime"]
        df["Value"] = self.data_df["AC System Output (W)"] /1000.0
        return df

    def data(self):
        return self.data_df
