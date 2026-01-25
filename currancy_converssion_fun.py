#WAF to conver USD into rupees
def converter(usd_val):
    rs_val=usd_val*85
    print(usd_val,"USD=","RS",rs_val)
  
converter(int(input("enter ammount:")))