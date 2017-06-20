#!/usr/bin/env python

# Web of Science search handler through SOAP WoS API
# For more information see:
# http://ip-science.interest.thomsonreuters.com/data-integration
#
# Requires username and password to access the service
# 
# Copyright 2017, Krzysztof Kutt

import zeep
from xml.etree import ElementTree


AUTH_URL = "http://search.webofknowledge.com/esti/wokmws/ws" \
           "/WOKMWSAuthenticate?wsdl"
auth_client = None
session_id = None


def wos_login():
    global auth_client, session_id
    auth_client = zeep.Client(wsdl=AUTH_URL)
    session_id = auth_client.service.authenticate()
    print("Session ID: {}".format(session_id))
    pass


def wos_logout():
    global auth_client, session_id
    if auth_client is not None:
        print(auth_client.service.closeSession())
    pass


def perform_search(query_string):
    """
    Performs search in PubMed with given query_string (exemplary query 
    string: 'asthma[mesh] AND leukotrienes[mesh] AND 2009[pdat]')
    :param query_string: list of terms to search
    :return: xml response with details (from summary service)
    """

    # prepare the basic search query
    # search_data = dict()
    # search_data['db'] = DATABASE
    # search_data['usehistory'] = 'y'
    # search_data['term'] = query_string
    #
    # url_base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
    # search_service = 'esearch.fcgi'
    # summary_service = 'esummary.fcgi'
    #
    # full_url = url_base + search_service + '?' + \
    #            urllib.parse.urlencode(search_data)
    #
    # # post the query
    # with urllib.request.urlopen(full_url) as search_response:
    #     # get WebEnv and QueryKey
    #     response_xml = search_response.read().decode('utf-8')
    #     web_env = re.search('<WebEnv>(\S+)</WebEnv>', response_xml).group(1)
    #     query_key = re.search('<QueryKey>(\d+)</QueryKey>',
    #                           response_xml).group(1)
    #
    #     # prepare the second query to receive the details
    #     summary_data = dict()
    #     summary_data['db'] = DATABASE
    #     summary_data['query_key'] = query_key
    #     summary_data['WebEnv'] = web_env
    #
    #     full_url = url_base + summary_service + '?' + \
    #                urllib.parse.urlencode(summary_data)
    #
    #     with urllib.request.urlopen(full_url) as response:
    #         response_xml = response.read().decode('utf-8')
    #         return response_xml
    pass


def handle_doc(doc):
    """
    Handles the xml node representing one document in results
    :param doc: xml node with document data
    :return: nothing
    """
    # print("Title: {}".format(doc.findall('./Item[@Name="Title"]')[0].text))
    # print("Authors: ", end="")
    # for author in doc.findall('./Item[@Name="AuthorList"]/'):
    #     print(author.text, end=", ")
    # print()
    # doi = doc.findall('./Item[@Name="DOI"]')
    # if len(doi):
    #     print("DOI: {}".format(doi[0].text))
    # else:
    #     print("DOI not available")
    pass


def handle_response(response_text):
    """
    Handles xml response to extract the articles data
    :param response_text: string with xml response 
    :return: nothing
    """
    # response = ElementTree.fromstring(response_text)
    #
    # for doc in response.findall('DocSum'):
    #     handle_doc(doc)
    #     print('---------------------------')
    pass


if __name__ == '__main__':
    wos_login()
    # query_string = 'asthma AND leukotrienes'
    # response_xml = perform_search(query_string)
    # handle_response(response_xml)
    # wos_logout()
