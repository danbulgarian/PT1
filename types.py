annualUsers14 = 130*1000
years = 5
totalUsers5yrs = annualUsers * years
print ("Total users over the last 5 years: {:,} million.".format(totalUsers5yrs))
averageDataUsage = 2
totalOfUsedSpaceinMB = totalUsers5yrs * averageDataUsage
print ("Total MB of used space: {:,} MB, or {:,} GB.".format(totalOfUsedSpaceinMB, totalOfUsedSpaceinMB/1024 ))

