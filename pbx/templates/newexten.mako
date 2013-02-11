<%inherit file='base.mako' />

% if failed==0:
Extension Added
% endif

<p><a href="${ request.route_url('home') }">Return to Home</a></p>
