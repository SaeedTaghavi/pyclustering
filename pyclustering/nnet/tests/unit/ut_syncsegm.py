"""!

@brief Unit-tests for double-layer oscillatory network 'syncsegm' for image segmentation based on Kuramoto model.

@authors Andrei Novikov (pyclustering@yandex.ru)
@date 2014-2018
@copyright GNU Public License

@cond GNU_PUBLIC_LICENSE
    PyClustering is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    PyClustering is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
@endcond

"""


import unittest;

# Generate images without having a window appear.
import matplotlib;
matplotlib.use('Agg');

from pyclustering.nnet.tests.syncsegm_templates import SyncsegmTestTemplates;

from pyclustering.samples.definitions import IMAGE_SIMPLE_SAMPLES;


class SyncsegmUnitTest(unittest.TestCase):
    def testImageSegmentationSimple17(self):
        SyncsegmTestTemplates.templatesyncsegmSegmentation(IMAGE_SIMPLE_SAMPLES.IMAGE_SIMPLE17, 225, 1, 0, 3, 3, False, False);

    def testImageSegmentationSimple18(self):
        SyncsegmTestTemplates.templatesyncsegmSegmentation(IMAGE_SIMPLE_SAMPLES.IMAGE_SIMPLE18, 225, 1, 0, 2, 3, True, False);


if __name__ == "__main__":
    unittest.main();
