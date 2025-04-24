from Projekt_DI import Sha
from Projekt_DI import Lister

def test_hash_it():
    a = Sha('a', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb')
    result=a.hash_it()
    expected='ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb'
    assert expected==result


def test_read():
    b= Lister()
    try:
        b.read()
        result = 1
    except FileExistsError:
        result=0

    expected=1
    assert expected == result