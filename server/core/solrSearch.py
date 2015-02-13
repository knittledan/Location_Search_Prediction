#! /usr/bin/env python
#------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# tailswitch
#------------------------------------------------------------------------------
from config.serverConfig import ServerConfig
from controller.solr.solrServer import SolrServer
from controller.solr.search.locationLookup import LocationLookup

import time
from pprint import pprint

server = ServerConfig()
solr   = SolrServer()

#------------------------------------------------------------------------------
# exposed methods
#------------------------------------------------------------------------------

def startSolrServer():
    """
    Starts the solr server in a new thread.
     server url http://127.0.0.1:8983/solr
    """
    solr.start()
    time.sleep(4)

def locationSerach():
    """
    Search the solr locationData database for a given location.
    format as zipcode, city, or zipcode & city
    """
    startSolrServer()
    test = LocationLookup("localhost", 8983, "locationData")

    # example code

    test.search("mount washington")
    results1 = test.results.documents
    test.search("89506 ren")
    results2 = test.results.documents
    test.search("monica")
    results3 = test.results.documents
    test.search("90016")
    results4 = test.results.documents
    test.search("dieg")
    results5 = test.results.documents
    print('\n-------------------\n')
    pprint(results1)
    print("\n---------------------\n")
    pprint(results2)
    print("\n---------------------\n")
    pprint(results3)
    print("\n---------------------\n")
    pprint(results4)
    print("\n---------------------\n")
    pprint(results5)
locationSerach()
