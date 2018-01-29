# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:21:24 2018

@author: marieke
"""



"""
truck a
	capacity = 9
	cost = 100
	cost_per_package = 11,111
	amount = 20
	total_package_amount = 180

truck b
	capacity = 13
	cost = 300
	cost_per_package = 23,077
	amount = 7
	total_package_amount = 133

truck c
	capacity = 15
	cost = 500
	cost_per_package = 33,333
	amount = 4
	total_package_amount = 60

truck d
	capacity = 18
	cost = 1000
	cost_per_package = 55,556
	amount = 2
	total_package_amount = 36
  
  
Since cost_per_package raises significantly with each bigger truck, it makes sense to first use up all the small trucks (truck a),
then go to truck b and so forth.
A bigger truck will only save us money if the truck costs plus exit edge cost plus truck cost and entry edge cost are bigger
than the cost of the bigger truck plus edge to connect the routes.
We can calculate that, but I'm not sure if it's worth it. Instead, we could just look at how many packages there are to be
delivered all together, then fill that up with truck a, go to truck b etc., and send out respective ant colonies to find routes.
For example, if there are 300 packages, we can get done without truck d so we don't need a colony for that.


###
def trucks_used():
	if total_packages > 409:
		print("too many packages")
		
	if total_packages <= 180:
		only use truck a
		
	if total_packages <= 313:
		while packages_delivered < 180:
			use truck a
		use truck b
		
	if total_packages <= 373:
		while packages_delivered < 313:
			use truck a and b
		use truck c
	else:
		while packages_delivered < 373:
			use truck a, b and c
		use truck d

 """
