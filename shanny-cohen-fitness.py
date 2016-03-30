#!/usr/bin/python
# coding: latin-1

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
  header { width: 100%; }
  .sub_title { border-top: 1px solid #eee; }
  .top_wrap { position: absolute; top: 0; left: 0; right: 0; height: 70px; }
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
    </ul>
    <div class="social_wrap">
      <a href="https://www.instagram.com/shannycohen_fitness/" target="_blank"><i class="fa fa-instagram"></i></a>
      <a href="" target="_blank"><i class="fa fa-twitter-square"></i></a>
      <a href="https://www.facebook.com/ShannyCohenAthletePage/timeline" target="_blank"><i class="fa fa-facebook-official"></i></a>
    </div><!-- . social_wrap - -->
    </nav><!-- - /main_nav - -->
'''
results_page_html = '''
  <div class="main_wrap">
  Results Page
    <img src="../../pics/results.jpg" />

  </div><!-- . main_wrap - -->
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
    <p>Sign in with your Google account</p>
  </div><!-- .main_wrap -->
'''
admin_nav_html = '''
  <nav class="main_nav"><ul>
    <a href="../../"><li id="programsNav">&#8672; Public</li></a>
    <a href="../../manage/client"><li id="clientNav">Client</li></a>
    <a href="../../manage/wishlist"><li id="wishlistNav">Wishlist</li></a>
    <a href="../../manage/exercise"><li id="exerciseNav">Exercise</li></a>
  </ul></nav><!-- - /main_nav - -->
'''
manage_page_html = '''
  <div class="main_wrap">
    <p>Choose a data set from the right to edit</p>
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
        <input type="checkbox" name="muscle_targeted" value="[!muscle.name!]" ng-model="muscle.selected" ng-click="toggle_selection(muscle.name)" class="hide"> [!muscle.name!]<br>        
      </label>        
      <label>
        <input type="checkbox" name="select_all" value="select_all" ng-model="select_all" ng-click="select_all_exercises()" class="hide"> All Exercises<br>        
      </label>       
    </div><!--.initial_category_wrap-->

   <div class="hide" id="exercise_wrap">

      <div class="select_category_wrap">
        <label>
          <input type="checkbox" name="select_all" value="all" ng-click="select_all_exercises()" class="hide"> Select All<br>        
        </label> 
        <label>
          <input type="checkbox" name="deselect_all" value="deselect_all"  ng-model="deselect_all"  ng-click="deselect_all_exercises()" class="hide"> Deselect All<br>        
        </label> 
        <hr>  
        <label ng-repeat="muscle in muscles">
          <input type="checkbox" name="muscle_targeted" value="[!muscle.name!]" ng-model="muscle.selected" ng-click="toggle_selection(muscle.name)"> [!muscle.name!]<br>   
        </label>            
      </div><!--.select_category_wrap-->

      <div class="select_data_wrap">
       <p>Find [!display_data.length!] exercise(s)</p>
       <hr>
        <div class="exercise_data" ng-repeat="item in display_data">
          <a ng-href="/exercise_detail/?data_id=[!item.data_id!]">
          <div class="img_wrap">
            <img ng-src="/render_img?exercise?medium?[!item.data_id!]">
          </div><!--.img_wrap-->

          <div class="text_wrap">
            <p> Exercise Name:<br>[! item.exercise_name !] </p>  
            <p> Equipment Type:<br>  [! item.equipment_type !] </p> 
            <p> Muscle Targeted:<br>  [! item.muscle_targeted !] </p> 
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
    .img_wrap{width: 100%; max-height: 400px; margin: 25 auto;}
  </style>
  <div class="main_wrap">
    <div class="video_wrap" >
      <video ng-show='item.exercise_video_key' width="300" height="200" ng-src="[!video_url!]" controls></video>
    </div><!--.video_wrap-->

    <div class="text_wrap">
      <p> Exercise Name: [! item.exercise_name !] </p>  
      <p> Equipment Type:  [! item.equipment_type !] </p> 
      <p> Muscle Targeted:  [! item.muscle_targeted !] </p> 
    </div><!--.text_wrap-->
    <hr>

    <div class="img_wrap">
      <h3>[!item.exercise_name!] Images</h3>
      <img ng-src="/render_img?exercise?medium?[!item.data_id!]">
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
    <div class="exercise_data" ng-repeat="item in exercise_data">
      <div class="text_wrap">
        <p> Add Time:  [! item.add_time | limitTo: 19 !] </p>
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
            <td class="label">Name</td>
            <td class="input"><input type="text" name="exercise_name" required/></td>
          </tr>
          <tr>
            <td class="label">Equipment Type</td>
            <td class="input"><input type="text" name="equipment_type" /></td>
          </tr>
          <tr>
            <td class="label">Muscle Targeted</td>
            <td class="input">
              <label ng-repeat="muscle in muscles">
                <input type="checkbox" name="muscle_targeted" value="[!muscle.name!]"> [!muscle.name!]
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
            <td class="label">Name</td>
            <td class="input"><input type="text" name="exercise_name" ng-model='exercise_name' required/></td>
          </tr>
          <tr>
            <td class="label">Equipment Type</td>
            <td class="input"><input type="text" name="equipment_type" ng-model='equipment_type' /></td>
          </tr>
          <tr>
            <td class="label">Muscle Targeted</td>
            <td class="input">
              <label ng-repeat="muscle in muscles">
                <input type="checkbox" name="muscle_targeted" value="[!muscle.name!]" ng-model="muscle.selected"> [!muscle.name!]<br>
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
  .sign_up_text {color: red; }
  .sign_up_btn {border:none; border-radius: 0; padding: 5px; font-size: 0.9rem;}
  </style>

  
  <div class="main_wrap">
  <h2 class="programs_title">Programs</h2>
  <h3 class="programs_title" style='color:red'>Test Mode, Not use this page to Sign up now</h3>
  <h3 class="programs_title" style='color:red'>Instead, please email shannycohen_fitness@gmail.com</h3>
  <!--
  <ul>
    <li>Strength and Conditioning</li>
    <li>Weight Loss</li>
    <li>Sport Specific Training</li>
    <li>Post-Injury Exercise Rehab</li>
    <li>Orthopedic Condition Specific Training</li>
  </ul>
  -->

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
        <div ng-show='platinum_avail'>
          <h4 class="sign_up_text">* Limited Spots Available</h4>
          <button class="sign_up_btn" ng-click=" confirm_signup('Platinum') ">Sign Up</button>
        </div>
        <div ng-show='!platinum_avail'>
          <h4 class="sign_up_text">* Add to Wishlist</h4>
          <button class="sign_up_btn" ng-click=" add2wishlist('Platinum') ">Add to Wishlist</button>
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
        <div ng-show='gold_avail'>
          <h4 class="sign_up_text">* Limited Spots Available</h4>
          <button class="sign_up_btn" ng-click=" confirm_signup('Gold') ">Sign Up</button>
        </div>
        <div ng-show='!gold_avail'>
          <h4 class="sign_up_text">* Add to Wishlist</h4>
          <button class="sign_up_btn" ng-click=" add2wishlist('Gold') ">Add to Wishlist</button>
        </div>
      </div><!-- . package_wrap - -->
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
add2wishlist_page_html = '''
  <style>
  .confirm_signup_btn{display: inline-block; border-radius: 0; border: none; padding: 5px;}
  </style>
  <div class="main_wrap">
    <p>You will be added to the Wishlist for [!program_chosen!] Program ($[!price!]/month).</p>
    <article class="form_wrap">
      <form action="/add_wishlist" method="post">
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
  .warning,.payment-errors{color:red;}
  </style>
  <div class="main_wrap">
    <h3>[!program_chosen!] Program</h3>
    <h3>Price: $[!price!]/month</h3>
    <p class="warning" ng-show="program_status=='Active'">You have already enrolled in a program.</p>
  <article class="form_wrap">
    <form action="/charge_card/" id="payment-form" method="post">
      <span class="payment-errors"></span>
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
  </article><!-- - /form_wrap - -->
  <p>*Secure Checkout Powered by Stripe</p>
  </div><!-- .main_wrap -->
'''
payment_success_page_html = '''
  <div class="main_wrap">
  <h2>Thank you for your payment.</h2>
  <h2>You will recieve an email reciept.</h2>
  </div><!-- .main_wrap -->
'''
my_program_page_html = '''
  <div class="main_wrap">
    <div>
      <p>Program: [!client_program!]</p> 
        <p ng-show='client_program'>Since: [!program_add_time | limitTo: 19!]</p> 
        <p ng-show='program_status'>Program Status: [!program_status !]</p> 
        <a ng-show="program_status!='Canceled'&&client_program&&stripe_cus_id&&stripe_subscription_id" ng-click="cancel_program()"><button>Cancenl Program</button></a>
        <p ng-show='comment'> [!comment!]</p> 
    </div>
    <hr>
    <div>
      <p>Wishlist: [!client_wishlist!]</p>
        <p ng-show='client_wishlist'>Since: [!wishlist_add_time | limitTo: 19!]</p> 
    </div>
  </div><!-- .main_wrap -->
'''
cancel_program_success_page_html = '''
  <div class="main_wrap">
  <h2>Your have quit the program.</h2>
  </div><!-- .main_wrap -->
'''
#----------------------------------------------#
#             Client Publish Manage            #
#----------------------------------------------#

manage_client_page_html = '''
  <style type="text/css">
    .client_data{border: 1px solid grey; border-radius: 3px; text-align: left; padding: 10px; margin-top: 15px;}
    .img_wrap{width: 40%}
    .text_wrap{width: 50%;}
    .img_wrap, .text_wrap{display: inline-block; vertical-align: top;}
  </style>
  <div class="main_wrap">
    <a href='/publish/client'><button>Add A New Client</button></a>
    <hr>
    <div class="client_data" ng-repeat="item in client_data" | orderBy: 'client_email'>
        <p> Add Time:  [! item.add_time | limitTo: 19 !] </p>
        <p> Client Name:  [! item.client_name !] </p>  
        <p> Client Email:  [! item.client_email !] </p> 
        <p> Client Program:  [! item.client_program !] </p> 
        <p> Program Status:  [! item.program_status !] </p> 
        <p> Phone:  [! item.client_phone !] </p> 
        <p> Address:  [! item.client_address !] </p> 
        <p>stripe_cus_id: [! item.stripe_cus_id !]</p>
        <p>stripe_subscription_id: [! item.stripe_subscription_id !]</p>
        <a ng-href='/edit/client?[!item.client_email!]'><button>Edit Info</button></a>
        <button ng-click="delete(item.client_email)">Remove</button>
    </div><!--.exercise_data-->
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
            <td class="input"><input type="text" name="client_email" ng-model='item.client_email' required/></td>
          </tr>
          <tr>
            <td class="label">Name</td>
            <td class="input"><input type="text" name="client_name" ng-model='item.client_name' required/></td>
          </tr>
          <tr>
            <td class="label">Client Program</td>
            <td class="input"><input type="text" name="client_program" ng-model='item.client_program' placeholder='Platinum or Gold or Silver or Bronze'/></td>
          </tr>
          <tr>
            <td class="label">Program Status</td>
            <td class="input"><input type="text" name="program_status" ng-model='item.program_status' placeholder='Active or Canceled'/></td>
          </tr>
          <tr>
            <td class="label">Stripe_cus_id</td>
            <td class="input"><input type="text" name="stripe_cus_id" ng-model='item.stripe_cus_id'/></td>
          </tr>
          <tr>
            <td class="label">stripe_subscription_id</td>
            <td class="input"><input type="text" name="stripe_subscription_id" ng-model='item.stripe_subscription_id' /></td>
          </tr>
          <tr>
            <td class="label">Phone</td>
            <td class="input"><input type="text" name="client_phone" ng-model='item.client_phone'/></td>
          </tr>
          <tr>
            <td class="label">Addess</td>
            <td class="input"><input type="text" name="client_address" ng-model='item.client_address'/></td>
          </tr>
          <tr>
            <td class="label">Photo</td>
            <td class="input"><img ng-src="/render_img?client?thumb?[!data_id!]"></td>
          </tr>
          <tr>
            <td class="label"></td>
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
            <td class="label">Name</td>
            <td class="input"><input type="text" name="client_name" ng-model='client_name' required/></td>
          </tr>
          <tr>
            <td class="label">Email</td>
            <td class="input"><input type="text" name="client_email" ng-model='client_email' required/></td>
          </tr>
          <tr>
            <td class="label">Client Program</td>
            <td class="input"><input type="text" name="client_program" ng-model='client_program' placeholder='Platinum or Gold or Silver or Bronze'/></td>
          </tr>
          <tr>
            <td class="label">Program Status</td>
            <td class="input"><input type="text" name="program_status" ng-model='program_status' placeholder='Active or Canceled'/></td>
          </tr>
          <tr>
            <td class="label">Stripe_cus_id</td>
            <td class="input"><input type="text" name="stripe_cus_id" ng-model='stripe_cus_id'/></td>
          </tr>
          <tr>
            <td class="label">stripe_subscription_id</td>
            <td class="input"><input type="text" name="stripe_subscription_id" ng-model='stripe_subscription_id' /></td>
          </tr>
          <tr>
            <td class="label">Phone</td>
            <td class="input"><input type="text" name="client_phone" ng-model='client_phone'/></td>
          </tr>
          <tr>
            <td class="label">Addess</td>
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
#             Wishlist Publish Manage          #
#----------------------------------------------#

manage_wishlist_page_html = '''
  <style type="text/css">
    .client_data{border: 1px solid grey; border-radius: 3px; text-align: left; padding: 10px; margin-top: 15px;}
    .img_wrap{width: 40%}
    .text_wrap{width: 50%;}
    .img_wrap, .text_wrap{display: inline-block; vertical-align: top;}
  </style>
  <div class="main_wrap">
    <a href='/publish/wishlist'><button>Add A New Client to Wishlist</button></a>
    <hr>
    <div class="client_data" ng-repeat="item in wishlist_data" | orderBy: 'client_id'>
        <p> Add Time:  [! item.add_time | limitTo: 19 !] </p>
        <p> Client Name:  [! item.client_name !] </p>  
        <p> Client Email:  [! item.client_email !] </p> 
        <p> Client Program:  [! item.client_program !] </p> 
        <a ng-href='/edit/wishlist?[!item.client_email!]'><button>Edit Info</button></a>
        <button ng-click="delete(item.client_email)">Remove</button>
    </div><!--.exercise_data-->
  </div><!-- .main_wrap -->
'''
edit_wishlist_page_html = '''
  <style>
  .form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px; padding: 45px; }
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  td img{max-width:70px;}
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap">
    <header class="hi"><span class="color_b">Edit a Client in Wishlist</span></header>
   <article class="form_wrap">
      <form action="/add_wishlist" method="post">
        <table>
          <tr>
            <td class="label">Name</td>
            <td class="input"><input type="text" name="client_name" ng-model="item.client_name" required/></td>
          </tr>
          <tr>
            <td class="label">Program</td>
            <td class="input"><input type="text" name="client_program" ng-model="item.client_program" required/></td>
          </tr>
          <tr>
            <td class="label">Email</td>
            <td class="input"><input type="text" name="client_email" ng-model="item.client_email" required/></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/wishlist"><button type="button">Cancel</button></a>
              <input type="submit" value="Save" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- - .main_wrap - -->
