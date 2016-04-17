#!/usr/bin/python
# coding: latin-1

Site = 'Shanny Cohen Fitness'

# Timezone = 'Pacific/Honolulu'
Timezone = 'US/Pacific'

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
  header { width: 100%; }
  .sub_title { border-top: 1px solid #eee; }
  .top_wrap { position: absolute; top: 0; left: 0; right: 0; height: 70px; width: 175px; }
  .social_wrap a { color: #fff; margin-bottom: 25px; padding-left: 10px;}
  .social_wrap a:hover { color: #444; }

  </style>
  <header>
    <div class="top_wrap">
      <div class="logo_wrap">SHANNY COHEN
        <div class="sub_title">FITNESS</div>
      </div>
    </div><!-- . top_wrap - -->
  </heeader>
'''
public_nav_html = '''
  <nav class="main_nav">
    <ul>
      <a href="../../programs"><li id="programsNav">Programs</li></a>
      <a href="../../results"><li id="resultsNav">Results</li></a>
      <a href="../../exercises"><li id="exercisesNav">Exercises</li></a>
      <a href="../../about"><li id="aboutNav">About</li></a>
      <a href="/contact"><li id="contactNav">Contact</li></a>
    </ul>
    <div class="social_wrap">
      <a href="https://www.instagram.com/shannycohen_fitness/" target="_blank"><i class="fa fa-instagram"></i></a>
      <a href="https://twitter.com/shannycohen_fit" target="_blank"><i class="fa fa-twitter-square"></i></a>
      <a href="https://www.facebook.com/ShannyCohenAthletePage/timeline" target="_blank"><i class="fa fa-facebook-official"></i></a>
    </div><!-- . social_wrap - -->
    </nav><!-- - /main_nav - -->
'''
about_page_html = '''
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
            <td class="label">Email Address</td>
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
    <p>Sign in with your Google account</p>
  </div><!-- .main_wrap -->
'''
admin_nav_html = '''
  <nav class="main_nav"><ul>
    <a href="../../"><li id="programsNav">&#8672; Public</li></a>
    <a href="../../manage/client"><li id="clientNav">Client</li></a>
    <a href="../../manage/waitlist"><li id="waitlistNav">Waitlist</li></a>
    <a href="../../manage/exercise"><li id="exerciseNav">Exercise</li></a>
    <a href="../../manage/testimonial"><li id="testimonialNav">Testimonial</li></a>
  </ul></nav><!-- - /main_nav - -->
'''
manage_page_html = '''
  <div class="main_wrap">
    <p>Choose a data set from the right to edit</p>
  </div><!-- .main_wrap -->
'''
#----------------------------------------------#
#           Contact me page                    #
#----------------------------------------------#
contact_page_html = '''
  <style>
  .form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px; padding: 45px; }
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  </style>
  <div class="main_wrap">
    <header class="hi"><span class="color_b">Submit a Question</span></header>
    <article class="form_wrap">
      <form action="/submit_question"  method="post">
        <table>
          <tr>
            <td class="label">Name*</td>
            <td class="input"><input type="text" name="client_name" required/></td>
          </tr>
          <tr>
            <td class="label">Email*</td>
            <td class="input"><input type="email" name="client_email" required/></td>
          </tr>
          <tr>
            <td class="label">Address</td>
            <td class="input"><textarea name="client_address" rows="5" cols="20" ></textarea></td>
          </tr>
          <tr>
            <td class="label">Question*</td>
            <td class="input"><textarea name="client_question" rows="20" cols="30" required></textarea></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right"><input type="submit" value="Submit" /></td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - .main_wrap - -->
'''
contact_success_page_html = '''
  <div class="main_wrap">
  <h2>Your question has been submitted.</h2>
  <h2>We'll reply as soon as possible.</h2>
  </div><!-- .main_wrap -->
'''
#----------------------------------------------#
#           Exersice Publish Manage            #
#----------------------------------------------#
exercises_page_html = '''
  <style type="text/css">
    #exercise_wrap{width:100%;}
    #initial_category_wrap, .select_category_wrap, .select_data_wrap{width: 20%; display: inline-block; vertical-align: top; margin: 15px 1%;} 
    .select_category_wrap{border: 1px solid grey;}
    .select_data_wrap{width:75%;}
    .exercise_data{border: 1px solid grey; border-radius: 3px; text-align: left; padding: 10px; margin-bottom: 15px;}
    .img_wrap{width: 30%}
    .text_wrap{width: 60%;}
    .img_wrap, .text_wrap{display: inline-block; vertical-align: top;}
  </style>
  <div class="main_wrap">

    <div id="initial_category_wrap" ng-click="display_exercises()">
      <label ng-repeat="muscle in muscles">
        <input type="checkbox" value="[!muscle.name!]" ng-model="muscle.selected" ng-click="toggle_muscle_selection(muscle.name)" class="hide"> [!muscle.name!]<br>        
      </label>        
      <label>
        <input type="checkbox" name="select_all" value="select_all" ng-click="select_all_exercises()" class="hide"> All Exercises<br>        
      </label>       
    </div><!--.initial_category_wrap-->

   <div class="hide" id="exercise_wrap">

      <div class="select_category_wrap">

        <form ng-submit='sel_by_name()'>
          <label>Seach by exercise name:</label><br>
          <input type="text" placeholder="e.g. Push Ups" ng-model='select_name' ng-change='sel_by_name()'>
          <input class="hide" type="submit" value="Submit" />
        </from>

        <hr>
        <p><b>Muscle Targeted</b></p>
        <label>
          <input type="checkbox" name="select_all" value="all" ng-click="select_all_muscles()" class="hide"> Select All<br>        
        </label> 
        <label>
          <input type="checkbox" name="deselect_all" value="deselect_all" ng-click="deselect_all_muscles()" class="hide"> Deselect All<br>        
        </label>  
        <label ng-repeat="muscle in muscles">
          <input type="checkbox" value="[!muscle.name!]" ng-model="muscle.selected" ng-click="toggle_muscle_selection(muscle.name)"> [!muscle.name!]<br>   
        </label> 

        <hr>
        <p><b>Equipment Type</b></p> 
        <label>
          <input type="checkbox" name="select_all" value="all" ng-click="select_all_equipments()" class="hide"> Select All<br>        
        </label> 
        <label>
          <input type="checkbox" name="deselect_all" value="deselect_all" ng-click="deselect_all_equipments()" class="hide"> Deselect All<br>        
        </label>  
        <label ng-repeat="equipment in equipments">
          <input type="checkbox" value="[!equipment.name!]" ng-model="equipment.selected" ng-click="toggle_equipment_selection(equipment.name)"> [!equipment.name!]<br>   
        </label>   
      
      </div><!--.select_category_wrap-->

      <div class="select_data_wrap">
       <p>Find [! (display_data| filter: select_name).length!] exercise(s)</p>
       <hr>
        <div class="exercise_data" ng-repeat="item in display_data | filter: select_name ">
          <a ng-href="/exercise_detail/?data_id=[!item.data_id!]">
          <div class="img_wrap">
            <img ng-src="/render_img?exercise?thumb?[!item.data_id!]">
          </div><!--.img_wrap-->

          <div class="text_wrap">
            <p> Exercise Name: [! item.exercise_name !] </p>  
            <p> Equipment Type: [! item.equipment_type !] </p> 
            <p> Muscle Targeted: [! item.muscle_targeted !] </p> 
          </div><!--.text_wrap-->
          </a>
        </div><!--.exercise_data-->
      </div><!--.select_data_wrap-->
    </div><!--.exercise_wrap-->
  </div><!-- .main_wrap -->
'''
exercise_detail_page_html = '''
  <style>
    .video_wrap{max-width:350px; max-height:250px;}
    .video_wrap, .text_wrap{display:inline-block; vertical-align:top;margin: 15px 10px;}
    .video_controls {opacity: 0; position: absolute; margin: 0 auto; width: 100%;}
    .video_controls:hover {opacity: 1;}
    #volume-bar{width: 50px;}
    .img_wrap{width: 100%; max-height: 400px; margin: 25 auto;}
  </style>
  <div class="main_wrap">
    <div class="video_wrap" ng-show='item.exercise_video_key'>
      <video id="video" width="300" height="200" ng-src="[!video_url!]"></video>

      <div id="video_controls">
        <button type="button" id="play-pause"><i class="fa fa-play"></i></button>
        <input type="range" id="seek-bar" value="0">
        <button type="button" id="mute"><i class='fa fa-volume-off'></i></button>
        <input type="range" id="volume-bar" min="0" max="1" step="0.1" value="1">
        <button type="button" id="full-screen"><i class="fa fa-expand"></i></button>
      </div><!--.video_controls-->
    </div><!--.video_wrap-->

    <div class="text_wrap">
      <p> Exercise Name: [! item.exercise_name !] </p>  
      <p> Equipment Type:  [! item.equipment_type !] </p> 
      <p> Muscle Targeted:  [! item.muscle_targeted !] </p> 
    </div><!--.text_wrap-->
    <hr>

    <div class="img_wrap">
      <h3>[!item.exercise_name!] Images</h3>
      <img ng-src="/render_img?exercise?large?[!item.data_id!]">
    </div><!--.img_wrap-->

  </div><!-- .main_wrap -->
'''
manage_exercise_page_html = '''
  <style type="text/css">
    .exercise_data{border: 1px solid grey; border-radius: 3px; text-align: left; padding: 10px; margin-top: 15px;}
    .img_wrap{width: 15%}
    .text_wrap{width: 80%;}
    .img_wrap, .text_wrap{display: inline-block; vertical-align: top; margin-left:auto; margin-right:auto;}
  </style>
  <div class="main_wrap">
    <a href='/publish/exercise'><button>Add A New Exercise</button></a>
    <hr>
    <div class="input-group">
      <span>Seach by exercise name:</span>
      <input ng-model='select_name' type="text" placeholder="e.g. Push Ups">
    </div>

    <div class="exercise_data" ng-repeat="item in exercise_data | filter:select_name">
      <div class="text_wrap">
        <p> Add Time:  [! item.add_time | limitTo: 10 !] </p>
        <p> User: [! item.user_name !] </p>
        <p> Exercise Name:  [! item.exercise_name !] </p>  
        <p> Equipment Type:  [! item.equipment_type !] </p> 
        <p> Muscle Targeted:  [! item.muscle_targeted !] </p> 
        <p ng-show='item.exercise_video_key'> <a ng-href="/view_video/[!item.exercise_video_key!]" target="_blank"> View Video </a></p>
      </div><!--.text_wrap-->

      <div class="img_wrap">
        <img ng-src="/render_img?exercise?thumb?[!item.data_id!]">
      </div><!--.img_wrap-->

      <br>
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
            <td class="label">Name*</td>
            <td class="input"><input type="text" name="exercise_name" required/></td>
          </tr>
          <tr>
            <td class="label">Equipment Type*</td>
            <td class="input">
              <select name="equipment_type" required>
                <option ng-repeat="equipment in equipments" value="[!equipment.name!]">[!equipment.name!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Muscle Targeted*</td>
            <td class="input">
              <label ng-repeat="muscle in muscles">
                <input type="checkbox" name="muscle_targeted" value="[!muscle.name!]" ng-model="muscle.selected" ng-click="toggle_selection()" ng-required="!if_any_selected"> [!muscle.name!]
                <br>
              </label>            
            </td>
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
            <td class="label">Name*</td>
            <td class="input"><input type="text" name="exercise_name" ng-model='exercise_name' required/></td>
          </tr>
          <tr>
            <td class="label">Equipment Type*</td>
            <td class="input">
              <select name="equipment_type" ng-model='equipment_type' required>
                <option ng-repeat="equipment in equipments" value="[!equipment.name!]">[!equipment.name!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Muscle Targeted*</td>
            <td class="input">
              <label ng-repeat="muscle in muscles">
                <input type="checkbox" name="muscle_targeted" value="[!muscle.name!]" ng-model="muscle.selected" ng-click="toggle_selection()" ng-required="!if_any_selected"> [!muscle.name!]<br>
              </label>            
            </td>
          </tr>
          <tr>
            <td class="label">Photo</td>
            <td class="input"><img ng-src="/render_img?exercise?thumb?[!data_id!]"></td>
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
#----------------------------------------------#
#    Programs Signup and Payment               #
#----------------------------------------------#
silver_brozen_coupon_limit =10

programs_page_html = '''
  <style>
  body { background: url("pics/programs.jpg") no-repeat center center fixed; background-size: cover;}
  .programs_title { color: #000; text-align: center; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), white, rgba(0, 0, 0, 0)); letter-spacing: 5px;}
  .package_list { text-align: center; padding-top: 30px;}
  .package_wrap { background: rgba(0, 0, 0, 0.8); display: inline-block; text-align: center; width: 400px; margin: 20px; vertical-align: top; padding: 20px; }
  .package_wrap ul { padding-left: 20px;}
  .package_wrap li { text-align: left; font-size: 14px; margin-bottom: 5px; padding: 5px;}
  .package_title { color: black; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), white, rgba(0, 0, 0, 0));}
  .package_info { background: rgba(255, 255, 255, 0.1); padding: 10px;}
  .sign_up_text {color: red; font-size:16px; }
  .sign_up_btn {border:none; border-radius: 0; padding: 5px; font-size: 14px; margin: 0 5px;}
  </style>

  
  <div class="main_wrap">
  <h3 class="programs_title" style='color:red'>Test Mode, Not use this page to Sign up now. <br> Instead, please email shannycohen.fitness@gmail.com</h3>
  <h2 class="programs_title">Personalized Packages</h2>

  <div class="package_list">
      <div class="package_wrap">
        <div class="package_data">
          <h2 class="package_title"><b>Platinum</b></h2>
          <p class="package_price">$550/Month</p>
            <p class="package_info"> 7 day a week program that is fully customized to each clients goals, fitness level, physical injuries and health conditions.</p>
              <ul class="package_list">
                <li>Written workout available online or printable daily. Weekly workouts posted or emailed Sunday nights.</li>
                <li>Personalized daily video of the focus for each exercise</li>
                <li>Start and end point photos of each written exercise</li>
                <li>Check in and feedback reports with Shanny throughout the week</li>
                <li>Customized to your fitness goals</li>
              </ul>
        </div><!-- . package_data - -->
        <div>
          <p class="sign_up_text">* Limited Spots Available</p>
          <button class="sign_up_btn" ng-disabled='!platinum_avail' ng-click=" confirm_signup('Platinum') ">Sign Up</button>
          <button class="sign_up_btn" ng-disabled='platinum_avail' ng-click=" add2waitlist('Platinum') ">Add to Waitlist</button>
        </div>
      </div><!-- . package_wrap - -->
      <div class="package_wrap">
        <div class="package_data">
          <h2 class="package_title"><b>Gold</b></h2>
          <p class="package_price">$330/Month</p>
            <p class="package_info"> 3 day a week program that is fully customized to each clients goals, fitness level, physical injuries and health conditions.</p>
              <ul class="package_list">
                <li>Written workout available online or printable three times a week. Weekly workouts posted or emailed Sunday nights.</li>
                <li>Personalized daily video of the focus for each exercise</li>
                <li>Start and end point photos of each written exercise</li>
                <li>Check in and feedback reports with Shanny throughout the week</li>
                <li>Customized to your fitness goals </li>
              </ul>
        </div><!-- . package_data - -->
        <div>
          <p class="sign_up_text">* Limited Spots Available</p>
          <button class="sign_up_btn" ng-disabled='!gold_avail' ng-click=" confirm_signup('Gold') ">Sign Up</button>
          <button class="sign_up_btn" ng-disabled='gold_avail' ng-click=" add2waitlist('Gold') ">Add to Waitlist</button>
        </div>
      </div><!-- . package_wrap - -->

      <h2 class="programs_title">Memberships</h2>
      <div class="package_wrap">
        <div class="package_data">
          <h2 class="package_title"><b>Silver</b></h2>
          <p class="package_price">$200/Month</p>
            <p class="package_info">5 workouts a week emailed directly to you.</p>
              <ul class="package_list">
                <li>3 workout lifting videos</li>
                <li>1 HIIT(High Intensity Interval Training) / class / abs</li>
                <li>Recovery, myofacial release, flexibility and balance work</li>
                <li>Focus on muscle definition, strength, endurance, weight loss, flexibility and balance</li>
              </ul>
        </div><!-- . package_data - -->
        <button class="sign_up_btn" ng-click="confirm_signup('Silver'); ">Sign Up</button>
      </div><!-- . package_wrap - -->
      <div class="package_wrap">
        <div class="package_data">
          <h2 class="package_title"><b>Bronze</b></h2>
          <p class="package_price">$100/Month</p>
            <p class="package_info"> 3 workouts a week emailed directly to you. </p>
              <ul class="package_list">
                <li>2 days of weight training</li>
                <li>1 day of HIIIT/ class and abs</li>
                <li>Focus on muscle definition, strength, endurance, weight loss, flexibility and balance</li>
              </ul>
        </div><!-- . package_data - -->
        <button class="sign_up_btn" ng-click=" confirm_signup('Bronze'); ">Sign Up</button>
      </div><!-- . package_wrap - -->
    </div><!-- . package_list - —>

  </div><!-- . main_wrap - -->
'''
confirm_signup_page_html = '''
  <style>
  .confirm_signup_btn{display: inline-block; border-radius: 0; border: none; padding: 5px;}
  </style>
  <div class="main_wrap">
    <p>You have chosen the [!program_chosen!] Program ($[!price!]/month).</p>
    <button class='confirm_signup_btn' ng-click="back2programs();">Cancel</button>
    <button class='confirm_signup_btn' ng-click="go2payment();">Go to Payment</button>
  </div><!-- .main_wrap -->
'''
add2waitlist_page_html = '''
  <style>
  .confirm_signup_btn{display: inline-block; border-radius: 0; border: none; padding: 5px;}
  </style>
  <div class="main_wrap">
    <p>You will be added to the Waitlist for [!program_chosen!] Program ($[!price!]/month).</p>
    <article class="form_wrap">
      <form action="/manage/add_waitlist" method="post">
        <table>
          <tr>
            <td class="label">Name</td>
            <td class="input"><input type="text" name="client_name" required/></td>
          </tr>
          <tr class="hide">
            <td class="label">Program</td>
            <td class="input"><input type="text" name="client_program" ng-model='program_chosen' required/></td>
          </tr>
          <tr class="hide">
            <td class="label">Email</td>
            <td class="input"><input type="text" name="client_email" ng-model='client_email' required/></td>
          </tr>
          <tr>
            <td class="label">Phone (optional)</td>
            <td class="input"><input type="text" name="client_phone"/></td>
          </tr>
          <tr>
            <td class="label">Adress (optional)</td>
            <td class="input"><input type="text" name="client_address"/></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href='/programs'><button type='button' class='confirm_signup_btn'>Cancel</button></a>
              <input class='confirm_signup_btn' type="submit" value="Yes" /></td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- .main_wrap -->
'''
payment_page_html = '''
  <style>
  .form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px;text-align:center;}
  form{padding: 15px 45px;}
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  td.input { font-size: 14px; text-align: left; padding-left: 10px; }
  .form_title{background: #0D47A1; padding: 10px; color:#fff;}
  .payment-errors{color:red;}
  .stripe_img{margin: 25px auto;}
  button[type='submit']{border-radius:0; padding: 5px; font-size: 12px;}
  </style>
  <div class="main_wrap">
  <article class="form_wrap">
    <div class="form_title">
      <h3>[!program_chosen!] Program</h3>
      <h3>Price: $[!price!]/month</h3>
    </div>
    <form action="/charge_card/" id="payment-form" method="post">
      <span class="payment-errors"></span>
      <span class="payment-errors" ng-show="program_status=='Active'">You have already enrolled in a program.</span>
    <table>
      <tr>
        <td class="label">Name*</td>
        <td class="input"><input type="text" name="client_name" required/></td>
      </tr>
      <tr class="hide">
        <td class="label">Email*</td>
        <td class="input"><input type="text" name="client_email" ng-model="client_email" required/></td>
      </tr>
      <tr class="hide">
        <td class="label">Program*</td>
        <td class="input"><input type="text" name="client_program" ng-model="program_chosen" required/></td>
      </tr>
      <tr class="hide">
        <td class="label">Price*</td>
        <td class="input"><input type="text" name="amout" ng-model="price" required/></td>
      </tr>     
      <tr>
        <td class="label">Phone</td>
        <td class="input"><input type="text" name="client_phone" /></td>
      </tr>   
      <tr>
        <td class="label">Address</td>
        <td class="input"><textarea type="text" name="client_address" rows="10" cols="20"></textarea></td>
      </tr>   
      <tr>
        <td class="label">Card Number*</td>
        <td class="input"><input type="text" size="20" data-stripe="number"/></td>
      </tr>
      <tr>
        <td class="label">CVC*</td>
        <td class="input"><input type="text" size="4" data-stripe="cvc"/></td>
      </tr>
      <tr>
        <td class="label">Expiration (MM/YYYY)*</td>
        <td class="input">
          <input type="text" size="2" data-stripe="exp-month"/>
          <span> / </span>
          <input type="text" size="4" data-stripe="exp-year"/>
        </td>
      </tr>
      <tr>
        <td></td>
        <td style="text-align:right"><button type="submit" ng-disabled="program_status=='Active'">Subscribe to Program</button></td>
      </tr>
     </table>
    </form>
    <img class="stripe_img" style="width:200px;" src='/pics/stripe.png'>
  </article><!-- - /form_wrap - -->
  </div><!-- .main_wrap -->
'''
payment_success_page_html = '''
  <div class="main_wrap">
  <h2>Thank you for your payment.</h2>
  <h2>You will recieve an email reciept.</h2>
  </div><!-- .main_wrap -->
'''
cancel_program_success_page_html = '''
  <div class="main_wrap">
  <h2>Your have quit the program.</h2>
  </div><!-- .main_wrap -->
'''

#----------------------------------------------#
#        Results and Testimonials              #
#----------------------------------------------#
results_page_html = '''
  <style type="text/css">
    .testimonial_wrap{border: 1px solid grey; border-radius: 3px; text-align: left; padding: 10px; margin-top: 15px;}
    .show_btn{color: steelblue;}
    .testimonial_thumb{max-width:100px;}
    .modal-backdrop{position: fixed; top: 0; left: 0; bottom: 0; right: 0;  z-index: 150;  background:rgba(0,0,0, 0.6);}
    .modal{position: absolute; top:25px; z-index: 200; text-align: center; margin: auto auto; max-height:90%; max-width:90%;}
    #lg_img{max-height: 90%; max-width: 90%; margin: auto auto;}
    </style>
  <div class="main_wrap">
    Results and Testimonials
    <hr>

    <div class="modal-backdrop" ng-show="modal_show"></div>
    <div class="modal" ng-show="modal_show">
      <img id="lg_img" ng-src='[!lg_img_url!]'>
      <button ng-click="hide_lg_img()">Close</button>
    </div>

    <div class="testimonial_wrap" ng-repeat="item in testimonial_data">
      <testimonial-view data="item"></testimonial-view>
    </div><!-- .testimonial_wrap -->
  </div><!-- . main_wrap - -->
'''
manage_testimonial_page_html = '''
  <style type="text/css">
    .testimonial_wrap{border: 1px solid grey; border-radius: 3px; text-align: left; padding: 10px; margin-top: 15px;}
    .show_btn{color: steelblue;}
    .testimonial_thumb{max-width:100px;}
    .modal-backdrop{position: fixed; top: 0; left: 0; bottom: 0; right: 0;  z-index: 150;  background:rgba(0,0,0, 0.6);}
    .modal{position: absolute; top:25px; z-index: 200; text-align: center; margin: auto auto;max-height:90%; max-width:90%;}
    #lg_img{max-height: 600px; max-width: 800px; margin: auto auto;}
  </style>
  <div class="main_wrap">
    <a href='/publish/testimonial'><button>Add A New Testimonial</button></a>
    <hr>

    <div class="modal-backdrop" ng-show="modal_show"></div>
    <div class="modal" ng-show="modal_show">
      <img id="lg_img" ng-src='[!lg_img_url!]'>
      <button ng-click="hide_lg_img()">Close</button>
    </div>

    <div class="testimonial_wrap" ng-repeat="item in testimonial_data">
      <testimonial-view></testimonial-view>
      <br>
      <a ng-href='/edit/testimonial?[!item.data_id!]'><button>Edit Info</button></a>
      <button ng-click="delete(item.data_id)">Remove</button>
    </div><!-- .testimonial_wrap -->

  </div><!-- . main_wrap - -->
'''
edit_testimonial_page_html = '''
  <style>
  .form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px; padding: 45px; }
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap">
   <header class="hi"><span class="color_b">Edit Testimonial</span></header>
   <article class="form_wrap">
      <form action="/manage/add_testimonial" enctype="multipart/form-data"  method="post">
        <table>
          <tr class="hide">
            <td class="label">data_id</td>
            <td class="input"><input type="text" name="data_id" ng-model='data_id' required/></td>
          </tr>
          <tr>
            <td class="label">Name*</td>
            <td class="input"><input type="text" name="client_name" ng-model="item.client_name" required/></td>
          </tr>
          <tr>
            <td class="label">Comment*</td>
            <td class="input"><textarea rows="20" cols="32" name="testimonial_text"  ng-model="item.testimonial_text" required></textarea></td>
          </tr>
          <tr>
            <td class="label">Photo</td>
            <td class="input"><input type="file" name="testimonial_photo"/></td>
          </tr>
          <tr>
            <td class="label">
             <img ng-src="[! item.has_photo?'/render_img?testimonial?thumb?'+item.data_id : '' !]">
             </td>
            <td class="input"></td>         
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/testimonial"><button type="button">Cancel</button></a>
              <input type="submit" value="Save" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - .main_wrap - --> 
'''
publish_testimonial_page_html = '''
  <style>
  .form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px; padding: 45px; }
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap">
   <header class="hi"><span class="color_b">Add New Testimonial</span></header>
   <article class="form_wrap">
      <form action="/manage/add_testimonial" enctype="multipart/form-data"  method="post">
        <table>
        <table>
          <tr>
            <td class="label">Name*</td>
            <td class="input"><input type="text" name="client_name" required/></td>
          </tr>
          <tr>
            <td class="label">Comment*</td>
            <td class="input"><textarea rows="20" cols="32" name="testimonial_text" required></textarea></td>
          </tr>
          <tr>
            <td class="label">Photo</td>
            <td class="input"><input type="file" name="testimonial_photo"/></td>
          </tr>          
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/testimonial"><button type="button">Cancel</button></a>
              <input type="submit" value="Save" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - .main_wrap - --> 
'''
#----------------------------------------------#
#             Client Interface                 #
#----------------------------------------------#
my_account_page_html = '''
  <div class="main_wrap">
    <p><a href="/my_account/my_workout">My Workout Plan</a></p>
    <p><a href="/my_account/my_testimonial">My Testimonials</a></p>
    <p><a href="/my_account/my_program">My Program</a></p>
    <p><a href="/my_account/my_info">My Info</a></p>
  </div><!-- .main_wrap -->
'''
my_program_page_html = '''
  <div class="main_wrap">
    <div>
      <p>Program: [!client_program!]</p> 
        <p ng-show='program_status'>Program Status: [!program_status !]</p> 
        <a ng-show="program_status!='Canceled'&&client_program&&stripe_cus_id&&stripe_subscription_id"><button ng-disabled="btn_disable" ng-click="cancel_program()">Cancenl Program</button></a>
        <p ng-show='comment'> [!comment!]</p> 
    </div>
    <hr>
    <div>
      <p>Waitlist: [!client_waitlist!]</p>
        <p ng-show='client_waitlist'>Since: [!waitlist_add_time | limitTo: 10!]</p> 
    </div>
  </div><!-- .main_wrap -->
'''
my_info_page_html = '''
  <style type="text/css">
    .client_data{border: 1px solid grey; border-radius: 3px; text-align: left; padding: 10px; margin-top: 15px;}
    .img_wrap{width: 15%}
    .text_wrap{width: 75%;}
    .img_wrap, .text_wrap{display: inline-block; vertical-align: top;}
  </style>
  <div class="main_wrap">
    <div class="client_data">
      <div class="text_wrap">
        <p> Client Name:  [! item.client_name !] </p>  
        <p> Phone:  [! item.client_phone !] </p> 
        <p> Address:  [! item.client_address !] </p> 
      </div><!--.text_wrap-->

      <div class="img_wrap">
        <img ng-src="[! item.has_photo?'/render_img?client?thumb?'+item.client_email : '' !]">
      </div><!--.img_wrap-->

      <br>
      <a ng-href='/my_account/edit_my_info'><button ng-disabled="btn_disable">Edit Info</button></a>
    </div><!--.client_data-->
  </div><!-- .main_wrap -->
'''
edit_my_info_page_html = '''
  <style>
  .form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px; padding: 45px; }
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  td img{max-width:70px;}
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap">
   <header class="hi"><span class="color_b">Edit Client [!item.client_email!]</span></header>
    <article class="form_wrap">
      <form action="/my_account/add_my_info" enctype="multipart/form-data" method="post">
        <table>
          <tr class="hide">
            <td class="label">Email</td>
            <td class="input"><input type="text" name="client_email" ng-model='item.client_email' required/></td>
          </tr>
          <tr>
            <td class="label">Name</td>
            <td class="input"><input type="text" name="client_name" ng-model='item.client_name' required/></td>
          </tr>
          <tr>
            <td class="label">Phone</td>
            <td class="input"><input type="text" name="client_phone" ng-model='item.client_phone'/></td>
          </tr>
          <tr>
            <td class="label">Address</td>
            <td class="input"><input type="text" name="client_address" ng-model='item.client_address'/></td>
          </tr>
          <tr>
            <td class="label">Photo</td>
            <td class="input"><input type="file" name="testimonial_photo"/></td>
          </tr>
          <tr>
            <td class="label"><img ng-src="[! item.has_photo?'/render_img?client?thumb?'+item.client_email : '' !]"></td>
            <td class="input"></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/my_account/my_info"><button type="button">Cancel</button></a>
              <input type="submit" value="Save" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - .main_wrap - -->
'''
my_testimonial_page_html = '''
  <style type="text/css">
    .testimonial_wrap{border: 1px solid grey; border-radius: 3px; text-align: left; padding: 10px; margin-top: 15px;}
    .show_btn{color: steelblue;}
    .testimonial_thumb{max-width:100px;}
    .modal-backdrop{position: fixed; top: 0; left: 0; bottom: 0; right: 0;  z-index: 150;  background:rgba(0,0,0, 0.6);}
    .modal{position: absolute; top:25px; z-index: 200; text-align: center; margin: auto auto;}
    #lg_img{max-height: 600px; max-width: 800px; margin: auto auto;}
    </style>
  <div class="main_wrap">
    <a href='/my_account/publish_my_testimonial'><button>Add A New Testimonial</button></a>
    <hr>

    <div class="modal-backdrop" ng-show="modal_show"></div>
    <div class="modal" ng-show="modal_show">
      <img id="lg_img" ng-src='[!lg_img_url!]'>
      <button ng-click="hide_lg_img()">Close</button>
    </div>

    <div class="testimonial_wrap" ng-repeat="item in testimonial_data">
      <testimonial-view data="item"></testimonial-view>
      <br>
      <a ng-href='/my_account/edit_my_testimonial?[!item.data_id!]'><button>Edit Info</button></a>
      <button ng-click="delete(item.data_id)">Remove</button>
    </div><!-- .testimonial_wrap -->
  </div><!-- . main_wrap - -->
'''
edit_my_testimonial_page_html = '''
  <style>
  .form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px; padding: 45px; }
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap">
   <header class="hi"><span class="color_b">Edit Testimonial</span></header>
   <article class="form_wrap">
      <form action="/manage/add_testimonial" enctype="multipart/form-data"  method="post">
        <table>
          <tr class="hide">
            <td class="label">data_id</td>
            <td class="input"><input type="text" name="data_id" ng-model='data_id' required/></td>
          </tr>
          <tr>
            <td class="label">Name*</td>
            <td class="input"><input type="text" name="client_name" ng-model="item.client_name" required/></td>
          </tr>
          <tr>
            <td class="label">Comment*</td>
            <td class="input"><textarea rows="20" cols="32" name="testimonial_text"  ng-model="item.testimonial_text" required></textarea></td>
          </tr>
          <tr>
            <td class="label">Photo</td>
            <td class="input"><input type="file" name="testimonial_photo"/></td>
          </tr>
          <tr>
            <td class="label">
             <img ng-src="[! item.has_photo?'/render_img?testimonial?thumb?'+item.data_id : '' !]">
             </td>
            <td class="input"></td>         
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/my_account/my_testimonial"><button type="button">Cancel</button></a>
              <input type="submit" value="Save" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - .main_wrap - --> 
'''
publish_my_testimonial_page_html = '''
  <style>
  .form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px; padding: 45px; }
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap">
   <header class="hi"><span class="color_b">Add New Testimonial</span></header>
   <article class="form_wrap">
      <form action="/manage/add_testimonial" enctype="multipart/form-data"  method="post">
        <table>
          <tr>
            <td class="label">Name*</td>
            <td class="input"><input type="text" name="client_name" required/></td>
          </tr>
          <tr>
            <td class="label">Comment*</td>
            <td class="input"><textarea rows="20" cols="32" name="testimonial_text" required></textarea></td>
          </tr>
          <tr>
            <td class="label">Photo</td>
            <td class="input"><input type="file" name="testimonial_photo"/></td>
          </tr>          
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/my_account/my_testimonial"><button type="button">Cancel</button></a>
              <input type="submit" value="Save" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - .main_wrap - --> 
'''
my_workout_page_html='''
  <style type="text/css">
    .main_wrap a{text-decoration:underline;}
    .outter_wrap{width: 100%; overflow-x:scroll;}
    .workout_plan{width: 1200px; table-layout: fixed; }
    .workout_plan th{background:#37474F; color: #fff; padding: 5px; min-width: 100px;}
    .workout_plan td{padding: 5px; min-width: 100px;}
    .White, .LightBlue, .LightGreen, .LightGrey, .BlueGrey {border:1px solid grey; padding: 10px 10px; margin: 5px auto;}
    .White{background:#fff;}
    .LightBlue{background:#81D4FA;}
    .LightGreen{background:#B2DFDB;}
    .LightGrey{background:#E0E0E0;}
    .BlueGrey{background:#B0BEC5;}
  </style>
  <div class="main_wrap">
        <p>[!item.program_date!]&nbsp;&nbsp;[!item.muscles!]&nbsp;&nbsp;[!item.client_name!]</p>
        <p>[!item.general_explanation!]</p>

        <div class="outter_wrap">
        <table class="workout_plan">

        <tr>
          <th>Exercise</th>
          <th>Warm up sets</th>
          <th>Set 1</th>
          <th>Set 2</th>
          <th>Set 3</th>
          <th ng-show="table_length>=4">Set 4</th>
          <th ng-show="table_length>=5">Set 5</th>
          <th>Image</th>
        </tr>

        <tr ng-repeat="exercise in item.workout" ng-class="exercise.exercise_color">
              <td><a href="/exercise_detail/?data_id=[!exercise.exercise_id!]" target="_blank">[!exercise.name!]</a><br>[!exercise.notes!]</td>
              <td><pre>[!exercise.warmup_set!]</pre></td>
              <td><pre>[!exercise.set1!]</pre></td>
              <td><pre>[!exercise.set2!]</pre></td>
              <td><pre>[!exercise.set3!]</pre></td>
              <td ng-show="table_length>=4"><pre>[!exercise.set4!]</pre></td>
              <td ng-show="table_length>=5"><pre>[!exercise.set5!]</pre></td>
              <td><img ng-src="/render_img?exercise?thumb?[!exercise.exercise_id!]"></td>
        </tr><!-- .exercise_list -->
        </table>
        </div><!-- .outter_wrap -->

  </div><!-- .main_wrap -->
'''
#----------------------------------------------#
#             Client Publish Manage            #
#----------------------------------------------#
manage_client_page_html = '''
  <style type="text/css">
    .client_data{border: 1px solid grey; border-radius: 3px; text-align: left; padding: 10px; margin-top: 15px;}
    .img_wrap{width: 15%}
    .text_wrap{width: 75%;}
    .img_wrap, .text_wrap{display: inline-block; vertical-align: top;}
  </style>
  <div class="main_wrap">
    <a href='/publish/client'><button>Add A New Client</button></a>
    <hr>
    <div class="input-group">
      <span>Seach:</span>
      <input ng-model='select_client' type="text">
    </div>

    <div class="client_data" ng-repeat="item in client_data  | orderBy: 'client_email' | filter:select_client " >
      <div class="text_wrap">
        <p> Add Time:  [! item.add_time | limitTo: 10 !] </p>
        <p> Client Name:  [! item.client_name !] </p>  
        <p> Client Email:  [! item.client_email !] </p> 
        <p> Client Program:  [! item.client_program !] </p> 
        <p> Program Status:  [! item.program_status !] </p> 
        <p> Phone:  [! item.client_phone !] </p> 
        <p> Address:  [! item.client_address !] </p> 
        <p>stripe_cus_id: [! item.stripe_cus_id !]</p>
        <p>stripe_subscription_id: [! item.stripe_subscription_id !]</p>
      </div><!--.text_wrap-->

      <div class="img_wrap">
        <img ng-src="[! item.has_photo?'/render_img?client?thumb?'+item.client_email : '' !]">
      </div><!--.img_wrap-->

      <br>
      <a ng-href='/edit/client?[!item.client_email!]'><button ng-disabled="btn_disable">Edit Info</button></a>
      <a ng-href='/manage/workout?[!item.client_email!]'><button ng-disabled="btn_disable">Manage Workouts</button></a>
      <button ng-click="delete(item.client_email)" ng-disabled="btn_disable">Remove</button>
    </div><!--.client_data-->
  </div><!-- .main_wrap -->
'''
edit_client_page_html = '''
  <style>
  .form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px; padding: 45px; }
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  td img{max-width:70px;}
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap">
   <header class="hi"><span class="color_b">Edit Client [!item.client_email!]</span></header>
    <article class="form_wrap">
      <form action="../../manage/add_client" enctype="multipart/form-data" method="post">
        <table>
          <tr class="hide">
            <td class="label">Email</td>
            <td class="input"><input type="email" name="client_email" ng-model='item.client_email' required/></td>
          </tr>
          <tr>
            <td class="label">Name*</td>
            <td class="input"><input type="text" name="client_name" ng-model='item.client_name' required/></td>
          </tr>
          <tr>
            <td class="label">Client Program*</td>
            <td class="input">
              <select ng-model='item.client_program' name="client_program" required>
                <option ng-repeat="program in programs" value="[!program.name!]">[!program.name!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Program Status*</td>
            <td class="input">
              <select ng-model='item.program_status' name="program_status" required>
                <option ng-repeat="status in program_status_list" value="[!status!]">[!status!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Phone</td>
            <td class="input"><input type="text" name="client_phone" ng-model='item.client_phone'/></td>
          </tr>
          <tr>
            <td class="label">Address</td>
            <td class="input"><input type="text" name="client_address" ng-model='item.client_address'/></td>
          </tr>
          <tr>
            <td class="label">Photo</td>
            <td class="input"><input type="file" name="client_photo"/></td>
          </tr>
          <tr>
            <td class="label"><img ng-src="[! item.has_photo?'/render_img?client?thumb?'+item.client_email : '' !]"></td>
            <td class="input"></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/client"><button type="button">Cancel</button></a>
              <input type="submit" value="Save" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - .main_wrap - -->
'''
publish_client_page_html = '''  
  <style>
  .form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px; padding: 45px; }
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap">
    <header class="hi"><span class="color_b">Add New Client</span></header>
   <article class="form_wrap">
      <form action="../../manage/add_client" enctype="multipart/form-data" method="post">
        <table>
          <tr>
            <td class="label">Name*</td>
            <td class="input"><input type="text" name="client_name" ng-model='client_name' required/></td>
          </tr>
          <tr>
            <td class="label">Email*</td>
            <td class="input"><input type="email" name="client_email" ng-model='client_email' required/></td>
          </tr>
          <tr>
            <td class="label">Client Program*</td>
            <td class="input">
              <select name="client_program" required>
                <option ng-repeat="program in programs" value="[!program.name!]">[!program.name!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Program Status*</td>
            <td class="input">
              <select name="program_status" required>
                <option ng-repeat="status in program_status_list" value="[!status!]">[!status!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Phone</td>
            <td class="input"><input type="text" name="client_phone" ng-model='client_phone'/></td>
          </tr>
          <tr>
            <td class="label">Address</td>
            <td class="input"><input type="text" name="client_address" ng-model='client_address'/></td>
          </tr>
          <tr>
            <td class="label">Photo</td>
            <td class="input"><input type="file" name="client_photo"/></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/client"><button type="button">Cancel</button></a>
              <input type="submit" value="Save" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - .main_wrap - --> 
'''
#----------------------------------------------#
#             Waitlist Publish Manage          #
#----------------------------------------------#

manage_waitlist_page_html = '''
  <style type="text/css">
    .client_data{border: 1px solid grey; border-radius: 3px; text-align: left; padding: 10px; margin-top: 15px;}
  </style>
  <div class="main_wrap">
    <a href='/publish/waitlist'><button>Add A New Client to Waitlist</button></a>
    <hr>
    <div class="input-group">
      <span>Seach:</span>
      <input ng-model='select_client' type="text">
    </div>

    <div class="client_data" ng-repeat="item in waitlist_data | orderBy: 'add_time' | filter:select_client">
        <p> Add Time:  [! item.add_time | limitTo: 19 !] </p>
        <p> Client Name:  [! item.client_name !] </p>  
        <p> Client Email:  [! item.client_email !] </p> 
        <p> Client Program:  [! item.client_program !] </p> 
        <p> Client Phone:  [! item.client_phone !] </p> 
        <p> Client Address:  [! item.client_address !] </p> 
        <a ng-href='/edit/waitlist?[!item.client_email!]'><button>Edit Info</button></a>
        <button ng-click="delete(item.client_email)">Remove</button>
    </div><!--.exercise_data-->
  </div><!-- .main_wrap -->
'''
edit_waitlist_page_html = '''
  <style>
  .form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px; padding: 45px; }
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap">
    <header class="hi"><span class="color_b">Edit a Client in Waitlist</span></header>
   <article class="form_wrap">
      <form action="/manage/add_waitlist" method="post">
        <table>
          <tr>
            <td class="label">Name*</td>
            <td class="input"><input type="text" name="client_name" ng-model="item.client_name" required/></td>
          </tr>
          <tr>
            <td class="label">Program*</td>
            <td class="input">
              <select name="client_program" ng-model="item.client_program" required>
                <option ng-repeat="program in programs" value="[!program.name!]">[!program.name!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Email*</td>
            <td class="input"><input type="email" name="client_email" ng-model="item.client_email" required/></td>
          </tr>
          <tr>
            <td class="label">Client Phone</td>
            <td class="input"><input type="text" name="client_phone" ng-model="item.client_phone" /></td>
          </tr>
          <tr>
            <td class="label">Client Address</td>
            <td class="input"><input type="text" name="client_address" ng-model="item.client_address" /></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/waitlist"><button type="button">Cancel</button></a>
              <input type="submit" value="Save" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - .main_wrap - -->
''' 
publish_waitlist_page_html = '''
  <style>
  .form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px; padding: 45px; }
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap">
   <header class="hi"><span class="color_b">Add New Client to Waitlist</span></header>
   <article class="form_wrap">
      <form action="/manage/add_waitlist" method="post">
        <table>
          <tr>
            <td class="label">Name*</td>
            <td class="input"><input type="text" name="client_name" required/></td>
          </tr>
          <tr>
            <td class="label">Program*</td>
            <td class="input">
              <select name="client_program" required>
                <option ng-repeat="program in programs" value="[!program.name!]">[!program.name!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Email*</td>
            <td class="input"><input type="email" name="client_email" required/></td>
          </tr>
          <tr>
            <td class="label">Client Phone</td>
            <td class="input"><input type="text" name="client_phone" /></td>
          </tr>
          <tr>
            <td class="label">Client Address</td>
            <td class="input"><input type="text" name="client_address" /></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/waitlist"><button type="button">Cancel</button></a>
              <input type="submit" value="Save" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - .main_wrap - --> 
'''
#----------------------------------------------#
#            Client Workouts Manage             #
#----------------------------------------------#
mange_workout_page_html = '''
  <style type="text/css">
    .main_wrap a{text-decoration:underline;}
    .outter_wrap{width: 100%; overflow-x:scroll;}
    .workout_plan{width: 1200px; table-layout: fixed; }
    .workout_plan th{background:#37474F; color: #fff; padding: 5px; min-width: 100px;}
    .workout_plan td{padding: 5px; min-width: 100px;}
    .White, .LightBlue, .LightGreen, .LightGrey, .BlueGrey {border:1px solid grey; padding: 10px 10px; margin: 5px auto;}
    .White{background:#fff;}
    .LightBlue{background:#81D4FA;}
    .LightGreen{background:#B2DFDB;}
    .LightGrey{background:#E0E0E0;}
    .BlueGrey{background:#B0BEC5;}
  </style>
  <div class="main_wrap">
    <header class="hi color_b">Exercise Plan for [!client_id!]</header>
        <a ng-href='/edit/workout?[!client_id!]'><button>Edit Workouts</button></a>
        <button ng-click="del_workout(client_id)">Remove Workouts</button>

        <p>[!item.program_date!]&nbsp;&nbsp;[!item.muscles!]&nbsp;&nbsp;[!item.client_name!]</p>
        <p>[!item.general_explanation!]</p>


        <div class="outter_wrap">
        <table class="workout_plan">

        <tr>
          <th>Exercise</th>
          <th>2 Warm up sets</th>
          <th>Set 1</th>
          <th>Set 2</th>
          <th>Set 3</th>
          <th ng-show="table_length>=4">Set 4</th>
          <th ng-show="table_length>=5">Set 5</th>
          <th>Image</th>
        </tr>

        <tr ng-repeat="exercise in item.workout" ng-class="exercise.exercise_color">
              <td><a href="/exercise_detail/?data_id=[!exercise.exercise_id!]" target="_blank">[!exercise.name!]</a><br>[!exercise.notes!]</td>
              <td><pre>[!exercise.warmup_set!]</pre></td>
              <td><pre>[!exercise.set1!]</pre></td>
              <td><pre>[!exercise.set2!]</pre></td>
              <td><pre>[!exercise.set3!]</pre></td>
              <td ng-show="table_length>=4"><pre>[!exercise.set4!]</pre></td>
              <td ng-show="table_length>=5"><pre>[!exercise.set5!]</pre></td>
              <td><img ng-src="/render_img?exercise?thumb?[!exercise.exercise_id!]"></pre></td>
        </tr><!-- .exercise_list -->
        </table>
        </div><!-- .outter_wrap -->

  </div><!-- .main_wrap -->
'''
edit_workout_page_html = '''
  <style>
  .form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 600px; padding: 45px; }
  tr { height: 32px; overflow-x:auto;}
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  input[type="text"] { width: 200px; height: 16px; }
  .modal{ position: absolute; top: 0; z-index: 200;  padding: 25px; background: #fff; text-align: center;}
  .modal-backdrop{position: fixed; top: 0; left: 0; bottom: 0; right: 0;  z-index: 100;  background:rgba(0,0,0, 0.6);}
  .main_wrap a{text-decoration:underline;}
  .outter_wrap{width: 100%; overflow-x:scroll;}
  .workout_plan{width: 1200px; table-layout: fixed; }
  .workout_plan th{background:#37474F; color: #fff; padding: 5px; min-width: 100px;}
  .workout_plan td{padding: 5px; min-width: 100px;}
  .White, .LightBlue, .LightGreen, .LightGrey, .BlueGrey {border:1px solid grey; padding: 10px 10px; margin: 5px auto;}
  .White{background:#fff;}
  .LightBlue{background:#81D4FA;}
  .LightGreen{background:#B2DFDB;}
  .LightGrey{background:#E0E0E0;}
  .BlueGrey{background:#B0BEC5;}
  .btn_wrap{margin: 25px auto;}
  </style>

  <div class="main_wrap">
   <header class="hi"><span class="color_b">Edit Workouts for [!item.client_email!]</span></header>
    <article class="form_wrap">
        <table>
          <tr class="hide">
            <td class="label">Email</td>
            <td class="input"><input type="text" name="client_email" ng-model='item.client_email' required/></td>
          </tr>
          <tr>
            <td class="label">Date</td>
            <td class="input"><input type="text" name="program_date" ng-model='item.program_date' placeholder="e.g. March 7-14" required/></td>
          </tr>
          <tr>
            <td class="label">Client Name</td>
            <td class="input"><input type="text" name="client_name" ng-model='item.client_name' required/></td>
          </tr>
          <tr>
            <td class="label">Muscles</td>
            <td class="input"><input type="text" name="muscles" ng-model='item.muscles' placeholder="e.g. Quads/Calves" required/></td>
          </tr>
          <tr>
            <td class="label">General Explanation</td>
            <td class="input"><textarea rows="3" cols="30" name="general_explanation" ng-model='item.general_explanation' placeholder="e.g. Super Sets with 90 second- 2 min Rest Between"> </textarea></td>
          </tr>
        </table>

        <div class="outter_wrap">
          <table class="workout_plan">

          <tr>
            <th>Exercise</th>
            <th>2 Warm up sets</th>
            <th>Set 1</th>
            <th>Set 2</th>
            <th>Set 3</th>
            <th>Set 4</th>
            <th>Set 5</th>
            <th>Image</th>
            <th>Delete</th>
            <th>Edit</th>
          </tr>

          <tr ng-repeat="exercise in item.workout" ng-class="exercise.exercise_color">
                <td>
                  <a href="/exercise_detail/?data_id=[!exercise.exercise_id!]" target="_blank">[!exercise.name!]</a>
                  <br>[!exercise.notes!]
                </td>
                <td><pre>[!exercise.warmup_set!]</pre></td>
                <td><pre>[!exercise.set1!]</pre></td>
                <td><pre>[!exercise.set2!]</pre></td>
                <td><pre>[!exercise.set3!]</pre></td>
                <td><pre>[!exercise.set4!]</pre></td>
                <td><pre>[!exercise.set5!]</pre></td>
                <td><img ng-src="/render_img?exercise?thumb?[!exercise.exercise_id!]"></td>
                <td><button ng-click="del_workout($index)">X</button></td>
                <td><button ng-click="edit_workout($index)">Edit</button></td>
          </tr><!-- .exercise_list -->
          </table>
        </div><!-- .outter_wrap -->


        <div class="btn_wrap">
          <button type="button" ng-click="new_workout()">Add an Exercise</button>
        </div><!-- - .btn_wrap - -->

        <div class="btn_wrap">
          <a href="/manage/workout?[!item.client_email!]"><button type="button">Cancel</button></a>
          <button ng-click="save_workout_plan()">Save</button>
        </div><!-- - .btn_wrap - -->
    </article><!-- - /form_wrap - -->

    <div class="modal" ng-show="if_modal_show">
      <article class="form_wrap">
        <form  method="post" ng-submit="add_workout()">
         <table>
          <tr>
            <td class="label">Exercise Name</td>
            <td class="input">
              <select ng-model='tmp.exercise_id' name="exercise_name">
                <option ng-repeat="(key, value) in exercise_list" value="[!key!]">[!value!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Exercise Color</td>
            <td class="input">
              <select ng-model='tmp.exercise_color' name="exercise_color">
                <option ng-repeat="color in color_list" value="[!color!]">[!color!]</option>
              </select>
            </td>
          </tr>
          <tr>
            <td class="label">Notes</td>
            <td class="input"><textarea rows="3" cols="30" name="notes" ng-model='tmp.notes' placeholder="e.g. 2*SUPERSET (Weight in heel)"></textarea></td>
          </tr>
          <tr>
            <td class="label">Warm up set</td>
            <td class="input"><textarea rows="3" cols="30" name="warmup_set" ng-model='tmp.warmup_set'></textarea></td>
          </tr>
          <tr>
            <td class="label">Set 1</td>
            <td class="input"><textarea rows="3" cols="30" name="set1" ng-model='tmp.set1' ></textarea></td>
          </tr>
          <tr>
            <td class="label">Set 2</td>
            <td class="input"><textarea rows="3" cols="30" name="set2" ng-model='tmp.set2' ></textarea></td>
          </tr>
          <tr>
            <td class="label">Set 3</td>
            <td class="input"><textarea rows="3" cols="30" name="set3" ng-model='tmp.set3' ></textarea></td>
          </tr>
          <tr>
            <td class="label">Set 4</td>
            <td class="input"><textarea rows="3" cols="30" name="set4" ng-model='tmp.set4' ></textarea></td>
          </tr>
          <tr>
            <td class="label">Set 5</td>
            <td class="input"><textarea rows="3" cols="30" name="set5" ng-model='tmp.set5' ></textarea></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <button type="button" ng-click="if_modal_show=flase;">Cancel</button>
              <input type="submit" value="Add" />
            </td>
          </tr>
        </table>
        </form>
      </article><!-- - /form_wrap - -->
      <button type="button" ng-click="if_modal_show=flase;">Close</button>
    </div><!--.modal-->

    <div class="modal-backdrop" ng-show="if_modal_show"></div>

  </div><!-- - .main_wrap - -->
'''
#----------------------------------------------#
#             Code                             #
#----------------------------------------------#
import os
import urllib
import wsgiref.handlers
import webapp2
from webapp2_extras import routes
import json
import logging
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
#-
import stripe

#----------------------------------------------#
#           Contact    page                    #
#----------------------------------------------#
class submitQuestion(webapp2.RequestHandler):
  def post(self):
    client_name = self.request.get('client_name')
    client_email = self.request.get('client_email')
    client_address = self.request.get('client_address')
    client_question = self.request.get('client_question')
    submit_time = int(time.time())

    #--mail to host
    message = mail.EmailMessage(sender="Web Question <ShannyCohen.Fitness@gmail.com>", subject="Question Recieved #" + str(submit_time))   
    message.to = "ShannyCohen.Fitness@gmail.com"
    message.reply_to = str(client_email)
    message.body = "Name: " + str(client_name) + "\n\n Email: " + str(client_email) + "\n\n Address: " + str(client_address) + "\n\n Question: \n" + str(client_question)
    message.send()

    self.redirect('/contact_success')

#----------------------------------------------#
#      Workout Data Stucture                   #
#----------------------------------------------#
class Workout_db(ndb.Model):
    add_time = ndb.StringProperty()
    program_date = ndb.StringProperty()
    muscles = ndb.StringProperty()
    client_name = ndb.StringProperty()
    client_email = ndb.StringProperty()
    general_explanation = ndb.StringProperty()

    workout = ndb.JsonProperty()

    @classmethod
    def _get_one_data(self,data_id):
        item = Workout_db.get_by_id(data_id)
        if item:
          db_data = item.to_dict()
        else: 
          db_data = None
        return json.dumps(db_data)

    @classmethod
    def _get_current_workout(self):
        client_email = users.get_current_user().email()
        item = Workout_db.get_by_id(client_email)
        if item:
          db_data = item.to_dict()
        else: 
          db_data = None
        return json.dumps(db_data)

class addWorkout_db(webapp2.RequestHandler):
    def post(self):
      if users.is_current_user_admin():
        request_data = json.loads(self.request.body)
        data_id = request_data.get('client_email')

        if data_id and data_id != '':
          item = Workout_db.get_by_id(data_id)
           
        if not item:
          item = Workout_db(id=data_id)
          item.add_time = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y%m%d%H%M%S")
        # - -
        item.program_date = request_data.get('program_date')
        item.muscles = request_data.get('muscles')
        item.client_name = request_data.get('client_name')
        item.client_email = request_data.get('client_email')
        item.general_explanation = request_data.get('general_explanation')
        item.workout = request_data.get('workout')
        
        item.put()
        time.sleep(1)

#----------------------------------------------#
#      Client and Waitlist Data Stucture       #
#----------------------------------------------#
class Client_db(ndb.Model):
    add_time = ndb.StringProperty()
    #
    # client_id = ndb.StringProperty()
    client_name = ndb.StringProperty()
    client_program = ndb.StringProperty()
    program_status = ndb.StringProperty()
    stripe_cus_id = ndb.StringProperty()
    stripe_subscription_id = ndb.StringProperty()
    client_email = ndb.StringProperty()
    client_phone = ndb.StringProperty()
    client_address = ndb.TextProperty()
    has_photo = ndb.BooleanProperty()
    client_photo = ndb.BlobProperty()

    @classmethod
    def _get_all_data(self):
        q = Client_db.query()
        db_data = []
        for item in q.iter():
          db_data.append(item.to_dict(exclude=['client_photo']))
        return json.dumps(db_data)

    @classmethod
    def _get_one_data(self,data_id):
        item = Client_db.get_by_id(data_id)
        if item:
          db_data = item.to_dict(exclude=['client_photo'])
        else: 
          db_data = []
        return json.dumps(db_data)

    @classmethod
    def _in_this_db(self,client_id):
        q = Client_db.get_by_id(client_id)
        if q:
          return True
        else:
          return False

    @classmethod
    def _count_client(self):
        q1 = Client_db.query( ndb.AND(Client_db.client_program == 'Platinum',Client_db.program_status == 'Active') ).fetch(keys_only = True)
        q2 = Client_db.query( ndb.AND(Client_db.client_program == 'Gold',Client_db.program_status == 'Active') ).fetch(keys_only = True)
        q3 = Client_db.query( ndb.AND(Client_db.client_program == 'Silver',Client_db.program_status == 'Active') ).fetch(keys_only = True)
        q4 = Client_db.query( ndb.AND(Client_db.client_program == 'Bronze',Client_db.program_status == 'Active') ).fetch(keys_only = True)
        return json.dumps({'Platinum':len(q1),'Gold':len(q2), 'Silver':len(q3), 'Bronze':len(q4)})
        # return json.dumps([len(q1), len(q2), len(q3), len(q4)])

    @classmethod
    def _get_current_client(self):
        client_email = users.get_current_user().email()
        item = Client_db.get_by_id(client_email)
        if item:
          db_data = item.to_dict(exclude=['client_photo'])
        else: 
          db_data = []
        return json.dumps(db_data)

class addClient_db(webapp2.RequestHandler):
    def post(self):

      if users.is_current_user_admin():

        client_email = self.request.get('client_email')

        if client_email and client_email != '':
          item = Client_db.get_by_id(client_email)
          if not item:
            item = Client_db(id=client_email)
            item.add_time = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y/%m/%d %H:%M:%S")

        # - -
        item.client_name = self.request.get('client_name')
        item.client_email = self.request.get('client_email')
        item.client_program = self.request.get('client_program')
        item.program_status = self.request.get('program_status')
        item.stripe_cus_id = self.request.get('stripe_cus_id')
        item.stripe_subscription_id = self.request.get('stripe_subscription_id')
        item.client_program = self.request.get('client_program')
        item.client_phone = self.request.get('client_phone')
        item.client_address = self.request.get('client_address')
        
        client_photo = self.request.get('client_photo')
        if client_photo:
          item.client_photo = images.resize(client_photo, 800, 600)
          item.has_photo = True
        else:
          if not item.client_photo:
            item.has_photo = False
        #
        item.put()
        time.sleep(1)
        self.redirect('/manage/client')

class addClient_db_user(webapp2.RequestHandler):
    def post(self):
      client_email = self.request.get('client_email')
      item = Client_db.get_by_id(client_email)

      if not item:
        item = Client_db(id=client_email)
        item.client_email = self.request.get('client_email')
        item.add_time = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y/%m/%d %H:%M:%S")

      item.client_name = self.request.get('client_name')
      item.client_phone = self.request.get('client_phone')
      item.client_address = self.request.get('client_address')
      
      client_photo = self.request.get('client_photo')
      if client_photo:
        item.client_photo = images.resize(client_photo, 800, 600)
        item.has_photo = True
      else:
        if not item.client_photo:
          item.has_photo = False
      #
      item.put()
      self.redirect('/my_account/my_info')

class Waitlist_db(ndb.Model):
    add_time = ndb.StringProperty()
    #
    client_name = ndb.StringProperty()
    client_program = ndb.StringProperty()
    client_email = ndb.StringProperty()
    client_phone = ndb.StringProperty()
    client_address = ndb.TextProperty()

    @classmethod
    def _get_all_data(self):
        q = Waitlist_db.query()
        db_data = []
        for item in q.iter():
          db_data.append(item.to_dict())
        return json.dumps(db_data)

    @classmethod
    def _get_one_data(self,data_id):
      item = Waitlist_db.get_by_id(data_id)
      if item:
        db_data = item.to_dict()
      else: 
        db_data = []
      return json.dumps(db_data)

    @classmethod
    def _get_current_waitlist(self):
        client_email = users.get_current_user().email()
        item = Waitlist_db.get_by_id(client_email)
        if item:
          db_data = item.to_dict()
        else: 
          db_data = []
        return json.dumps(db_data)

class addWaitlist_db(webapp2.RequestHandler):
    def post(self):

      if users.get_current_user():

        client_email = self.request.get('client_email')
        if client_email:
          item = Waitlist_db.get_by_id(client_email)
          if not item:
            item = Waitlist_db(id=client_email)
            item.client_email = self.request.get('client_email')
            item.add_time = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y/%m/%d %H:%M:%S")

          item.client_program = self.request.get('client_program')
          item.client_name = self.request.get('client_name')
          item.client_phone = self.request.get('client_phone')
          item.client_address = self.request.get('client_address')
          item.put()
          time.sleep(1)

          if users.is_current_user_admin():
            self.redirect('/manage/waitlist')
          else:
            self.redirect('/my_program')

#----------------------------------------------#
#             Payment Records                  #
#----------------------------------------------#
class chargeCard(webapp2.RequestHandler):
  def post(self):

    #- stripe key and plan
    stripe.api_key = "xxxxx"

    # stripe.Plan.create(
    #   amount=55000,
    #   interval='month',
    #   name='Platinum',
    #   currency='usd',
    #   id='Platinum')

    # Get the credit card details submitted by the form
    token = self.request.POST['stripeToken']
    client_email = users.get_current_user().email()
    # data_id = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    if not Client_db._in_this_db(client_email):
      item = Client_db(id=client_email)
    else:
      item = Client_db.get_by_id(client_email)
 
    item.client_name = self.request.get('client_name')
    item.client_email = self.request.get('client_email')
    item.client_program = self.request.get('client_program')
    item.client_phone = self.request.get('client_phone')
    item.client_address = self.request.get('client_address')
    if not item.client_photo:
      item.has_photo = False
    item.add_time = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y/%m/%d %H:%M:%S")
    
    # - create stripe customer
    try:
      # coupon for silver and brozen customers
      # if item.client_program == 'Silver' or item.client_program == 'Bronze':
      #   client_count = json.loads(Client_db._count_client())
      #   if client_count["Silver"] + client_count["Bronze"] < silver_brozen_coupon_limit:
      #     customer = stripe.Customer.create(
      #     source=token,
      #     plan=item.client_program,
      #     email=item.client_email,
      #     coupon="50%OFF"
      #     )
      #   else:
      #     customer = stripe.Customer.create(
      #     source=token,
      #     plan=item.client_program,
      #     email=item.client_email
      #     )
      # else:
        customer = stripe.Customer.create(
        source=token,
        plan=item.client_program,
        email=item.client_email
        )
    except stripe.error.CardError, e:
        self.response.out.write(str(e)) 
    except stripe.error.RateLimitError, e:
        self.response.out.write(str(e)) 
    except stripe.error.InvalidRequestError, e:
        self.response.out.write(str(e)) 
    except stripe.error.AuthenticationError, e:
        self.response.out.write(str(e)) 
    except stripe.error.APIConnectionError, e:
        self.response.out.write(str(e)) 
    except stripe.error.StripeError, e:
        self.response.out.write(str(e)) 
    else:
      item.program_status = 'Active'
      item.stripe_cus_id = customer["id"]
      item.stripe_subscription_id = customer["subscriptions"]["data"][0]["id"]
      item.put()

      #--mail to client
      message = mail.EmailMessage(sender="Shanny Cohen Fitness <ShannyCohen.Fitness@gmail.com>", subject="Confirmation of Program Enrollment")    
      message.to = item.client_email
      message.reply_to = "ShannyCohen.Fitness@gmail.com"
      message.body = "Dear " + str(item.client_name) + ", \n\n You have enrolled in the following program: " + "\n " + str(item.client_program) + '\n\n Shanny Cohen Personal Training LLC.'
      message.send()

      self.redirect('/payment_success')

class cancelProgram(webapp2.RequestHandler):
  def get(self):

    #- stripe key 
    stripe.api_key = "xxxxx"

    if users.get_current_user():
      client_email = users.get_current_user().email()
      item = Client_db.get_by_id(client_email)
      
      try:
        customer = stripe.Customer.retrieve(item.stripe_cus_id)
        customer.subscriptions.retrieve(item.stripe_subscription_id).delete()
      except stripe.error.CardError, e:
        self.response.out.write(str(e)) 
      except stripe.error.RateLimitError, e:
        self.response.out.write(str(e)) 
      except stripe.error.InvalidRequestError, e:
        self.response.out.write(str(e)) 
      except stripe.error.AuthenticationError, e:
        self.response.out.write(str(e)) 
      except stripe.error.APIConnectionError, e:
        self.response.out.write(str(e)) 
      except stripe.error.StripeError, e:
        self.response.out.write(str(e)) 
      else:
        item.program_status = 'Canceled'
        item.put()
        self.redirect('/cancel_program_success')

def cancelProgram_admin(client_email):
    #- stripe key 
    stripe.api_key = "xxxxx"

    item = Client_db.get_by_id(client_email)
    if item.program_status == 'Active' and item.stripe_cus_id and item.stripe_subscription_id:
      try:
        customer = stripe.Customer.retrieve(item.stripe_cus_id)
        customer.subscriptions.retrieve(item.stripe_subscription_id).delete()
      except stripe.error.CardError, e:
        return str(e) 
      except stripe.error.RateLimitError, e:
        return str(e) 
      except stripe.error.InvalidRequestError, e:
        return str(e) 
      except stripe.error.AuthenticationError, e:
        return str(e) 
      except stripe.error.APIConnectionError, e:
        return str(e) 
      except stripe.error.StripeError, e:
        return str(e) 
      else:
        item.program_status = 'Canceled'
        item.put()
        return 'success'

class redirect2Payment(webapp2.RequestHandler):
  def get(self):
    program_chosen = self.request.get('program_chosen')
    url = "http://payment.shannycohen.fitness/?program_chosen=" + program_chosen
    self.redirect(str(url), True)

#----------------------------------------------#
#           Testimonial Data Stucture          #
#----------------------------------------------#
class Testimonial_db(ndb.Model):
    add_time = ndb.StringProperty()
    data_id = ndb.StringProperty()
    client_name = ndb.StringProperty()
    client_email = ndb.StringProperty()
    testimonial_text = ndb.TextProperty()
    testimonial_photo = ndb.BlobProperty()
    has_photo = ndb.BooleanProperty()

    @classmethod
    def _get_all_data(self):
        q = Testimonial_db.query()
        db_data = []
        for item in q.iter():
          db_data.append(item.to_dict(exclude=['testimonial_photo']))
        return json.dumps(db_data)

    @classmethod
    def _get_one_data(self,data_id):
        item = Testimonial_db.get_by_id(data_id)
        if item:
          db_data = item.to_dict(exclude=['testimonial_photo'])
        else: 
          db_data = []
        return json.dumps(db_data)

    @classmethod
    def _get_current_testimonial(self):
        client_email = users.get_current_user().email()
        q = Testimonial_db.query(Testimonial_db.client_email == client_email)
        db_data = []
        for item in q.iter():
          db_data.append(item.to_dict(exclude=['testimonial_photo']))
        return json.dumps(db_data)

class addTestimonial_db(webapp2.RequestHandler):
    def post(self):

      user = users.get_current_user()

      if user:

        data_id = self.request.get('data_id')
        if data_id and data_id != '':
          item = Testimonial_db.get_by_id(data_id)
        else:
          data_id = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y%m%d%H%M%S")
          item = Testimonial_db(id=data_id)
          item.data_id = data_id
          item.add_time = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y/%m/%d %H:%M:%S")
          item.client_email = user.email()

        item.client_name = self.request.get('client_name')
        item.testimonial_text= self.request.get('testimonial_text')

        testimonial_photo = self.request.get('testimonial_photo')
        if testimonial_photo:
          item.testimonial_photo = images.resize(testimonial_photo, 800, 600)
          item.has_photo = True
        else:
          if not item.testimonial_photo:
            item.has_photo = False

        item.put()
        time.sleep(1)

        if users.is_current_user_admin():
          self.redirect('/manage/testimonial')
        else:
          self.redirect('/my_account/my_testimonial')

#----------------------------------------------#
#           Exercise Data Stucture             #
#----------------------------------------------#
class Exercise_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
    #
    user_name = ndb.StringProperty()
    #
    exercise_id = ndb.StringProperty()
    exercise_name = ndb.StringProperty()
    equipment_type = ndb.StringProperty()
    # muscle_targeted = ndb.StringProperty(repeated=True)
    muscle_targeted = ndb.StringProperty()
    exercise_photo = ndb.BlobProperty()
    exercise_video_key = ndb.StringProperty()

    @classmethod
    def _get_all_data(self):
        q = ndb.gql('SELECT data_id, add_time, user_name, exercise_name, equipment_type, muscle_targeted, exercise_video_key FROM Exercise_db')
        db_data = []
        for item in q.iter():
          db_data.append({'data_id': item.data_id, 'add_time': str(item.add_time), 'user_name': item.user_name, 'exercise_name': item.exercise_name, 'equipment_type': item.equipment_type, 'muscle_targeted': item.muscle_targeted, 'exercise_video_key': item.exercise_video_key})
        return json.dumps(db_data)

    @classmethod
    def _get_one_data(self,data_id):
        # item = Exercise_db.get_by_id(data_id)
        q =ndb.gql('SELECT exercise_name, equipment_type, muscle_targeted, exercise_video_key from Exercise_db WHERE data_id= :1', data_id)
        for item in q:
          db_data = {'data_id': data_id, 'exercise_name': item.exercise_name, 'equipment_type': item.equipment_type, 'muscle_targeted': item.muscle_targeted, 'exercise_video_key': item.exercise_video_key}
        return json.dumps(db_data)

    @classmethod
    def _get_all_names(self):
        q =ndb.gql('SELECT data_id, exercise_name from Exercise_db')
        db_data = {}
        for item in q.iter():
          db_data[item.data_id] = item.exercise_name
        return json.dumps(db_data)

class addExercise_db(webapp2.RequestHandler):
    def post(self):

      if users.is_current_user_admin():
        data_id = self.request.get('data_id')
        if data_id and data_id != '':
          item = Exercise_db.get_by_id(data_id)
        else:
          data_id = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y%m%d%H%M%S")
          item = Exercise_db(id=data_id)
          item.data_id = data_id
        # - -
        item.user_name = users.get_current_user().nickname()
        item.exercise_id = self.request.get('exercise_id')
        item.exercise_name = self.request.get('exercise_name')
        item.equipment_type = self.request.get('equipment_type')
        muscle_targeted = self.request.POST.getall('muscle_targeted')
        item.muscle_targeted = ', '.join(muscle_targeted)
        
        exercise_photo = self.request.get('exercise_photo')
        if exercise_photo:
          item.exercise_photo = images.resize(exercise_photo, 800, 600)
        #
        item.put()
        time.sleep(1)
        self.redirect('/manage/exercise')

#----------------------------------------------#
#          List and Delete Data                #
#----------------------------------------------#
class deleteData(webapp2.RequestHandler):
    def get(self):
      if users.is_current_user_admin():
        page_address = self.request.uri
        base = os.path.basename(page_address)
        split_address = base.split('?')
        data_set = split_address[1]
        data_id = split_address[2]
    
        if data_set == "exercise":
          item = Exercise_db.get_by_id(data_id)
          if item.exercise_video_key and len(item.exercise_video_key) > 0:
            blobkey = blobstore.blobstore.BlobKey(item.exercise_video_key)
            blobstore.delete(blobkey)

          item.key.delete()
          time.sleep(1)
          self.redirect('/list_data?exercise')

        if data_set == "payment":
          item = Payment_db.get_by_id(data_id)
          item.key.delete()
          time.sleep(1)
          self.redirect('/list_data?payment')

        if data_set == "client":
          item = Client_db.get_by_id(data_id)
          # delete workout plan for this client
          workout_item = Workout_db.get_by_id(data_id)
          if workout_item:
            workout_item.key.delete()
            time.sleep(1)

          stripe_remove_msg = 'success'
          if item.program_status == 'Active' and item.stripe_cus_id and item.stripe_subscription_id:
            stripe_remove_msg = cancelProgram_admin(data_id)
          if stripe_remove_msg == 'success':
            item.key.delete()
            time.sleep(1)
            self.redirect('/list_data?client')
          else:
            self.response.out.write("Error! " + stripe_remove_msg) 

        if data_set == "waitlist":
          item = Waitlist_db.get_by_id(data_id)
          item.key.delete()
          time.sleep(1)
          self.redirect('/list_data?waitlist')

        if data_set == "testimonial":
          item = Testimonial_db.get_by_id(data_id)
          item.key.delete()
          time.sleep(1)
          self.redirect('/list_data?testimonial')

        if data_set == "workout":
          item = Workout_db.get_by_id(data_id)
          if item:
            item.key.delete()
            time.sleep(1)
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(json.dumps({})) 

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

        if data_set == 'exercise_names' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Exercise_db._get_all_names()) 

        if data_set == 'exercise' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Exercise_db._get_one_data(data_id)) 

        if data_set == 'client' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Client_db._get_all_data()) 

        if data_set == 'client' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Client_db._get_one_data(data_id)) 

        if data_set == 'client_number' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Client_db._count_client()) 

        if data_set == 'current_client' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Client_db._get_current_client()) 

        if data_set == 'waitlist' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Waitlist_db._get_all_data()) 

        if data_set == 'waitlist' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Waitlist_db._get_one_data(data_id)) 

        if data_set == 'current_waitlist' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Waitlist_db._get_current_waitlist()) 

        if data_set == 'testimonial' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Testimonial_db._get_all_data()) 

        if data_set == 'testimonial' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Testimonial_db._get_one_data(data_id)) 

        if data_set == 'current_testimonial' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Testimonial_db._get_current_testimonial()) 

        if data_set == 'workout' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Workout_db._get_one_data(data_id)) 

        if data_set == 'current_workout' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Workout_db._get_current_workout()) 

