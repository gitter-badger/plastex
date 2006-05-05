#!/usr/bin/env python

"""
C.9 Figures and Other Floating Bodies (p196)

"""

from plasTeX import Command, Environment
from plasTeX import GlueCommand, DimenCommand
from plasTeX.Logging import getLogger


class Caption(Command):
    args = '[ toc ] title'

#
# C.9.1 Figures and Tables
#

class figure(Environment):
    args = 'loc:str'

    class caption(Caption):
        counter = 'figure'

class FigureStar(figure):
    macroName = 'figure*'

class table(Environment):
    args = 'loc:str'

    class caption(Caption):
        counter = 'table'

class TableStar(table):
    macroName = 'table*'

class suppressfloats(Command):
    pass

# Counters

class topfraction(Command):
    unicode = '0.25'

class bottomfraction(Command):
    unicode = '0.25'

class textfraction(Command):
    unicode = '0.25'

class floatpagefraction(Command):
    unicode = '0.25'

class dbltopfraction(Command):
    unicode = '0.25'

class dblfloatpagefraction(Command):
    unicode = '0.25'

class floatsep(GlueCommand):
    value = GlueCommand.new(0)

class textfloatsep(GlueCommand):
    value = GlueCommand.new(0)

class intextsep(GlueCommand):
    value = GlueCommand.new(0)

class dblfloatsep(GlueCommand):
    value = GlueCommand.new(0)

class dbltextfloatsep(GlueCommand):
    value = GlueCommand.new(0)


#
# C.9.2 Marginal Notes
#

class marginpar(Command):
    args = '[ left ] right'

class reversemarginpar(Command):
    pass

class normalmarginpar(Command):
    pass

# Style Parameters

class marginparwidth(DimenCommand):
    value = DimenCommand.new(0)

class marginparsep(DimenCommand):
    value = DimenCommand.new(0)

class marginparpush(DimenCommand):
    value = DimenCommand.new(0)
