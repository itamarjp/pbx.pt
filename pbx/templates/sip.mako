% for extension in extensions:
[${"%04d" % extension.extension_id}]
type=friend
callerid="${"%04d" % extension.extension_id}" <${"%04d" % extension.extension_id}>
username=${"%04d" % extension.extension_id}
host=dynamic
secret=${extension.password}
context=free
disallow=all
allow=alaw
allow=ulaw
canreinvite=no
nat=force_rport,comedia
% endfor

