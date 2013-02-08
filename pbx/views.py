from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError



from pyramid.httpexceptions import HTTPForbidden
from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPNotFound
from pyramid.security import authenticated_userid
from pyramid.security import forget
from pyramid.security import remember
from pyramid.view import forbidden_view_config




from .models import (
    DBSession,
    MyModel,
    User,
    Extension,
    )
conn_err_msg = """we having a problem using the database."""

@view_config(route_name='home',renderer='home.mako',)
def home_view(request):
    login = authenticated_userid(request)
    user = User.by_email(login)
    return {'user': user,'user_pages': [],}

@view_config(route_name='user',)
def user_view(request):
    pass

@view_config(route_name='newexten',renderer='newexten.mako')
def newexten(request):
   import string
   from random import choice
   size = 40
   pwd = ''.join([choice(string.letters + string.digits) for i in range(size)])

   login = authenticated_userid(request)
   user = User.by_email(login)
   user_id = user.user_id

   exten = Extension(password=pwd,user_id=user_id,active=True)
   DBSession.add(exten)
   return {'exten':exten.extension_id,'password':pwd}


@view_config(route_name='newaccount',renderer='newaccount.mako')
def newaccount(request):
 if request.method == 'POST':
   import string
   from random import choice
   size = 40
   pwd = ''.join([choice(string.letters + string.digits) for i in range(size)])
   if request.POST.get('email'):
        email=request.POST.get('email')
        from datetime import date
        u = User(email_address = email ,    display_name = '' ,    password = pwd ,    created = date.today() ,)
        DBSession.add(u)
        request.session.flash('New account added, please check your e-mail account.')
        return HTTPFound(location=request.route_url('home'))
   else:
        request.session.flash('Please enter your e-mail!')
 return {}



@view_config(route_name='logout',)
def logout_view(request):
    headers = forget(request)
    loc = request.route_url('home')
    return HTTPFound(location=loc, headers=headers)

@view_config(route_name='listexten',renderer='listexten.mako')
def listexten(request):
   login = authenticated_userid(request)
   user = User.by_email(login)
   rs = DBSession.query(Extension).filter(Extension.user_id == user.user_id).all()
  # print rs
   #extensions = [dict(id=row[0], password=row[1]) for row in rs.fetchall()]
   #return {'extensions':extensions}
   return dict(extensions=rs)


@view_config(route_name='sip.conf',renderer='sip.mako')
def sip_conf(request):
   rs = DBSession.query(Extension).all()
   return dict(extensions=rs)


@view_config(route_name='features',renderer='features.mako')
def features(request):
  return {}

@view_config(route_name='support',renderer='support.mako')
def support(request):
  return {}


@view_config(route_name='contact',renderer='contact.mako')
def contact(request):
  return {}


@view_config(route_name='login',renderer='login.mako',)
def login_view(request):
    next = request.params.get('next') or request.route_url('home')
    login = ''
    did_fail = False
    if 'submit' in request.POST:
        login = request.POST.get('login', '')
        passwd = request.POST.get('passwd', '')

        user = User.by_email(login)
        if user and user.verify_password(passwd):
            headers = remember(request, login)
            return HTTPFound(location=next, headers=headers)
        did_fail = True

    return {
        'login': login,
        'next': next,
        'failed_attempt': did_fail,
        'users': User,
    }


