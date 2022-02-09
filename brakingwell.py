def dist(v, mu):
    # the distance is calculated from v and mu
    # first convert km/h to m/s
    speed_in_ms = v*(1000/(60*60))
    g = 9.81
    t=1
    d1=(speed_in_ms*speed_in_ms)/(2*mu*g)
    # plus we need to add how far the vehicle has travelled in the reaction time, which is 1 s
    # so as the speed is in meters per second in one second it will have travelled speed_in_ms times
    d1= d1+(t *speed_in_ms)
    return d1



def speed(d, mu):
    v=3
    return v