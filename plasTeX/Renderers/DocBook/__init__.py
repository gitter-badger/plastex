#!/usr/bin/env python
import re
from plasTeX.Renderers.PageTemplate import Renderer as _Renderer
from plasTeX.Base.LaTeX import table as Ptable, tabular as Ptabular

class table(Ptable):
    class tabular(Ptabular):
        pass


class DocBook(_Renderer):
    """ Renderer for DocBook documents """
    fileExtension = '.xml'
    imageTypes = ['.png','.jpg','.jpeg','.gif']
    vectorImageTypes = ['.svg']

    def cleanup(self, document, files, postProcess=None):
        res = _Renderer.cleanup(self, document, files, postProcess=postProcess)
        return res

    def processFileContent(self, document, s):
        s = _Renderer.processFileContent(self, document, s)
        s = re.compile(r'</partintro>\s*<partintro>',re.I).sub(r'',s)
        #
        s = re.compile(r'<para>\s*(<articleinfo>)',re.I).sub(r'\1',s)
        s = re.compile(r'(</articleinfo>)\s*</para>',re.I).sub(r'\1',s)
        #
        s = re.compile(r'(<informalfigure>)\s*<para>',re.I).sub(r'\1',s)
        s = re.compile(r'</para>\s*(</informalfigure>)',re.I).sub(r'\1',s)
        #
        s = re.compile(r'(<para>)(\s*<para>)+',re.I).sub(r'\1',s)
        s = re.compile(r'(</para>\s*)+(</para>)',re.I).sub(r'\2',s)
        #
        s = re.compile(r'<para>\s*</para>', re.I).sub(r'', s)
        return s

Renderer = DocBook
