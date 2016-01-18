from Products.Archetypes.interfaces import IFieldDefaultProvider
from Products.Archetypes.mimetype_utils import getDefaultContentType
from Products.Archetypes.utils import shasattr, mapply
from Products.CMFCore.utils import getToolByName

from DateTime import DateTime
from zope import component
from zope.component import getAdapters

_marker = []


def setDefaults(self, instance):
    """Only call during object initialization. Sets fields to
    schema defaults
    """
    # # TODO think about layout/vs dyn defaults
    for field in self.values():

        value = None

        # if analysis request, set sampling date to default to today
        if field.getName().lower() == 'samplingdate' \
                and instance.portal_type == 'AnalysisRequest':
            now = DateTime().strftime("%Y-%m-%d %H:%M")
            value = now

        # From here, the rest of the body of the original function:
        # Products.Archetypes.Schema.BasicSchema#setDefaults

        if field.getName().lower() == 'id':
            continue
        # The original version skipped all reference fields.  I obviously do
        # find some use in defining their defaults anyway, so if our adapter
        # reflects a value for a reference field, I will allow it.
        if field.type == "reference" and not value:
            continue

        default = value if value else field.getDefault(instance)

        # always set defaults on writable fields
        mutator = field.getMutator(instance)
        if mutator is None:
            continue

        args = (default,)
        kw = {'field': field.__name__,
              '_initializing_': True}
        if shasattr(field, 'default_content_type'):
            # specify a mimetype if the mutator takes a
            # mimetype argument
            # if the schema supplies a default, we honour that,
            # otherwise we use the site property
            default_content_type = field.default_content_type
            if default_content_type is None:
                default_content_type = getDefaultContentType(instance)
            kw['mimetype'] = default_content_type

        mapply(mutator, *args, **kw)
