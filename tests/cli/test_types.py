from unittest import TestCase
from click.types import BadParameter
from periodo_umbrella_periods_cli.cli.types import IRIParamType

from faker import Faker

fake = Faker()


class TestTypes(TestCase):

    def test_validate_iri_valid(self):

        validation = IRIParamType.validate_iri(fake.uri())

        self.assertTrue(validation)

    def test_validate_iri_invalid(self):

        validation = IRIParamType.validate_iri('invalid-uri')

        self.assertFalse(validation)

    def test_validate_iri_none(self):

        validation = IRIParamType.validate_iri(None)

        self.assertTrue(validation)

    def test_convert_valid(self):

        iri = fake.uri()

        iri_param = IRIParamType()

        converted = iri_param.convert(iri, None, None)

        self.assertEqual(iri, converted)

    def test_convert_invalid(self):

        iri = 'invalid-iri'

        iri_param = IRIParamType()

        with self.assertRaises(BadParameter):

            iri_param.convert(iri, None, None)

    def test_convert_none(self):

        iri = None

        iri_param = IRIParamType()

        converted = iri_param.convert(iri, None, None)

        self.assertIsNone(converted)
