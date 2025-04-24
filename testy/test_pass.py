from Projekt_DI import Sha


def test_pass():
    a = Sha('a', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb')
    result=a.hash_it()
    expected='ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb'
    assert expected==result
