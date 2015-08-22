class elect_tou_tier:
    def __init__(self, start_time, end_time, dollars_per_kwh, 
                 start_month=1, end_month=12 ):
        # input start and end times and dates,  inclusive of effective tou tier
        self.start = start_time
        self.end_time = end_time
        self.dollars_per_kwh = dollars_per_kwh
        self.start_month = start_month
        self.end_month = end_month
        
    def is_datetime_in_tier(self, dt):
        month_in = True
        hour_in  = True
        if( self.start_month < self.end_month ):
            if( dt.month < self.start_month or dt.month > self.end_month ):
                month_in = False
        elif( self.start_month > self.end_month ):
            if( dt.month < self.start_month or dt.month > self.end_month):
                month_in = False
        if( self.start_time < self.end_time ):
            if( dt.time < self.start_time or dt.time > self.end_time):
                hour_in = False
        elif( self.start_time > self.end_time ):
            if( dt.time < self.start_time and dt.month > self.end_time):
                hour_in = False

        
        
class elect_rates:
    def __init__(self):
        self.tiers = list()
    
    def add_sdge_tou_ev_rates(self):
        self.add_tier( elect_tou_tier(0, 4, 0.17, 5, 9) )
        self.add_tier( elect_tou_tier(0, 4, 0.18, 10, 4) )
        self.add_tier( elect_tou_tier(5, 11, 0.20, 5, 9) )
        self.add_tier( elect_tou_tier(5, 11, 0.21, 10, 4) )
        self.add_tier( elect_tou_tier(12, 17, 0.48, 5, 9) )
        self.add_tier( elect_tou_tier(12, 17, 0.21, 10, 4) )
        self.add_tier( elect_tou_tier(18, 11, 0.20, 5, 9) )
        self.add_tier( elect_tou_tier(18, 11, 0.21, 10, 4) )
        
    
    def add_tier(self, tou_tier):
        self.tiers.append( tou_tier )
        
    def get_rate(self, dt):
        pass
        # pass in a "datetime" object
        
    def get_ave_rate(self):
        # TODO: Do the actual average based on usage
        return self.tiers[0].dollars_per_kwh
        