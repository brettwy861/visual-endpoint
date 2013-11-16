<?php
session_start();
?>

<html>
<body>
<?php
$_SESSION['airportorcity']=$_POST['airportorcity'];
$_SESSION['pickupmonth']=$_POST['pickupmonth'];
$_SESSION['pickupday']=$_POST['pickupday'];
$_SESSION['pickuptime']=$_POST['pickuptime'];
$_SESSION['dropoffmonth']=$_POST['dropoffmonth'];
$_SESSION['dropoffday']=$_POST['dropoffday'];
$_SESSION['dropofftime']=$_POST['dropofftime'];
$_SESSION['rentalclass']=$_POST['rentalclass'];
//$_SESSION['rentalopt']=$_POST['rentalopt'];
$_SESSION['gps']=$_POST['gps'];
$_SESSION['srd']=$_POST['srd'];
$_SESSION['chs']=$_POST['chs'];
$_SESSION['smk']=$_POST['smk'];
?>
<form action="creditcard.php" method="post">
<fieldset><legend>Card information</legend>
Please fill in your billing information:<br />
<input type="radio" name="cardtype" value="visa" />Visa
<input type="radio" name="cardtype" value="master" />MasterCard
<input type="radio" name="cardtype" value="amex" />AmericanExpress<br />

Credit card Number <input type="text" name="cardno" size="23" maxlength="19">
CVC <input type="text" name="cvc" size = "4" maxlength="4">
Expiration Date
<select name="exmonth" size="1">
<option value="" selected="selected">month</option>
<option value="01">01</option>
<option value="02">02</option>
<option value="03">03</option>
<option value="04">04</option>
<option value="05">05</option>
<option value="06">06</option>
<option value="07">07</option>
<option value="08">08</option>
<option value="09">09</option>
<option value="10">10</option>
<option value="11">11</option>
<option value="12">12</option>
...
</select>
<select name="exyear" size="1">
<option value="" selected="selected">year</option>
<option value="12">12</option>
<option value="13">13</option>
<option value="14">14</option>
<option value="15">15</option>
...
</select><br />
</fieldset>
<br />
<fieldset><legend>Cardholder's Name</legend>
First Name <input type="text" name="fname" size="15" maxlength="20">
Last Name <input type="text" name="lname" size="15" maxlength="20">
</fieldset>
<br />
<fieldset><legend size="50">Billing Address</legend>
Street Address <input type="text" name="addr" size="40" maxlength="40"><br />
City <input type="text" name="city" size="20" maxlength="20">
State
<select name="state" size="1">
<option value="" selected="selected"></option>
<option value="AK">AK</option>
<option value="AL">AL</option>
<option value="FL">FL</option>
<option value="GA">GA</option>
<option value="KY">KY</option>
<option value="MS">MS</option>
<option value="NC">NC</option>
<option value="OH">OH</option>
<option value="SC">SC</option>
<option value="TN">TN</option>
...
</select>
Zipcode <input type="text" name="zip" size="6" maxlength="5"><br />
</fieldset><br />
<input type="submit" name="submit" value="Submit"/>
</form>
</body>
</html>
