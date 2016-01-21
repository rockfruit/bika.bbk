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
        schema['Batch'].widget.visible = False
        schema['SubGroup'].widget.visible = False
        schema['SamplingRound'].widget.visible = False
        schema['Template'].widget.visible = False
        schema['Specification'].widget.visible = False
        schema['SamplePoint'].widget.visible = False
        schema['StorageLocation'].widget.visible = False
        schema['ClientOrderNumber'].widget.visible = False
        schema['SamplingDeviation'].widget.visible = False
        schema['SamplingDeviation'].widget.visible = False
        schema['SampleCondition'].widget.visible = False
        schema['EnvironmentalConditions'].widget.visible = False
        schema['DefaultContainerType'].widget.visible = False
        schema['Composite'].widget.visible = False
        schema['ReportDryMatter'].widget.visible = False
        schema['InvoiceExclude'].widget.visible = False
        schema['AdHoc'].widget.visible = False
        schema['Priority'].widget.visible = False
        schema['Sampler'].widget.visible = False

        # BBK Wants these fields to be editable in states < verified:
        permissive_fields = ['Cultivar',
                             'Vintage',
                             'Tank',
                             'SamplingDate',
                             'SampleType',
                             'ClientReference',
                             'ClientSampleID']
        for fieldname in permissive_fields:
            field = schema[fieldname]
            field.widget.visible = \
                {'edit': 'visible',
                 'view': 'visible',
                 'add': 'edit',
                 'secondary': 'disabled',
                 'header_table': 'visible',
                 'sample_registered': {'view': 'visible', 'edit': 'visible', 'add': 'edit'},
                 'to_be_sampled':     {'view': 'visible', 'edit': 'visible'},
                 'sampled':           {'view': 'visible', 'edit': 'visible'},
                 'to_be_preserved':   {'view': 'visible', 'edit': 'visible'},
                 'sample_due':        {'view': 'visible', 'edit': 'visible'},
                 'sample_received':   {'view': 'visible', 'edit': 'visible'},
                 'attachment_due':    {'view': 'visible', 'edit': 'visible'},
                 'to_be_verified':    {'view': 'visible', 'edit': 'visible'},
                 'verified':          {'view': 'visible', 'edit': 'invisible'},
                 'published':         {'view': 'visible', 'edit': 'invisible'},
                 'invalid':           {'view': 'visible', 'edit': 'invisible'},
                 }

        schema.moveField('Tank', before='Sample')
        schema.moveField('Vintage', before='Tank')
        schema.moveField('Cultivar', before='Vintage')
        return schema
