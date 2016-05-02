from nose.tools import *
from bin.app import app
from tests.tools import assert_response 

def test_index():
	
	resp = app.request("/game")
	assert_response(resp)
	
	resp = app.request("/")
	assert_response(resp)
	
	resp = app.request("/lobby")
	assert_response(resp)
	
	resp = app.request("/help")
	assert_response(resp)