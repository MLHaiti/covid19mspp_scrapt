import unittest
from helper import increment_msppdate , read_department_report, is_pdf_link, get_right_covid19links
import pandas as pd

class TestHelper(unittest.TestCase):
    def test_increment_msppdatedef(self):
        self.assertEqual(increment_msppdate('29-02-2020')["str"],"01-03-2020")

    def test_read_department_report(self):
        url = "https://mspp.gouv.ht/site/downloads/Sitrep 05-04-2020.pdf"
        self.assertTrue(isinstance(read_department_report(url), pd.DataFrame))

    def test_is_pdf_link(self):
        url = "https://mspp.gouv.ht/site/downloads/Sitrep 05-04-2020.pdf"
        self.assertTrue(is_pdf_link(url))
        self.assertFalse(is_pdf_link('https://mspp.gouv.ht/site/downloads/Sitrep 05'))

    def test_get_right_covid19links(self):
        str_start_date ='07-04-2020'
        links = get_right_covid19links(str_start_date)
        self.assertGreater(len(links),3)
if __name__ == '__main__':
    unittest.main()