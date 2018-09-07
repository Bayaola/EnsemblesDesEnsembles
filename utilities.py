#! /usr/bin/env Python
# -*- coding: utf-8 -*-
# Author    : Batouré Bamana Apollinaire
# Date      : 30/03/2017
# Purpose   : utilities


def rename_dimension():
    response = input("Rename dimension? (1) yes or (0) no: ")
    if response == "1":
        return True
    elif response == "0":
        return False


def add_attribute_to_dim():
    response = input("Add attributes? (1) yes or (0) no: ")
    if response == "1":
        return True
    elif response == "0":
        return False


def OK(attribute):

    response = input("Does the " + "\"" + attribute + "\"" + " attribute require modifications?" + " (1) oui or (0) non? ")
    return response


def f(attrib, part_i):
    response = input(attrib + " | this attribute describes " + str(part_i) + " (1) yes or (0) no? ")
    return response


def union(a, b):
    """union of two lists"""
    return a + [e for e in b if e not in a]


def print_partitions(partitions):
    """print partitions"""
    to_print = []
    for elt in partitions:
        to_print.append(elt.nom + ": " + str(elt.content))
    print("Partitions: ", to_print)


def print_dimensions(dimensions):
    """print dimensions"""
    to_print = []
    for elt in dimensions:
        to_print.append(elt.nom + ": " + str(elt.content))
    print("Dimensions: ", to_print)


class Partition(object):
    """Define a partition"""
    def __init__(self, nom=""):
        self.nom = nom
        self.content = []

    def __str__(self):
        return "Partition name: " + self.nom + " Content: " + str(self.content)

    def set_nom(self, nom):
        self.nom = nom

    def get_nom(self):
        return self.nom

    def set_content(self, content):
        self.nom = content

    def get_content(self):
        return self.content

    def append_element(self, elt):
        self.content.append(elt)

    def get_len(self):
        return len(self.content)

    def insert_element(self, idx, elt):
        self.content.insert(idx, elt)


class Dimension(object):
    """Define a partition"""

    def __init__(self, nom=""):
        self.nom = nom
        self.content = []

    def __str__(self):
        return "Dimension name: " + self.nom + " Content: " + str(self.content)

    def set_nom(self, nom):
        self.nom = nom

    def get_nom(self):
        return self.nom

    def set_content(self, content):
        self.nom = content

    def get_content(self):
        return self.content

    def append_element(self, elt):
        self.content.append(elt)

    def insert_element(self, idx, elt):
        self.content.insert(idx, elt)
