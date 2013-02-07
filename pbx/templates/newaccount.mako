# -*- coding: utf-8 -*- 
<%inherit file="base.mako"/>

<h1>New Account</h1>

<form action="${request.route_url('newaccount')}" method="post">
  <label>email:</label><input type="text" maxlength="100" name="email">
  <input type="submit" name="add" value="ADD" class="button">
</form>

