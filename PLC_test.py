# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:17:07 2024


Let's talk to the PLC

@author: Pycomm Library
"""


from pycomm3 import LogixDriver

with LogixDriver('192.168.3.100') as plc:
    print(plc)
    
    
    
    #tag = plc.read('CF12A_PE1')
    
    #alarm_array = plc.
    #print(tag)
    
    # OUTPUT:
    # Program Name: PLCA, Device: 1756-L83E/B, Revision: 28.13

    #print(plc.info)
    # OUTPUT:
    # {'vendor': 'Rockwell Automation/Allen-Bradley', 'product_type': 'Programmable Logic Controller',
    #  'product_code': 166, 'version_major': 28, 'version_minor': 13, 'revision': '28.13', 'serial': 'FFFFFFFF',
    #  'device_type': '1756-L83E/B', 'keyswitch': 'REMOTE RUN', 'name': 'PLCA'}
    
    #HOPS Tags 
    
    
    
    """
    with LogixDriver('10.20.30.100') as plc:
    plc.read('tag1', 'tag2', 'tag3')  # read multiple tags
    plc.read('array{10}') # read 10 elements starting at 0 from an array
    plc.read('array[5]{20}) # read 20 elements starting at elements 5 from an array
    plc.read('string_tag')  # read a string tag and get a string
    plc.read('a_udt_tag') # the response .value will be a dict like: {'attr1`: 1, 'attr2': 'a string', ...}

    # writes require a sequence of tuples of [(tag name, value), ... ]
    plc.write('tag1', 0)  # single writes do not need to be passed as a tuple
    plc.write(('tag1', 0), ('tag2', 1), ('tag3', 2))  # write multiple tags
    plc.write(('array{5}', [1, 2, 3, 4, 5]))  # write 5 elements to an array starting at the 0 element
    plc.write('array[10]{5}', [1, 2, 3, 4, 5])  # write 5 elements to an array starting at element 10
    plc.write('string_tag', 'Hello World!')  # write to a string tag with a string
    plc.write('string_array[2]{5}', 'Write an array of strings'.split())  # write an array of 5 strings starting at element 2
    plc.write('a_udt_tag', {'attr1': 1, 'attr2': 'a string', ...})  # can also use a dict to write a struct

    # Check the results
    results = plc.read('tag1', 'tag2', 'tag3')
    if all(results):
        print('They all worked!')
    else:
        for result in results:
            if not result:
                print(f'Reading tag {result.tag} failed with error: {result.error}')
               
    """
    