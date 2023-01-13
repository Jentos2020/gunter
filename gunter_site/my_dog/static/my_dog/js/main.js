let photo = document.querySelector('#photo');
let like_svg = document.querySelector('#heart_svg');

$("#next_photo").click(function (e) {
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/next_photo",
        beforeSend: function() {
            $('#photo').hide();
            $('#photo').attr("src",'');
            $("#next_photo").html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Загрузка...');
            $("#next_photo").addClass('disabled');
        },
        complete: function() {
            $('#photo').show();
            $("#next_photo").html('Далее');
            $("#next_photo").removeClass('disabled');
        },
        success: function (response) {
        $('.tags').html('');
            for (let num = 0; num < response.cats.length; num++) {
            	$('.tags').append(`<span class="badge bg-dark me-1">#${response.cats[num].photo_category.toLowerCase()}</span>`);
            }
            $('#photo').attr("src",response.photo);
            if (response.likes >= 1) {
                $('#like_count').show();
                $('#like_count').html(response.likes + ' ' + '<span class="visually"><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" class="bi bi-heart-fill" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/></svg></span>')
            }
            else {
                $('#like_count').hide();
            }
        },
        error: function (response) {
            $('#photo').attr("alt","Ошибка, перезагрузите страницу");
        }
    })
})


$("#download_btn").click(function (e) {
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/download_photo",
        success: function (response) {
            var temp_link = document.createElement('a');
	        temp_link.setAttribute('href', response);
	        temp_link.setAttribute('download', 'file');
	        temp_link.click();
        },
        error: function (response) {
            console.log("Ошибка скачивания файла");
        }
    })
})


$(function(){
	$('#like_btn').click(function(){
	    $.ajax({
            type: 'POST',
            url: "/like_photo",
            success: function (response) {
                $('#like_count').show();
                $('#like_count').html(response.likes + ' ' + '<span class="visually"><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" class="bi bi-heart-fill" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/></svg></span>')
                photo.classList.add('like_animate_img');
                like_svg.classList.add('like_animate_svg');

                like_svg.addEventListener("animationend", AnimationHandler, false);

                function AnimationHandler () {
                    photo.classList.remove('like_animate_img');
                    like_svg.classList.remove('like_animate_svg');
                }
                console.log(response)
            },
            error: function (response) {
                console.log(response)
            }
        })

	});
});
