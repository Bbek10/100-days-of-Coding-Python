class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
      """
        Constructor for initializing a new flight data instance with specific travel details.
        Parameters:
        - price: The cost of the flight.
        - origin_airport: The IATA code for the flight's origin airport.
        - destination_airport: The IATA code for the flight's destination airport.
        - out_date: The departure date for the flight.
        - return_date: The return date for the flight.
        """
      self.price = price
      self.origin_airport = origin_airport
      self.destination_airport = destination_airport
      self.out_date = out_date
      self.return_date = return_date
   
    def find_cheapest_flight(self, origin_city_code, destination_city_code, from_time, to_time):
       
         """
    Parses flight data received from the Amadeus API to identify the cheapest flight option among
    multiple entries.
    Args:
        data (dict): The JSON data containing flight information returned by the API.
    Returns:
        FlightData: An instance of the FlightData class representing the cheapest flight found,
        or a FlightData instance where all fields are 'NA' if no valid flight data is available.
    This function initially checks if the data contains valid flight entries. If no valid data is found,
    it returns a FlightData object containing "N/A" for all fields. Otherwise, it starts by assuming the first 
    flight in the list is the cheapest. It then iterates through all available flights in the data, updating
     the cheapest flight details whenever a lower-priced flight is encountered. The result is a populated 
     FlightData object with the details of the most affordable flight.
    """
         
         pass