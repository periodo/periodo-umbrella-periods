from unittest import TestCase
from click.testing import CliRunner

from periodo_umbrella_periods_cli.cli import root


class TestCreateCommand(TestCase):

    def test_src_option_invalid(self):

        runner = CliRunner()
        with runner.isolated_filesystem():

            with open('hello.txt', 'w') as f:

                f.write('Hello World!')

            result = runner.invoke(root, ['create', 'http://n2t.net/ark:/99152/p086kj99t98'])
            self.assertFalse(result.exit_code == 0)
