#!/bin/python3
import os

from flask import render_template


class routes():
    """ routes is a class with a static contents to route templates directory
     content to flask route (using @app.route) """
    pages = [] # the whole list
    @staticmethod
    def template_route(app,route_path,template_dir):
        """ route the whole template directory to the app by creating page objects """
        global template_path
        template_path= template_dir
        server_contents = os.listdir(template_dir) # get list of contents from dir
        for html_file in server_contents: # loop in contents
            if os.path.isdir(template_dir+'/'+html_file): # if it's dir
                routes.route(app,route_path+'/'+html_file,template_dir+'/'+html_file) # route the dir
            else: # it's html file now
                f_route_path = route_path+'/'+html_file
                f_html_path = template_dir+'/'+html_file
                routes.pages.append(routes.page(app,f_route_path,f_html_path,html_file)) # create new page
    
    @staticmethod
    def route(app,route_path,html_dir):
        """ route the directory to the app by creating page objects """

        server_contents = os.listdir(html_dir) # get list of contents from dir
        for html_file in server_contents: # loop in contents
            if os.path.isdir(html_dir+'/'+html_file): # if it's dir
                routes.route(app,route_path+'/'+html_file,html_dir+'/'+html_file) # route the dir
            else: # it's html file now
                f_route_path = route_path+'/'+html_file
                f_html_path = html_dir+'/'+html_file
                html_file = f_html_path[len(template_path):]
                routes.pages.append(routes.page(app,f_route_path,f_html_path,html_file))  # create new page

    class page(object):
        """ page class is the class that route web page to route path """
        def __init__(self,app,f_route_path,f_html_path,html_file):
            self.f_route_path = f_route_path
            self.f_html_path = f_html_path
            self.app = app
            
            @app.route(f_route_path[:-len('.html')],endpoint=f_html_path)
            @app.route(f_route_path,endpoint=f_html_path)
            def load_page():
                return render_template(html_file)
            
            self.load_page = load_page
