$(document).ready(function(){
  $('form').on('submit', function (event){
	$.ajax({
  		type: "POST",
		url: "/convert3",
		data: {
			myinput: $('#myinput').val()
		}
	})
  .done(function(data){
    if(data.error){
      //Do something
    }
    else{
      $("#myoutput").val(data.myoutput).show();
    }
  });

  event.preventDefault();
});
});
