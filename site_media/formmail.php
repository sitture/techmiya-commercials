<?php

$my_email = "henrykabu@yahoo.com";
$continue = "/";

$errors = array();

if(count($_COOKIE)){foreach(array_keys($_COOKIE) as $value){unset($_REQUEST[$value]);}}

// Validate email field.

if(isset($_REQUEST['email']) && !empty($_REQUEST['email']))
{

$_REQUEST['email'] = trim($_REQUEST['email']);

if(substr_count($_REQUEST['email'],"@") != 1 || stristr($_REQUEST['email']," ")){$errors[] = "Email address is invalid";}else{$exploded_email = explode("@",$_REQUEST['email']);if(empty($exploded_email[0]) || strlen($exploded_email[0]) > 64 || empty($exploded_email[1])){$errors[] = "Email address is invalid";}else{if(substr_count($exploded_email[1],".") == 0){$errors[] = "Email address is invalid";}else{$exploded_domain = explode(".",$exploded_email[1]);if(in_array("",$exploded_domain)){$errors[] = "Email address is invalid";}else{foreach($exploded_domain as $value){if(strlen($value) > 63 || !preg_match('/^[a-z0-9-]+$/i',$value)){$errors[] = "Email address is invalid"; break;}}}}}}

}

// Check referrer is from same site.

if(!(isset($_SERVER['HTTP_REFERER']) && !empty($_SERVER['HTTP_REFERER']) && stristr($_SERVER['HTTP_REFERER'],$_SERVER['HTTP_HOST']))){$errors[] = "You must enable referrer logging to use the form";}

// Check for a blank form.

function recursive_array_check_blank($element_value)
{

global $set;

if(!is_array($element_value)){if(!empty($element_value)){$set = 1;}}
else
{

foreach($element_value as $value){if($set){break;} recursive_array_check_blank($value);}

}

}

recursive_array_check_blank($_REQUEST);

if(!$set){$errors[] = "You cannot send a blank form";}

unset($set);

// Display any errors and exit if errors exist.

if(count($errors)){foreach($errors as $value){print "$value<br>";} exit;}

if(!defined("PHP_EOL")){define("PHP_EOL", strtoupper(substr(PHP_OS,0,3) == "WIN") ? "\r\n" : "\n");}

// Build message.

function build_message($request_input){if(!isset($message_output)){$message_output ="";}if(!is_array($request_input)){$message_output = $request_input;}else{foreach($request_input as $key => $value){if(!empty($value)){if(!is_numeric($key)){$message_output .= str_replace("_"," ",ucfirst($key)).": ".build_message($value).PHP_EOL.PHP_EOL;}else{$message_output .= build_message($value).", ";}}}}return rtrim($message_output,", ");}

$message = build_message($_REQUEST);

$message = $message . PHP_EOL.PHP_EOL."-- ".PHP_EOL."Thank you. http://WebZipDesign.com";

$message = stripslashes($message);

$subject = "Techmiya Contact Form";

$subject = stripslashes($subject);

$from_name = "$email";

if(isset($_REQUEST['name']) && !empty($_REQUEST['name'])){$from_name = stripslashes($_REQUEST['name']);}

$headers = "From: $name <$email>";

mail($my_email,$subject,$message,$headers);

?>


<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=windows-1250">
    <title>WebZipDesign &raquo Get Your Website Designed - Contact</title>
    <link rel="stylesheet" href="css/contact_style.css" type="text/css"/>
    <link rel="stylesheet" href="css/menulinks.css" type="text/css"/>
    <script type="text/javascript" src="javascript/htmltooltip.js"></script>
    <script type="text/javascript" src="javascript/webzip.js"></script>
	<META NAME="KEYWORDS" CONTENT="webzip, web zip, web zip design, webzip design, webzipdesign, web, website, design, download, html, video webs, film websites, cards, business website, business cards, samples, review, free hosting, web hosting, website hosting, free website">
	<meta name="Author" content="WebZip">
	<meta name='description' content='WebZip Designs, a professional website development company based in Leeds, UK. We are offering a full range of web services including web site development, custom website design, graphic design, logo design, corporate identity design and other design work.'>
	</head>

	<body>
    
	<div id="container">
            
		<div class="header">
			<table width="980"><tr><td><div class="logo"></div></td>
        <td align="left"><img border="0" src="images/contact_banner.gif" width="650" height="90" /></td>
		</tr></table>
        </div>
	  
        <div class="navi">
			<li class="link"><a href="index.html">Home</a></li>
			<li class="link"><a href="prices.html">Pricing</a></li>
			<li class="link"><a href="samples.html">Samples</a></li>
			<li class="link"><a href="about_us.html">About Us</a></li>
			<li class="link"><a href="contact.html">Contact Us</a></li>
		</div>
      <!---------------- Menu ---------------->
		<div id="menus">
		</div>
 
		<div class="sidebar">
		
			<div class="menurightcontent">
				<h1 class="titletxt">Our Services</h2>
					<img border="0" src="images/contact_banner2.gif" width="170" height="340" />
					</div><br>
		
		</div>

		<div class="menucontent">
		
			<h1 class="titletxt">Thank You!</h1>
			<p><font size="4pt"><b>Thank you <?php if(isset($_REQUEST['name'])){print stripslashes($_REQUEST['name']);} ?></b></font></p>
			
			<p><font size="4pt">Your request has been sent sucessfully!<br>We will contact you back as soon as possible.</font></p>
			<p>&nbsp;</p>
		</div>
		<div id="menus">
		<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
		</div>

		<div class="footer">
			<center><b>&copy; 2009 WebZipDesigns. All rights Reserved</b></center>
		</div>
    </div>
	
	</body>

</html>