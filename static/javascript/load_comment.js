// $(document).ready(function() {
//     $('#comment').fadeOut('fast', function(){
// 	$('#comment').load("/get_comment/"+id_article, function() {
// 	    $('#comment').fadeIn('fast');
// 	});
//     });
// });


// post
$(document).ready(function() {
    $('#form_post').submit(function() { // catch the form's submit event
	$.ajax({ // create an AJAX call...
	    data: $(this).serialize(), // get the form data
	    type: $(this).attr('method'), // GET or POST
	    url: $(this).attr('action'), // the file to call
	    success: function(response) { // on success..
		$('#comment').fadeOut('fast', function(){
		    $('#comment').load("/get_comment/"+id_article, function() {
			$('#form_post').find('textarea').val('');
			$('#comment').fadeIn('fast');
		    });
		});
	    }
	});
	return false;
    });
});


