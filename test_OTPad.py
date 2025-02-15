import OTPad
import pytest

def test_encrypt_key_equal_plaintext():
    assert(OTPad.decrypt("A", "A") == chr(0))

def test_encrypt_null_key():
    assert(pytest.raises(ValueError, lambda: OTPad.decrypt("A", "")))