'''
publish_wishlist_page_html = '''
  <style>
  .form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px; padding: 45px; }
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  input[type="text"] { width: 200px; height: 16px; }
  </style>
  <div class="main_wrap">
   <header class="hi"><span class="color_b">Add New Client to Wishlist</span></header>
   <article class="form_wrap">
      <form action="/add_wishlist" method="post">
        <table>
          <tr>
            <td class="label">Name</td>
            <td class="input"><input type="text" name="client_name" required/></td>
          </tr>
          <tr>
            <td class="label">Program</td>
            <td class="input"><input type="text" name="client_program" required/></td>
          </tr>
          <tr>
            <td class="label">Email</td>
            <td class="input"><input type="text" name="client_email" required/></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/wishlist"><button type="button">Cancel</button></a>
              <input type="submit" value="Save" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
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
#      Client and Wishlist Data Stucture       #
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
    client_photo = ndb.BlobProperty()
    client_email = ndb.StringProperty()
    client_phone = ndb.StringProperty()
    client_address = ndb.TextProperty()

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
        return json.dumps([len(q1), len(q2)])

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

      # user = users.get_current_user()
      # item = Client_db(id=user.user_id())
      # # - -
      # item.client_name = self.request.get('client_name')
      # item.client_id = user.user_id()
      # item.client_type = self.request.get('client_type')
      # item.client_email = user.nickname()
      # item.client_status = 'Wishlist'

      # item.put()
      # time.sleep(1)
      # self.redirect('/my_program')
      if users.is_current_user_admin():
        data_id = self.request.get('data_id')
        if data_id and data_id != '':
          item = Client.get_by_id(data_id)
        else:
          client_email = self.request.get('client_email')
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
        #
        item.put()
        time.sleep(1)
        self.redirect('/manage/client')

