# -*- coding: utf-8 -*- 
<!DOCTYPE html>  
<html>
<head>
  <meta charset="utf-8">
  <title>pbx.pt - your free sip account</title>
  <link rel="shortcut icon" href="/static/favicon.ico">
  <link rel="stylesheet" href="/static/style.css">

</head>

% if request.session.peek_flash():
  <div id="flash">
    <% flash = request.session.pop_flash() %>
	% for message in flash:
	${message}<br>
	% endfor
  </div>
% endif


<html>
    <body>
        ${ next.body() }
    </body>
</html>
