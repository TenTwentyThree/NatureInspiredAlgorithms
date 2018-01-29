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

truck b
	capacity = 13
	cost = 300
	cost_per_package = 23,077
	amount = 7

truck c
	capacity = 15
	cost = 500
	cost_per_package = 33,333
	amount = 4

truck d
	capacity = 18
	cost = 1000
	cost_per_package = 55,556
	amount = 2
  
  
Since cost_per_package raises significantly with each bigger truck, it makes sense to first use up all the small trucks (truck a),
then go to truck b and so forth.
A bigger truck will only save us money if the truck costs plus exit edge cost plus truck cost and entry edge cost are bigger
than the cost of the bigger truck plus edge to connect the routes.
We can calculate that, but I'm not sure if it's worth it. Instead, we could just look at how many packages there are to be
delivered all together, then fill that up with truck a, go to truck b etc., and send out respective ant colonies to find routes.
For example, if there are 300 packages, we can get done without truck d so we don't need a colony for that.


###

Pseudocode

 """
