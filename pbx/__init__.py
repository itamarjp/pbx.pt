from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from pyramid.session import UnencryptedCookieSessionFactoryConfig


from .models import (
    DBSession,
    Base,
    )

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    #session factory
    my_session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    config = Configurator(settings=settings,session_factory = my_session_factory)
    config.include('pyramid_mailer')
    authn_policy = AuthTktAuthenticationPolicy('seekpbxrit', hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.add_static_view('static', 'static', cache_max_age=3600)
    #config.add_route('index', '/index',permission='add')
    config.add_route('home', '/')
    config.add_route('user', '/user')
    config.add_route('newaccount', '/newaccount')
    config.add_route('newexten', '/newexten')
    config.add_route('listexten', '/listexten')
    config.add_route('logout','/logout')
    config.add_route('login','/login')
    config.add_route('features','/features')
    config.add_route('contact','/contact')
    config.add_route('support','/support')
    config.add_route('sip.conf','/sip.conf')
    config.scan()
    return config.make_wsgi_app()

