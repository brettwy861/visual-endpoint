//Tells user to login before voting
function wpv_regclose() {
var regobj = document.getElementById('wpvregbox');
regobj.style.display = "none";
}
function wpv_regopen() {
var regobj = document.getElementById('wpvregbox');
regobj.style.display = "block";
}