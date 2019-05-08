import rfc3987
from click.types import BadParameter, ParamType


class IRIParamType(ParamType):

    name = 'iri'

    @staticmethod
    def validate_iri(value):

        if value is None or rfc3987.match(value, rule='IRI') is not None:

            return True

        else:

            return False

    def convert(self, value, param, ctx):

        if self.validate_iri(value):

            return value

        else:

            self.fail('%s is not a valid IRI' % value, param, ctx)

    def fail(self, message, param=None, ctx=None):

        raise BadParameter(message, ctx=ctx, param=param)