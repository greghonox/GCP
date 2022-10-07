from os import environ

def test_echo_security_github_test() -> None:
    """ Test print """
    variable = environ.get('SECURITY_GITHUB')
    print(variable)
    
