import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from tdf.tuclayout.testing import\
    TDF_TUCLAYOUT_INTEGRATION


class TestExample(unittest.TestCase):

    layer = TDF_TUCLAYOUT_INTEGRATION
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')
    
    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product 
            installed
        """
        pid = 'tdf.tuclayout'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')
