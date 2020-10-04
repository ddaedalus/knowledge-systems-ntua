from rdflib import URIRef, Literal, Namespace, Graph
from rdflib.namespace import RDF

import pandas as pd

# Define the namespace for geo coordinates
GEO = Namespace("http://www.openlinksw.com/schemas/virtrdf#Geometry") 

# Read csv files
dataset_routes = pd.read_csv("/home/ddaedalus/Downloads/gnwsi/routes.txt")
dataset_stops = pd.read_csv("stops.txt")
dataset_trips = pd.read_csv("trips.txt")
dataset_stop_times = pd.read_csv("stop_times.txt")

# Classes
bus = Namespace("http://www.ex.org/ontologyEL15187/Bus") 
route_bus = Namespace("http://www.ex.org/ontologyEL15187/RouteBus") 
station_bus = Namespace("http://www.ex.org/ontologyEL15187/StationBus") 
trip_bus = Namespace("http://www.ex.org/ontologyEL15187/TripBus") 

# Object properties
fulfils_route = Namespace("http://www.ex.org/ontologyEL15187/fulfilsRouteBus") 
fulfils_trip = Namespace("http://www.ex.org/ontologyEL15187/fulfilsTripBus")   
has_station = Namespace("http://www.ex.org/ontologyEL15187/hasStationBus") 
route_has_trip = Namespace("http://www.ex.org/ontologyEL15187/routeBusHasTripBus") 

# Data properties
station_located_at = Namespace("http://www.ex.org/ontologyEL15187/stationBusIsLocatedAt") 
station_name = Namespace("http://www.ex.org/ontologyEL15187/stationBusHasName") 
trip_stop_time = Namespace("http://www.ex.org/ontologyEL15187/tripBusHasStopTime")  
station_stop_time = Namespace("http://www.ex.org/ontologyEL15187/stationBusStopTime") 
route_name = Namespace("http://www.ex.org/ontologyEL15187/routeBusHasName")
trip_name = Namespace("http://www.ex.org/ontologyEL15187/tripBusHasName") 

mygraph1 = Graph() # initialiaze an RDF graph for classes
mygraph2 = Graph() # initialiaze an RDF graph for object properties
mygraph3 = Graph() # initialiaze an RDF graph for data properties

# Fill the graphs
for _, row in dataset_routes.iterrows():
    mygraph1.add((URIRef(bus + "/" + row[1]), RDF.type, URIRef(bus))) 
    mygraph1.add((URIRef(route_bus + "/" + row[0]), RDF.type, URIRef(route_bus))) 
    mygraph2.add((URIRef(bus + "/" + row[1]), URIRef(fulfils_route), URIRef(route_bus + "/" + row[0]))) 
    mygraph3.add((URIRef(route_bus + "/" + row[0]), URIRef(route_name), Literal(row[2]))) 

for _, row in dataset_stops.iterrows():
    mygraph1.add((URIRef(station_bus + "/" + str(row[0])), RDF.type, URIRef(station_bus))) 
    mygraph3.add((URIRef(station_bus + "/" + str(row[0])), URIRef(station_located_at), 
                        Literal("POINT("+str(row[4]) + " " + str(row[5]) + ")", datatype = GEO)))  
    mygraph3.add((URIRef(station_bus + "/" + str(row[0])), URIRef(station_name), Literal(row[2]))) 

for _, row in dataset_trips.iterrows():
    mygraph1.add((URIRef(trip_bus + "/" + str(row[2])), RDF.type, URIRef(trip_bus))) 
    mygraph2.add(((URIRef(route_bus + "/" + row[0])), URIRef(route_has_trip), URIRef(trip_bus + "/" + row[2])))
    mygraph2.add((URIRef(bus + "/" + row[0].split("-")[0]), URIRef(fulfils_trip), URIRef(trip_bus + "/" + str(row[2])))) 
    mygraph3.add((URIRef(trip_bus + "/" + row[2]), URIRef(trip_name), Literal(row[3]))) 

for _, row in dataset_stop_times.iterrows():
    mygraph2.add((URIRef(trip_bus + "/" + str(row[0])), URIRef(has_station), URIRef(station_bus + "/" + str(row[3])))) 
    mygraph3.add((URIRef(trip_bus + "/" + row[0]), URIRef(trip_stop_time), Literal(row[1]))) 
    mygraph3.add((URIRef(station_bus + "/" + str(row[3])), URIRef(station_stop_time), Literal(row[1]))) 

mygraph1.serialize('rdf_classes.ttl', format='turtle')
mygraph2.serialize('rdf_object_properties.ttl', format='turtle')
mygraph3.serialize('rdf_data_properties.ttl', format='turtle')