#----------------------------------------------#
#             Multi-Media Rendering            #
#----------------------------------------------#
class RenderImg(webapp2.RequestHandler):
    def get(self):
        page_address = self.request.uri
        base = os.path.basename(page_address)
        data_set = base.split('?')[1]
        img_size = base.split('?')[2]
        data_id = base.split('?')[3]

        if data_set == 'exercise':
          item = Exercise_db.get_by_id(data_id)
          img = images.Image(item.exercise_photo)

        if data_set == 'client':
          item = Client_db.get_by_id(data_id)
          img = images.Image(item.client_photo)

        if data_set == 'testimonial':
          item = Testimonial_db.get_by_id(data_id)
          img = images.Image(item.testimonial_photo)

        if img_size == 'thumb':
            img.resize(width=100)
        if img_size == 'small':
            img.resize(width=200)
        if img_size == 'medium':
            img.resize(width=350)
        if img_size == 'large':
            img.resize(width=800)
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

#----------------------------------------------#
#             HTML Page Production             #
#----------------------------------------------#
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
          user_name = user.email()
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
        program_chosen = ''
        data_id = ''

        if users.is_current_user_admin():
            admin = 'true' 

        if path_layer == 'exercises':
            page_id = 'exercises'
            page_name = 'Exercises'
            page_html = page_header + exercises_page_html

        if path_layer == 'exercise_detail':
            page_id = 'exercise_detail'
            page_name = 'Exercises'
            page_html = page_header + exercise_detail_page_html
            data_id = self.request.get("data_id")

        if path_layer == 'about':
            page_id = 'about'
            page_name = 'About'
            page_html = page_header + about_page_html

        if path_layer == 'results':
            page_id = 'results'
            page_name = 'Results'
            page_html = page_header + results_page_html

        if path_layer == 'programs':
            page_id = 'programs'
            page_name = 'Programs'
            page_html = page_header + programs_page_html

        if path_layer == 'confirm_signup':
            page_id = 'confirm_signup'
            page_name = 'Confirm Signup'
            page_html = page_header + confirm_signup_page_html
            program_chosen = self.request.get('program_chosen')

        if path_layer == 'payment_success':
            page_id = 'payment_success'
            page_name = 'Payment Success'
            page_html = page_header + payment_success_page_html

        if path_layer == 'cancel_program_success':
            page_id = 'cancel_program_success'
            page_name = 'Cancel Program Success'
            page_html = page_header + cancel_program_success_page_html

        if path_layer == 'contact':
            page_id = 'contact'
            page_name = 'Contact'
            page_html = page_header + contact_page_html

        if path_layer == 'contact_success':
            page_id = 'contact_success'
            page_name = 'Contact Success'
            page_html = page_header + contact_success_page_html

        # - manage, edit, publish pages for public 
        if path_layer == 'manage' or path_layer == 'edit' or path_layer == 'publish':
            page_id = 'login_page'
            page_name = 'Log in'
            nav_html = admin_nav_html
            page_html = manage_page_html
            page_class = 'manage'

        # - some other pages for public 
        if path_layer == 'payment' or path_layer == 'add2waitlist' or path_layer == 'my_account' :
          page_id = 'login_page'
          page_name = 'Log in'
          page_html = page_header + login_page_html

        if user:
          if path_layer == 'payment':
              page_id = 'payment'
              page_name = 'Payment'
              page_html = page_header + payment_page_html
              program_chosen = self.request.get('program_chosen')

          if path_layer == 'add2waitlist':
              page_id = 'add2waitlist'
              page_name = 'Add to Waitlist'
              page_html = page_header + add2waitlist_page_html
              program_chosen = self.request.get('program_chosen')

          if path_layer == 'my_account':
            print "layer"
            print base
            if base == 'my_account' or base == '':
              page_id = 'my_account'
              page_name = 'My Account'
              page_html = page_header + my_account_page_html

            if base == 'my_program':
                page_id = 'my_program'
                page_name = 'My Program'
                page_html = page_header + my_program_page_html

            if base == 'my_info':
                page_id = 'my_info'
                page_name = 'My Info'
                page_html = page_header + my_info_page_html

            if base == 'edit_my_info':
                page_id = 'edit_my_info'
                page_name = 'Edit My Info'
                page_html = page_header + edit_my_info_page_html

            if base == 'my_testimonial':
                page_id = 'my_testimonial'
                page_name = 'My Testimonial'
                page_html = page_header + my_testimonial_page_html

            if base == 'my_workout':
                page_id = 'my_workout'
                page_name = 'My Workout'
                page_html = page_header + my_workout_page_html

            if base == 'publish_my_testimonial':
                page_id = 'publish_my_testimonial'
                page_name = 'Publish My Testimonial'
                page_html = page_header + publish_my_testimonial_page_html

            if base.startswith('edit_my_testimonial'):
                page_id = 'edit_my_testimonial'
                page_name = 'Edit My Testimonial'
                page_html = page_header + edit_my_testimonial_page_html
                data_id = base.split('?')[1]

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

              if base == 'client':
                page_id = 'manage_client'
                page_name = 'Manage Client'
                nav_html = admin_nav_html
                page_html = manage_client_page_html

              if base == 'waitlist':
                page_id = 'manage_waitlist'
                page_name = 'Manage Waitlist'
                nav_html = admin_nav_html
                page_html = manage_waitlist_page_html

              if base == 'testimonial':
                page_id = 'manage_testimonial'
                page_name = 'Manage Testimonial'
                nav_html = admin_nav_html
                page_html = manage_testimonial_page_html

              if base.startswith('workout'):
                page_id = 'mange_workout'
                page_name = 'Mange Workout'
                nav_html = admin_nav_html
                page_html = mange_workout_page_html
                data_id = base.split('?')[1]

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

              if base.startswith('client'):
                page_id = 'edit_client'
                page_name = 'Edit Client'
                nav_html = admin_nav_html
                page_html = edit_client_page_html
                data_id = base.split('?')[1]

              if base.startswith('waitlist'):
                page_id = 'edit_waitlist'
                page_name = 'Edit Waitlist'
                nav_html = admin_nav_html
                page_html = edit_waitlist_page_html
                data_id = base.split('?')[1]

              if base.startswith('testimonial'):
                page_id = 'edit_testimonial'
                page_name = 'Edit Testimonial'
                nav_html = admin_nav_html
                page_html = edit_testimonial_page_html
                data_id = base.split('?')[1]

              if base.startswith('workout'):
                page_id = 'edit_workout'
                page_name = 'Edit Workout'
                nav_html = admin_nav_html
                page_html = edit_workout_page_html
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

              if base == 'client':
                page_id = 'publish_client'
                page_name = 'Publish Client'
                nav_html = admin_nav_html
                page_html = publish_client_page_html

              if base == 'waitlist':
                page_id = 'publish_waitlist'
                page_name = 'Publish Waitlist'
                nav_html = admin_nav_html
                page_html = publish_waitlist_page_html

              if base == 'testimonial':
                page_id = 'publish_testimonial'
                page_name = 'Publish Testimonial'
                nav_html = admin_nav_html
                page_html = publish_testimonial_page_html

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
            'program_chosen': program_chosen,     
        }
      # - render
        path = os.path.join(os.path.dirname(__file__), 'html/publicSite.html')
        self.response.out.write(template.render(path, objects))

