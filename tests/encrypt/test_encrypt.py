import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("", "")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 1)

    assert (
        encrypt_message("pneumoultramicroscópicosilicovulcaniconiótico", 9)
        == "tluomuenp_ocitóinocinacluvocilisocipócsorcimar"
    )
    assert encrypt_message("abcdef", 4) == "fe_dcba"
    assert encrypt_message("abcdef", 10) == "fedcba"
