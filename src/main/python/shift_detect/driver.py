#!/usr/bin/env python
# -*- c-file-style: "sourcery" -*-
#
# Use and distribution of this software and its source code is governed
# by the terms and conditions defined in the "LICENSE" file that is part
# of this source code package.
#
"""
UNDER CONSTRUCTION: Driver for training the covariate shift detector on the command line.

Usage:
  shift_detect [options] DATASETS PREPROCESS

Arguments:

  DATASETS                    comma separated list of datasets in importance order
  PREPROCESS                  comma separated list of preprocessing directives for each dataset specified

Options:
  -h, --help                  show this help message and exit
  -v, --version               show version and exit

  -g, --debug                 operate in debug mode
  -b, --benchmark             operate in benchmark mode

  -m, --host M                database host name
  -p, --port P                database port
  -d, --database D            database name
  -c, --collection C          run detector on named database collection

  -o, --test                  use fixed gaussian sample data against covariate shift detection algorithm

  -a, --alpha A               use A as the alpha relative parameter (ULSIF {a = 0}, RULSIF {a > 0} )
  -s, --sigma S               use G as the gaussian width parameter override, sigma
  -l, --lambda L              use L as the regularization parameter override, lamda
  -k, --kernels K             use K number of kernels basis functions as an override
  -f, --folds F               use F number of cross validation folds, where leave one out CV is used if {f = 0}

  --dataset1 1                run detector on named data set field name from the specified collection; treated as R^d=1
  --dataset2 2                run detector on named data set field name from the specified collection; treated as R^d=2
  --dataset3 3                run detector on named data set field name from the specified collection; treated as R^d=3
  --dataset4 4                run detector on named data set field name from the specified collection; treated as R^d=4
  --dataset5 5                run detector on named data set field name from the specified collection; treated as R^d=5
  --dataset6 6                run detector on named data set field name from the specified collection; treated as R^d=6
  --dataset7 7                run detector on named data set field name from the specified collection; treated as R^d=7
  --dataset8 8                run detector on named data set field name from the specified collection; treated as R^d=8
  --dataset9 9                run detector on named data set field name from the specified collection; treated as R^d=9
  --dataset0 0                run detector on named data set field name from the specified collection; treated as R^d=10

  --preprocessCategorical 1   preprocess categorical variables using [NONE, ONEHOT, BINARIZE_LABEL]
  --preprocessOrdinal 2       preprocess ordinal     variables using [NONE, BINARIZE_LABEL]
  --preprocessContinuous 3    preprocess continuous  variables using [NONE, STANDARDIZE, RESCALE, NORMALIZE]

"""
from __future__             import print_function
from docopt                 import docopt

import sys
import signal
import json
import shift_detect


class Driver(object) :

    def _front_matter(self, options) :
        print("Change Detector")
        print("------------------------------------------------------------\n")
        print("Command line tool still under construction\n")
        self._show_options(options)


    def _show_options(self, options, message=None) :
        if options["--debug"] :
            print(message if message is not None else "[ Compute Options ]")
            print(json.dumps(options, sort_keys=True, indent=4, separators=(",", " : ")))
            print("------------------------------------------------------------\n")


    def _exit_signal_handler(self, signal, frame) :
        """
        Default signal handler that exits gracefully on an interrupt.
        """
        sys.exit(0)


    def _install_signal_handlers(self) :
        """
        Installs signal handlers to trap user or system initiated interrupts.
        """
        signal.signal(signal.SIGINT , self._exit_signal_handler)
        signal.signal(signal.SIGHUP , self._exit_signal_handler)
        signal.signal(signal.SIGUSR2, self._exit_signal_handler)


    def start(self, override_docopt=None) :
        try :
            self._install_signal_handlers()

            options = docopt(__doc__, version=shift_detect.__version__)

            self._front_matter(options)

        except Exception as e :
            print("ERROR: Caught {} : {}".format(type(e), e), file=sys.stderr)
            sys.exit(1)