#----------------------------------------------#
#            Error Handling                    #
#----------------------------------------------#
def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('A 404 error occurred!')
    response.set_status(404)

def handle_500(request, response, exception):
    logging.exception(exception)
    response.write('A 500 error occurred!')
    response.set_status(500)
#----------------------------------------------#
#                                              #
#----------------------------------------------#
app = webapp2.WSGIApplication([    # - Pages

    ('/', publicSite),
    
    ('/programs/?', publicSite),
      ('/confirm_signup/?', publicSite),
      ('/redirect2payment/?', redirect2Payment),
      ('/payment/?', publicSite),
      ('/charge_card/?', chargeCard),
      ('/payment_success', publicSite),
      ('/cancel_program/?', cancelProgram),
      ('/cancel_program_success/?', publicSite),

      ('/add2waitlist/?', publicSite),

    ('/my_account/?', publicSite),
    ('/my_account/my_program/?', publicSite),
    ('/my_account/my_info/?', publicSite),
    ('/my_account/my_testimonial/?', publicSite),
    ('/my_account/my_workout/?', publicSite),
    ('/my_account/edit_my_info/?', publicSite),
    ('/my_account/add_my_info/?', addClient_db_user),
    ('/my_account/publish_my_testimonial/?', publicSite),
    ('/my_account/edit_my_testimonial/?', publicSite),

    ('/results/?', publicSite),
    ('/exercises/?', publicSite),
    ('/exercise_detail/?', publicSite),
    ('/about/?', publicSite),

    ('/contact/?', publicSite),
    ('/submit_question/?', submitQuestion),
    ('/contact_success/?', publicSite),

    ('/manage/?', publicSite),
    ('/manage/exercise/?', publicSite),
    ('/manage/client/?', publicSite),
    ('/manage/waitlist/?', publicSite),
    ('/manage/testimonial/?', publicSite),
    ('/manage/workout/?', publicSite),

    ('/edit/?', publicSite),
    ('/edit/exercise/?', publicSite),
    ('/edit/client/?', publicSite),
    ('/edit/waitlist/?', publicSite),
    ('/edit/testimonial/?', publicSite),
    ('/edit/workout/?', publicSite),

    ('/publish/exercise/?', publicSite),
    ('/publish/exercise_video?', publicSite),
    ('/publish/client/?', publicSite),
    ('/publish/waitlist/?', publicSite),
    ('/publish/testimonial/?', publicSite),

    ('/manage/add_exercise/?', addExercise_db),
    ('/upload_exercise_video/?', UploadExerciseVideo),
    ('/manage/add_client/?', addClient_db),
    ('/manage/add_waitlist/?', addWaitlist_db),
    ('/manage/add_testimonial/?', addTestimonial_db),
    ('/manage/add_workout/?', addWorkout_db),

    # ('/manage/add_client/?', addClient_db),
    ('/list_data/?', listData),
    ('/delete_data/?', deleteData),
    ('/render_img/?', RenderImg),
    ('/view_video/([^/]+)?', ViewVideo),

], debug=True)
# app.error_handlers[404] = handle_404
# app.error_handlers[500] = handle_500
