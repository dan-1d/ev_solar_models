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


    def ingest_daily_production_enlightenmanager_csv(self, filename):
        df = pd.read_csv(filename,thousands=',', parse_dates=[0])
        df.columns = ['datetime','Wh']
        self.data_df = df
        ##
        ## Helpful Notes:
        #df['Date/Time'] = pva_df['Date/Time'].apply(dateutil.parser.parse)
        #df['Date/Time'] = pd.to_datetime(pva_df['Date/Time'])



    def export_kwatts_for_elect_rates(self):
        df = pd.DataFrame()
        df["datetime"] = self.data_df["datetime"]
        df["Value"] = self.data_df["AC System Output (W)"] /1000.0
        return df

    def export_daily_energy_from_pvwatts(self):
        df = pd.DataFrame()
        df["datetime"] = self.data_df["datetime"]
        df["Wh"] = self.data_df["AC System Output (W)"]
        df.index = df.datetime
        df = df.resample("D", how='sum')
        return df
        ## TODO: use date_range() and DatetimeIndex

    def export_daily_energy_from_enlightenmanager(self):
        df = pd.DataFrame()
        df["datetime"] = self.data_df["datetime"]
        df["Wh"] = self.data_df["Wh"]
        df.index = df.datetime
        df = df.resample("D", how='sum')
        return df

    def data(self):
        return self.data_df
