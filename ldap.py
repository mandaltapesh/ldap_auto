import subprocess

proc_pkg_install = subprocess.Popen(["sudo", "apt-get", "-y", "install", "slapd", "ldap-utils"], stdin=subprocess.PIPE)

proc_pkg_install.communicate()

proc_pkg_install.stdin.close()

slapd_conf = subprocess.call(["sudo", "dpkg-reconfigure", "--default-priority", "slapd"])

cmd1 = ["ldapadd", "-D", "cn=admin,dc=redhat,dc=com", "-w", "secret", "-f", "org.ldif"]
org_create = subprocess.call(cmd1)

cmd2 = ["ldapadd", "-D", "cn=admin,dc=redhat,dc=com", "-w", "secret", "-f", "users.ldif"]
add_users = subprocess.call(cmd2)
 
