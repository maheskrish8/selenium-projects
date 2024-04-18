# -k -v --lf --ff --nf -s -x -r -m
def test_text():
    str='maheswari'
    assert str.title()=="Maheswari"

def test_verify_Number():
    n=100
    assert n+25==125

def test_verify_add():
    assert 25<20

def test_verify_m1():
    assert 10==10
