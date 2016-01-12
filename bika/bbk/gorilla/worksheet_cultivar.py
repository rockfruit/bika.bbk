from Products.CMFPlone.utils import safe_unicode


def getSampleTypeTitle(sample):
    """Given a sample, return the Cultivar's title instead
    of the SampleType's title. BBK considers this really important.
    """
    sampletype = sample.getField('SampleType').get(sample)
    st_title = sampletype.Title()
    if sample.REQUEST['PARENTS'][0].portal_type == 'Worksheet':
        cultivar = sample.getField('Cultivar').get(sample)
        if cultivar:
            return safe_unicode(cultivar.Title()).encode('utf-8')
        else:
            return st_title
    else:
        return st_title
