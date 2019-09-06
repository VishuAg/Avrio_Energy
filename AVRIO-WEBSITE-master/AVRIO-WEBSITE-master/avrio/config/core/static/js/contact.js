

var firebaseConfig = {
   apiKey: "AIzaSyCbWefTvvW4gCQdE9lXndzvBLh9VeCT8eQ",
   authDomain: "contact-5f10e.firebaseapp.com",
   databaseURL: "https://contact-5f10e.firebaseio.com",
   projectId: "contact-5f10e",
   storageBucket: "contact-5f10e.appspot.com",
   messagingSenderId: "952211572300",
   appId: "1:952211572300:web:d614d2b52bf07022"
 };
 // Initialize Firebase
 firebase.initializeApp(firebaseConfig);

function writeuserdataforgeneral(){
  var name = document.getElementById("name");
  var email = document.getElementById("email");
  var mobile = document.getElementById("mobilenumber");
  var comment = document.getElementById("comment");
  var iAm = document.getElementById("inputGroupSelect01");

  var data_obj = {
    username : name.value,
    email: email.value,
    mobilenumber: mobile.value,
    comment: comment.value,
    iam:iAm.value

  };

  var db_ref = firebase.database().ref();
  db_ref = db_ref.child("contacts");
  db_ref = db_ref.child(iAm.value);
  db_ref = db_ref.push();
  db_ref.set(data_obj,function(error){
    if(error){

    }
    else{

$('#exampleModal').modal('toggle');
$('#exampleModal').modal('show');
    }
  });
}
 function writeUserData() {
   var name = document.getElementById("iname");
   var email = document.getElementById("iemail");
   var mobile = document.getElementById("imobile");
   var comment = document.getElementById("icomment");

   var data_obj = {
     username : name.value,
     email: email.value,
     mobilenumber: mobile.value,
     comment: comment.value

   };

   var db_ref = firebase.database().ref();
   db_ref = db_ref.child("contacts");
   db_ref = db_ref.child("investor");
   db_ref = db_ref.push();
   db_ref.set(data_obj,function(error){
     if(error){

     }
     else{

 $('#exampleModal').modal('toggle');
 $('#exampleModal').modal('show');
     }
   });
}
 $(document).ready(function() {

   $(".navbar").css("background", "linear-gradient(to right, #1abc9c 0%, #0f705d 100%)");// if not, change it back to transparent

 });
