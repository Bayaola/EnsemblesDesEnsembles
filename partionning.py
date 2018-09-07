#! /usr/bin/env Python
# -*- coding: utf-8 -*-
# Author    : Batouré Bamana Apollinaire
# Date      : 30/03/2017
# Purpose   : partitionning

from utilities import *


# PARTITIONING
def partioning():
    print("\n----       PARTITIONNING       ----\n")

    n = int(input("Enter the number of attributes non key of the UR: "))

    partitions = []

    # BEGIN
    attributes = []

    for i in range(n):
        rep = input("Enter attributes " + str(i+1) + ": ")
        attributes.append(rep)

    att1 = attributes[0]

    nom_part_1 = input("Enter the partition name for the first attribute " + att1 + ": ")

    part1 = Partition(nom_part_1)
    part1.content = [att1]

    partitions.append(part1)

    print(part1)
    print_partitions(partitions)
    # print partitions

    for i in range(1, n):
        control = False
        for k in range(len(partitions)):
            if f(attributes[i], partitions[k]) == "1":
                partitions[k].content = union(partitions[k].content, [attributes[i]])
                control = True
                print("Attribut: ", attributes[i])
                print(partitions[k])
                print_partitions(partitions)
                print("\n")
                break
        if control == False:
            partk_plus_1 = Partition(input("Enter Name of the new partition: "))
            partk_plus_1.content = [attributes[i]]
            partitions.append(partk_plus_1)
            print("Attribut ", i + 1)
            print(partk_plus_1)
            print_partitions(partitions)
            print("\n")

    return partitions

# TESTS
if __name__ == "__main__":
    print_partitions(partioning())
