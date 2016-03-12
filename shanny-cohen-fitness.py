#!/usr/bin/env python

Site = 'Shanny Cohen Fitness'

Timezone = 'Pacific/Honolulu'

Colors = '''
    base03:    #002b36;
    base02:    #073642;
    base01:    #586e75;
    base00:    #657b83;
     base0:    #839496;
     base1:    #93a1a1;
     base2:    #eee8d5;
     base3:    #fdf6e3;
    yellow:    #b58900;
    orange:    #cb4b16;
       red:    #dc322f;
   magenta:    #d33682;
    violet:    #6c71c4;
      blue:    #268bd2;
      cyan:    #2aa198;
     green:    #859900;
''' # - http://ethanschoonover.com/solarized

Analytics = '''<script>
</script>'''

# - HTML Page Code

main_page_html = '''<style></style>
  <div class="page_html">
   <header class="hi"><span class="color_b">SHANNY COHEN</span></header>
  </div><!-- - /page_html - -->
'''
page_header = '''<style>
  header { position: relative; width: 100%; }
  .sub_title { border-top: 1px solid #eee; }
  .top_wrap { position: absolute; top: 0; left: 0; right: 0; height: 100px; }
  .social_wrap { position: absolute; right: 125px; font-size: 14px; }
  .social_wrap a { color: #555; margin-right: 25px; }
  .social_wrap a:hover { color: #111; }

  </style>
  <header>
    <div class="top_wrap">
      <div class="logo_wrap">SHANNY COHEN
        <div class="sub_title">FITNESS</div>
      </div>
      <nav class="social_wrap">
        <a href="https://www.instagram.com/shannycohen_fitness/" target="_blank">Instagram</a>
        <a href="" target="_blank">Twitter</a>
        <a href="https://www.facebook.com/ShannyCohenAthletePage/timeline" target="_blank">Facebook</a>
      </nav><!-- . social_wrap - -->
    </div><!-- . top_wrap - -->
  </header>
'''
public_nav_html = '''
  <nav class="main_nav"><ul>
    <a href="../../programs"><li id="programsNav">Programs</li></a>
    <a href="../../results"><li id="resultsNav">Results</li></a>
    <a href="../../exercises"><li id="exercisesNav">Exercises</li></a>
    <a href="../../about"><li id="aboutNav">About</li></a>
  </ul></nav><!-- - /main_nav - -->
'''
programs_page_html = '''<style>
  .main_wrap img { width: 95%; }
  </style>

  <div class="main_wrap">
  Programs Page

  <ul>
    <li>Strength and Conditioning</li>
    <li>Weight Loss</li>
    <li>Sport Specific Training</li>
    <li>Post-Injury Exercise Rehab</li>
    <li>Orthopedic Condition Specific Training</li>
  </ul>

  </div><!-- . main_wrap - -->
'''
results_page_html = '''
  <div class="main_wrap">
  Results Page
    <img src="../../pics/results.jpg" />

  </div><!-- . main_wrap - -->
'''
exercises_page_html = '''
  <style type="text/css">
    .exercise_data{border: 1px solid grey; border-radius: 3px; text-align: left; padding: 10px; margin-top: 15px;}
    .img_wrap{width: 40%}
    .text_wrap{width: 50%;}
    .img_wrap, .text_wrap{display: inline-block; vertical-align: top;}
  </style>
  <div class="main_wrap">
    <div class="exercise_data" ng-repeat="item in exercise_data">
      <div class="text_wrap">
        <p> Exercise Name:  [! item.exercise_name !] </p>  
        <p> Exercise Type:  [! item.exercise_type !] </p> 
        <p> Exercise Class:  [! item.exercise_class !] </p> 
        <p ng-show='item.exercise_video_key'> <a ng-href="/view_video/[!item.exercise_video_key!]" target="_blank"> View Video </a></p>
      </div><!--.text_wrap-->

      <div class="img_wrap">
        <img ng-src="/render_img?medium?[!item.data_id!]">
      </div><!--.img_wrap-->
    </div><!--.exercise_data-->
  </div><!-- .main_wrap -->
'''
about_page_html = '''<style>
  </style>

  <div class="main_wrap">
    <img src="../../pics/home.jpg" />
  </div><!-- . main_wrap - -->
'''
entries_page_html = '''
  <style>
  .text_wrap { margin-left: 65px; }
  </style>
  <div class="page_html">
   <header class="hi"><span class="color_b">Form Entries</span></header>
    <article class="text_wrap">
      <p>Sign in as an &nbsp; <b><span class="color_a">Admin User</span></b> &nbsp; to view form data</p>
    </article><!-- - /form_wrap - -->
  </div><!-- - /page_html - -->
'''
entries_page_html_admin = '''
  <style>
  .form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px; padding: 45px; }
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="page_html">
   <header class="hi"><span class="color_b">Fill Out The Form</span></header>
    <article class="form_wrap">
      <form action="../../add_form" enctype="multipart/form-data" method="post">
        <table>
          <tr>
            <td class="label">Email Addess</td>
            <td class="input"><input type="text" name="email_address" /></td>
          </tr>
          <tr>
            <td class="label">User Name</td>
            <td class="input"><input type="text" name="user_name" /></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right"><input type="submit" value="Sign Up" /></td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - /page_html - -->

  <style>
  .list_wrap { margin-left: 25px; margin-top: 45px; }
  .item_wrap { width: 400px; border-bottom: 1px solid #eee; padding: 15px; padding-bottom: 10px; margin-top: 45px; }
  .item_wrap:hover { border-bottom: 1px solid #657b83; }
  .right_wrap { float: right; text-align: right; font-size: 12px; }
  .right_wrap a { color: #cb4b16; }
  .right_wrap a:hover { text-decoration: underline; }
  .id_wrap { padding-top 40px; color: #839496; }
  .email_address { font-size: 14px; line-height: 20px; }
  .user_name { font-size: 22px; color: #073642; }
  </style>
  <div class="page_html">
   <header class="hi"><span class="color_b">Form Entries</span></header>
    <article class="list_wrap">
      <div class="item_wrap" ng-repeat="item in items">
        <div class="item_data">

          <div class="right_wrap">
            <p><a href ng-click="delete(item.data_id)">Delete</a></p>
            <div class="id_wrap">[!item.data_id!]</div>
          </div><!-- - /right_wrap - -->

          <p><span class="email_address">[!item.email_address!]</span>
          <br />
          <span class="user_name">[!item.user_name!]</span></p>
          
        </div><!-- - /item_data - -->
      </div><!-- - /item_data - -->
    </article><!-- - /list_wrap - -->
  </div><!-- - /page_html - -->
'''
code_page_html = '''<style>
  .link_wrap { margin-left: 85px; margin-top: 45px; }
  </style>
  <div class="page_html">
   <header class="hi"><span class="color_b">Code Link</span></header>
    <div class="link_wrap">
      <p>View on &nbsp; <a href="https://github.com/Kyle2501/App-Engine-Parts" target="_blank">GitHub</a></p>
    </div><!-- - /link_wrap - -->
  </div><!-- - /page_html - -->
'''
login_page_html = '''
  <div class="main_wrap">
    <p>Sign in as an &nbsp; <b><span class="color_a">Admin User</span></b> &nbsp; to view form data</p>
  </div><!-- .main_wrap -->
'''
admin_nav_html = '''
  <nav class="main_nav"><ul>
    <a href="../../"><li id="programsNav">Public</li></a>
    <a href="../../manage/exercise"><li id="programsNav">Exercise</li></a>
  </ul></nav><!-- - /main_nav - -->
'''
manage_page_html = '''
  <div class="main_wrap">
    <p>Choose a data set from the right to edit</p>
  </div><!-- .main_wrap -->
'''
manage_exercise_page_html = '''
  <style type="text/css">
    .exercise_data{border: 1px solid grey; border-radius: 3px; text-align: left; padding: 10px; margin-top: 15px;}
    .img_wrap{width: 40%}
    .text_wrap{width: 50%;}
    .img_wrap, .text_wrap{display: inline-block; vertical-align: top;}
  </style>
  <div class="main_wrap">
    <a href='/publish/exercise'><button>Add A New Exercise</button></a>
    <hr>
    <div class="exercise_data" ng-repeat="item in exercise_data">
      <div class="text_wrap">
        <p> Add Time:  [! item.add_time | limitTo: 19 !] </p>
        <p> User: [! item.user_name !] </p>
        <p> Exercise Name:  [! item.exercise_name !] </p>  
        <p> Exercise Type:  [! item.exercise_type !] </p> 
        <p> Exercise Class:  [! item.exercise_class !] </p> 
        <p ng-show='item.exercise_video_key'> <a ng-href="/view_video/[!item.exercise_video_key!]" target="_blank"> View Video </a></p>
      </div><!--.text_wrap-->

      <div class="img_wrap">
        <img ng-src="/render_img?small?[!item.data_id!]">
      </div><!--.img_wrap-->

      <a ng-href='/edit/exercise?[!item.data_id!]'><button>Edit Info</button></a>
      <a ng-href='/publish/exercise_video?[!item.data_id!]'><button>Edit Video</button></a>
      <button ng-click="delete(item.data_id)">Delete Exercise</button>
    </div><!--.exercise_data-->
  </div><!-- .main_wrap -->
'''
publish_exercise_page_html = '''
  <style>
  .form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px; padding: 45px; }
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap">
   <header class="hi"><span class="color_b">Create New Exercise</span></header>
    <article class="form_wrap">
      <form action="../../manage/add_exercise" enctype="multipart/form-data" method="post">
        <table>
          <tr>
            <td class="label">Name</td>
            <td class="input"><input type="text" name="exercise_name" required/></td>
          </tr>
          <tr>
            <td class="label">Type</td>
            <td class="input"><input type="text" name="exercise_type" /></td>
          </tr>
          <tr>
            <td class="label">Class</td>
            <td class="input"><input type="text" name="exercise_class" /></td>
          </tr>
          <tr>
            <td class="label">Photo</td>
            <td class="input"><input type="file" name="exercise_photo"/></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right"><input type="submit" value="Add New Exercise" /></td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - .main_wrap - -->
'''
edit_exercise_page_html = '''
  <style>
  .form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px; padding: 45px; }
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  td img{max-width:70px;}
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap">
   <header class="hi"><span class="color_b">Edit Exercise</span></header>
    <article class="form_wrap">
      <form action="../../manage/add_exercise" enctype="multipart/form-data" method="post">
        <table>
          <tr class="hide">
            <td class="label">data_id</td>
            <td class="input"><input type="text" name="data_id" ng-model='data_id' required/></td>
          </tr>
          <tr>
            <td class="label">Name</td>
            <td class="input"><input type="text" name="exercise_name" ng-model='exercise_name' required/></td>
          </tr>
          <tr>
            <td class="label">Type</td>
            <td class="input"><input type="text" name="exercise_type" ng-model='exercise_type' /></td>
          </tr>
          <tr>
            <td class="label">Class</td>
            <td class="input"><input type="text" name="exercise_class" ng-model='exercise_class' /></td>
          </tr>
          <tr>
            <td class="label">Photo</td>
            <td class="input"><img ng-src="/render_img?thumb?[!data_id!]"></td>
          </tr>
          <tr>
            <td class="label"></td>
            <td class="input"><input type="file" name="exercise_photo"/></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/exercise"><button type="button">Cancel</button></a>
              <input type="submit" value="Save" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - .main_wrap - -->
'''
publish_exercise_video_page_html = '''
  <div class="main_wrap">
    <header class="hi"><span class="color_b">Video for [!exercise_name!]</span></header>
    <article class="form_wrap">
      <form action="{0}" enctype="multipart/form-data" method="post">
        <table>
          <tr class="hide">
            <td class="label">data_id</td>
            <td class="input"><input type="text" name="data_id" ng-model='data_id' required/></td>
          </tr>
          <tr>
            <td class="label">Upload Video</td>
            <td class="input"><input type="file" name="video_file"/></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right"><input type="submit" value="Add Exercise Video" /></td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - .main_wrap - -->  
'''

