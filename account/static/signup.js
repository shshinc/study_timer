// 가입부분 체크

function signUpCheck(){

  let email = document.getElementById("email").value
  let name = document.getElementById("name").value
  let password = document.getElementById("password").value
  let passwordCheck = document.getElementById("passwordCheck").value
  let purpose = document.getElementById("purpose").value
  let check = true;

  // 이메일확인
  if(email.includes('@')){
    let emailId = email.split('@')[0]
    let emailServer = email.split('@')[1]
    if(emailId === "" || emailServer === ""){
      document.getElementById("emailError").innerHTML="이메일이 올바르지 않습니다."
      check = false
    }
    if(emailServer.includes('.')){
        let emailServ1 = emailServer.split('.')[1]
        if(emailServ1 !== "com" && emailServ1 !== "net" && emailServ1 !== "ac"){
            document.getElementById("emailError").innerHTML="이메일이 올바르지 않습니다."
            check = false
        }
    }
    else{
      document.getElementById("emailError").innerHTML=""
    }
  }else{
    document.getElementById("emailError").innerHTML="이메일이 올바르지 않습니다."
    check = false
  }


  // 이름확인
  if(name===""){
    document.getElementById("nameError").innerHTML="이름이 올바르지 않습니다."
    check = false
  }else{
    document.getElementById("nameError").innerHTML=""
  }

  if(password===""){
    document.getElementById("passwordError").innerHTML="비밀번호를 입력해주세요."
    check = false
  }else{
    document.getElementById("passwordError").innerHTML=""
  }

  if(passwordCheck===""){
    document.getElementById("passwordCheckError").innerHTML="비밀번호를 다시 입력해주세요."
    check = false
  }else{
    if(password !== passwordCheck){
      document.getElementById("passwordError").innerHTML=""
      document.getElementById("passwordCheckError").innerHTML="비밀번호가 동일하지 않습니다."
      check = false
    }
    else{
      document.getElementById("passwordError").innerHTML=""
      document.getElementById("passwordCheckError").innerHTML=""
    }
  }

  // 지역선택 확인
  if(purpose === "공부 목적을 선택해주세요."){
    document.getElementById("purposeError").innerHTML="공부 목적을 선택해주세요."
    check = false
  }else{
    document.getElementById("purposeError").innerHTML=""
  }
  
  if(check){
    document.getElementById("emailError").innerHTML=""
    document.getElementById("nameError").innerHTML=""
    document.getElementById("passwordError").innerHTML=""
    document.getElementById("passwordCheckError").innerHTML=""
    document.getElementById("purposeError").innerHTML=""
    
    //비동기 처리이벤트
    setTimeout(function() {
      alert("가입이 완료되었습니다.")
  },0);
  }
}

$(document).ready(function(){
  $('.password i' || '.passwordCheck i').on('click',function(){
      $('input').toggleClass('active');
      if($('input').hasClass('active')){
          $(this).attr('class',"fa fa-eye-slash fa-lg")
          .prev('input').attr('type',"text");
      }else{
          $(this).attr('class',"fa fa-eye fa-lg")
          .prev('input').attr('type','password');
      }
  });
});