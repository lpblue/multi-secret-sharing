# Prototype of Multi-secret sharing scheme by Roy & Adhikari
# Filip Kubicz 2016

from nose.tools import assert_equal
from nose.tools import assert_raises
from prototype.Dealer import Dealer

# TODO: test if hash is the same for the same Dealer object and different among separate objects with random AES-CTR nonce

""" Declare basic params used to initialize Dealer in test cases """
# large prime from NIST P-256 elliptic curve 
p256 = 2**256 - 2**224 + 2**192 + 2**96 - 1
# multi secret sharing parameters
s_secrets = [7, 313, 671] # s_i
n_participants = 3
# access structure: to which secret what group has access
# Gamma(s_i) = [A1, A2, ... Al], Aq = (P1, P2, Pm), q=1,2...l
# gamma1 is a group of users authorized to reconstruct s1
gamma1 = [(1,3)]
gamma2 = [(1,2), (2,3)] # A1, A2 implicitly
gamma3 = [(1,2,3)] # to secret s3 only all 3 users together can gain access
access_structures = [gamma1, gamma2, gamma3]


def test_init():
    """ check exception handling if params are faulty """
    
    # test for proper exception: p not prime
    with assert_raises(ValueError):
        dealer = Dealer(24, n_participants, s_secrets, access_structures)
    
    # test for proper exception: too little participants
    with assert_raises(ValueError):
        dealer = Dealer(p256, 1, s_secrets, access_structures)


def test_hash():
    """ set up Dealer object and chech hash repeatability """
    
    # Create a Dealer
    dealer = Dealer(p256, n_participants, s_secrets, access_structures)

    # test hash function - it should be repeatable for the same Dealer object
    hash1 = dealer.hash(b'BYTESEQUENCE')
    hash2 = dealer.hash(b'BYTESEQUENCE')
    assert_equal(hash1, hash2)


def test_modulo_p():
    
    p = 1009
    dealer = Dealer(p, n_participants, s_secrets, access_structures)
    
    assert_equal(dealer.modulo_p(2011), 1002)
    
    