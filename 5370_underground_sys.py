'''
Implement the class UndergroundSystem that supports three methods:

1. checkIn(int id, string stationName, int t)

A customer with id card equal to id, gets in the station stationName at time t.
A customer can only be checked into one place at a time.
2. checkOut(int id, string stationName, int t)

A customer with id card equal to id, gets out from the station stationName at time t.
3. getAverageTime(string startStation, string endStation)

Returns the average time to travel between the startStation and the endStation.
The average time is computed from all the previous traveling from startStation to endStation that happened directly.
Call to getAverageTime is always valid.
You can assume all calls to checkIn and checkOut methods are consistent. That is, if a customer gets in at time t1 at some station, then it gets out at time t2 with t2 > t1. All events happen in chronological order.
'''
class UndergroundSystem(object):

    def __init__(self):
        self.in_flight = dict()
        self.t_times = dict()

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.in_flight[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        s_s, t_s = self.in_flight[id]
        del self.in_flight[id]
        tup = (s_s, stationName)
        if tup in self.t_times:
            self.t_times[tup].append(t-t_s)
        else:
            self.t_times[tup] = [t-t_s]

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        tup = (startStation, endStation)
        if tup in self.t_times:
            return sum(self.t_times[tup]) / len(self.t_times[tup])
        return 0

undergroundSystem = UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);
undergroundSystem.checkOut(27, "Waterloo", 20);
undergroundSystem.checkOut(32, "Cambridge", 22);
print undergroundSystem.getAverageTime("Paradise", "Cambridge");       # return 14.0. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
print undergroundSystem.getAverageTime("Leyton", "Waterloo");          # return 11.0. There were two travels from "Leyton" to "Waterloo", a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.0
undergroundSystem.checkIn(10, "Leyton", 24);
print undergroundSystem.getAverageTime("Leyton", "Waterloo");          # return 11.0
undergroundSystem.checkOut(10, "Waterloo", 38);
print undergroundSystem.getAverageTime("Leyton", "Waterloo");          # return 12.0
