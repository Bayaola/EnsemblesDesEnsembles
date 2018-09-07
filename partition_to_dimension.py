#! /usr/bin/env Python
# -*- coding: utf-8 -*-
# Author    : Batouré Bamana Apollinaire
# Date      : 30/03/2017
# Purpose   : partitionning

from utilities import *
from partionning import partioning


# DIMENSION
def dimension(partitions):
    print("---- PARTITIONS TO DIMENSIONS ----\n")

    m = int(input("Enter the number of partitions: "))
    # dim = []
    dimensions = []

    for k in range(m):
        n = partitions[k].get_len()
        dim_k = Partition("dim_" + partitions[k].get_nom())
        print("\n--- WORKING ON " + partitions[k].get_nom())
        for i in range(n):
            att_i = partitions[k].content[i]
            if OK(att_i) == "0":
                dim_k.content = union(dim_k.content, [att_i])
            else:
                new_name = input("Enter new name: ")
                # rename att_i
                partitions[k].content[i] = new_name
                dim_k.content = union(dim_k.content, [new_name])

        if rename_dimension():
            new_name = input("Enter new name: ")
            dim_k.nom = "dim_" + new_name
        while add_attribute_to_dim():
            attribute_name = input("Enter attribute name: ")
            dim_k.append_element(attribute_name)
        # dim_k.append_element("pk_" + dim_k.get_nom())
        # set pk_ as first element
        dim_k.insert_element(0, "pk_" + dim_k.get_nom())
        dimensions.append(dim_k)

    return dimensions

# TESTS
if __name__ == "__main__":
    print_partitions(dimension(partioning()))
