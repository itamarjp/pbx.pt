<%inherit file='base.mako' />

% if user:
<p>You are logged in as: <a href="${ request.route_url('user', login=user.email_address) }">${ user.email_address }</a></p>
<p><a href="${ request.route_url('logout') }">Logout</a></p>
<p><a href="${ request.route_url('listexten') }">Extension List</a></p>
<p><a href="${ request.route_url('newexten') }">New Extension</a></p>

% else:
<p>You are not logged in!</p>
<p><a href="${ request.route_url('login') }">Login</a></p>
<p><a href="${ request.route_url('newaccount') }">New Account</a></p>
% endif
<p><a href="${ request.route_url('features') }">Features</a></p>
<p><a href="${ request.route_url('support') }">Support</a></p>
<p><a href="${ request.route_url('contact') }">Contact</a></p>








