"use stric"

function show1(){
    var x = document.getElementById("menu");
    var y = document.getElementById("logo");
    x.style.width = '50%';
    y.style.marginLeft = '45%';
    y.style.opacity = "0"
}

function close1(){
    var x = document.getElementById("menu");
    var y = document.getElementById("logo");
    x.style.width = '0';
    y.style.marginLeft = '0';
    y.style.opacity = "1"
}


function more() {
    var dots = document.getElementById("dots");
    var moreText = document.getElementById("more");
    var btnText = document.getElementById("bt3");
  
    if (dots.style.display === "none") {
      dots.style.display = "inline";
      btnText.innerHTML = "كشف اكثر"; 
      moreText.style.display = "none";
    } else {
      dots.style.display = "none";
      btnText.innerHTML = "كشف اقل"; 
      moreText.style.display = "inline";
    }
}


function chick1(){
  var x = document.getElementById("error3");
  var y = document.getElementById("exampleInputEmail3").value;
  var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  if(y.match(mailformat)){
    x.innerHTML = "ايميل تمام و مافي كلام";
    x.style.color = "#486B88";
    return true;
  }
  if(y == ""){
    x.innerHTML = "مافي زول بشوفه ما تلاوز";
    x.style.color = "#486B88";
    return false;
  }

  else{
    x.style.color = "red";
    x.innerHTML = "ايميلك دا قاطعو من راسك مش";
    return false;
  }
  
}


function chick2(){
  var x = document.getElementById("error1");
  var y = document.getElementById("exampleInputEmail1").value;
  var RegEx = /^[\u0600-\u065F\u066A-\u06EF\u06FA-\u06FFa-zA-Z ]+[\u0600-\u065F\u066A-\u06EF\u06FA-\u06FFa-zA-Z-_]*$/;
  if(y.match(RegEx)){
    x.innerHTML = "";
    return true;
    
  }
  if(y == ""){
    x.innerHTML = "";
    return false;
  }
  else{
    x.style.color = "red";
    x.innerHTML = "اسمك بدون ارقام و رموز  ";
   
    return false;
  }
  
}



function chick3(){
  var x = document.getElementById("error2");
  var y = document.getElementById("exampleInputEmail2").value;
  var RegEx = /[a-zA-Z+0-9]/;
  if(y.match(RegEx)){
    x.innerHTML = "";
    return true;
    
  }
  if(y == ""){
    x.innerHTML = "";
    return false;
  }
  else{
    x.style.color = "red";
    x.innerHTML = "ايشن بس";
    return false;
  }
  
}


function chick4(){
  var x = document.getElementById("error4");
  var y = document.getElementById("exampleInputEmail4").value;
  var RegEx = /^[0-9]/;
  if(y.match(RegEx)){
    x.innerHTML = "رقم العسل";
    x.style.color = "#486B88";
    return true;
    
  }
  if(y == ""){
    x.innerHTML = "اكتب ساي، ما بنشاغل الشينين";
    x.style.color = "#486B88";
    return false;
  }
  else{
    x.style.color = "red";
    x.innerHTML = " ارقام بس";
    return false;
  }
  
}



function chick5(){
  var x = document.getElementById("error5");
  var y = document.getElementById("exampleInputEmail5").value;
  var z = document.getElementById("exampleInputEmail6").value;
 
  if(y == z){
    x.innerHTML = "";
    return true;
  }
  if(y != z){
    x.innerHTML = "لا يوجد تطابق يا زكي";
    x.style.color = "red";
    return false;
  }
  if(y == ""){
    x.innerHTML = "";
    return false;
  }
  
}



function chick6(){
  var x = document.getElementById("exampleCheck1");
  if (x.checked == true){
    return true;
  }else{
    return false;
  }
};


function chick7(){
  var x = document.getElementById("exampleCheck2");
  if (x.checked == true){
    return true;
  }else{
    return false;
  }
};



function yourFunction(){
  // do whatever you like here
  var x = document.getElementById("b1");
  chick1();
  chick2();
  chick3();
  chick4();
  chick5();
  chick6();
  chick7();
  if (chick1() && chick2() && chick3() && chick4() && chick5() && chick6()&& chick7()){
    x.disabled = false;
  }else{
    x.disabled = true;
  }
  setTimeout(yourFunction, 100);
};



if (window.location.pathname == "/register"){
  yourFunction();
}else{
  console.log("end");
};


if (window.location.pathname == "/admin"){
  function doo(){
  $.ajax({
      url: "/datapass",
      type: "GET",
      contentType: "application/json",
  }).done(function(data) {
      var mens = data["mens"];
      var womens = data["womens"]
      var ctx = document.getElementById('myChart').getContext('2d');
      var chart = new Chart(ctx, {
          // The type of chart we want to create
          type: 'pie',
      
          // The data for our dataset
          data: {
            title: "المستخدمين",
              labels: ['راسطات', 'كنداكات'],
              datasets: [{
                  label: 'احصائيات',
                  borderColor: ['rgba(75, 192, 192, 1)', 'rgba(192, 0, 0, 1)'],
                  backgroundColor: ['rgba(75, 192, 192, 0.2)', 'rgba(192, 0, 0, 0.2)'],
                  data: [mens, womens]
              }]
          },
      
          // Configuration options go here
          options: {
            animation: {
              duration : 2000
            }
              
          },
      });
  })
  
  };
  doo();
  window.setInterval(function(){
    /// call your function here
    doo();
  }, 10000);
  
}else{
  console.log("end");
};

function alert1(){
  alert("تم النسخ الي الحافظة")
};






























new ClipboardJS('#bt4');