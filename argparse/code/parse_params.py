#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', action='store', dest='simple_value',
                        help='Store a simple value')

    parser.add_argument('-c', action='store', dest='constant_value',
                        help='Store a constant value')

    parser.add_argument('-t', action='store_true', default=False,
                        dest='boolean_switch',
                        help='Set a switch to true')

    parser.add_argument('-a', action='append', dest='collection',
                        default=[],
                        help='Add repeated values to a list')

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    results = parser.parse_args()
    print 'simple_value     =', results.simple_value
    print 'constant_value   =', results.constant_value
    print 'boolean_switch   =', results.boolean_switch
    print 'collection       =', results.collection
