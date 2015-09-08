class vehicle_ice:
    def __init__(self, name, mpg_hwy, mpg_city, average_override=None):
        self.mpg_hwy = mpg_hwy
        self.mpg_city = mpg_city
        self.name = name
        if average_override != None:
            self.mpg_hwy = average_override
            self.mpg_city = average_override
        
    def get_ave_mpg(self, fract_hwy=.50):
        return fract_hwy*self.mpg_hwy + (1-fract_hwy)*self.mpg_city
    
    
class vehicle_ev:
    def __init__(self, name, kwh_per_mile, charge_rate_kw=3.3):
        self.kwh_per_mile = kwh_per_mile
        self.charge_rate_kw = charge_rate_kw
        
    class get_charge_needs_hourly(self, total_charge_kwh):
        daily_charge_needs_kwh = total_charge_kwh
        daily_charge_hourly_df = pd.DataFrame()
        daily_charge_hourly_df["hour"] = np.arange(0,24,1)
        daily_charge_hourly_df["energy_kw"] = np.zeros(24)
        charge_rate_kw = self.charge_rate_kw

        charge_remaining = daily_charge_needs_kwh
        current_hour = 0  #midnight
        while charge_remaining > charge_rate_kw:
            daily_charge_hourly_df["energy_kw"]
            daily_charge_hourly_df.loc[daily_charge_hourly_df['hour'] == current_hour, "energy_kw"] = charge_rate_kw
            current_hour += 1
            charge_remaining -= charge_rate_kw
        # handle remaining charge for the fraction of an hour
        daily_charge_hourly_df.loc[daily_charge_hourly_df['hour'] == current_hour, "energy_kw"] = charge_remaining

        # print charge_remaining

        return daily_charge_hourly_df


class vehicle_usage:
    def __init__(self, miles_per_month, fract_hwy):
        self.miles_per_month = miles_per_month
        self.fract_hwy = fract_hwy

        
def gas_costs_per_month( miles_per_month, gas_dollars_per_gal, miles_per_gallon ):
    ## TODO: generalize so any input parameter can be a vector, and all combos are explored
    ## pass in: 
    ##   miles_per_month, miles_per_gallon: real number
    ##   numpy arrays, 
    ## Return: generate an ndarray
    ##
    dollars_per_month = miles_per_month * gas_dollars_per_gal * (1.0/miles_per_gallon)
    return dollars_per_month


def electr_cost_per_month( miles_per_month, ave_dollars_per_kwh, kwh_per_mile ):
    dollars_per_month = miles_per_month * ave_dollars_per_kwh * kwh_per_mile
    return dollars_per_month