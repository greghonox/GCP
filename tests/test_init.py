from os import environ

def test_echo_security_github_test() -> str:
    """ Test print """
    variable = environ.get('SECURITY_GITHUB')
    return variable
    
