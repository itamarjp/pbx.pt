# -*- coding: utf-8 -*- 
<%inherit file="base.mako"/>

<h1>Password Recovery</h1>

<form action="${request.route_url('password_recovery')}" method="post">
  <label>email:</label><input type="text" maxlength="100" name="email">
  <input type="submit" name="add" value="Send Password" class="button">
</form>

