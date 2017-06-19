#!/usr/bin/env python

# PeerJ search handler
# PeerJ does not have an API, but after playing with the site I discovered
# that request can be sent to https://peerj.com/articles/index.json to
# receive the JSON-formatted list of results
# 
# Copyright 2017, Krzysztof Kutt

import json
import urllib.parse
import urllib.request


def perform_search(query_string):
    """
    Performs search with given query_string
    :param query_string: list of terms to search
    :return: json response with details
    """

    # prepare the basic search query
    search_data = dict()
    search_data['q'] = query_string

    url_base = 'https://peerj.com/articles/index.json'
    full_url = url_base + '?' + urllib.parse.urlencode(search_data)

    # post the query
    search_response = urllib.request.urlopen(full_url)
    response_xml = search_response.read().decode('utf-8')
    return response_xml


def handle_doc(doc):
    """
    Handles the json node representing one document in results
    :param doc: json node with document data
    :return: nothing
    """
    print("Title: {}".format(doc['title']))
    print("Authors: ", end="")
    print(doc['author']) if isinstance(doc['author'], str) \
                         else print(" and ".join(doc['author']))
    print("DOI: {}".format(doc['doi'])) if 'doi' in doc else print("DOI not "
                                                                   "available")


def handle_response(response_text):
    """
    Handles json response to extract the articles data
    :param response_text: string with json response from ScienceDirect 
    :return: nothing
    """
    response = json.loads(response_text)
    print(response)

    for doc in response['_items']:
        handle_doc(doc)
        print('---------------------------')


if __name__ == '__main__':
    response_json = perform_search("asthma leukotrienes")
    handle_response(response_json)
