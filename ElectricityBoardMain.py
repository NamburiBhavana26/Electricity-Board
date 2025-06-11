class ElectricityBoardMain:
    def __init__(self):
        self.__electricityMap = {}

    def get_electricityMap(self):
        return self.__electricityMap

    def set_electricityMap(self, electricity_map):
        self.__electricityMap = electricity_map

    def findCountOfConnectionsBasedOnTheConnectionType(self, connectionType):
        count = 0
        for value in self.__electricityMap.values():
            if value.lower() == connectionType.lower():
                count += 1
        return count if count > 0 else -1

    def findConnectionIdsBasedOnTheConnectionType(self, connectionType):
        result = []
        for key, value in self.__electricityMap.items():
            if value.lower() == connectionType.lower():
                result.append(key)
        return result
