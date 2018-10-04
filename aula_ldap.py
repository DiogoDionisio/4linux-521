from ldap3.utils.hashed import hashed
from ldap3 import Server, Connection, HASHED_MD5

server = Server('ldap://127.0.0.1:389')
DN = 'cn=admin,dc=dexter,dc=com,dc=br'
ldap = Connection(server, DN, '4linux')

if ldap.bind():
    print('Conectado ao server LDAP')
else:
    print('usuario ou senha invalidos')

user = {
    'cn' : 'Diogo',
    'sn' : 'Dionisio',
    'mail' : 'diogo@4linux.com.br',
    'UserPassword' : hashed(HASHED_MD5, '4linux')
}

objectClass = ['person','inetOrgPerson','OrganizationalPerson','top']
dn = 'mail={0},dc=dexter,dc=com,dc=br'.format(user['mail'])

if ldap.add(dn, objectClass, user):
    print('usuario cadatrado com sucesso')
else:
    print('problema ao cadastrar o usuario')