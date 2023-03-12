# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 15:24:05 2023

@author: Besher
"""

from py2neo import Graph, Node, Relationship
import requests
from lxml import etree
import xml.etree.ElementTree as ET

graph = Graph("bolt://localhost:7687", auth=("besher", "00000000"))
tree = ET.parse('protien.xml')
root = tree.getroot()




tree = ET.parse('protien.xml')
root = tree.getroot()

# Iterate over each protein entry in the XML file
for entry in root.findall('{http://uniprot.org/uniprot}entry'):
   print("test")
    
   protein_accession = entry.find('{http://uniprot.org/uniprot}accession').text
   protein_name = entry.find('{http://uniprot.org/uniprot}name').text
   protein_node = Node("Protein", accession =protein_accession, name=protein_name)
   graph.create(protein_node)
   
   
   for protien in entry.find('{http://uniprot.org/uniprot}protein'):
   
       if ("recommendedName" in protien.tag ):
           fullName = protien.find('{http://uniprot.org/uniprot}fullName').text
           shortName = protien.find('{http://uniprot.org/uniprot}shortName').text         
           fullName_node = Node("fullName", fullName =fullName)
           shortName_node = Node("shortName", shortName =shortName)
           graph.create(fullName_node)
           graph.create(shortName_node)
           graph.create(Relationship(protein_node, "has_fullname", fullName_node))
           graph.create(Relationship(protein_node, "has_shortname", shortName_node))

   for gene in entry.find('{http://uniprot.org/uniprot}gene'): 
                         
           gene_name = gene.text             
           gene_name_node = Node("gene", gene_name =gene_name) 
           graph.create(gene_name_node)
           graph.create(Relationship(protein_node, "has_gene", gene_name_node, status = gene.attrib["type"]))
       
           
   for reference in entry.findall('{http://uniprot.org/uniprot}reference'):  
     
           type_name = reference.find('{http://uniprot.org/uniprot}citation').attrib["type"]
           date = reference.find('{http://uniprot.org/uniprot}citation').attrib["date"]  
                                
           reference_node = Node("reference", type_name =type_name,date=date)
           graph.create(reference_node)       
           graph.create(Relationship(protein_node, "has_reference", reference_node))
 
           citation_obj = reference.find('{http://uniprot.org/uniprot}citation')
           authorlist_obj = citation_obj.find('{http://uniprot.org/uniprot}authorList')
           
           for author in authorlist_obj.findall('{http://uniprot.org/uniprot}person'):                  
                   name = author.attrib["name"]
                   author_node = Node(" author", name =name)
                   graph.create(author_node)
                   graph.create(Relationship(reference_node, "has_author", author_node))
               
               
               
           
           
          

           





