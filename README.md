# maps-graphs
Translate your local maps into graphs, recursively.

## Why?
This project was conceived as an attempt to represent a city's streets and intersections as a graph which allows a more organized handling of the information. In said graph, each node would correspond to the intersection of two streets.

The idea is to end up with a database similar to those that give support to navigating applications (e.g. Waze, Uber) but can be complemented with additional layers of information besides traffic (e.g. air pollution, criminality, noise disturbance). This last phase however, is not the scope of the presented project and its code. As a secondary objective, this project intends to introduce OSMApi as an effective tool to work and experiment with geospatial data.

## How is it made?
To achieve this, we needed to start with a robust source of road information. We decided to work with [OpenStreetMaps](https://www.openstreetmaps.org) and particularly with its API called OSMApi. This seemed to us as an excellent option since OSM is an open-sourced project which allows anyone to edit the maps of its city, guaranteeing much more precision and abundance of detail. Also, it’s API is very easy to learn and works with dynamic data structures like lists and dictionaries (json and xml) which simplified the job substantially.

In short, the code finds a single node for each intersection between two or more streets. The result are nodes connected with edges represented by streets between this two intersections. So, if street A is intersected by street B and then street C, this would create two nodes (intersection A-B, intersection A-C) and the edge that joins them would represent street A. Finally, in the visual representation provided in this code, one can effectively check that each node (symbolized by a marker-pin) drops exactly into the intersections of the streets.

## How does it work?
1. The application starts with **intersections.py** which uses *osmapi* to extract all the ways and nodes of a given region indicated by 4 coordinates which generate a bounding box.
  - Right now the coordinates refer to district of Jesus Maria in Lima, Peru, but this can be changed to whatever coordinates the user desires. (*Caution: Beware of requesting a very large bounding box*)

2. Once we have an array of all the streets and it’s attributes as well as the nodes inside the bounding box, (which are presented in a json format), **intersections.py** proceeds to apply a couple of filters to make sure that we remain only with the ways that correspond, in effect, to streets (and not footways, cycleways, etc)

3. After this verification has been made, the next lines of code are in charge of performing the most important task of the program which is finding the streets that intersect each other.
  - This is accomplished by looking for the streets that share the same node. 3 nested for-loops: the first one iterates through the ways of the bounding box and saves the nodes they hold. On the second for-loop, a query is made for each node that was saved, getting all the ways that they are part of. And finally, the last loop searches for nodes that appear in two different ways.

## What's next?

As was mentioned earlier, the next step would be to start adding layers of information to the graph. This could be done by linking this graph to other sources of data like different types of sensors positioned throughout the city and in a predetermined intersection (node in our graph). Given this information, the application could start fulfilling tasks like: find the fastest way between point A and point B, or the less contaminated way, or the safest way. It all depends on the data that is fed into the model and how it is going to be used.

We consider [NetworkX](https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html
) a great option for that.

## Credits
This project was made possible by Faculty of Engineering at Universidad del Pacífico in Lima, Perú. Especially by professors: Hugo Alatrista Salas, PhD; Miguel Nuñez del Prado Cortez, PhD; Ana Eugenia Luna Adan, PhD.

As well as students: Juan Diego Gonzales Morales, Gonzalo Herrera Medina and Carlos Fabbri Garcia, who contributed by helping with the code and by providing different ways of approaching the problem.

## License
MIT
