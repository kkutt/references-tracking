#!/usr/bin/env python

# arXiv search handler using URL Request to arXiv API
# For more information see: https://arxiv.org/help/api/index
# 
# Copyright 2017, Krzysztof Kutt

import feedparser
import urllib.parse
import urllib.request


def perform_search(query_string) -> str:
    """
    Performs search with given query_string
    :param query_string: list of terms to search
    :return: atom response with details
    """

    # prepare the basic search query
    search_data = dict()
    search_data['search_query'] = query_string
    search_data['max_results'] = 10
    search_data['start'] = 0

    url_base = 'http://export.arxiv.org/api/query'
    full_url = url_base + '?' + urllib.parse.urlencode(search_data)

    # post the query
    search_response = urllib.request.urlopen(full_url)
    response_atom = search_response.read().decode('utf-8')
    return response_atom


def handle_doc(doc) -> None:
    """
    Handles the xml/atom node representing one document in results
    :param doc: xml/atom node with document data
    :return: nothing
    """
    print("Title: {}".format(doc['title'].replace('\n', '').replace('\r', '')))
    print("Authors: ", end="")
    for author in doc['authors']:
        print("{}".format(author['name']),
              end=" and ")
    print()
    if 'arxiv_doi' in doc:
        print("DOI: {}".format(doc['arxiv_doi']))
    else:
        print("DOI not available")


def handle_response(response_text) -> None:
    """
    Handles xml/atom response to extract the articles data
    :param response_text: string with xml/atom response 
    :return: nothing
    """
    response = feedparser.parse(response_text)

    for doc in response['entries']:
        handle_doc(doc)
        print('---------------------------')


if __name__ == '__main__':
    response_atom = perform_search("asthma leukotrienes")
    # response_atom = dummy_search()
    handle_response(response_atom)
