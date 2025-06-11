from ElectricityBoardMain import ElectricityBoardMain

if __name__ == "__main__":
    eb = ElectricityBoardMain()
    electricity_map = {}

    n = int(input("Enter the number of connection records to be added\n"))
    print("Enter the connection records (ConnectionId:Connectiontype)")
    for _ in range(n):
        record = input()
        if ':' in record:
            conn_id, conn_type = record.split(":")
            electricity_map[conn_id.strip()] = conn_type.strip()

    eb.set_electricityMap(electricity_map)

    search_type = input("Enter the Connection type to be searched\n")
    count = eb.findCountOfConnectionsBasedOnTheConnectionType(search_type)
    if count == -1:
        print(f"No Connection Ids were found for {search_type}")
    else:
        print(f"The count of connection Ids based on {search_type.upper()} are {count}")

    filter_type = input("Enter the Connection type to identify the Connection Ids\n")
    filtered = eb.findConnectionIdsBasedOnTheConnectionType(filter_type)
    if not filtered:
        print(f"No Connection Ids were found for the {filter_type}")
    else:
        print(f"Connection Ids based on the {filter_type.upper()} are")
        for conn_id in filtered:
            print(conn_id)
