#!/usr/bin/env python

import argparse
import gzip
import h5py
import hdf5plugin

def parse_arguments(args=None):
    parser = argparse.ArgumentParser(description='Extract correction factors from a HiCExplorer .h5 file')
    parser.add_argument('input_h5', help='input HiCExplorer .h5 file')
    parser.add_argument('output_bedGraph', help='output .bedGraph.gz file')
    parser.add_argument('--read-coverage', help='extract read coverage instead of correction factors', default=False, action='store_true')
    return parser.parse_args(args)

def main(args=None):
    args = parse_arguments(args)

    h5 = h5py.File(args.input_h5, 'r')
    out = gzip.open(args.output_bedGraph, "wt")

    if args.read_coverage:
        for row in zip(
            [x.decode("utf-8") for x in h5['intervals']['chr_list'][:]],
            h5['intervals']['start_list'][:],
            h5['intervals']['end_list'][:],
            h5['intervals']['extra_list'][:]):
                out.write('\t'.join(str(x) for x in row) + '\n')
    else:
        for row in zip(
            [x.decode("utf-8") for x in h5['intervals']['chr_list'][:]],
            h5['intervals']['start_list'][:],
            h5['intervals']['end_list'][:],
            h5['correction_factors'][:, 0]):
                out.write('\t'.join(str(x) for x in row) + '\n')

    out.close()

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