# - System
import os
import urllib
import wsgiref.handlers
import webapp2
import json
# - 
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
# -
from google.appengine.ext import db
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
# -
from urlparse import urlparse
# -
import time
import datetime
from pytz.gae import pytz


class Exercise_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
    #
    user_name = ndb.StringProperty()
    #
    exercise_id = ndb.StringProperty()
    exercise_name = ndb.StringProperty()
    exercise_type = ndb.StringProperty()
    exercise_class = ndb.StringProperty()
    exercise_photo = ndb.BlobProperty()
    exercise_video_key = ndb.StringProperty()

    @classmethod
    def _get_all_data(self):
        q = ndb.gql('SELECT data_id, add_time, user_name, exercise_name, exercise_type, exercise_class, exercise_video_key FROM Exercise_db')
        db_data = []
        for item in q.iter():
            db_data.append({'data_id': item.data_id, 'add_time': str(item.add_time), 'user_name': item.user_name, 'exercise_name': item.exercise_name, 'exercise_type': item.exercise_type, 'exercise_class': item.exercise_class, 'exercise_video_key': item.exercise_video_key})
        return json.dumps(db_data)

    @classmethod
    def _get_one_data(self,data_id):
        # item = Exercise_db.get_by_id(data_id)
        q =ndb.gql('SELECT exercise_name, exercise_type, exercise_class from Exercise_db WHERE data_id= :1', data_id)
        for item in q:
          db_data = {'data_id': data_id, 'exercise_name': item.exercise_name, 'exercise_type': item.exercise_type, 'exercise_class': item.exercise_class}
        return json.dumps(db_data)

