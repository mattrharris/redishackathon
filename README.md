# redishackathon
Welcome to the Redis Hackathon.

Have fun, get to meet new colleagues, explore some new technology and build some cool stuff!

The Python script will generate some dummy risk data for you to use but please feel free to experiment. You can adapt as required to suit your use case.

The teams are as follows:

BLUE TEAM
- James Cane
- Amelia Sommer
- Petteri Uronen
- Keith Walters
 
RED TEAM
- Tomas Pavli
- Marijn Huis
- Mattias Andersson
- LeeZsa Lim

GREEN TEAM
- Neofytos Mylona
- Anthony Dunford
- Weiping Miao
- Slava Sharashkin

PURPLE TEAM
- Simon Anderson
- Liam O'Shea
- Callie Hardt
- Pete Warnock

The challenges are:
1. What is the best Redis data structure to store risk data. Explore streams, lists, hash sets, json, etc. What's the relative performance of these options and can you quantify any pros and cons? Feel free to explore other options not mentioned 

2. What is the best way to aggregate and/or join data. E.g., RediSearch for aggregation. What other ways are there and how do they compare?
 
3. We need to ensure we do not lose messages and we want to minimise the time to recovery. What is the best resilience strategy? E.g., explore RDB + AOF, streams and custom code 

4. What is the best way to perform compound operations. For example, retrieving groups of data as items within a hashset or by storing as keys referenced in a set.  E.g., RedisGears, Custom Module, LUA script. What are the trade-offs and performance differences between the approaches? 

5. What is the best way to subscribe to changes e.g., RedisGears trigger, streams + custom code, pub/sub etc. Can you show Redis handling real-time data? 

6. What is the best way of optimising the space required for the cache but making older data available with reduced performance? E.g., Add cache miss operation to retrieve the data from disk if not found in cache. 

7. How does Redis handle concurrent read and writes – what is the best approach for handling both at scale? What causes Redis to break? This is a good one if you like breaking things! 
