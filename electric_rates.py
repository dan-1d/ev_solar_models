class elect_use_cost_tou:
    def __init__(self, rates, use):
        self.rates = rates
        self.use = use
    
    def total_cost(self):
        pass  #TODO



class elect_tou_tier:
    def __init__(self, start_time, end_time, dollars_per_kwh, 
                 start_month=1, end_month=12 ):
        # input start and end times and dates,  inclusive of effective tou tier
        self.start_time = start_time
        self.end_time = end_time
        self.dollars_per_kwh = dollars_per_kwh
        self.start_month = start_month
        self.end_month = end_month

    def get_dollars_per_kwh(self):
        return self.dollars_per_kwh
        
    def is_datetime_in_tier(self, dt):
        month_in = True
        hour_in  = True
        #print "tier: s/e months s/e hours    "+str(self.start_month)+"/"+str(self.end_month)+"   "+str(self.start_time)+"/"+str(self.end_time)
        #print "query: month="+str(dt.month)+"   hour="+str(dt.hour)
        if( self.start_month < self.end_month ):
            if( dt.month < self.start_month or dt.month > self.end_month ):
                month_in = False
        elif( self.start_month > self.end_month ):
            if( dt.month < self.start_month and dt.month > self.end_month):
                month_in = False

        if( self.start_time < self.end_time ):
            if( dt.hour < self.start_time or dt.hour > self.end_time):
                hour_in = False
        elif( self.start_time > self.end_time ):
            if( dt.hour < self.start_time and dt.hour > self.end_time):
                hour_in = False

       # print "inmonth?="+str(month_in)+"    inhour?="+str(hour_in)
        return (month_in & hour_in)

        
        
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
        self.add_tier( elect_tou_tier(18, 23, 0.20, 5, 9) )
        self.add_tier( elect_tou_tier(18, 23, 0.21, 10, 4) )
        
    
    def add_tier(self, tou_tier):
        self.tiers.append( tou_tier )
        

    def get_rate(self, dt):
        # pass in a "datetime" object
        # search for rate for this datetime
        tiers_for_dt = list()  #this should only have one result
        for tier in self.tiers:
            #print "tier: "+str(tier)
            if( tier.is_datetime_in_tier(dt) ):
                tiers_for_dt.append(tier)
        assert(len(tiers_for_dt) < 2 )
        rate = tiers_for_dt[0].get_dollars_per_kwh()
        return rate
        
        
    def get_ave_rate(self):
        # TODO: Do the actual average based on usage
        return self.tiers[0].dollars_per_kwh
        