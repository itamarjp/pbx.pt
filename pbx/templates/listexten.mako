<%inherit file='base.mako' />

<h1>Extension's List</h1>

<ul id="extensions">
% if extensions:
  % for extension in extensions:
  <li>
    <span class="name">${extension.extension_id}</span>
    <span class="name">${extension.password}</span>
    <span class="actions">
      [ <a href="${request.route_url('logout')}">close</a> ]
    </span>
  </li>
  % endfor
% else:
  <li>There are no open extensions</li>
% endif
  <li class="last">
    <a href="${request.route_url('newexten')}">Add a new extension</a>
  </li>
</ul>

