import xmlrpc.client

with xmlrpc.client.ServerProxy('http://localhost:8000/') as proxy:
    print('Digite um número para saber se ele é par:')
    n = int(input())
    is_even = proxy.is_even(n)
    print('%s é par: %s' % (str(n), str(is_even)))