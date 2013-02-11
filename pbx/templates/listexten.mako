<%inherit file='base.mako' />

<h1>Extension's List</h1>

% if extensions:
  <table border=1>
  <tr>
    <td align=center>extension</td><td align=center>password</td>
  </tr>

  % for extension in extensions:
   <tr>
       <td>${"%04d" % extension.extension_id}</td>
       <td>${extension.password}</td>
   </tr>
  % endfor
  </table>
% endif


<p><a href="${ request.route_url('home') }">Return to Home</a></p>
