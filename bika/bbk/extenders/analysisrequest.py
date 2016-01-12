from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import ISchemaModifier
from bika.lims import bikaMessageFactory as _b
from bika.lims.fields import *
from bika.lims.interfaces import IAnalysisRequest
from Products.Archetypes import public as at
from Products.CMFCore import permissions
from Products.CMFCore.utils import getToolByName
from zope.component import adapts
from zope.interface import implements


class AnalysisRequestSchemaExtender(object):
    adapts(IAnalysisRequest)
    implements(IOrderableSchemaExtender)

    fields = [
    ]

    def __init__(self, context):
        self.context = context

    def getOrder(self, schematas):
        return schematas

    def getFields(self):
        return self.fields


class AnalysisRequestSchemaModifier(object):
    adapts(IAnalysisRequest)
    implements(ISchemaModifier)

    def __init__(self, context):
        self.context = context

    def fiddle(self, schema):
        schema['ReportDryMatter'].widget.visible = False
        schema['SamplingDeviation'].widget.visible = False
        schema['DefaultContainerType'].widget.visible = False
        schema['AdHoc'].widget.visible = False
        schema['Composite'].widget.visible = False
        return schema