class Wishlist_db(ndb.Model):
    add_time = ndb.StringProperty()
    #
    client_name = ndb.StringProperty()
    client_program = ndb.StringProperty()
    client_email = ndb.StringProperty()

    @classmethod
    def _get_all_data(self):
        q = Wishlist_db.query()
        db_data = []
        for item in q.iter():
          db_data.append(item.to_dict())
        return json.dumps(db_data)

    @classmethod
    def _get_one_data(self,data_id):
      print "lala"
      item = Wishlist_db.get_by_id(data_id)
      print item
      if item:
        db_data = item.to_dict()
      else: 
        db_data = []
      return json.dumps(db_data)

    @classmethod
    def _get_current_wishlist(self):
        client_email = users.get_current_user().email()
        item = Wishlist_db.get_by_id(client_email)
        if item:
          db_data = item.to_dict()
        else: 
          db_data = []
        return json.dumps(db_data)

class addWishlist_db(webapp2.RequestHandler):
    def post(self):

      client_email = self.request.get('client_email')
      if client_email:
        item = Wishlist_db.get_by_id(client_email)
        if item:
          item.client_program += ' ,' + self.request.get('client_program')
        else:
          item = Wishlist_db(id=client_email)
          item.client_email = self.request.get('client_email')
          item.client_program = self.request.get('client_program')
          item.add_time = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y/%m/%d %H:%M:%S")

        item.client_name = self.request.get('client_name')
        item.put()
        time.sleep(1)

        if users.is_current_user_admin():
          self.redirect('/manage/wishlist')
        else:
          self.redirect('/my_program')