class addExercise_db(webapp2.RequestHandler):
    def post(self):

      if users.is_current_user_admin():
        data_id = self.request.get('data_id')
        if data_id and data_id != '':
          item = Exercise_db.get_by_id(data_id)
        else:
          date_time = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y%m%d%H%M%S")
          data_id = date_time
          item = Exercise_db(id=data_id)
          item.data_id = data_id
        # - -
        item.user_name = users.get_current_user().nickname()
        item.exercise_id = self.request.get('exercise_id')
        item.exercise_name = self.request.get('exercise_name')
        item.exercise_type = self.request.get('exercise_type')
        item.exercise_class = self.request.get('exercise_class')
        
        exercise_photo = self.request.get('exercise_photo')
        if exercise_photo:
          item.exercise_photo = images.resize(exercise_photo, 800, 600)
        #
        item.put()
        time.sleep(1)
        self.redirect('/manage/exercise')

class deleteData(webapp2.RequestHandler):
    def get(self):
        page_address = self.request.uri
        base = os.path.basename(page_address)
        split_address = base.split('?')
        data_set = split_address[1]
        data_id = split_address[2]

        if users.is_current_user_admin():
          item = Exercise_db.get_by_id(data_id)
          if item.exercise_video_key and len(item.exercise_video_key) > 0:
            blobkey = blobstore.blobstore.BlobKey(item.exercise_video_key)
            blobstore.delete(blobkey)

          item.key.delete()
          time.sleep(1)
          self.redirect('/list_data?exercise')

