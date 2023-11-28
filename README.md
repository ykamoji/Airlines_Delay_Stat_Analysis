About Project


About Dataset

Source: https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp

Flight delay data collected for the latest 6 months on below airlines and airports:

1. Airlines:
   1. American Airlines Inc. (AA)
   2. Delta Air Lines Inc. (UA )
   3. Delta Air Lines Inc. (DL)
   4. Envoy Air (MQ)


2. Airports:
   1. Boston, MA: Logan International (BOS)
   2. New York, NY: John F. Kennedy International (JFK)
   3. Washington, DC: Ronald Reagan Washington National (DCA)
   4. Los Angeles, CA: Los Angeles International (LAX)

A flight is considered delayed when it arrived 15 or more minutes than the schedule. 
Delayed minutes are calculated for delayed flights only. (Updated) Early arrivals and departures 
are shown in negative minutes.

Data Dictionary

1. DAY_OF_WEEK → 1 (Monday) - 7 (Sunday)
2. FL_DATE → Scheduled date 
3. OP_UNIQUE_CARRIER → Unique carrier code 
4. ORIGIN_AIRPORT_ID -> Origin IATA code
5. ORIGIN  -> IATA(International Air Transport Association) airport code
5. DEST_AIRPORT_ID -> Destination IATA code
6. DEST -> Destination IATA code
7. DEP_DELAY -> Difference in minutes between scheduled and actual departure time (in minutes)
8. DEP_DEL15 -> Indicates delay in departure (0 = No, 1 = Yes)
9. ARR_DELAY -> Difference in minutes between scheduled and actual arrival time
10. ARR_DEL15 -> Indicates delay in arrival (0 = No, 1 = Yes)
11. ACTUAL_ELAPSED_TIME -> Actual time an airplane spends in the air(in minutes) with TaxiIn/Out
12. AIR_TIME -> Flight Time (in minutes)
13. DISTANCE -> Distance between airports (miles)
14. CARRIER_DELAY -> Flight delay due to carrier(e.g. maintenance or crew problems, aircraft cleaning, fueling, etc), 0 = No, yes = (in minutes)
15. WEATHER_DELAY -> Flight delay due to weather, 0 = No, yes = (in minutes)
16. NAS_DELAY -> Flight delay by NSA(National Aviation System), 0 = No, yes = (in minutes)
17. SECURITY_DELAY -> Flight delay by this reason, 0 = No, yes = (in minutes)
18. LATE_AIRCRAFT_DELAY -> Flight delay by this reason, 0 = No, yes = (in minutes)




