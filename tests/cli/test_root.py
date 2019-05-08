from unittest import TestCase
from click.testing import CliRunner

from periodo_umbrella_periods_cli.cli import root


class TestRootCommand(TestCase):

    def test_root_without_subcommand_or_params(self):

        runner = CliRunner()
        result = runner.invoke(root)

        self.assertTrue(result.exit_code == 0)
