# Python 3
 
 
 
import matplotlib.pyplot as plt
import numpy   as np
 
 
limit=100
quantity1 = np.linspace(0, limit, 100)
quantity2 = np.linspace(0, limit, 100)
marginal_cost  =   150-  3*quantity1   +.06*quantity1**(2)
total_cost = 150*quantity1- 1.5*quantity1*2 + .02*quantity1**3
 


fig1, (ax1,ax2) = plt.subplots(2 )
fig1.set_size_inches(2, 4)
plt.subplots_adjust(hspace = .5)
 
ax1.set_xlabel("Quantity")
ax1.text(-70, 10000 ,"Total\nCost\nin\nDollars", fontsize = 10)
ax1.set_xlim(0,100 ) 
ax1.set_ylim(0,35000 ) 
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.set_yticks([0,10000,20000,30000])

 

ax1.plot(quantity1,total_cost) 
ax2.plot(quantity2,  marginal_cost) 
ax2.set_xlabel("Quantity")
ax2.set_xlim(0,100 ) 
ax2.set_ylim(0,450 )    
ax2.text(-70,100 ,"Marginal\nCost\nin\nDollars\nper\nUnit", fontsize = 10)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

 
plt.savefig("marginal_cost1.png", bbox_inches = "tight")
#That's the end. 