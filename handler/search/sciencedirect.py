#!/usr/bin/env python

# ScienceDirect search handler using URL Requests to Search API
# Full description: https://api.elsevier.com/documentation/SCIDIRSearchAPI.wadl
#
# Requires API key
#
# Copyright 2017, Krzysztof Kutt

import json
import urllib.parse
import urllib.request

import config


def perform_search(query_string) -> str:
    """
    Performs search with given query_string
    :param query_string: list of terms to search
    :return: json response with details
    """

    # prepare the basic search query
    search_data = dict()
    search_data['apiKey'] = config.SCIENCEDIRECT_API_KEY
    search_data['query'] = query_string
    search_data['count'] = 10

    url_base = 'http://api.elsevier.com/content/search/scidir'
    full_url = url_base + '?' + urllib.parse.urlencode(search_data)

    # post the query
    search_response = urllib.request.urlopen(full_url)
    response_xml = search_response.read().decode('utf-8')
    return response_xml


def handle_doc(doc) -> None:
    """
    Handles the dictionary representing one document in results
    :param doc: dictionary with document data
    :return: nothing
    """
    print("Title: {}".format(doc['dc:title']))
    print("Authors: ", end="")
    for author in doc['authors']['author']:
        print("{} {}".format(author['surname'], author['given-name']),
              end=" and ")
    print()
    if 'dc:identifier' in doc:
        print("DOI: {}".format(doc['dc:identifier']))
    else:
        print("DOI not available")


def handle_response(response_text) -> None:
    """
    Handles json response to extract the articles data
    :param response_text: string with json response 
    :return: nothing
    """
    response = json.loads(response_text)

    for doc in response['search-results']['entry']:
        handle_doc(doc)
        print('---------------------------')


if __name__ == '__main__':
    response_json = perform_search("asthma leukotrienes")
    handle_response(response_json)
