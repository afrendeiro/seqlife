#! /usr/bin/env python

from Bio import Entrez


def fetchPublicationDate(pmid):
    """
    Get publication date of an article.
    """
    handle = Entrez.efetch(db='pubmed', id=pmid, retmode='xml')
    xml = Entrez.read(handle)[0]

    for time in xml['PubmedData']['History']:
        if time.attributes['PubStatus'] == "accepted":
            return (time["Year"], time["Month"], time["Day"])


def fetchCitations(pmid):
    """
    Get PMIDs of articles citing.
    """
    handle = Entrez.efetch(db='pubmed', id=pmid, retmode='xml')
    xml = Entrez.read(handle)[0]
    
    cites = list()

    for cite in xml['MedlineCitation']["CommentsCorrectionsList"]:
        cites.append(str(cite['PMID']))

    return cites


Entrez.email = ""