class listData(webapp2.RequestHandler):
    def get(self):
        page_address = self.request.uri
        base = os.path.basename(page_address)
        split_address = base.split('?')
        data_set = split_address[1]
        data_id = None
        if len(split_address) == 3:
          data_id = split_address[2]

        if data_set == 'exercise' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Exercise_db._get_all_data()) 

        if data_set == 'exercise' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Exercise_db._get_one_data(data_id)) 

class RenderImg(webapp2.RequestHandler):
    def get(self):
        page_address = self.request.uri
        base = os.path.basename(page_address)
        img_size = base.split('?')[1]
        data_id = base.split('?')[2]

        item = Exercise_db.get_by_id(data_id)
        img = images.Image(item.exercise_photo)
        if img_size == 'thumb':
            img.resize(width=70)
        if img_size == 'small':
            img.resize(width=250)
        if img_size == 'medium':
            img.resize(width=450)
        if img_size == 'large':
            img.resize(width=700)
        image = img.execute_transforms(output_encoding=images.JPEG)
        self.response.headers['Content-Type'] = 'image/jpeg'
        self.response.out.write(image)

class ViewVideo(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, video_key):
        if not blobstore.get(video_key):
            self.error(404)
        else:
            self.send_blob(video_key)

class UploadExerciseVideo(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        try:
            upload = self.get_uploads()[0]
            data_id = self.request.get('data_id')
            item = Exercise_db.get_by_id(data_id)

            if item:
              if item.exercise_video_key and len(item.exercise_video_key) > 0:
                blobkey = blobstore.blobstore.BlobKey(item.exercise_video_key)
                blobstore.delete(blobkey)
                item.exercise_video_key = str(upload.key())
              else:
                item.exercise_video_key = str(upload.key())
              item.put()
              self.redirect('/manage/exercise')
        except:
            self.error(500)

class publicSite(webapp2.RequestHandler):
    def get(self):
      # - page url
        page_address = self.request.uri
        path_layer = urlparse(page_address)[2].split('/')[1]
        base = os.path.basename(page_address)
      # - user
        user = users.get_current_user()
        if users.get_current_user(): # - logged in
          login_key = users.create_logout_url(self.request.uri)
          gate = 'Sign out'
          user_name = user.nickname()
        else: # - logged out
          login_key = users.create_login_url(self.request.uri)
          gate = 'Sign in'
          user_name = 'No User'
      # - app data
        app = Site
        page_name = 'Main'
        page_id = 'about'
        analytics = Analytics
        nav_html = public_nav_html
        page_html = page_header + about_page_html
        admin = ''
        data_id = ''
        if users.is_current_user_admin():
            admin = 'true' 

        if path_layer == 'programs':
            page_id = 'programs'
            page_name = 'Programs'
            page_html = page_header + programs_page_html

        if path_layer == 'results':
            page_id = 'results'
            page_name = 'Results'
            page_html = page_header + results_page_html

        if path_layer == 'exercises':
            page_id = 'exercises'
            page_name = 'Exercises'
            page_html = page_header + exercises_page_html

        if path_layer == 'about':
            page_id = 'about'
            page_name = 'About'
            page_html = page_header + about_page_html

        # - manage, edit, publish pages for public 
        if path_layer == 'manage' or path_layer == 'edit' or path_layer == 'publish':
            page_id = 'login_page'
            page_name = 'Log in'
            nav_html = admin_nav_html
            page_html = manage_page_html
            page_class = 'manage'

        # - manage, edit, publish pages for admin
        if admin == 'true':

          if path_layer == 'manage':
              if base == 'manage' or base == '':
                page_id = 'manage'
                page_name = 'Manage'
                nav_html = admin_nav_html
                page_html = manage_page_html

              if base == 'exercise':
                page_id = 'manage_exercise'
                page_name = 'Manage Exercise'
                nav_html = admin_nav_html
                page_html = manage_exercise_page_html

          if path_layer == 'edit':
              if base == 'edit' or base == '':
                page_id = 'edit'
                page_name = 'Edit'
                nav_html = admin_nav_html
                page_html = manage_page_html

              if base.startswith('exercise'):
                page_id = 'edit_exercise'
                page_name = 'Edit Exercise'
                nav_html = admin_nav_html
                page_html = edit_exercise_page_html
                data_id = base.split('?')[1]

          if path_layer == 'publish':
              if base == 'exercise':
                page_id = 'publish_exercise'
                page_name = 'Publish Exercise'
                nav_html = admin_nav_html
                page_html = publish_exercise_page_html

              if base.startswith('exercise_video'):
                page_id = 'publish_exercise_video'
                page_name = 'Publish Exercise Video'
                nav_html = admin_nav_html
                upload_url = blobstore.create_upload_url('/upload_exercise_video')
                page_html = publish_exercise_video_page_html.format(upload_url)
                data_id = base.split('?')[1]

          if path_layer == 'entries':
              page_id = 'entries'
              page_name = 'Entries'
              if admin == 'true':         
                  page_html = entries_page_html_admin #!
              else:
                  page_html = entries_page_html

          if path_layer == 'code':
              page_id = 'code'
              page_name = 'Code'
              page_html = code_page_html
               
      # - template
        objects = {
            'Site': app,
            'analytics': analytics,
            'login_key': login_key,
            'gate': gate,
            'user_name': user_name,
            'admin': admin,
          # -
            'path_layer': path_layer,
            'base': base,
            'page_name': page_name,
            'page_id': page_id,
            'nav_html': nav_html,
            'page_html': page_html,
            'data_id': data_id,     
        }
      # - render
        path = os.path.join(os.path.dirname(__file__), 'html/publicSite.html')
        self.response.out.write(template.render(path, objects))

#----------------------------------------------#
#                                              #
#----------------------------------------------#
app = webapp2.WSGIApplication([    # - Pages
    ('/', publicSite),
    
    ('/programs/?', publicSite),
    ('/results/?', publicSite),
    ('/exercises/?', publicSite),
    ('/about/?', publicSite),

    ('/manage/?', publicSite),
    ('/manage/exercise/?', publicSite),

    ('/edit/?', publicSite),
    ('/edit/exercise/?', publicSite),

    ('/publish/exercise/?', publicSite),
    ('/publish/exercise_video?', publicSite),

    ('/manage/add_exercise/?', addExercise_db),
    ('/upload_exercise_video/?', UploadExerciseVideo),
    ('/list_data/?', listData),
    ('/delete_data/?', deleteData),
    ('/render_img/?', RenderImg),
    ('/view_video/([^/]+)?', ViewVideo),

    ('/entries/?', publicSite),
      ('/list_exercises/?', listData),
    ('/code/?', publicSite),


], debug=True)