#----------------------------------------------#
#             Payment Records                  #
#----------------------------------------------#
class chargeCard(webapp2.RequestHandler):
  def post(self):

    #- stripe key and plan
    stripe.api_key = "xxxxxxxxxxxx"

    # stripe.Plan.create(
    #   amount=55000,
    #   interval='month',
    #   name='Platinum',
    #   currency='usd',
    #   id='Platinum')

    # stripe.Plan.create(
    #   amount=33000,
    #   interval='month',
    #   name='Gold',
    #   currency='usd',
    #   id='Gold')

    # stripe.Plan.create(
    #   amount=20000,
    #   interval='month',
    #   name='Silver',
    #   currency='usd',
    #   id='Silver')

    # stripe.Plan.create(
    #   amount=10000,
    #   interval='day',
    #   name='Bronze',
    #   currency='usd',
    #   id='Bronze')

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
    item.add_time = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y/%m/%d %H:%M:%S")
    
    # - create stripe customer
    try:
      customer = stripe.Customer.create(
      source=token,
      plan=item.client_program,
      email=item.client_email
      )
    except stripe.error.CardError, e:
      self.response.headers['Content-Type'] = 'application/json'
      self.response.out.write('error') 
    else:
      item.program_status = 'Active'
      item.stripe_cus_id = customer["id"]
      item.stripe_subscription_id = customer["subscriptions"]["data"][0]["id"]
      item.put()

      self.redirect('/payment_success')

