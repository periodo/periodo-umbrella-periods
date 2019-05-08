import uuid


PERIODO_SKOLEM_IRI_PREFIX = "https://perio.do/.well-known/genid/"


def create_periodo_skolem_iri():
    """
    Attaches a random UUID to the PeriodO skolem IRI prefix
    :return: A PeriodO centric skolem IRI.
    """
    return "{skolem}{uuid}".format(skolem=PERIODO_SKOLEM_IRI_PREFIX, uuid=uuid.uuid1())
