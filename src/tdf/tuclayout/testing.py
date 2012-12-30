from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import tdf.tuclayout


TDF_TUCLAYOUT = PloneWithPackageLayer(
    zcml_package=tdf.tuclayout,
    zcml_filename='testing.zcml',
    gs_profile_id='tdf.tuclayout:testing',
    name="TDF_TUCLAYOUT")

TDF_TUCLAYOUT_INTEGRATION = IntegrationTesting(
    bases=(TDF_TUCLAYOUT, ),
    name="TDF_TUCLAYOUT_INTEGRATION")

TDF_TUCLAYOUT_FUNCTIONAL = FunctionalTesting(
    bases=(TDF_TUCLAYOUT, ),
    name="TDF_TUCLAYOUT_FUNCTIONAL")
