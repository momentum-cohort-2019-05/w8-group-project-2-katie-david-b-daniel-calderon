$(function() {


    // Submit post on submit
    $('#answer-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        add_answer();
    });
   // AJAX for posting
    function add_answer() {
        console.log("add answer is working!") 
        $.ajax({
            url : "add_answer/",
            type : "POST",
            data : { the_answer : $('#id_text').val(),
                     the_question: $('#id_question_answered').val()},
            // handle a successful response
            success : function(json) {
                $('#answer-text').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
                $("#talk").prepend("<li><strong>"+json.text+"</strong> - <em> "+json.author+"</em> - <span> "+json.created+
                    "</span> - <a id='delete-answer-"+json.answerpk+"'>delete me</a></li>");
                console.log("success"); // another sanity check
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };
      // This function gets cookie with a given name
      function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});



























// let url = 'http://127.0.0.1:8000/core/add_answer/'




// console.log("hello")

// const answer = document.querySelector('#ans' );
// const ansButton = document.querySelector('#answer-button');
// const csrftoken = Cookies.get('csrftoken')


// ansButton.addEventListener('click', (e) =>{
//     console.log('Its working')
//     fetch(url ,{
//         credentials: 'include',
//           method: 'POST',
//           headers: {
//             'X-CSRFToken': csrftoken
//           },
//           body: JSON.stringify({ 'body': ouranswername })
//         })
//     .then(data => data.json())
//     .then(json => {
//         console.log(json)
//         const ansDiv=  document.querySelector('question_detail')
//         answerDiv.innerHTML += `
//         ${ json['user'] }:
//         <p>
//             ${json['body'] }
//         </p>
        
//     `
//      })
//     });