class cancelProgram(webapp2.RequestHandler):
  def get(self):

    #- stripe key 
    stripe.api_key = "xxxxxxxxxxxx"

    if users.get_current_user():
      client_email = users.get_current_user().email()
      item = Client_db.get_by_id(client_email)
      
      try:
        customer = stripe.Customer.retrieve(item.stripe_cus_id)
        customer.subscriptions.retrieve(item.stripe_subscription_id).delete()
      except (RuntimeError, TypeError, NameError,ValueError):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps({'status':'error'})) 
      else:
        item.program_status = 'Canceled'
        item.put()
        self.redirect('/cancel_program_success')

def cancelProgram_admin(client_email):
    #- stripe key 
    stripe.api_key = "xxxxxxxxxxxx"

    item = Client_db.get_by_id(client_email)
    if item.program_status == 'Active' and item.stripe_cus_id and item.stripe_subscription_id:
      try:
        customer = stripe.Customer.retrieve(item.stripe_cus_id)
        customer.subscriptions.retrieve(item.stripe_subscription_id).delete()
      except (RuntimeError, TypeError, NameError,ValueError):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps({'status':'error'})) 
      else:
        item.program_status = 'Canceled'
        item.put()

class redirect2Payment(webapp2.RequestHandler):
  def get(self):
    program_chosen = self.request.get('program_chosen')
    url = "http://payment.shannycohen.fitness/?program_chosen=" + program_chosen
    self.redirect(str(url), True)

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
          if item.program_status == 'Active' and item.stripe_cus_id and item.stripe_subscription_id:
            cancelProgram_admin(data_id)
          item.key.delete()
          time.sleep(1)
          self.redirect('/list_data?client')

        if data_set == "wishlist":
          item = Wishlist_db.get_by_id(data_id)
          item.key.delete()
          time.sleep(1)
          self.redirect('/list_data?wishlist')

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

        if data_set == 'wishlist' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Wishlist_db._get_all_data()) 

        if data_set == 'wishlist' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Wishlist_db._get_one_data(data_id)) 

        if data_set == 'current_wishlist' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Wishlist_db._get_current_wishlist()) 

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

        if img_size == 'thumb':
            img.resize(width=100)
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

        if path_layer == 'programs':
            page_id = 'programs'
            page_name = 'Programs'
            page_html = page_header + programs_page_html

        if path_layer == 'confirm_signup':
            page_id = 'confirm_signup'
            page_name = 'Confirm Signup'
            page_html = page_header + confirm_signup_page_html
            program_chosen = self.request.get('program_chosen')

        if path_layer == 'payment':
            page_id = 'payment'
            page_name = 'Payment'
            if user:
              page_html = page_header + payment_page_html
              program_chosen = self.request.get('program_chosen')
            else:
              page_html = page_header + login_page_html

        if path_layer == 'payment_success':
            page_id = 'payment_success'
            page_name = 'Payment Success'
            page_html = page_header + payment_success_page_html

        if path_layer == 'add2wishlist':
            page_id = 'add2wishlist'
            page_name = 'Add to Wishlist'
            if user:   
              page_html = page_header + add2wishlist_page_html
              program_chosen = self.request.get('program_chosen')
            else:
              page_html = page_header + login_page_html

        if path_layer == 'my_program':
            page_id = 'my_program'
            page_name = 'My Program'
            if user:
              page_html = page_header + my_program_page_html
            else:
              page_html = page_header + login_page_html

        if path_layer == 'cancel_program_success':
            page_id = 'cancel_program_success'
            page_name = 'Cancel Program Success'
            if user:
              page_html = page_header + cancel_program_success_page_html
            else:
              page_html = page_header + login_page_html

        if path_layer == 'results':
            page_id = 'results'
            page_name = 'Results'
            page_html = page_header + results_page_html

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

              if base == 'client':
                page_id = 'manage_client'
                page_name = 'Manage Client'
                nav_html = admin_nav_html
                page_html = manage_client_page_html

              if base == 'wishlist':
                page_id = 'manage_wishlist'
                page_name = 'Manage Wishlist'
                nav_html = admin_nav_html
                page_html = manage_wishlist_page_html

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

              if base.startswith('wishlist'):
                page_id = 'edit_wishlist'
                page_name = 'Edit Wishlist'
                nav_html = admin_nav_html
                page_html = edit_wishlist_page_html
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

              if base == 'wishlist':
                page_id = 'publish_wishlist'
                page_name = 'Publish Wishlist'
                nav_html = admin_nav_html
                page_html = publish_wishlist_page_html
               
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
      ('/my_program/?', publicSite),
      ('/cancel_program/?', cancelProgram),
      ('/cancel_program_success/?', publicSite),

      ('/add2wishlist/?', publicSite),

    ('/results/?', publicSite),
    ('/exercises/?', publicSite),
    ('/exercise_detail/?', publicSite),
    ('/about/?', publicSite),

    ('/manage/?', publicSite),
    ('/manage/exercise/?', publicSite),
    ('/manage/client/?', publicSite),
    ('/manage/wishlist/?', publicSite),

    ('/edit/?', publicSite),
    ('/edit/exercise/?', publicSite),
    ('/edit/client/?', publicSite),
    ('/edit/wishlist/?', publicSite),

    ('/publish/exercise/?', publicSite),
    ('/publish/exercise_video?', publicSite),
    ('/publish/client/?', publicSite),
    ('/publish/wishlist/?', publicSite),

    ('/manage/add_exercise/?', addExercise_db),
    ('/upload_exercise_video/?', UploadExerciseVideo),
    ('/manage/add_client/?', addClient_db),
    ('/add_wishlist/?', addWishlist_db),

    # ('/manage/add_client/?', addClient_db),
    ('/list_data/?', listData),
    ('/delete_data/?', deleteData),
    ('/render_img/?', RenderImg),
    ('/view_video/([^/]+)?', ViewVideo),

], debug=True)

