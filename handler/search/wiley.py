#!/usr/bin/env python

# wiley
# 
# Copyright 2017, Krzysztof Kutt

import json
import urllib.parse
import urllib.request

import config


def perform_search(query_string):
    """
    Performs search with given query_string
    :param query_string: list of terms to search
    :return: json response with details
    """

    # prepare the basic search query
    search_data = dict()
    search_data['query'] = query_string

    search_headers = dict()
    search_headers['CR-Clickthrough-Client-Token'] = config.WILEY_API_KEY
    # FIXME Does not work - even if I accepted the Wiley license, it still
    # shows an error message...

    url_base = 'https://api.wiley.com/onlinelibrary/tdm/v1/articles/10.1002%2Fcbic.201300351'
    full_url = url_base + '?' + urllib.parse.urlencode(search_data)

    # post the query
    search_response = urllib.request.urlopen(urllib.request.Request(
        url_base, headers=search_headers))
    response_xml = search_response.read().decode('utf-8')
    print(response_xml)
    return response_xml


def handle_doc(doc):
    """
    Handles the dictionary representing one document in results
    :param doc: dictionary with document data
    :return: nothing
    """
    # print("Title: {}".format(doc['dc:title']))
    # print("Authors: ", end="")
    # for author in doc['authors']['author']:
    #     print("{} {}".format(author['surname'], author['given-name']),
    #           end=" and ")
    # print()
    # if 'dc:identifier' in doc:
    #     print("DOI: {}".format(doc['dc:identifier']))
    # else:
    #     print("DOI not available")
    pass


def handle_response(response_text):
    """
    Handles json response to extract the articles data
    :param response_text: string with json response 
    :return: nothing
    """
    # response = json.loads(response_text)
    #
    # for doc in response['search-results']['entry']:
    #     handle_doc(doc)
    #     print('---------------------------')
    pass


if __name__ == '__main__':
    response_json = perform_search("asthma leukotrienes")
    # handle_response(response_json)
