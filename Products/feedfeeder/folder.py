from zope import interface
from zope import component
from zope.schema import fieldproperty
from zope.annotation import factory

import persistent

from Products.CMFCore import interfaces

from Products.feedfeeder.interfaces import folder

class FolderFeeds(persistent.Persistent):
    interface.implements(folder.IFolderFeeds)
    component.adapts(interfaces.IFolderish)

    feedURLs = fieldproperty.FieldProperty(
        folder.IFolderFeeds['feedURLs'])

    def __init__(self):
        self.itemType = folder.IFolderFeeds['itemType'].default
        self.itemTransitions = []
 
FolderFeedsFactory = factory(FolderFeeds)
